from datetime import datetime, timedelta
import time

def d_day():
    now = datetime.now()
    target = datetime(2025, 12, 25)  # 크리스마스
    diff = target - now
    return print(f"크리스마스까지 D-{diff.days}")

def log_file():
    now = datetime.now()
    filename = f"log_{now.strftime('%Y%m%d_%H%M%S')}"
    print(filename)

def api_time():
    now = datetime.now()
    start_time = now
    print(f"시작 : {start_time.strftime('%H%M%S')}")
    time.sleep(2)
    end_time = datetime.now()
    duration = (end_time-start_time).total_seconds()
    print(f"종료: {end_time.strftime('%H:%M:%S')}")
    print(f"소요 시간: {duration}초")
    
def date_filter():
    data = [
    {"date": "2025-11-10", "value": 100},
    {"date": "2025-11-12", "value": 200},
    {"date": "2025-11-13", "value": 300},
    ]

    week_ago = datetime.now() - timedelta(days=7)

    recent_data = []
    for item in data:
        item_date = datetime.strptime(item["date"], "%Y-%m-%d")
        if item_date > week_ago:
            recent_data.append(item)

    print(recent_data)
    
            
def main():
    d_day()
    log_file()
    api_time()
    date_filter()

if __name__ == "__main__":
    main()