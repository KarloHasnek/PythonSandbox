# Importing library
import qrcode

# Data for which you want to make QR Code
# Here we are using URL of MakeUseOf website
data = "https://www.chess.com/home"

# Name of the QR Code Image file
QRCodefile = "ChessCom.png"

# instantiate QRCode object
qrObject = qrcode.QRCode(border=2)

# add data to the QR code
qrObject.add_data(data)

# compile the data into a QR code array
qrObject.make()
image = qrObject.make_image(fill_color="black")

# Saving image into a file
image.save(QRCodefile)
