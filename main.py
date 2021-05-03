import pyqrcode  # install pyqrcode
import png # install pypng (it is mandatory to download the package)
import random

text = input("Enter any text or url : ")
qrCode = pyqrcode.create(text)

fileName = input("Enter any file name : ")

base_file_location = "R:\\qrcodes\\"
extended_file_name = str(fileName) + "_" + str(random.randint(0, 100))

qrCode.png(base_file_location + "pngs\\" + extended_file_name + ".png", scale=6)
qrCode.svg(base_file_location + "svgs\\" + extended_file_name + ".svg", scale=8)

print("qrcode generate for text : " + text)
