# logger.py
import datetime

def log(msg):
    print(f"[{datetime.datetime.now()}] {msg}")
