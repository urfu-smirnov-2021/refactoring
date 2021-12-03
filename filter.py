from PIL import Image
import numpy as np

def get_current_color(picture_array, width, picture_width, height, picture_height):
    mosaic_resolution = picture_height * picture_width
    current_color_on_screen = np.sum(picture_array[width: width + picture_width, height: height + picture_height]) //  3
    return current_color_on_screen // mosaic_resolution

def get_picture_array(picture_array, picture_width, picture_height, scale):
    for i in range(0, len(picture_array) , picture_width):
        for j in range(0, len(picture_array[1]) , picture_height):
            current_color = get_current_color(picture_array, i, picture_width , j, picture_height)
            picture_array[i: i + picture_width, j: j + picture_height] = np.full(3, current_color - current_color % scale)
    return picture_array

def transform_picture(in_picture, picture_width, picture_height, scale, picture_name, format):
    picture_array = np.array(in_picture)
    mosaic_array = get_picture_array(picture_array, picture_width, picture_height, scale)
    mosaic_image = Image.fromarray(mosaic_array)
    mosaic_image.save(picture_name + format)

in_picture = Image.open(input("Введите путь до изображения:  "))
picture_width = int(input("Введите ширину мозайки: "))
picture_height = int(input("Введите высоту мозайки: "))
scale = int(input("Введите масштаб изменения серого цвета в мозайке: "))
picture_name = input("Введите название готовой мозайки:  ")
format = input("Введите формат изображения готовой мозайки: ")
transform_picture(in_picture, picture_width, picture_height, scale, picture_name, format)

