import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file:
        data = web_file.read()
        with open(dst_path, mode='wb') as local_file:
            local_file.write(data)

f = open('img/url.txt', 'r')
line = f.readline()
num = 0

while line:
    num = num + 1
    url = line.strip()
    dst_path = str(num) + '.png'
    download_file(url, dst_path)
    line = f.readline()
f.close()
