import requests
import webbrowser
import re
import sys

sys.argv.pop(0)
filePath = ' '.join(sys.argv)

class Online_image():
    searchUrl = 'http://saucenao.com/search.php'
    multipart = {'file': open(filePath, 'rb').read()}
    data = {'url':'', 'frame':1,'hide':0, 'database':999}  

    def __init__(self, img_dir):
        response = requests.post(self.searchUrl, files=self.multipart, data = self.data, allow_redirects=False)
        self.img_url = re.findall('image_url=(.*?).png&safe=off', response.text)

    def __str__(self):
        return self.img_url[0]+'.png'


class Engine():
    def __init__(self, img_url):
        self.img_url = img_url

    def Google(self):
        return 'https://www.google.com/searchbyimage?image_url=%s&safe=off' % self.img_url

    def SauceNao(self):
        return 'http://saucenao.com/search.php?url=%s&db=999' % self.img_url

    def IQDB(self):
        return 'https://iqdb.org/?url=%s' % self.img_url

    def TinEye(self):
        return 'https://www.tineye.com/search/?url=%s' % self.img_url

    def WhatAnime(self):
        return 'https://whatanime.ga/?auto&url=%s' % self.img_url


class Searcher():
    def __init__(self, file_path):
        self.img_url = Online_image(file_path)
        self.engine = Engine(self.img_url)
        
    def search_in_Google(self):
        webbrowser.open_new_tab(self.engine.Google())

    def search_in_SauceNao(self):
        webbrowser.open_new_tab(self.engine.SauceNao())
        
    def search_in_IQDB(self):
        webbrowser.open_new_tab(self.engine.IQDB())
                
    def search_in_TinEye(self):
        webbrowser.open_new_tab(self.engine.TinEye())
                
    def search_in_WhatAnime(self):
        webbrowser.open_new_tab(self.engine.WhatAnime())
    

img_searcher = Searcher(filePath)
img_searcher.search_in_Google()
img_searcher.search_in_SauceNao()
img_searcher.search_in_IQDB()
img_searcher.search_in_TinEye()
img_searcher.search_in_WhatAnime()
