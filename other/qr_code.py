import qrcode

img = qrcode.make('http://www.ifeng.com')
img.save("test.png")

img = qrcode.make('http://www.hivemq.com/demos/websocket-client/')
img.save("hivemq_client.png")