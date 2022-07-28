import qrcode
import os


class QrCodeGenerator:

    def __init__(self):
        self.current = 0
        self.images = []

    def generate(self, data):
        qr = qrcode.make(data)
        path = f'.\\static\\{self.current}.png'
        qr.save(path)
        self.images.append(path)
        self.current += 1
        return path

    def __del__(self):
        for i in self.images:
            os.remove(i)
