import qrcode

print("-"*60)
print("QR Code Generator".center(60, "-"))
print("-"*60)
link = input("Insert your link here: ")

#Image name
QRCode_Img = input("Input image name: ")
QRCode_Img = QRCode_Img+".png"

#Creating Object
QRObject = qrcode.QRCode(border=2)
QRObject.add_data(link)
QRObject.make(fit=True)

#Creating Image
image = QRObject.make_image(fill_color="black")
image.save(QRCode_Img)
