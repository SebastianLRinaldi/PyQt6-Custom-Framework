import os

BASE_DIR = 'src/apps'

def force_lowercase_filenames(base_dir):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.py') or file == '__init__.py':
                continue

            old_path = os.path.join(root, file)
            temp_path = os.path.join(root, f"{file}_temp")

            lower_file = file.lower()
            lower_path = os.path.join(root, lower_file)

            if file != lower_file:
                print(f"Renaming: {file} -> {lower_file}")

                # Rename to temp first
                os.rename(old_path, temp_path)
                # Rename to lowercase
                os.rename(temp_path, lower_path)

if __name__ == '__main__':
    force_lowercase_filenames(BASE_DIR)
    print("✅ All files force-renamed to lowercase.")
