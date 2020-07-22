'''
This is a sample class for a model. You may choose to use it as-is or make any changes to it.
This has been provided just to give you an idea of how to structure your model class.
'''
import time, os
import cv2
import numpy as np
import math
from inference import Network
from openvino.inference_engine import IENetwork, IECore


class FaceDetection:
    '''
    Class for the Face Detection Model.
    '''
    def __init__(self, model_name, device='CPU', extensions=None):
        '''
        TODO: Use this to set your instance variables.
        '''
        self.model_xml  = model_name
        self.device = device
        self.extensions = extensions
        self.infer_Network = Network()
        self.plugin = IECore()
        self.model_bin = os.path.splitext(self.model_xml)[0] + ".bin"
        self.network = self.plugin.read_network(model=self.model_xml, weights=self.model_bin)
        
        print('initialised FaceDetection model')
        #raise NotImplementedError

    def load_model(self):
        '''
        TODO: You will need to complete this method.
        This method is for loading the model to the device specified by the user.
        If your model requires any Plugins, this is where you can load them.
        '''
        self.infer_network = Network()

        self.infer_network.load_model(self.model_xml, self.device, self.extensions)
        #raise NotImplementedError

    def predict(self, image):
        '''
        TODO: You will need to complete this method.
        This method is meant for running predictions on the input image.
        '''
        self.infer_network.exec_net(image)
        if self.infer_network.wait() == 0:
            # end time of inference
            end_time = time.time()
            result = (self.infer_network.get_output())[self.infer_network.output_blob]
            return result

        #raise NotImplementedError

    def check_model(self):

        supported_layers = self.plugin.query_network(network=self.network, device_name=self.device)
        unsupported_layers = [layer for layer in self.network.layers.keys() if layer not in supported_layers]
        if len(unsupported_layers) > 0:
            print("Please check extention for these unsupported layers =>" + str(unsupported_layers))
            exit(1)
        #logging.Info("Face Detection layers loaded correctly")

    def preprocess_input(self, image):
        '''
        Before feeding the data into the model for inference,
        you might have to preprocess it. This function is where you can do that.
        '''
        net_input_shape = self.infer_network.get_input_shape()

        #p_frame = np.copy(image)
        p_frame = cv2.resize(image, (net_input_shape[3], net_input_shape[2]))
        p_frame = p_frame.transpose(2,0,1)
        p_frame = p_frame.reshape(1, *p_frame.shape)

        return p_frame
        #raise NotImplementedError

    def preprocess_output(self, outputs, image, print_flag=True, threshold = 0.5):
        '''
        Before feeding the output of this model to the next model,
        you might have to preprocess the output. This function is where you can do that.
        '''
        height = image.shape[0]
        width = image.shape[1]
        faceboxes = []
        # Drawing the box/boxes 
        for i in range(len(outputs[0][0])):
            box = outputs[0][0][i] # i-th box
            confidence = box[2]
            if confidence>threshold:
                xmin = int(box[3] * width)
                ymin = int(box[4] * height)
                xmax = int(box[5] * width)
                ymax = int(box[6] * height)

                # Drawing the box in the image
                if(print_flag):
                    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255,0,0), 1)
                faceboxes.append([xmin, ymin,xmax, ymax])
        return image, faceboxes
        #raise NotImplementedError
