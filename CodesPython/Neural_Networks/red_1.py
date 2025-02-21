# Program that generate in a one eural network with detection of imagenes
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential #type: ignore
from keras.layers import Dense, Input #type: ignore 
from keras.utils import to_categorical #type: ignore
from keras.datasets import mnist #type: ignore

def train_image_detection_model():

    # Training data 
    (train_data_x, train_labels_y), (test_data_x, test_labels_y) = mnist.load_data() # Data: input data, and labels: used to calculate the loss function
    #mnist.load_data() this is a method, download the images from internt, all this is a tuple

    # Information about the training data
    print(train_data_x.shape) # form that the training vector has, in a tensor with 60 thousand 28*28 images
    print(train_labels_y[1]) # which label has the first image 
    print(test_data_x.shape)
    plt.imshow(train_data_x[1])

    # Neural network architecture using TensorFlow and Keras
    model = Sequential([ 
        Input(shape = (28*28,)), # how in a vector
        Dense(512, activation = 'relu'), # number of neurons
        Dense(10, activation = 'softmax')
        ])

    # Compile the model 
    model.compile( 
        optimizer = 'rmsprop', # loss function, is the way we update the weights, based on the gradient algorithm.
        loss = 'categorical_crossentropy', # type of loss function 
        metrics = ['accuracy']
        )

    # Resume of model 
    model.summary() # show the network being built

    # Training data preprocessing, generate of normality of data
    x_train = train_data_x.reshape(60000, 28*28) # we convert a 3d tensor into a matrix, a 3d to 2d tensor
    x_train = x_train.astype('float32')/255 # generate of normality, generate black and white, 0 and 1
    y_train = to_categorical(train_labels_y)

    # Testing data preprocessing
    x_test = test_data_x.reshape(10000, 28*28)
    x_test = x_test.astype('float32')/255 # generate of normality  
    y_test = to_categorical(test_labels_y)

    # Train the model 
    model.fit(x_train, y_train, epochs = 3, batch_size = 128) # generate the train five, or five cicles, and the batch is for how pase the imagenes
    # we pass in 128 in 128 images in packs, in 3 cycles. 

    # Evaluate of model, the Neural Network 
    model.evaluate(x_test,y_test) # evaluate of model utilice date of test 

    return model  

#train_image_detection_model()

