# MongoDB Launch Script

if pgrep mongod; then 
    echo "[INFO] MongoDB is already running"
else
    echo "[INFO] Launching a new MongoDB server"
    sudo mongod --fork --logpath ~/mongo_logs
fi
