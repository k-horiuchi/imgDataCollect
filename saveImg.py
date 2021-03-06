import os
import pprint
import time
from time import sleep
import urllib.error
import urllib.request

def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file:
        data = web_file.read()
        with open(dst_path, mode='wb') as local_file:
            local_file.write(data)

f = open('url-list.txt', 'r')
line = f.readline()
num = 0

while line:
    num = num + 1
    url = line.strip()
    dst_path = "img/" + str(num) + '.png'
    download_file(url, dst_path)
    line = f.readline()
    sleep(1)
f.close()
