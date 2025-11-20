from dotenv import load_dotenv
import os
from pathlib import Path

def key_load():
    load_dotenv()

    openai_key = os.getenv("OPENAI_KEY")
    print(openai_key)
    
def db_load():
    #key_load랑 똑같음 사실
    load_dotenv()
    
    DATABASE_CONFIG = {
        "hosts" : os.getenv("DB_HOSTS"),
        "ports" : os.getenv("DB_PORTS"),
        "name" : os.getenv("DB_NAME")
    }
    print(DATABASE_CONFIG)
    
def except_env():
    
    
def main():
    db_load()
    
if __name__ == "__main__":
    main()

