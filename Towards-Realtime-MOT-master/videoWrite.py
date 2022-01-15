import cv2
import os
import numpy as np
def main():
    data_path = "./results/frame/"
    fps = 30  # 视频帧率
    size = (1080, 608)  # 需要转为视频的图片的尺寸
    video = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
    for filename in os.listdir(data_path):
        image_path=data_path+filename
        img= cv2.imread(image_path)
        cv2.imwrite('output.jpg',img)
        #print(image_path)
        video.write(cv2.imread('output.jpg'))

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()