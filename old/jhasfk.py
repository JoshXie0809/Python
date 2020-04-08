import json, requests, webbrowser, glob, os
from bs4 import BeautifulSoup

path = "./2019"
if not os.path.isdir(path):
    os.mkdir(path)
c = ['201907', '201908']
for year in c:
    for i in glob.glob(r'./' + c +'/*'):
        a = i.split('/')
        path = "./2019/" + a[-1]
        if not os.path.isdir(path):
            os.mkdir(path)
        for j in glob.glob(r'' + i + '/*.json'):
            b = j.split('/')
            b = b[-1].split('.')
            with open(j, 'r', encoding='utf-8') as f:
                x = f.read()
                y = json.loads(x)

            with open('./2019/' + a[-1] + '/' + b[0] + '.txt', 'w+', encoding='utf-8') as f:
                for i in y.keys():
                    f.write(i + ':  ')
                    f.write(y[i] + '\n')


