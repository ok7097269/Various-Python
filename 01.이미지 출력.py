#!/usr/bin/env python
# coding: utf-8

# # 환경 설정
# Anaconda Promt 에서 다음 명령 수행
# >pip install opencv-python

# In[2]:


import cv2
cv2.__version__


# # OpenCV (Computer Vision)
# 다양한 영상 (이미지) / 동영상 처리에 사용되는 오픈소스 라이브러리

# # 1. 이미지 출력

# In[9]:


import cv2
img = cv2.imread('img.jpg') # 해당 결로의 파일 읽어오기
cv2.imshow('img', img) # img 라는 이름의 창에 img 표시
cv2.waitKey(5000) # 지정된 시간(ms) 동안 사용자 키 입력 대기 / 0 넣으면 무ㅏcv2.waitKey(5000) # 지정된 시간(ms) 동안 사용자 키 입력 대기 / 0 넣으면 무cv2.waitKey(5000) # 지정된 시간(ms) 동안 사용자 키 입력 대기 / 0 넣으면 무ㅏcv2.waitKey(5000) # 지정된 시간(ms) 동안 사용자 키 입력 대기 / 0 넣으면 무ㅏ한
cv2.destroyAllWindows() # 모든 창 닫기


# ## 읽기 옵션
# 1. cv2.IMREAD_COLOR : 컬러 이미지, 투명 영역은 무시 (기본값)
# 1. cv2.IMREAD_GRAYSCALE : 흑백 이미지
# 1. cv2.IMREAD_UNCHANGED : 투명 영역까지 포함

# In[11]:


import cv2
img_color = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('img.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('jpg_color', img_color)
cv2.imshow('jpg_gray', img_gray)
cv2.imshow('jpg_unchanged', img_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Shape
# 이미지의 height, width, channel 정보

# In[12]:


import cv2
img = cv2.imread('img.jpg')
img.shape # 세로, 가로, Channel

