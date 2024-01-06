# QR CODE Generator

# install the libraries needed
# create a function that collects a text and converts it to a qr code
# save the qr code as an image
# run the function

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("code1.png")

url = input("Hello! Please enter the URL you want to convert into a QR CODE: ")
generate_qrcode(url)
print("Sucess, QR Code Generated!")
