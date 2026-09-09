import os

ROOT_DIR = os.path.join("src")

def safe_lowercase_rename(old_path):
    dirname, basename = os.path.split(old_path)
    new_basename = basename.lower()
    if basename == new_basename:
        return  # already lowercase

    temp_path = os.path.join(dirname, f"__temp__{new_basename}")
    final_path = os.path.join(dirname, new_basename)

    # Rename to temp first to bypass Windows case-insensitivity
    os.rename(old_path, temp_path)
    os.rename(temp_path, final_path)
    print(f"Renamed: {old_path} -> {final_path}")

def recursive_lowercase(path):
    # First rename subfolders
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            recursive_lowercase(full_path)
            safe_lowercase_rename(full_path)

    # Then rename files
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path) and name != "__init__.py":
            safe_lowercase_rename(full_path)

if __name__ == "__main__":
    recursive_lowercase(ROOT_DIR)
    print("✅ All files and folders under src/components lowercased.")


