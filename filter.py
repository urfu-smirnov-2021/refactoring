from PIL import Image
import numpy as np
input_image = Image.open("img2.jpg")
image_array = np.array(input_image)
width = len(image_array)
height = len(image_array[1])
current_width = 0
while current_width < width - 9:
    current_height = 0
    while current_height < height - 9:
        total_brightness = 0
        for n in range(current_width, current_width + 10):
            for k in range(current_height, current_height + 10):
                first_component = image_array[n][k][0]
                second_component = image_array[n][k][1]
                third_component = image_array[n][k][2]
                local_brightness = int(first_component) + int(second_component) + int(third_component)
                total_brightness += local_brightness
        total_brightness = int(total_brightness / 3 // 100)
        for n in range(current_width, current_width + 10):
            for comp in range(current_height, current_height + 10):
                image_array[n][comp][0] = int(total_brightness // 50) * 50
                image_array[n][comp][1] = int(total_brightness // 50) * 50
                image_array[n][comp][2] = int(total_brightness // 50) * 50
        current_height = current_height + 10
    current_width = current_width + 10
mosaic_image = Image.fromarray(image_array)
mosaic_image.save('res.jpg')
