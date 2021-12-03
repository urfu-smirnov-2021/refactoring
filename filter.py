from PIL import Image
import numpy as np


def get_average_brightness(arr_of_pixels, mosaic_size, i, j):
    area = arr_of_pixels[i:i + mosaic_size, j:j + mosaic_size]
    total_brightness = np.sum(area)
    return int(total_brightness // 3 // mosaic_size ** 2)


def change_pixels_color(arr_of_pixels, mosaic_size, grayscale, average_brightness, i, j):
    pixel_value = int(average_brightness // grayscale) * grayscale
    arr_of_pixels[i:i + mosaic_size, j:j + mosaic_size] = pixel_value
    return arr_of_pixels


def grey_filter(image, mosaic_size, grayscale):
    arr_of_pixels = np.array(image)
    height = len(arr_of_pixels)
    width = len(arr_of_pixels[1])
    for i in range(0, height - mosaic_size + 1, mosaic_size):
        for j in range(0, width - mosaic_size + 1, mosaic_size):
            average_brightness = get_average_brightness(arr_of_pixels, mosaic_size, i, j)
            arr_of_pixels = change_pixels_color(arr_of_pixels, mosaic_size, grayscale, average_brightness, i, j)
    return arr_of_pixels


input_image = Image.open("img2.jpg")
image_in_gray_tones = Image.fromarray(grey_filter(input_image, 10, 50))
image_in_gray_tones.save('res.jpg')
