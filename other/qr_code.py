import qrcode

img = qrcode.make('http://www.ifeng.com')
img.save("test.png")