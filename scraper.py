from bs4 import BeautifulSoup
import requests

def bynogame():
    url ="https://www.bynogame.com/tr/oyunlar/knight-online/gold-bar"
    try:
        r = requests.get(url)
        res = BeautifulSoup(r.content,"html.parser")
        data = res.find_all("form",attrs={"action":"/tr/satis-onay"})
    except:
        data = ""

    my_dict = dict()

    keys = list()
    if len(data):
        for i in range(len(data)):
            keys.append(float((data[i].text.split()[0])))
    else:
        keys = ["Hata"]*9

    my_dict.update({'Sirius': keys[0]})
    my_dict.update({'Vega': keys[1]})
    my_dict.update({'Altar': keys[2]})
    my_dict.update({'Destan': keys[3]})
    my_dict.update({'Olympia': keys[4]})
    my_dict.update({'Ares': keys[5]})
    my_dict.update({'Diez': keys[6]})
    my_dict.update({'Gordion': keys[7]})
    my_dict.update({'Rosetta': keys[8]})
    x = dict(sorted(my_dict.items())).values()


    return x

def kopazar():
    url = "https://www.kopazar.com/knight-online-gold-bar"
    try:
        r = requests.get(url)
        res = BeautifulSoup(r.content, "html.parser")
        data = res.find_all("strong", attrs={"class" : "caret-up"})
    except:
        data = ""

    my_dict = dict()

    keys = list()
    if (len(data)):
        for i in range(len(data)) :
            keys.append(float((data[i].text.split()[0].replace(".","")[:-1])))
    else:
        keys = ["Hata"]*9

    my_dict.update({'Altar' : keys[0]})
    my_dict.update({'Vega' : keys[1]})
    my_dict.update({'Sirius' : keys[2]})
    my_dict.update({'Ares' : keys[3]})
    my_dict.update({'Diez' : keys[4]})
    my_dict.update({'Gordion' : keys[5]})
    my_dict.update({'Rosetta' : keys[6]})
    my_dict.update({'Olympia' : keys[7]})
    my_dict.update({'Destan' : keys[8]})
    x = dict(sorted(my_dict.items())).values()
    return x

def oyuneks():

    url = "https://oyuneks.com/game-gold/knight-online-goldbar-alim-satim"
    try:
        r = requests.get(url)
        res = BeautifulSoup(r.content, "html.parser")
        data = res.find_all("div", class_="satinal")
    except:
        data = ""

    my_dict = dict()

    keys = list()
    for i in range(len(data)) :
        keys.append(float((data[i].text.split()[2][1:].replace(",","")[:-1])))

    my_dict.update({'Sirius' : keys[0]})
    my_dict.update({'Altar' : keys[1]})
    my_dict.update({'Destan' : keys[2]})
    my_dict.update({'Vega' : keys[3]})
    my_dict.update({'Rosetta' : keys[4]})
    my_dict.update({'Olympia' : keys[5]})
    my_dict.update({'Ares' : keys[6]})
    my_dict.update({'Diez' : keys[7]})
    my_dict.update({'Gordion' : keys[8]})
    x = dict(sorted(my_dict.items())).values()
    return x

def oyunfor():

    url = "https://www.oyunfor.com/knight-online/gb-gold-bar"
    try:
        r = requests.get(url)
        res = BeautifulSoup(r.content, "html.parser")
        data = res.find_all("div", class_="sellToUsBtn")
    except:
        data = ""
    my_dict = dict()

    keys = list()
    for i in range(len(data)) :
        keys.append(float(data[i].text.split()[2].replace(".",""))/10)

    my_dict.update({'Altar' : keys[0]})
    my_dict.update({'Sirius' : keys[2]})
    my_dict.update({'Vega' : keys[4]})
    my_dict.update({'Destan' : keys[6]})
    my_dict.update({'Rosetta' : keys[8]})
    my_dict.update({'Diez' : keys[10]})
    my_dict.update({'Ares' : keys[12]})
    my_dict.update({'Olmpia' : keys[14]})
    my_dict.update({'Gordion' : keys[16]})
    x = dict(sorted(my_dict.items())).values()
    return x

