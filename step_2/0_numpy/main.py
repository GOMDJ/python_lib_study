import numpy as np 

def naive_usage():
    arr = np.array([1,2,3,4,5])
    print(arr)
    print(type(arr))

    print(arr+10)
    print(arr*2)
    print(arr**2) #제곱

    print(arr.sum())
    print(arr.mean())   #avg    
    print(arr.max())
    print(arr.min())
    
def arr_set():
    arr = np.array([1,2,3,4,5])
    zeros_arr = np.zeros(5) #0으로 채운 배열 요소 5개
    ones_arr = np.ones(3)   #1로 채운 배열 요소 3개
    seq_arr = np.arange(0, 10, 3) # 0부터 10미만까지 연속된 배열 생성, 3씩 증가
    lin_arr = np.linspace(1, 3, 5) #1~3까지 5등분
    rand = np.random.rand(5) #0~1사이 랜덤값 배열 생성, 요소는 5개
    rand_int = np.random.randint(0, 10, 5) #0부터 10 미만까지 정수 5개 랜덤 배열
    typed = arr.dtype   #arr의 타입 출력
    print(arr)
    print(zeros_arr)
    print(ones_arr)
    print(seq_arr)
    print(lin_arr)
    print(rand)
    print(rand_int)
    print(typed)
    
def two_dimansion():
    arr_2d = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(arr_2d)
    
    print(arr_2d.shape) #(3,3) 출력
    
    print(arr_2d[0])    #인덱싱
    print(arr_2d[1][1]) #인덱싱
    
    print(arr_2d[:, 0]) #슬라이싱, 모든 행의 0열 출력
    print(arr_2d[0,:])  #슬라이싱, 0행의 모든 열 출력
    print(arr_2d[0:2, 1:3]) #슬라이싱 (0~1)행, (1~2)열 출력

def cal_arr():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    # 요소별 연산
    print(a + b)   # [5 7 9]
    print(a - b)   # [-3 -3 -3]
    print(a * b)   # [4 10 18]
    print(a / b)   # [0.25 0.4 0.5]
    

def statistic_arr():
    arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

    # 전체 통계
    print(arr.sum())   # 45
    print(arr.mean())  # 5.0
    print(arr.std())   # 표준편차
    print(arr.max())   # 9
    print(arr.min())   # 1
    
def transform_arr():
    #reshape
    arr = np.array([1,2,3,4,5,6])
    reshaped = arr.reshape(2,3) #2행,3열 배열로 reshape
    print(reshaped)
    
    #flatten 2차원 -> 1차원
    arr_2d = np.array([[1,2], [3,4]])
    flat = arr_2d.flatten()
    print(flat)
    
    #transpose 전치(행<->열)
    arr_2d = np.array([[1, 2, 3],[4, 5, 6]])
    transposed = arr_2d.T
    print(transposed)
        
def main():
    arr_set()

if __name__ == "__main__":
    main()
