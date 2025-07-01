#!/bin/bash

REPO_URL="https://github.com/Mirzakochak/OPT-CHECK.git"
FOLDER_NAME="botproject"
SERVICE_NAME="telegrambot"

clear
echo "========================="
echo " Telegram Bot Installer"
echo "========================="
echo "1. Install bot"
echo "2. Uninstall bot"
echo "3. Exit"
read -p "Choose an option (1/2/3): " choice

if [[ $choice == "1" ]]; then
  read -p "🔑 Enter your Telegram bot token: " TOKEN
  read -p "👤 Enter your numeric Telegram ID: " OWNER_ID

  sudo apt update -y
  sudo apt install python3 python3-pip python3-venv git -y

  git clone $REPO_URL $FOLDER_NAME
  cd $FOLDER_NAME || exit

  sed -i "s|TOKEN_HERE|$TOKEN|g" bot3.py
  sed -i "s|OWNER_ID_HERE|$OWNER_ID|g" bot3.py

  chmod +x start.sh
  python3 SETUP.py

  PROJECT_DIR=$(pwd)

  sudo bash -c "cat > /etc/systemd/system/$SERVICE_NAME.service << EOF
[Unit]
Description=Telegram Bot
After=network.target

[Service]
ExecStart=$PROJECT_DIR/start.sh
WorkingDirectory=$PROJECT_DIR
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF"

  sudo systemctl daemon-reexec
  sudo systemctl daemon-reload
  sudo systemctl enable $SERVICE_NAME
  sudo systemctl start $SERVICE_NAME

  echo '✅ Bot is installed and running in the background.'
  echo 'To view logs: journalctl -u telegrambot -f'

elif [[ $choice == "2" ]]; then
  echo "🗑 Uninstalling..."
  sudo systemctl stop $SERVICE_NAME
  sudo systemctl disable $SERVICE_NAME
  sudo rm /etc/systemd/system/$SERVICE_NAME.service
  sudo systemctl daemon-reload
  sudo rm -rf ~/$FOLDER_NAME
  echo "✅ Bot uninstalled successfully."

elif [[ $choice == "3" ]]; then
  echo "👋 Exiting installer."
  exit

else
  echo "⛔ Invalid option."
fi
