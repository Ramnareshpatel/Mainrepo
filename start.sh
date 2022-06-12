if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Ramnareshpatel/mainrepo.git /LUNA-EXTRA-FEATURES
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LUNA-EXTRA-FEATURES
fi
cd /LUNA-EXTRA-FEATURES
pip3 install -U -r requirements.txt
echo "Starting Mᴇʟᴏᴅʏ 💖..."
python3 bot.py
