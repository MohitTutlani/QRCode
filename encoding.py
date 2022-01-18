import qrcode

data = "https://www.instagram.com/mohit_tutlani/"


qr = qrcode.QRCode(version = 3, box_size=10, border = 5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='red',back_color = 'white')
img.save('E:/Study Material/LAB/Python/QRcode/Instagram.png')