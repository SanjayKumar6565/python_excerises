import qrcode
import emoji
# generating a QR code using the make() function
qr_img = qrcode.make(emoji.emojize("MADDA KUDDUV :middle_finger::middle_finger:"))
# saving the image file
qr_img.save("mg1.jpg")
print("QR Code generated--verify")