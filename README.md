# Computer Pointer Controller

*TODO:* Write a short introduction to your project

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

## Documentation
*TODO:* Include any documentation that users might need to better understand your project code. For instance, this is a good place to explain the command line arguments that your project supports.
-fdm Provide the location to the face detection model .xml file
-lmm Provide the location to the Landmarks regression model .xml file
-hpm Provide the location to the Human pose estimation model .xml file
-gem Provide the location to the Gaze estimation model .xml file
-i Provide the location to the video file .mp4
-d (optional) Mention the target device for inference of the video file.

If the error rises about incompatible extension, go to the location - C:\Program Files (x86)\IntelSWTools\openvino\opencv 
and run the ffmpeg-download file with powershell


## Benchmarks
*TODO:* Include the benchmark results of running your model on multiple hardwares and multiple model precisions. Your benchmarks can include: model loading time, input/output processing time, model inference time etc.

============== Models Load time ===============
Face Detection Model: 689.6ms

Facial Landmarks Detection Model: 276.3ms

Headpose Estimation Model: 209.4ms

Gaze Estimation Model: 226.4ms

## Results
*TODO:* Discuss the benchmark results and explain why you are getting the results you are getting. For instance, explain why there is difference in inference time for FP32, FP16 and INT8 models.

## Stand Out Suggestions
This is where you can provide information about the stand out suggestions that you have attempted.

### Async Inference
If you have used Async Inference in your code, benchmark the results and explain its effects on power and performance of your project.

### Edge Cases
There will be certain situations that will break your inference flow. For instance, lighting changes or multiple people in the frame. Explain some of the edge cases you encountered in your project and how you solved them to make your project more robust.
