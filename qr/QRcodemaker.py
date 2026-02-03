import qrcode


url = input("Enter the URL: ").strip()
file_path  = "/home/aldie/Documents/alden_python/qr/qrcode.png"

qr  = qrcode.QRCode()

qr.add_data(url)

img  = qr.make_image()

img.save(file_path)


print("It has been made")