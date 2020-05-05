import numpy as np
import cv2
import pdb
import os
from os import path

def create_folder(input_path):
    if not(path.exists(input_path)):
        os.mkdir(input_path)

def camera_position(folder_path):
    if ('after' in folder_path):
        if len(subject) == 4:
            cam_pos = 'right'
        else:
            cam_pos = 'left'
    elif ('before' in folder_path):
        if len(subject) == 4:
            cam_pos = 'left'
        else:
            cam_pos = 'right'
    return cam_pos

def write_jpg(cnt, cam_pos, frame, save_path):
    str_cnt = str(cnt).zfill(6)
    frame1 = frame[:,0:half_width,:]
    frame2 = frame[:,half_width:width,:]
    if cam_pos == 'left':
        cv2.imwrite(save_path + '/cam1/' + str_cnt + '.jpg', frame1) # Cam 1
        cv2.imwrite(save_path + '/cam2/' + str_cnt + '.jpg', frame2) # Cam 2
    elif cam_pos == 'right':
        cv2.imwrite(save_path + '/cam3/' + str_cnt + '.jpg', frame1) # Cam 3
        cv2.imwrite(save_path + '/cam4/' + str_cnt + '.jpg', frame2) # Cam 4

acl_path = '/media/thomas/Samsung_T51/_data/acl/'
vid_path = 'test_vids/'
pic_path = 'test_images/'

export_path = acl_path + pic_path
create_folder(export_path)

folder_paths = [f.path for f in os.scandir(acl_path + vid_path) if f.is_dir()]
folder_names = [f.name for f in os.scandir(acl_path + vid_path) if f.is_dir()]
for folder_path, folder_name in zip(folder_paths, folder_names):
    create_folder(export_path + folder_name + '/')

    video_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    video_names = [f.name for f in os.scandir(folder_path) if not f.is_dir()]
    
    for video_path, video_name in zip(video_paths, video_names):
        if ('.avi' in video_name):
            cap = cv2.VideoCapture(video_path)
            video_name = os.path.splitext(video_name)[0]
            subject = video_name.split('_')[0][0:-1]
            subject_str = 'S' + str(int(subject))

            create_folder(export_path + folder_name + '/' + subject_str + '/')

            cam_pos = camera_position(folder_path)

            if (cam_pos == 'left'):
                create_folder(export_path + folder_name + '/' + subject_str + '/cam1')
                create_folder(export_path + folder_name + '/' + subject_str + '/cam2')
            elif (cam_pos == 'right'):
                create_folder(export_path + folder_name + '/' + subject_str + '/cam3')
                create_folder(export_path + folder_name + '/' + subject_str + '/cam4')

            cnt = 0
            while(cap.isOpened()):
                ret, frame = cap.read()
                if (ret):
                    width = int(frame.shape[1])
                    half_width = int(width/2)
                else:
                    break
                write_jpg(cnt, cam_pos, frame, export_path + folder_name + '/' + subject_str)
                cnt += 1

            cap.release()