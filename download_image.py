import os
import re
import shutil
import urllib.request
import random
import sys

def create_folder(name):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.mkdir(name)
    os.chdir(name)

def open_url(url):
    # ip_lists = ["106.75.9.39:8080", "222.182.56.193:8118","101.236.43.153:8866"]
    # proxy_support = urllib.request.ProxyHandler({"http":random.choice(ip_lists)})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    response = urllib.request.urlopen(req)
    # response = opener.open(req)
    return response

def find_image_url(url):
    pattern = re.compile(r"img\s.*src\s*=\s*\"(\S*\.jpe*g)\"", re.I)
    response = open_url(url)
    html = response.read().decode("utf-8")
    m = pattern.findall(html)
    return m

def save_image(img_addrs):
    for index, each in enumerate(img_addrs):
        name = "image_%s_%s" % (index, each.split("/")[-1])
        with open(name, "wb") as fout:
            data=open_url(each).read()
            fout.write(data)
    
def main(url):
    create_folder("images")
    images = find_image_url(url)
    print(images)
    save_image(images)

if __name__ == "__main__":
    main(sys.argv[1])
