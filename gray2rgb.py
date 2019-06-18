# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:30:30 2019

@author: lzy
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import matplotlib  
matplotlib.use('Agg')  

global count
count=0

#import colormaps as cmaps
def gary2Jetcolor(src_path):
    for video_file_name in tqdm(os.listdir(src_path)):
        
        if '.DS_Store' == video_file_name:
            continue
        if 'depth' not in tqdm(os.listdir(src_path)):
            target_path=src_path+video_file_name+'/'
            gary2Jetcolor(target_path)
        if 'depth' in tqdm(os.listdir(src_path)) and video_file_name != 'depth':
            continue
        if 'depth' in tqdm(os.listdir(src_path)) and video_file_name == 'depth':
            if not os.path.exists(src_path+'depth_jetcolor'):
                os.mkdir(src_path+'depth_jetcolor')
            for video_name in tqdm(os.listdir(src_path+'depth'+'/')):
                fig = plt.gcf()
                print(src_path)
                print(video_name)
                if(video_name.endswith('.png')):
                    my_image=cv2.imread(src_path+'depth'+'/'+video_name)
                #cv2.imshow("o_image",my_image)
                img_gray = cv2.cvtColor(my_image,cv2.COLOR_RGB2GRAY)
                blank_image = np.zeros(img_gray.shape, np.uint8)
                #final_image = np.zeros(img_gray.shape, np.uint8)
                #归一化到0-255
                cv2.normalize(img_gray,blank_image,0,255,cv2.NORM_MINMAX)
                #使用colormaping
                
                height, width= blank_image.shape 
                #如果dpi=300，那么图像大小=height*width 
                plt.axis('off')
                plt.imshow(blank_image, cmap="jet")
                #去除白边
                # fig.set_size_inches(width/100.0/3.0, height/100.0/3.0) 
                fig.set_size_inches(width, height)
                plt.gca().xaxis.set_major_locator(plt.NullLocator()) 
                plt.gca().yaxis.set_major_locator(plt.NullLocator()) 
                plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0) 
                plt.margins(0,0)
                #保存图片
                fig.savefig(src_path+'./depth_jetcolor/'+video_name, format='png',dpi=1)
                plt.close('all')
                global count
                count+=1
                print('save image:',str(count))
            
if __name__ == '__main__': 
	gary2Jetcolor(src_path="./SUNRGBD/")