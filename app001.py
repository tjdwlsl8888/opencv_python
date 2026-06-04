import numpy as np 

# 1. numpy 배열 생성
py_list = [1, 2, 3, 4, 5] 
print(f'py_list: {py_list}')

np_arr = np.array(py_list)
# np_arr = np.array([1,2,3,4,5,6,7,8,9,10])  가장 자리수가 큰 숫자에 자리수를 맞춤. 공백길이 
print(f'np_arr: {np_arr}')   # 구분자가 없음 
print(f'type of np_arr: {type(np_arr)}')   # class 'numpy.ndarray'

# n차원 numpy 배열 생성
# 2차원 numpy 배열 
np_arr = np.array(
    [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 0]
    ])
print(f'np_arr: \n{np_arr}')      # 터미널에서 보기 좋게 \n
print(f'np_arr type: {type(np_arr)}')
print(np_arr[1][3])  # 9

for idx, arr in enumerate(np_arr):
    print(f'idx: {idx}')
    for num in arr:
        print(f'num: {num}')

# 3차원 배열 
np_arr = np.array(
    [
        [
            [1, 2, 3, 4,  5],
            [6, 7, 8, 9, 0]
        ],

        [    
            [10, 20, 30, 40, 50],
            [60, 70, 80, 90, 100]
        ],
        [    
            [100, 200, 300, 400, 500],
            [600, 700, 800, 900, 1000]
        ]
    ]
)

for arr1th in np_arr:
    for arr2th in arr1th:
        for arr3th in arr2th:
            print(f'arr3th: {arr3th}') 


# numpy 복사 
np_arr = np.array([1, 2, 3, 4, 5])
print(f'np_arr: {np_arr}')           

np_arr_copy = np_arr.copy()     # 깊은 복사 b = a.copy()로만 되는 이유 -> 진짜 중첩구조가 아님. 실제 메모리 방 '일렬로 길게 늘어선 거대한 한 덩어리
print(np_arr is np_arr_copy)    # False 
print(np.array_equal(np_arr, np_arr_copy))  # 값 자체를 비교: True   
# 원소(item) 마다 비교 
print(np_arr == np_arr_copy)    # 원소(item) 마다 비교 [True, True, True, True, True....]

# numpy 배열 연산
np_arr = np.array([10, 20, 30, 40, 50])
print(f'np_arr: {np_arr}')

print(f'np_arr + 10: {np_arr + 10}')    # [20 30 40 50 60]
print(f'np_arr - 10: {np_arr - 10}')    # [ 0 10 20 30 40]
print(f'np_arr * 5: {np_arr * 5}')      # [ 50 100 150 200 250]
print(f'np_arr / 10: {np_arr / 10}')    # [1. 2. 3. 4. 5.]
print(f'np_arr % 10: {np_arr % 10}')    # [0 0 0 0 0]
print(f'np_arr // 10: {np_arr // 10}')  # [1 2 3 4 5]

# numpy 배열 속성 확인 
# 1. 배열 원소 데이터 타입(dtype) 설정 
np_arr = np.array([1, 2, 3], dtype=float)
print(f'np_arr: {np_arr}')  # [1. 2. 3.]

np_arr = np_arr.astype(np.int64)
print(f'np_arr: {np_arr}')  # [1, 2, 3]
print(f'np_arr type: {type(np_arr)}')  # class 'numpy.ndarray'

# 2. numpy 배열 속성(차원, 형태, 데이터타입) 확인
np_arr = np.array(
    [
        [1.,2.,3.,4.,5.],
        [10, 20, 30, 40, 50],
        [100, 200, 300, 400, 500]
    ]
)

# 배열 차원 
print(f'차원: {np_arr.ndim}')  # 2

# 배열 형태 
print(f'형태: {np_arr.shape}')  # (3, 5)

# 배열 데이터타입
print(f'데이터 타입: {np_arr.dtype}') # float64   -> 한 행만 float여도 다른 행까지 실수형식으로 표기됨

# 모든 원소가 x인 배열 만들기
# 1. ones() $ ones_like()

np_arr = np.ones((3, 5), dtype=int)
print(f'np_arr: \n{np_arr}')
'''
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
'''

py_list = [1, 2, 3]     # **********************
np_arr = np.ones_like(py_list, dtype=float)
print(f'np_arr: {np_arr}')

'''
[1., 1., 1.]
'''
py_list = [[1,2,3], [4,5,6]]        
np_arr = np.ones_like(py_list, dtype=float)
print(f'np_arr: \n{np_arr}')

'''
[[1. 1. 1.]
 [1. 1. 1.]]
'''

#2. zeros() & zeros_like()
# 모든 원소가 0인 배열 만들기 **********************

np_arr = np.zeros((3, 5), dtype=int)
print(f'np_arr: \n{np_arr}')

'''
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
'''

py_list = [1,2,3]  
np_arr = np.zeros_like(py_list, dtype=int) # **********************
print(f'np_arr: \n{np_arr}')
'''
[0 0 0]
'''

py_list = [[1,2,3], [4,5,6]]
np_arr = np.zeros_like(py_list, dtype=int)
print(f'np_arr: \n{np_arr}')

'''
[[0 0 0]
 [0 0 0]]
'''
# 3. empty() & empty_like()
np_arr = np.empty((3,5), dtype=int)
print(f'np_arr: \n{np_arr}')

'''
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
'''

py_list = [1, 2, 3]
np_arr = np.empty_like(py_list, dtype=int)
print(f'np_arr: \n{np_arr}')


# 2차원 배열 shape 변경

'''
np_arr[2][1][2]

print(np_arr[2, 1, 2])


1. 조건부 슬라이싱: "불리언 인덱싱 (Boolean Indexing)"

ex) traffic > 2000

2. 브로드캐스팅 (Broadcasting)

# 2차원 배열 (3명 학생의 국/영/수 점수)
scores = np.array([
    [80, 90, 70],
    [85, 95, 80],
    [75, 80, 85]
])

# 모든 학생의 점수에 5점씩 보너스를 주고 싶다면?
# 1차원 스칼라 값을 그냥 더해버리면 됩니다.
bonus_scores = scores + 5 

# 심지어 과목별로 가산점을 다르게 줄 수도 있습니다.
# 국어+10, 영어+0, 수학+20
weights = np.array([10, 0, 20])
final_scores = scores + weights

3. 방향의 마스터: "Axis (축) 로직" ⭐️ (가장 중요)

'''


'''
np.zeros() 활용가치
'''
🎨 1. 컴퓨터 비전(OpenCV)의 "빈 도화지 (Black Canvas)"  '완벽한 검은색'

import numpy as np
import cv2 # OpenCV

# 풀HD 해상도의 완벽하게 까만 '빈 도화지'를 하나 생성합니다.
black_canvas = np.zeros((1080, 1920, 3), dtype=np.uint8)
# 이제 이 까만 도화지 위에 자동차가 인식된 위치에만 빨간색 네모를 그립니다.
# (원본 이미지를 훼손하지 않고, 깔끔한 마스크 필터를 하나 만드는 과정입니다.)

2. 뼈대부터 짓고 시작하기 "메모리 찜하기 (Pre-allocation)"

초보자의 방식 (파이썬 기본 리스트):
빈 리스트 []를 만들고 .append()로 데이터를 계속 추가합니다.
컴퓨터는 데이터가 들어올 때마다 "어? 방이 좁네? 이사 가야겠다"를 
100만 번 반복하며 엄청난 시간과 메모리를 낭비합니다.

전문가의 방식 (np.zeros):
애초에 np_arr = np.zeros(1000000)으로 방 100만 개짜리 호텔(메모리)을 미리 한 번에 지어버립니다. 
(빈방에는 일단 0을 채워둡니다.) 그리고 데이터가 들어오면 np_arr[5] = 23.5 처럼 
해당 호실에 손님을 꽂아 넣기만 합니다. 속도가 수십 배 이상 빨라집니다.

🏷️ 3. 인공지능의 정답지 "원-핫 인코딩 (One-Hot Encoding)"
데이터를 인공지능이 이해할 수 있게 변환할 때도 필수입니다.
예를 들어 과일 이미지를 보고 [사과, 바나나, 포도, 오렌지, 수박] 중 하나로 분류하는 인공지능이 있다고 해보죠. 정답이 '포도'일 때, 컴퓨터는 '포도'라는 글자를 읽지 못합니다.

이때 np.zeros(5)를 써서 [0, 0, 0, 0, 0]을 만듭니다. 그다음 포도의 위치(인덱스 2번)만 딱 1로 바꿔줍니다.
👉 [0, 0, 1, 0, 0] (이것이 컴퓨터가 이해하는 '포도'의 정답지입니다.)