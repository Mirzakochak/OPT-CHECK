import os
import subprocess

VENV_DIR = "venv"

required_packages = [
    "requests",
    "pyfiglet",
    "telebot",
    "faker",
    "beautifulsoup4",
    "colorama",
    "pycountry",
    "cloudscraper",
    "user-agent"
]

def create_venv():
    print("[+] Creating virtual environment...")
    os.system(f"python3 -m venv {VENV_DIR}")

def install_packages():
    pip_path = f"./{VENV_DIR}/bin/pip"
    for package in required_packages:
        subprocess.run([pip_path, "install", package], check=False)
        print(f"DONE install [ {package} ]")

def print_done():
    print("\n✅ All packages installed in venv. To run the bot use ./start.sh")

if __name__ == "__main__":
    create_venv()
    install_packages()
    print_done()
