from jinja2 import Environment, FileSystemLoader

def render_fallback(symbol: str, mod_lines: list[str]) -> str:
    env = Environment(loader=FileSystemLoader("tools/templates"))
    template = env.get_template("fallback_symbol.j2")
    app_imported = any("from slack_bolt import App" in line for line in mod_lines)
    return template.render(symbol=symbol, app_imported=app_imported)

def attempt_fix_import(file_path: str, line: int, symbol: str, import_module: str):
    print(f"🛠 Attempting fix for {symbol} from {import_module}...")

    try:
        spec = importlib.util.find_spec(import_module)
        if spec is None or spec.origin is None:
            print(f"❌ Could not resolve module: {import_module}")
            return
        mod_path = Path(spec.origin)
        mod_lines = mod_path.read_text().splitlines()
    except Exception as e:
        print(f"❌ Import resolution failed: {e}")
        return

    try:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"⚠️ Error loading module: {e}")
        return

    if hasattr(module, symbol):
        print(f"✅ `{symbol}` exists in {import_module}")
        return

    # Use Jinja to create the fallback code
    fallback_code = render_fallback(symbol, mod_lines)
    with open(mod_path, "a") as f:
        f.write("\n\n# --- Auto-patched ---\n")
        f.write(fallback_code)
        f.write("\n")
    print(f"✅ Auto-patched `{symbol}` in {mod_path}")
