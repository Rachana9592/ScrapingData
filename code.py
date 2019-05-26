import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import array
import re
import xlwt
from xlwt import Workbook
import csv
import xlsxwriter
import urllib.request
import zipfile
import os


def download_img(src,disease):
    # print(src)

    # for d in range(0,17):
    if (src[0] == '/'):
        src = 'http://www.agriculture.gov.au' + src
        print(src)

            # print(src)
            # src.save("/Users/rajeevsaxena/Desktop/images", ".jpg")

        urllib.request.urlretrieve(src, "/Users/rajeevsaxena/Desktop/images/file_%s.jpg"%disease)
         # print(v1)

        # src_fname, ext = os.path.splitext(src)  # split filename and extension
    return

def web_page1(data):
    # global df
    '''go to link provided
    ,inspect the HTML page
    ,find the class name in div
    ,return the details such as title,image_link,second page link etc........'''
    # print(data.text)
    soup = BeautifulSoup(data.text, 'html.parser')
    # print(soup)
    web = soup.find(class_="flex-container")
    # print(web)
    # find all instances of that class
    web_list = web.find_all(class_='flex-item')
    d1=[]
    t1=[]
    i1=[]
    l=[]
    for i in web_list:
        disease = i.text
        # print(disease)
        # print(disease)
        ref = i.a
        title = ref.get('title')
        # print(title)
        link = ref.get('href')
        # print(link)

        img = ref.img['src']
        download_img(img,disease)

        # print(img)
        d1.append(disease)
        t1.append(title)
        i1.append(img)
        l.append(link)
    # download_img(i1)
    # print(len(l))
    # print(l)
    # df = l_data1(l)
    # print(df)

    # print(len(l1),len(d1))
    df1 = pd.DataFrame({'disease': d1,'image_link': i1,'secondLink': l})

    # print(df1)
    # final_df=pd.concat(df1,df)
    # print(final_df
    # df({'disease': d1, 'title': t1, 'image_link': i1, 'link': l1})
    # print(df)
    # print(df)
    # return df1
    return df1,l

def link_data1(link):
    # print(link)
    for l in link:
        # print(l)
        # for values in link_data2(l):
        #     print(type(values))
        #     df=i
        df=link_data2(l)
        # print(df)
    return df


def link_data2(l):
    # print(l[0:15])
    lis=[]
    if (l[0] == '/'):
        l = 'http://www.agriculture.gov.au' + l
        # print(l)
        df=web_page2(l)
        # x,y,z=next(df)
        # print(x,y,z)
    return #df
df = pd.DataFrame()

def suspect_specimens(soup1):
    '''get data for Secure any suspect specimens
       '''
    web2 = soup1.find_all("h3", class_="trigger")
    # print(web2.find_all("h3").findNext("h3"))
    # secondP1 = web2.find("p").findNext("p")
    # web3 = web2.findAll("a", id_="collapsible-trigger-link-2")
    # web3=web2.find_all('a')
    web3 = web2[-1]
    # quote1 = web3.blockquote
    web4 = web3.findNext("div")
    web5 = web4.find_all('p')
    web6 = ''.join(web4.findAll(text=True))
    # print("*******************")
    # print(web6)
    return web6

def legally_in_austelia(soup1):
    web2 = soup1.find_all("h3", class_="trigger")
    # print(web2.find_all("h3").findNext("h3"))
    # secondP1 = web2.find("p").findNext("p")
    # web3 = web2.findAll("a", id_="collapsible-trigger-link-2")
    # web3=web2.find_all('a')
    web3 = web2[-2]
    # print(web3)
    # quote1 = web3.blockquote
    web4 = web3.findNext("div")
    web5 = web4.find_all('p')
    web6 = ''.join(web4.findAll(text=True))
    # print("\n")
    # print("*******************")
    # print(web6)
    return web6


def web_page2(l):
    pest_disease = requests.get(l)
    # print(pest_disease.text)

    soup1 = BeautifulSoup(pest_disease.text, 'html.parser')
    # print(suspect_specimens(soup1))
    # legally_in_austelia(soup1)
    print(legally_in_austelia(soup1))
    # p = re.compile('origin:*')
    # print(soup1.find_all(p))
    # print(soup1.h1.next_sibling)
    # print(len(soup1.strings))



    web1 = soup1.find_all(class_="pest-header-content")
    # print(web1)

    in1 = []
    o = []
    d = []
    l1 = []

    f=[]
    for p in web1:
        l1.append(l)
        secondP = p.find("p").findNext("p")
        insects = secondP.find("strong").nextSibling
        # print(insects, sep="******")
        origin = secondP.find("strong").nextSibling.next.next.next.next
        # print(insects)
        # print(origin)
        distribution = secondP.find("strong").nextSibling.next.next.next.next.next.next.next.next
        # print(distribution)
        # print(insects,origin,distribution)
        in1.append(insects)
        o.append(origin)
        d.append(distribution)
    df1 = pd.DataFrame({'insects': in1, 'origin': o, 'distribution': d})
    df2=pd.DataFrame(df1)
    # print(df2)

    # web2=soup1.find_all(data-hash_="secure-any-suspect-specimens")

    return #insects,origin,distribution




data = requests.get('http://www.agriculture.gov.au/pests-diseases-weeds/plant#identify-pests-diseases')
# print(data)
# for values in web_page1(data):
    # print(values)

df1,link=web_page1(data)
# final_df=df1[df1['secondLink'].astype(str).str[0]=='/']
#
# final_df.to_csv("/Users/rajeevsaxena/Desktop/mine.csv", index=False)
# df_new = pd.read_csv('/Users/rajeevsaxena/Desktop/mine.csv')
# writer = pd.ExcelWriter('/Users/rajeevsaxena/Desktop/data_file.xlsx')
# df_new.to_excel(writer, index = False)
# writer.save()

# df1.to_csv("/Users/rajeevsaxena/Desktop/mine.csv")
# print(df1)
# for j in df1['secondLink']:
#     if (j[0] == '/'):
#         print(df1)
    # print(i[0])
# print(df1)
df2=link_data1(link)
