"""
    main.py
"""

from CodesPython.Neural_Networks.red_2 import train_neural_network
from CodesPython.Neural_Networks.red_1 import train_image_detection_model

def main():
    """
    Función principal que ejecuta los archivos de las redes neuronales.
    """
    params = train_neural_network() # Llamar a la función de entrenamiento desde red_2.py
    print(params) 
    
    model_image = train_image_detection_model()
    print(model_image)
    
   
if __name__ == "__main__": # el if _name_ == "__main__" ; sirve para mandar a ejecutar el código
    main()


