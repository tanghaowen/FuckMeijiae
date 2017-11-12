import requests

class MeijiaeRequest():
    headers = {"Host":"shop.meijiae.com",
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3248.0 Safari/537.36",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
             "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
             "Referer":"http://shop.meijiae.com/"}

    session = None
    proxies = {}
    def __init__(self  ,proxy = None):


        self.session = requests.session()
        self.session.headers.update( self.headers )

        if not proxy == None:

            self.proxies = {
              "http": "http://%s" % proxy,
              "https": "http://%s"% proxy}


    def getUrl(self,url):
        response =  self.session.get(url, proxies=self.proxies)
        return response.text

    def downloadImg(self,imgpath,gooId ,goodName = None,domain = "http://shop.meijiae.com" ):
        imgurl = domain+"/"+imgpath

        imgres = self.session.get(imgurl, proxies=self.proxies)
        if imgres.status_code == 200:
            goodfilenemae ="img/goodImage-%d.jpg" %(gooId)
            goodfilename2 = "img/%d - %s.jpg" %(gooId, goodName)
            if not goodName == None:
                open(goodfilename2, 'wb').write(imgres.content)
                print("获取商品id:%d - %s 成功" %(gooId, goodName) )
            else:
                open(goodfilenemae,'wb').write(imgres.content)
                print("获取商品id:%d - %s 成功" % (gooId))


            return True
        else:
            return False
