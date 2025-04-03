import os
import sys


def create_folder_structure():
    """ Yaratilishi kerak bo'lgan papkalar va fayllar """
    folders = [
        "handlers", "utils", "services", "state"
    ]
    
    files = [
        "bot.py", "loader.py", ".env", ".env.example",
        "dockerfile", "docker-compose.yml", ".gitignore",
        "requirements.txt"
    ]
    
    files_structure = {
        "handlers": ["__init__.py", "start.py"],
        "utils": ["__init__.py", "texts.py", "buttons.py", "env.py"],
        "services": ["__init__.py", "services.py"],
        "state": ["__init__.py", "state.py"]
    }

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    for file in files:
        with open(file, "w") as f:
            f.write("")

    for folder, sub_files in files_structure.items():
        for sub_file in sub_files:
            file_path = os.path.join(folder, sub_file)
            with open(file_path, "w") as f:
                if sub_file == "__init__.py":
                    f.write("from . import start\n" if folder == "handlers" else "pass\n")
                else:
                    f.write(f"# {sub_file} fayli\n")
    
    print("Paket struktura yaratildi!")


def create():
    """ `tmp create` komandasini terminalda bajarish uchun """
    print("Paket strukturasini yaratish uchun tasdiqlang (y/n): ")
    confirm = input().strip().lower()
    
    if confirm == "y":
        create_folder_structure()
        print("✅ Paket struktura yaratildi!")
    else:
        print("❌ Yaratish bekor qilindi.")
        sys.exit(0)


if __name__ == "__main__":
    create()
