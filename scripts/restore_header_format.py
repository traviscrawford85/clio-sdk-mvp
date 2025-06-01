import re

OPENAPI_SPEC = "../openapi_resources_patched_fixed.yaml"
HEADER_NAME = "IF-MODIFIED-SINCE"

# Regex to match the IF-MODIFIED-SINCE header param schema
HEADER_BLOCK_RE = re.compile(r'(name:\s*'+HEADER_NAME+r'\n[\s\S]*?schema:\n)([ \t]+type: string\n)', re.MULTILINE)

FORMAT_LINE = "      format: date-time\n"

def restore_format_to_headers():
    with open(OPENAPI_SPEC, encoding="utf-8") as f:
        content = f.read()
    
    def replacer(match):
        block = match.group(1)
        type_line = match.group(2)
        indent = re.match(r'(\s*)type: string', type_line).group(1)
        # Only add format if not already present
        if f"{indent}format: date-time\n" not in block:
            return block + f"{indent}format: date-time\n" + type_line
        else:
            return block + type_line

    new_content = HEADER_BLOCK_RE.sub(replacer, content)
    with open(OPENAPI_SPEC, "w", encoding="utf-8") as fw:
        fw.write(new_content)
    print(f"Restored 'format: date-time' to all {HEADER_NAME} header parameters.")

if __name__ == "__main__":
    restore_format_to_headers()
