import os, sys
import numpy as np
import h5py
import pdb 

bboxes_path = os.path.join("thomas/bboxes-acl3d-GT.npy")
bboxes = np.load(bboxes_path, allow_pickle=True).item()

cam1_bbox = bboxes['S26']['20180913']['cam1']
cam2_bbox = bboxes['S26']['20180913']['cam2']
cam3_bbox = bboxes['S26']['20180913']['cam3']
cam4_bbox = bboxes['S26']['20180913']['cam4']
print("Original cam1_bbox " + str(cam1_bbox))
print("Original cam2_bbox " + str(cam2_bbox))
print("Original cam3_bbox " + str(cam3_bbox))
print("Original cam4_bbox " + str(cam4_bbox))

cam3_bbox = cam3_bbox + [150,75,-50,-30]
cam4_bbox = cam4_bbox + [150,75,-50,-30]

bboxes['S26']['20180913']['cam3'] = cam3_bbox
bboxes['S26']['20180913']['cam4'] = cam4_bbox

np.save("./thomas/tmp", bboxes)

new_bboxes = np.load("thomas/tmp.npy", allow_pickle=True).item()
new_cam1_bbox = new_bboxes['S26']['20180913']['cam1']
new_cam2_bbox = new_bboxes['S26']['20180913']['cam2']
new_cam3_bbox = new_bboxes['S26']['20180913']['cam3']
new_cam4_bbox = new_bboxes['S26']['20180913']['cam4']
print("New cam1_bbox " + str(new_cam1_bbox))
print("New cam2_bbox " + str(new_cam2_bbox))
print("New cam3_bbox " + str(new_cam3_bbox))
print("New cam4_bbox " + str(new_cam4_bbox))
