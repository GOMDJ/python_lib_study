from pathlib import Path
from datetime import datetime
def log_file():
    now = datetime.now()
    log_dir = Path("logs") / str(now.year) / str(now.month) / str(now.day)
    log_dir.mkdir(parents=True, exist_ok=True)
    # Path(f"logs/{now.year}/{now.month}/{now.day}").mkdir(parents=True, exist_ok=True), log_dir재사용안할 때 이렇게도 가능
    # Path("logs/2025/12/12").mkdir(parents=True, exist_ok=True), 경로 하드코딩할 때
    log_file = log_dir / f"app{now.strftime('%H%M%S')}.log"
    log_file.write_text("application started\n", encoding = "utf-8")

def main():
    log_file()
        
if __name__ == "__main__":
    main()
    