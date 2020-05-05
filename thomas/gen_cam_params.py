import os, sys
import numpy as np
import h5py
import pdb 

camera_params_path = os.path.join("thomas/camera_parameters.npy")
cameras_params = np.load(camera_params_path, allow_pickle=True).item()
# There are four cameras 1,2,3,4
camera_num_list = cameras_params['S26']['20180913'].keys()

# There are these attributes R, T, c, f, k, p

# Lets store individual camera parameters separately 
cam1 = camera_num_list = cameras_params['S26']['20180913']['cam1']
cam2 = camera_num_list = cameras_params['S26']['20180913']['cam2']
cam3 = camera_num_list = cameras_params['S26']['20180913']['cam3']
cam4 = camera_num_list = cameras_params['S26']['20180913']['cam4']
pdb.set_trace()