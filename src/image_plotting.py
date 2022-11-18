import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def to_array(image):
    array = np.empty((28, 28))
    image = image.to_numpy()

    for i, j in enumerate(range(0, 784, 28)):
        array[i,:] = image[j:j+28]
    
    print(array)
    return array

def plot_image_data(image1, image2):
    image1 = to_array(image1)
    image2 = to_array(image2)
    
    fig = plt.figure()
    fig.suptitle('Comparison')
    rows = 1
    columns = 2

    fig.add_subplot(rows, columns, 1)
    plt.imshow(image1, cmap='Greys')
    plt.title('Greyscale')

    fig.add_subplot(rows, columns, 2)
    plt.imshow(image2, cmap='Greys')
    plt.title('Black & White')

    plt.show()