import os

# Adjust to your actual paths
API_DIR = "clio_client/api"
MODEL_DIR = "clio_client/models"

def extract_functions(filepath):
    with open(filepath, encoding="utf-8") as f:
        return [
            line.strip().split()[1].split("(")[0]
            for line in f.readlines()
            if line.startswith("def ")
        ]

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
        api_map[module_name] = extract_functions(full_path)

model_map = {}
for file in sorted(os.listdir(MODEL_DIR)):
    if file.endswith(".py"):
        module_name = file.replace(".py", "")
        full_path = os.path.join(MODEL_DIR, file)
        model_map[module_name] = extract_classes(full_path)

print("✅ API Modules and Methods:")
for module, funcs in api_map.items():
    print(f"{module}_api: {funcs}")

print("\n✅ Model Modules and Classes:")
for module, classes in model_map.items():
    print(f"{module}: {classes}")
