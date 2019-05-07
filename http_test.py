#!/usr/bin/env python3

import requests
import json
import base64
import socket

if __name__ == '__main__':
    def getByte(path):
        with open(path, 'rb') as f:
            img_byte = base64.b64encode(f.read())
        img_str = img_byte.decode('ascii')
        return img_str

    img_str = getByte('./testImgs/timg.jpg')
    res = requests.post(url='http://127.0.0.1', data=img_str)
    print(res.text)