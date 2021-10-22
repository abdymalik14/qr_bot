import qrcode
import uuid
import os

dirname = os.path.dirname(__file__)
abs_path = os.path.join(dirname,'..//python')

def link_to_qr(link):
    img = qrcode.make(link)
    name = str(uuid.uuid4())
    path = abs_path + f'{name}.png'
    img.save(path)
    return path

print(link_to_qr('https://github.com/eternnoir/pyTelegramBotAPI'))