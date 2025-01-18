import tensorflow as tf
from tensorflow.keras import model, _tf_uses_legacy_keras
import matplotlib.pyplot as plt
import numpy as np
from sklearn import train_test_data_split

def main():
    train_model()
    
def train_model():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

    train_images = train_images / 127.5 - 1
    test_images = test_images / 127.5 - 1

    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'horse', 'ship', 'truck')
    

if "__main__" == __name__:
    main()