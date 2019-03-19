import MeijiaeRequest
from bs4 import BeautifulSoup
meijiaeRequest = MeijiaeRequest.MeijiaeRequest()



for goodid in range(0,20000):
    goodUrl = "http://shop.meijiae.com/goods.php?id=%d" % (goodid)
    response = meijiaeRequest.getUrl( goodUrl)
    resBs = BeautifulSoup( response , "lxml")
    goodPrevImg = resBs.select("div.product-img > img")

    goodnameP = resBs.select("p.title_name")


    if len( goodPrevImg )> 0:
        goodPrevImg = goodPrevImg[0]
        goodImgUrl = goodPrevImg["src"]
        if len(goodnameP) > 0:
            meijiaeRequest.downloadImg(goodImgUrl,goodid,goodnameP[0].string)
        else:
            meijiaeRequest.downloadImg(goodImgUrl,goodid)
    else:
        print("id:%d 没有预览图或者商品页%d 不存在！！" % (goodid,goodid))
    goodid+=1