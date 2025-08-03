import os
import re

ROOT_DIR = os.path.join("src")

IGNORE_LIST = {"__pycache__", ".venv"}
IGNORE_EXTENSIONS = {".pyc", ".log"}

def camel_to_snake(name):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower()

def safe_rename(old_path, new_name):
    dirname = os.path.dirname(old_path)
    new_path = os.path.join(dirname, new_name)
    if os.path.abspath(old_path) == os.path.abspath(new_path):
        return
    temp_path = os.path.join(dirname, f"__temp__{new_name}")
    os.rename(old_path, temp_path)
    os.rename(temp_path, new_path)
    print(f"Renamed: {old_path} -> {new_path}")

def should_ignore(name):
    if name in IGNORE_LIST:
        return True
    _, ext = os.path.splitext(name)
    return ext in IGNORE_EXTENSIONS

def recursive_fix(path):
    for name in os.listdir(path):
        if should_ignore(name):
            continue
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            recursive_fix(full_path)
            new_folder_name = camel_to_snake(name)
            if name != new_folder_name:
                safe_rename(full_path, new_folder_name)

    for name in os.listdir(path):
        if should_ignore(name):
            continue
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
