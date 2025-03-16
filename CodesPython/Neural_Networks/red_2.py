import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles

def train_neural_network():
    # We create datasets from scratch - For an example of classification, data training
    N = 1000
    gaussian_quantiles = make_gaussian_quantiles(
        mean=None,
        cov=0.1,
        n_samples=N,
        n_features=2,
        n_classes=2,
        shuffle=True,
        random_state=None)

    X, Y = gaussian_quantiles
    Y = Y[:,np.newaxis]

    print(X.shape)
    print(Y.shape)

    plt.scatter(X[:,0], X[:,1],c=Y, s=40, cmap=plt.cm.Spectral)

    # Activation functions

    def sigmoid(x, derivate=False):
        if derivate:
            return np.exp(-x)/(np.exp(-x)+1)**2
        else:
            return 1/(1+np.exp(-x))

    def relu(x, derivate=False):
        if derivate:
            x[x<=0]=0
            x[x>0]=1
            return x
        else:
            return np.maximum(0,x)

    # Loss function

    def mse(y, y_hat, derivate=False):
        if derivate:
            return (y_hat-y)
        else:
            return np.mean((y_hat-y)**2)

    # Network structure: assignment of weights and bias

    def initialize_parameters_deep(layers_dims):
        parameters = {}
        L = len(layers_dims)
        for l in range(0,L-1):
            parameters['W'+str(l+1)] = (np.random.rand(
                            layers_dims[l], layers_dims[l+1])*2)-1
            parameters['b'+str(l+1)] = (np.random.rand(1,
                            layers_dims[l+1])*2)-1
        return parameters


    def train(x_data, learning_rate, params, training=True):

        params['A0']=x_data

        # First layer
        params['Z1']=np.matmul(params['A0'], params['W1'])+params['b1']
        params['A1']=relu(params['Z1'])

        # Second layer
        params['Z2']=np.matmul(params['A1'], params['W2'])+params['b2']
        params['A2']=relu(params['Z2'])

        # Third layer
        params['Z3']=np.matmul(params['A2'], params['W3'])+params['b3']
        params['A3']=sigmoid(params['Z3'])

        output = params['A3']

        if training:
            # Backpropagation
            # Weights in the last layer
            params['dZ3'] = mse(Y,output,True)*sigmoid(params['A3'],True)
            params['dW3']=np.matmul(params['A2'].T, params['dZ3'])

            # Weights in the penultimate layer
            params['dZ2']=np.matmul(params['dZ3'], params['W3'].T)*relu(params['A2'],True)
            params['dW2']=np.matmul(params['A1'].T, params['dZ2'])

            # Weights of the first layer
            params['dZ1']=np.matmul(params['dZ2'], params['W2'].T)*relu(params['A1'], True)
            params['dW1']=np.matmul(params['A0'].T, params['dZ1'])

            # Gradient Descent Algorithm
            params['W3']=params['W3']-params['dW3']*learning_rate
            params['W2']=params['W2']-params['dW2']*learning_rate
            params['W1']=params['W1']-params['dW1']*learning_rate

            params['b3']=params['b3']-(np.mean(params['dW3'], axis=0, keepdims=True))*learning_rate
            params['b2']=params['b2']-(np.mean(params['dW2'], axis=0, keepdims=True))*learning_rate
            params['b1']=params['b1']-(np.mean(params['dW1'], axis=0, keepdims=True))*learning_rate

        return output


    layers_dims = [2, 6, 10, 1]
    params = initialize_parameters_deep(layers_dims)
    errors = []

    # Epochs for the neural network

    for _ in range(50000):
        output = train(X, 0.001, params)
        if _%50==0:
            print(mse(Y,output))
            errors.append(mse(Y,output))
    
    plt.plot(errors)

    data_test_x = (np.random.rand(1000,2) * 2) - 1 # this is data test 
    data_test_y = train(data_test_x, 0.0001, params, training = False) # arquitecture of red list train 

    y = np.where(data_test_y > 0.5, 1, 0 )

    plt.scatter(data_test_x[:,0], data_test_x[:,1],c=y, s=40, cmap=plt.cm.Spectral)

    plt.show()
    

