import requests
import re
from bs4 import BeautifulSoup
import pyautogui
import time
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import richxerox
import pyperclip
import clipboard
from PIL import Image
import webbrowser
import sys
import random

###############################################################

try: 
    first_item_location= 395, 279
    n= 1
    q= "https://www.guitarcenter.com/Electric-Guitars.gc?N=1076#narrowSideBar"
    webbrowser.open(q)
    while pyautogui.locateOnScreen("images/a.png") == None:
        print("WAITING #1")
        time.sleep(2)
    else:
        pyautogui.hotkey("command","ctrlleft","f")
    while n < 5:
        while pyautogui.locateOnScreen("images/a.png") == None:
            print("WAITING #2")
            time.sleep(2)
        else: 
            pyautogui.keyDown("command")
            pyautogui.click(first_item_location)
            time.sleep(2)
            safari_first_tab_location= 925, 49
            pyautogui.click(safari_first_tab_location)
        while pyautogui.locateOnScreen("images/c.png") == None:
            print("WAITING #3")
            time.sleep(2)
        else: 
            browser_url_location= 661, 19
            pyautogui.click(browser_url_location)
            pyautogui.hotkey("command","c")
            w= clipboard.paste()
            w= str(w)
            page = requests.get(w)
            soup = BeautifulSoup(page.content, "html.parser")
            #TITLE
            my_table = soup.find("h1", {"class": "jsx-4061264120"})
            xxxlist= []
            xxxlist.append(my_table.text)
            #PRICE
            e= soup.find("span", {"class":"price-format text-2xl md:text-4xl sale-price flex-shrink-0 w-full md:flex-shrink-1 md:w-auto"})
            xxxlist.append(e.text)
            #DESRIPTION
            r= soup.find("div",{"class":"jsx-3369637344 description-content gc-font-light mb-8 px-4 md:px-0"})
            print(r, "R-----------")
            if r == None: 
                print("NO DESCRIPTION")
            else:
                xxxlist.append(r.text) 
            #IMAGE
            t= soup.find("img",{"alt":"product middle image number 1"})
            y= t["src"]
            pyautogui.hotkey("command","t")
            pyautogui.click(browser_url_location)
            pyautogui.write(y)
            pyautogui.keyDown("enter")
            time.sleep(5)
            pyautogui.hotkey("command","s")
            time.sleep(5)
            p= str(random.random())
            pyautogui.write(p)
            pyautogui.keyDown("enter")
            pyautogui.hotkey("command","w")
            time.sleep(1)
            pyautogui.hotkey("command","w")
            print(xxxlist)
            s= xxxlist[0]
            d= s.replace("Used","")
            c= d.replace("Electric Guitar","")

            #print(d, "D")
        #EBAY
        pyautogui.hotkey("command","t")
        u= "https://www.ebay.com/sl/prelist/suggest"
        pyautogui.click(browser_url_location)
        pyautogui.write(u)  
        pyautogui.keyDown("enter")
        while pyautogui.locateOnScreen("images/c.png") == None:
            print("WAITING #4")
            time.sleep(2)
        else: 
            ebay_input_field_first= 257, 232
            pyautogui.click(ebay_input_field_first)
            #i= xxxlist[0]
            #TEXT ENTERED INTO EBAY
            pyautogui.write(c[0:35])
            #CLICK SUMBIT BUTTON - LOOKING GLASS ICON
            a= pyautogui.locateOnScreen("images/g.png")[0:2]
            pyautogui.click(a) 

        #CHECKS FOR PAGE LOADED
        while pyautogui.locateOnScreen("images/e.png") == None:
            print("WAITING #5")
            time.sleep(1)
        else:
            #CLICKS "VIEW POSSIBLE MATCHES"
            o= pyautogui.locateOnScreen("images/f.png")[0:2]
            pyautogui.click(o)

        #SELF REFERRING PAGE LOAD CHECK
        for x in range(2):
            if pyautogui.locateOnScreen("images/h.png") == None:
                print("WAITING #6")
                time.sleep(1)
            else:
                #CLICKS "CONTINUE WITHOUT SELECTION"
                f= pyautogui.locateOnScreen("images/h.png")[0:2]
                pyautogui.click(f)

        #SELF REFERRING PAGE LOAD CHECK
        while pyautogui.locateOnScreen("images/i.png") == None:
            print("WAITING #7")
            time.sleep(2)
        else:
            #CLICKS "USED"
            g= pyautogui.locateOnScreen("images/i.png")[0:2]
            pyautogui.click(g)
        #SELF REFERRING PAGE LOAD CHECK
        while pyautogui.locateOnScreen("images/j.png") == None:
            print("WAITING #8")
            time.sleep(2)
        else:
            #CLICKS "NEXT"
            h= pyautogui.locateOnScreen("images/j.png")[0:2]
            pyautogui.click(h)

        #SCROLLS THROUGH PAGE TO FIND MARK
        while pyautogui.locateOnScreen("images/k.png") == None:
            print("WAITING #9")
            pyautogui.keyDown("down")
            pyautogui.keyDown("down")
            pyautogui.keyDown("down")
        else:
            #CLICKS "ADD FROM COMPUTER" PICTURE
            j= pyautogui.locateOnScreen("images/k.png")[0:2]
            pyautogui.click(j)
            time.sleep(2)
            pyautogui.keyDown(p[0])
            pyautogui.keyDown(p[1])
            pyautogui.keyDown(p[2])
            pyautogui.keyDown("enter")

        while pyautogui.locateOnScreen("images/l.png") == None:
            print("WAITING #10")
            pyautogui.keyDown("down")
            pyautogui.keyDown("down")
            pyautogui.keyDown("down")
        else:
            #CLICKS "FONT INPUT FIELD" PICTURE
            k= pyautogui.locateOnScreen("images/l.png")[0:2]
            pyautogui.click(k)
            time.sleep(.5)
            pyautogui.click(k)
            pyautogui.keyDown("tab")
            pyautogui.keyDown("tab")
            for c in range(35):
                pyautogui.hotkey("fn","delete")
            #TITLE
            pyautogui.write(xxxlist[0])
            pyautogui.write(". ")
            if len(xxxlist) == 3:
                #DESCRIPTION
                pyautogui.write(xxxlist[2])
            else:
                print("NO DESCRIPTION")
            pyautogui.write("Minimum Bid: ")
            #PRICE 
            pyautogui.write(xxxlist[1])
            pyautogui.write(". ")

            #PICTURE
            pyautogui.keyDown("tab")
            pyautogui.write("10")
            pyautogui.keyDown("tab")
            pyautogui.write("1")
            pyautogui.keyDown("tab")
            pyautogui.write("60")
            pyautogui.keyDown("tab")
            pyautogui.write("11.5")
            pyautogui.keyDown("tab")
            pyautogui.write("10")
            pyautogui.keyDown("tab")
            pyautogui.keyDown("tab")
            time.sleep(4)
            v= pyautogui.locateOnScreen("images/o.png")[0:2]
            pyautogui.click(v)
            time.sleep(1)
            b= pyautogui.locateOnScreen("images/p.png")[0:2]
            pyautogui.click(b)

            last_click_location_random= 140,340
            pyautogui.click(last_click_location_random)
            pyautogui.hotkey("command","down")
            time.sleep(1)

            #CLICK "LIST IT"
            z= pyautogui.locateOnScreen("images/n.png")[0:2]
            pyautogui.click(z)
            time.sleep(1)
            pyautogui.click(z)
            time.sleep(4)
            pyautogui.hotkey("command","w")
            time.sleep(3)
            pyautogui.keyDown("enter")
            n+=1
            first_item_location=first_item_location[0]+275,first_item_location[1]
            if n==5:
                n=1
            else: 
                print("NOT EXCEEDING 5")


except KeyboardInterrupt:
    sys.exit()


#HAVE TO FIX BRAND :()