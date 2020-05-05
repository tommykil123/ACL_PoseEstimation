# ACLposeEstimation

Hi Thomas! So I'm just copying over any new code I've writted/adapted. To start, you'll want to download the learnable-triangulation-pytorch repo from [here.](https://github.com/karfly/learnable-triangulation-pytorch)

I'll walk you through some elements of the repo... first, there's some example videos (026P... .avi and 0026P... .avi) of a single leg press trial. The code videos_to_frames.py can be used to convert .avi files to .jpg, but you'll want to change the paths and image save filenames if you're gonna use it. 026P corresponds to the left stereo camera, while 0026P corresponds to the right stereo camera.

I've included 4 frames from these videos in data/acl3d/processed/S26/20180913/imageSequence/cam{1, 2, 3, 4}... the file path is quite long but I tried to keep it consistent with what the 3D pose people did.

The files create_bboxes.py, save_camera_params.py should save .npy files to the data/acl3d/extra folder with bounding box and camera parameter information. I adapted generate-labels-npy-multiview-acl3d.py from their code, and it should create a .npy file with the correct structure to load things correctly into their evaluation code.

I adapted their evaluation code (contained within train.py) in test_pose.py. Basically, I'm replacing their evaluation dataset with our ACL dataset and hoping the results look reasonable. Note that we don't have ground truth 3D joint positions, so I just said these were at [1, 1, 1]^T for each joint.

The configuration files necessary for test_pose.py can be found in experiments/acl3d/eval. Right now we can only use the "algebraic" version of their code (acl3d_alg.yaml), since the "volumetric" requires an estimate of the 3D pelvis position to orient a volumetric bounding box. You'll want to pass arguments when calling test_pose.py that look something like args='--eval --config /home/patrick/Documents/pose_estimation/learnable-triangulation-pytorch/experiments/acl3d/eval/acl3d_alg.yaml'

After running test_pose.py, I've just been using some tensorboard thing they set up using this command: "tensorboard --logdir ./logs" which you can access through your internet browser.

Lastly, all the paths are going to be messed up cuz I just copied and pasted things into this folder, so that'll be the first thing to fix! Let me know if you have any questions or anything's unclear :)
