#OpenCV 모듈 가져오기 
import cv2

# 버전 확인
print(cv2.__version__)
'''
## 이미지 불러와서 출력하기   - (https://www.pexels.com/ko-kr/photo/)
# 이미지 읽기
# forestImg = cv2.imread('./res/img/forest1.jpg') 

print(f'forestImg shape: {forestImg.shape}')     # (세로,가로, 3(BGR) )

forestImg = cv2.resize(forestImg, (575, 384))

cv2.imshow('title-forestImg', forestImg)         # 이미지 출력 
cv2.waitKey(1000 * 5)                            # 3초 동안 출력이 된다.   단위는 밀리seconds
cv2.waitKey(0)                                   # 어떤 키를 누를 때까지 기다려라    
cv2.destroyAllWindows()                          # 모든 창 닫기
'''
## 읽기 옵션 

# forestImgColor = cv2.imread('./res/img/forest1.jpg', cv2.IMREAD_COLOR)    # BGR 유지
# forestImgColor = cv2.resize(forestImgColor, (384, 575))

# forestImgGray = cv2.imread('./res/img/forest1.jpg', cv2.IMREAD_GRAYSCALE) # GRAYSCALE
# forestImgGray = cv2.resize(forestImgGray, (384, 575))

# forestImgUnchanged = cv2.imread('./res/img/forest1.jpg', cv2.IMREAD_UNCHANGED) # ALPHA 유지 
# forestImgUnchanged = cv2.resize(forestImgGray, (384, 575))

# cv2.imshow('title-forestImgColor', forestImgColor)
# cv2.imshow('title-forestImgGray', forestImgGray)
# cv2.imshow('title-forestImgGray', forestImgUnchanged)  #PNG 투명한 부분이 있으면 그대로 유지. 

# cv2.waitKey(0)
# cv2.destroyAllWindows()

## 동영상  -  https://www.pexels.com/ko-kr/
# OpenCV에서 동영상을 불러온다는 것은  '동영상 -> 프레임(frame) 추출 -> 이미자화 -> 출력' 


forestMov = cv2.VideoCapture('./res/mov/')
while forestMov.isOpened(): # 동영상 파일이 연결되어 있다면...
    result, frame = forestMov.read()        # result: read 성공 여부, frame: 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    # 사이즈 조정
    frame = cv2.resize(frame, (384, 575))

    # print(f'frame: {frame}')
    cv2.imshow('title-forestFrame', frame)   # 매우 빠르게 frame(이미지)가 출력 된다.

    if cv2.waitKey(1) == ord('q'):   # 1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다. 
        break 

forestMov.release()       # 외부 자원 해제 
cv2.destroyAllWindows()   # 윈도우 창 닫기 


# 캠에서 동영상 실시간으로 불러오기  
# forestMov = cv2.VideoCapture(0)   # 드론으로 실시간 영상을 받아서 출력 
# while forestMov.isOpened():       # 동영상 파일이 연결되어 있다면...
#     result, frame = forestMov.read()       # result: read 성공 여부, frame: 받아온 이미지(프레임)
#     if not result:
#         print('END FRAME')
#         break

#     # 사이즈 조정
#     frame = cv2.resize(frame, (384, 575))

#     # print(f'frame: {frame}')
#     cv2.imshow('title-forestFrame', frame)   # 매우 빠르게 frame(이미지)가 출력 된다.

#     if cv2.waitKey(1) == ord('q'):   # 1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다. 
#         break 

# forestMov.release()       # 외부 자원 해제 
# cv2.destroyAllWindows()   # 윈도우 창 닫기