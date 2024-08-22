import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
import os
import numpy as np
import re

reviewlist = []
c1 = 0
def getRandomProxy():
    proxy = {"http": f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000 + random.randint(0, 9)}",
       "https": f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000 + random.randint(0, 9)}"}
    return proxy
product_title = ""
def extractReviews(reviewUrl, pageNumber):
    global product_title
    q = 1
    while q != 0:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        proxies=getRandomProxy()
        resp = requests.get(reviewUrl, proxies, headers=headers)
        with open('response.html', 'w+', encoding="utf-8") as fout:
                fout.write(resp.text+"\n")   
        soup = BeautifulSoup(resp.text, 'html.parser')
        captha = soup.find('title')
        captha2 =soup.find('h4')
        product_title = captha.text
        if captha !=None :
                captha= captha.text
        else:
            captha = "Null"
        if captha2 != None :
                captha2 = captha2.text
        else :
            captha2 = "Null"
        print(captha+"\n"+captha2)
        compare = "Enter the characters you see below"
        if resp.status_code == 200:
            if captha != "Page Not Found" and captha2 != compare and captha != "Amazon Sign In" :
                q = 0
        else:
            q = 1
    reviews = soup.findAll('div', {'data-hook':"review"})
    for item in reviews:
        with open('outputs/file.html', 'w', encoding='utf-8') as f:
            f.write(str(item))
        review = {
            'producttitle': soup.title.text.strip(),
            'title': item.find('a', {'data-hook':"review-title"}).text.strip(),
            'rating': item.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
            'review': item.find('span', {'data-hook': 'review-body'}).text.strip() ,
        }
        reviewlist.append(review)  
def totalPages(productUrl):
    for x in productUrl:
        proxies=getRandomProxy()
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        resp = requests.get(productUrl, proxies, headers=headers)#
        with open('response.html', 'w+', encoding="utf-8") as fout:
            fout.write(resp.text+"\n")
        soup = BeautifulSoup(resp.text, 'html.parser')
        reviews = soup.find('div', {'data-hook':"cr-filter-info-review-rating-count"})
        if reviews!= None:
            break
    print(str(c1) +"> "+ str(proxies))
    reviews = str(reviews)
    idx1 = reviews.index("total ratings")
    idx2 = reviews.index("with reviews")
    res = ''
    for idx in range(idx1 + len("total ratings") + 1, idx2):
        res = res + reviews[idx]
    reviews = res.strip()
    return int(reviews)
def main():
    print("Enter Web Address:\n")
    productUrl = input()
    reviewUrl = productUrl.replace("dp", "product-reviews")
    print("Default URL : " + reviewUrl)
    totalPg = totalPages(reviewUrl)
    print("Total reviews : ")
    print(totalPg)
    Pgs = totalPg
    if totalPg < 10:
        Pgs = 10
    Pgs = 10
    for i in range(Pgs//10):
        print(f"Running for page {i+1}")
        try: 
            reviewUrl2 = productUrl.replace("dp", "product-reviews")
            extractReviews(reviewUrl2, i+1)
        except Exception as e:
            print(e)
    df = pd.DataFrame(reviewlist)
    qo = re.sub(r'[^a-zA-Z\s]', '', product_title)
    print(qo)
    df.to_excel(''+qo+'.xlsx', index=False)
    print(df)
    print("\n\nReviews scrapped and exorted in output file")
main()