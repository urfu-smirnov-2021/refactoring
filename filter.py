from PIL import Image
import numpy as np


def generate_img():
    img = Image.open("img2.jpg")
    arr = np.array(img)
    a = len(arr)
    a1 = len(arr[1])
    i = 0
    while i < a - 9:
        j = 0
        while j < a1 - 9:
            s = 0
            for n in range(i, i + 10):
                for n1 in range(j, j + 10):
                    c1 = arr[n][n1][0]
                    c2 = arr[n][n1][1]
                    c3 = arr[n][n1][2]
                    M = int(c1) + int(c2) + int(c3)
                    s += M
            s = int(s // 100)
            for n in range(i, i + 10):
                for n1 in range(j, j + 10):
                    arr[n][n1][0] = int(s // 150) * 50
                    arr[n][n1][1] = int(s // 150) * 50
                    arr[n][n1][2] = int(s // 150) * 50
            j = j + 10
        i = i + 10
    res = Image.fromarray(arr)
    res.save('res.jpg')


if __name__ == "__main__":
    generate_img()
