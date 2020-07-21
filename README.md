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

##Face Detection Model

python downloader.py –-name face-detection-adas-binary-0001 -o  <\destination location address>

##Landmarks Regression Model

python downloader.py –-name landmarks-regression-retail-0009 -o  <\destination location address>

##Human Pose Estimation Model

python downloader.py –-name head-pose-estimation-adas-0001 -o  <\destination location address>

##Gaze Estimation Model

python downloader.py –-name gaze-estimation-adas-0002 -o  <\destination location address>


## Demo
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


## Observed Values

This was run on FP16 for all model except face detection model.

============== Models ================ Load time ========== Processing Time ========Inference Time ================
                                ||                   ||                           ||                     ||
Face Detection Model            ||       898.7ms     ||       34.8ms              ||     29.7ms          ||
                                ||                   ||                           ||                     || 
Facial Landmarks Model          ||       376.3ms     ||       3.0ms               ||     2.2ms           || 
                                ||                   ||                           ||                     ||
Headpose Estimation Model       ||       309.4ms     ||       8.0ms               ||     6.4ms           ||
                                ||                   ||                           ||                     ||
Gaze Estimation Model           ||       326.4ms     ||       7.0ms               ||     9.2ms           ||
 ====================================================================================================================
 FP32
============== Models ================ Load time ========== Processing Time ========Inference Time ================
                                ||                   ||                           ||                     ||
Face Detection Model            ||       898.6ms     ||       51.9ms              ||     69.8ms          ||
                                ||                   ||                           ||                     || 
Facial Landmarks Model          ||       411.9ms     ||       3.0ms               ||     2.5ms           || 
                                ||                   ||                           ||                     ||
Headpose Estimation Model       ||       321.1ms     ||       11.0ms              ||     10.0ms          ||
                                ||                   ||                           ||                     ||
Gaze Estimation Model           ||       322.1ms     ||       10.0ms              ||     11.5ms          ||
 ====================================================================================================================


## Results
From the above results we can see that FP16 performs faster than FP32. This was run on CPU device. Although load time appears almost same, the processing time and the inference time taken is better for FP16.


## Stand Out Suggestions
This is where you can provide information about the stand out suggestions that you have attempted.

### Async Inference
If you have used Async Inference in your code, benchmark the results and explain its effects on power and performance of your project.

### Edge Cases
There will be certain situations that will break your inference flow. For instance, lighting changes or multiple people in the frame. Explain some of the edge cases you encountered in your project and how you solved them to make your project more robust.
