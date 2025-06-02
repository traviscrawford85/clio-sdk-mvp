import os

API_DIR = "clio_client/api"
MODEL_DIR = "clio_client/models"


def extract_functions(filepath):
    sync_funcs = []
    async_funcs = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("def "):
                sync_funcs.append(line.split()[1].split("(")[0])
            elif line.startswith("async def "):
                async_funcs.append(line.split()[2].split("(")[0])
    return sync_funcs, async_funcs


def extract_classes(filepath):
    with open(filepath, encoding="utf-8") as f:
        return [
            line.strip().split()[1].split("(")[0]
            for line in f.readlines()
            if line.startswith("class ")
        ]


api_map = {}
for file in sorted(os.listdir(API_DIR)):
    if file.endswith("_api.py"):
        module_name = file.replace("_api.py", "")
        full_path = os.path.join(API_DIR, file)
        sync_funcs, async_funcs = extract_functions(full_path)
        api_map[module_name] = {
            "sync": sync_funcs,
            "async": async_funcs,
        }

model_map = {}
for file in sorted(os.listdir(MODEL_DIR)):
    if file.endswith(".py"):
        module_name = file.replace(".py", "")
        full_path = os.path.join(MODEL_DIR, file)
        model_map[module_name] = extract_classes(full_path)

print("✅ API Modules and Methods:")
for module, funcs in api_map.items():
    print(f"{module}_api:")
    print(f"  async: {funcs['async']}")
    print(f"  sync:  {funcs['sync']}")

print("\n✅ Model Modules and Classes:")
for module, classes in model_map.items():
    print(f"{module}: {classes}")
