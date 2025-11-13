import time

#현재시간
timestamp = time.time()
print(timestamp) #현재시간 1970년 1월 1일부터 경과 초

#프로그램 멈추기(sleep)
print("3초 대기")
time.sleep(3)
print("계속 진행")

#실행시간측정
start = time.time() #측정 시작
for i in range(1000000):
    pass
end = time.time()   #측정 종료
print(f"실행 시간: {end - start}초")