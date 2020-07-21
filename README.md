# Computer Pointer Controller - Overview

This is an application that uses a face, humanpose and gaze detection models to control the mouse cursor using an input video file.

## Project Set Up and Installation
To set up the project, install the OpenVino toolkit in your desktop.
Navigate to the location where openVino is installed and run setupvars.bat

Navigate to the location where starter files are downloaded.
Create a virtual environment and activate the same.
Run the requirements.txt file with this command - pip install -r requirements.txt

Download the models using the model downloader into separate folders.
For this project we need the below mentioned models.

## Face Detection Model

python downloader.py –-name face-detection-adas-binary-0001 -o  <\destination location address>

## Landmarks Regression Model

python downloader.py –-name landmarks-regression-retail-0009 -o  <\destination location address>

## Human Pose Estimation Model

python downloader.py –-name head-pose-estimation-adas-0001 -o  <\destination location address>

## Gaze Estimation Model

python downloader.py –-name gaze-estimation-adas-0002 -o  <\destination location address>


## Running the Demo
After the necessary models are downloaded and environment is ready, ensure the demo.mp4 video is there in the bin folder. This is the video we are going to use here for the demo.
Run the below command to get the execution going.

python src\main.py -fdm <\location to the model>\face-detection-adas-binary-0001\FP32-INT1\face-detection-adas-binary-0001.xml -lmm <\location to the model>\landmarks-regression-retail-0009\FP16\landmarks-regression-retail-0009.xml -gem <\location to the model>\gaze-estimation-adas-0002\FP16\gaze-estimation-adas-0002.xml -hpm <\location to the model>\head-pose-estimation-adas-0001\FP16\head-pose-estimation-adas-0001.xml -i bin\demo.mpg -d CPU

## Argument explanation

-fdm Provide the location to the face detection model .xml file
-lmm Provide the location to the Landmarks regression model .xml file
-hpm Provide the location to the Human pose estimation model .xml file
-gem Provide the location to the Gaze estimation model .xml file
-i Provide the location to the video file .mp4
-d (optional) Mention the target device for inference of the video file.

If the error rises about incompatible extension, go to the location - C:\Program Files (x86)\IntelSWTools\openvino\opencv 
and run the ffmpeg-download file with powershell

## Directory Structure

1. bin folder has the demo.mp4 file which will be used for running the project
2. src folder consists of
	- face_detection.py which helps to preprocess, predict and detect the face and process the output detected image
	- facial_landmarks_detection.py helps to detect the eye landmarks and process the output
	- head_pose_estimation.py helps to detect the movement and position of the head by considering yaw, pitch and roll and process the output
	- gaze_estimation.py helps to crop the left eye, right eye and process the output
	- inference.py is where the inference engine is loaded and the async is controlled.
	- input_feeder.py helps to initialize video return the frames one by one. 
	- mouse_controller.py helps to take x, y coordinates value, speed, precisions and according these values it moves the mouse pointer by using pyautogui library. (Pyautogui library has to be installed if not installed automatically)
	- main.py helps to start the project where all the functions are centrally controlled.
3. venv - This will be the virtual environment where all the required libraries and its corresponding versions are installed.

## Observed Benchamark Values

This was run on FP16 for all model except face detection model.

| Models                |      Load time          | Processing Time    |Inference Time |
|-------------------    |   -------------------   |-------------------|------------------- |
|Face Detection Model    |      898.7ms     |        34.8ms           |     29.7ms          |
|Facial Landmarks Model          |       376.3ms     |      3.0ms     |   2.2ms             |
|Headpose Estimation Model       |       309.4ms     |      8.0ms     |     6.4ms           |
|Gaze Estimation Model           |       326.4ms     |       7.0ms    |     9.2ms           |

 FP32 model was used for all
| Models                |      Load time          | Processing Time    |Inference Time |
|-------------------    |   -------------------   |-------------------|------------------- |
|Face Detection Model            |       898.6ms     |       51.9ms              |     69.8ms          |
|Facial Landmarks Model          |       411.9ms     |       3.0ms               |     2.5ms           |                        
|Headpose Estimation Model       |       321.1ms     |       11.0ms              |     10.0ms          |
|Gaze Estimation Model           |       322.1ms     |       10.0ms              |     11.5ms          |

## Results
From the above results we can see that FP16 performs faster than FP32. This was run on CPU device. Although load time appears almost same, the processing time and the inference time taken is better for FP16. The accuracy was also good as the mouse pointer moved around faster when using FP16. 


### Edge Cases
Since we have only 1 person in the video, considered the first face image only and did all subsequent inferences on the same image only.
