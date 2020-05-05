# ACLposeEstimation

###### acl3d_alg.yaml #######
- This is the config file for aclpose which does the following
- Sets the image size, batch size, name, checkpoint, heatmap, backbone
- Also where the images are stored "aclrd_root" folder

to geth the .npy of the camera calibration do the following
######### generate-labels-npy-multiview-acl3d.py #########
- Under line 71 there is a variable call cameras_params
-- cameras_params['S26']['20180913']['cam1'].keys()
