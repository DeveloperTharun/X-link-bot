echo "Cloning Repo...."
git clone https://github.com/DeveloperTharun/X-link-bot.git /X-link-bot
cd /X-link-bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
