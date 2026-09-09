
import qrcode

url = input("Enter the URL: ").strip()
file_path = "S:PYTHONQRcode.png"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
img.save(file_path)

print(f"QR Code generated and saved to {file_path}")