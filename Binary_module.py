import cv2

def binary (): 

    # 이미지를 읽기
    image = cv2.imread('./image/mountain.jpg')  #이미지 읽기

    # 이미지 이진화
    threshold_value = 128  # 임계값 (적절한 값을 선택하여 조절 가능)
    max_value = 255  # 픽셀값의 최댓값
    ret, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

    # 결과 이미지 출력
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()