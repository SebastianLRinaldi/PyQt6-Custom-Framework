import os
import re

ROOT_DIR = os.path.join("src")

def camel_to_snake(name):
    # Convert CamelCase or PascalCase to snake_case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower()

def safe_rename(old_path, new_name):
    dirname = os.path.dirname(old_path)
    new_path = os.path.join(dirname, new_name)
    if os.path.abspath(old_path) == os.path.abspath(new_path):
        return  # same path, no rename needed

    temp_path = os.path.join(dirname, f"__temp__{new_name}")
    os.rename(old_path, temp_path)
    os.rename(temp_path, new_path)
    print(f"Renamed: {old_path} -> {new_path}")

def recursive_fix(path):
    # First fix subfolders
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            recursive_fix(full_path)
            new_folder_name = camel_to_snake(name)
            if name != new_folder_name:
                safe_rename(full_path, new_folder_name)

    # Then fix files
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path) and name != "__init__.py":
            base, ext = os.path.splitext(name)
            new_base = camel_to_snake(base)
            new_name = new_base + ext.lower()
            if name != new_name:
                safe_rename(full_path, new_name)

if __name__ == "__main__":
    recursive_fix(ROOT_DIR)
    print("✅ All files and folders under src/ renamed to snake_case.")
