import pyqrcode
import png

link = input("Kindly enter link you want QR Code of ")

qrcode = pyqrcode.create(link)
qrcode.png("qrcodeimage.png", scale=5)
