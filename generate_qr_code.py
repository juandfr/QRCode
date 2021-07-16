import pyqrcode
import png
from pyqrcode import QRCode

#Link de destino do QRCode
QRString = 'https://github.com/juandfr'

#Construção do QR
url = pyqrcode.create(QRString)

url.png(r'qrcode.png', scale=8)