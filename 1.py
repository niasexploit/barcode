import pyqrcode

code = pyqrcode.create("niasxploit.com")
code.png("hasil.png",scale=6)
code.show()
