from PIL import Image
import numpy as np


def load_img(path):
    img = Image.open(path)
    img_array = np.array(img)
    img_height = len(img_array)
    img_width = len(img_array[1])
    return img_array, img_height, img_width


def get_user_settings():
    x = int(input("Mosaic pixel height: "))
    y = int(input("Mosaic pixel width: "))
    gr_multiplier = int(input("Grey gradation multiplier: "))
    return x, y, gr_multiplier


def get_pixels_brightness(img_array, cur_height, cur_width, m_height, m_width):
    pixels_brightness = 0
    for x in range(cur_height, cur_height + m_height):
        for y in range(cur_width, cur_width + m_width):
            r = img_array[x][y][0]
            g = img_array[x][y][1]
            b = img_array[x][y][2]
            pixel_brightness = int(r) + int(g) + int(b)
            pixels_brightness += pixel_brightness
    return int(pixels_brightness // (m_height * m_width))


def create_mosaic_pixel(img_array, cur_height, cur_width, m_height, m_width, gr_multiplier):
    pixels_brightness = get_pixels_brightness(img_array, cur_height, cur_width, m_height, m_width)
    for x in range(cur_height, cur_height + m_height):
        for y in range(cur_width, cur_width + m_width):
            img_array[x][y][0] = int(pixels_brightness // (150 * gr_multiplier)) * 50 * gr_multiplier
            img_array[x][y][1] = int(pixels_brightness // (150 * gr_multiplier)) * 50 * gr_multiplier
            img_array[x][y][2] = int(pixels_brightness // (150 * gr_multiplier)) * 50 * gr_multiplier


def generate_img():
    img_array, img_height, img_width = load_img("img2.jpg")
    m_height, m_width, gr_multiplier = get_user_settings()
    for cur_height in range(0, img_height - (m_height - 1), m_height):
        for cur_width in range(0, img_width - (m_width - 1), m_width):
            create_mosaic_pixel(img_array, cur_height, cur_width, m_height, m_width, gr_multiplier)
    res = Image.fromarray(img_array)
    res.save('res.jpg')


if __name__ == "__main__":
    generate_img()
