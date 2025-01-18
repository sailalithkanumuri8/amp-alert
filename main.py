import tensorflow as tf
from tensorflow import models, layers
import matplotlib.pyplot as plt
from sklearn import train_test_data_split

def main():
    train_model()
    
def train_model():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

    train_images = train_images / 127.5 - 1
    test_images = test_images / 127.5 - 1

    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'horse', 'ship', 'truck')

    print("Number of images in the training dataset: " + train_images.shape[0])
    print("NUmber of images in the testng dataset: " + test_images.shape[0])

    print("Shape of the images in the training dataset: " + train_images[0].shape)

    fig, axes = plt.subplots(1, 10, figsize = (10, 10))

    # Using matplotlib to show the first 10 images to make sure it works
    for i in range(10):
        image = train_images[i]
        denormalized_image = (image + 1) / 2
        axes[i].imshow(denormalized_image)
        axes[i].set_title(classes[train_labels[i][0]])
        axes[i].axis("off")

    # creation of the model
    model = models.Sequential([
        layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32,32,3)),
        layers.MaxPooling2D((2, 2), strides=(2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2), strides=(2, 2)),
        # Vectorizing the image to put it in a CNN
        layers.flatten(),
        layers.Dense(120, activation='relu'),
        layers.Dense(84, activation='relu'),
        layers.Dense(10, activiation='softmax')
    ])

    # model.summary() 

    model.compile(optimizer='adam',
                    loss = 'sparse_categorical_crossentropy',
                    metrics = ['accuracy'])
    
    history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_images))

    #Show accuracy
    test_loss, test_accuracy = model.evaluate(test_images, test_labels)
    print(f'The accuracy of neural network on the {test_images.shape[0]} test images: {test_accuracy*100:.2f}%')

if "__main__" == __name__:
    main()