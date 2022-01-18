from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("E:/Study Material/LAB/Python/QRcode/Instagram.png")

result = decode(img)
print(result)
    