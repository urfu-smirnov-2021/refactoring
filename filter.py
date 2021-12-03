from PIL import Image
import numpy as np
input_image = Image.open("img2.jpg")
image_array = np.array(input_image)

def get_average_color(image_array, width, mosaic_width, height, mosaic_height):
    mosaic_resolution = mosaic_height * mosaic_width
    average_color_on_screen = np.sum(image_array[width: width + mosaic_width, height: height + mosaic_height]) //  3
    average_color = average_color_on_screen // mosaic_resolution
    return average_color

def get_gray_mosaic_array(image_array, mosaic_width, mosaic_height, scale):
    width = len(image_array)
    height = len(image_array[1])
    for current_width in range(0, width , mosaic_width):
        for current_height in range(0, height , mosaic_height):
            average_color = get_average_color(image_array, current_width, mosaic_width , current_height, mosaic_height)
            gray_color = int(average_color // scale) * scale
            image_array[current_width: current_width + mosaic_width, current_height: current_height + mosaic_height] = np.full(3, gray_color)
    return image_array

mosaic_width = 10
mosaic_height = 10
scale = 50
mosaic_array = get_gray_mosaic_array(image_array, mosaic_width, mosaic_height, scale)
mosaic_image = Image.fromarray(mosaic_array)
mosaic_image.save('res.jpg')
