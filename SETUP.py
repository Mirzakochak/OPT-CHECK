import os

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

def upgrade_pip():
    os.system("python3 -m pip install --upgrade pip")

def install_packages(packages):
    for package in packages:
        os.system(f"pip3 install {package}")
        print(f"DONE install [ {package} ]")

def print_done_message():
    print("\nDone install :) ...... Mr.Ali")

def print_done_message1():
    input("\press any key to exit :)")

if __name__ == "__main__":
    install_packages(required_packages)
    upgrade_pip()
    print_done_message()
    print_done_message1()
