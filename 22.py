import requests, json, os, sys
from threading import Thread
import threading
from datetime import datetime
from time import strftime
from time import sleep
from sys import platform
import requests
import os
import json
import random
from datetime import timezone, datetime, timedelta
import requests
from time import sleep
import threading
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import requests
import socket
from pystyle import *

os.system('cls' if os.name == 'nt' else 'clear')

import sys, time
from colorama import Fore, Style, init
init(autoreset=True)

# Màu sẽ luân phiên theo từng dòng
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]

def slow_print_line(line, color, delay=0.0005):
    """In từng ký tự của 1 dòng với hiệu ứng"""
    for char in line:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    text_banner = """
██████╗░░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██║░░██║█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
""".strip("\n").split("\n")

    for i, line in enumerate(text_banner):
        slow_print_line(line, colors[i % len(colors)], delay=0.0005)

def info():
    text_info = """
Admin Tool : CapyUwU            Phiên Bản : 1.0
════════════════════════════════════════════════
Youtuber : Liggdzut
Zalo : https://zalo.me/g/ibcydq552
📱 Telegram: botsiuvip22
════════════════════════════════════════════════
""".strip("\n").split("\n")

    for i, line in enumerate(text_info):
        slow_print_line(line, colors[i % len(colors)], delay=0.0005)

# Test
banner()
info()

def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address

url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "

ck=input("\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Cookie Facebook Cần Nuôi : \033[1;36m")
idck=re.findall("c_user=.*?;",ck)[0]
idfb=idck.replace("c_user=","").replace(";","")
head={"Host":"mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","cookie":ck}

def like(head):
  link =requests.get("https://mbasic.facebook.com/",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/like.php?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('ft_ent_identifier=.*?&',tcheck)[0].replace("ft_ent_identifier=","").replace("&","")
    print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mLike | {idbv}")
def addfr(head):
  link =requests.get("https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/mobile/friends/add_friend.php?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('id=.*?&',tcheck)[0].replace("id=","").replace("&","")
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mAdd Friends | {idbv}")

def jond(head):
  link =requests.get("https://mbasic.facebook.com/search/groups/?q=Freefire&source=filter&isTrending=0",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/group/join/?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('group_id=.*?&',tcheck)[0].replace("group_id=","").replace("&","")
    print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mJoin Group | {idbv}")
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print(f"\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mStart Raising UID | {idfb}")
print (Colorate.Diagonal(Colors.blue_to_green, "══════════════════════════════════════════════════════════════"))
while(True):
  list=["addfr(head)","like(head)","jond(head)"]
  rd=random.choice(list)
  exec(rd)