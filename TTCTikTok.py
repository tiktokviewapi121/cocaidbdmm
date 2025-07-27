import sys, os, re, json, requests
from datetime import datetime
from time import sleep
import random

os.system("clear")
dau="\033[1;32m~ "
dem=0
os.system('cls' if os.name == 'nt' else 'clear')
banner = f"""
\033[1;33m██████╗    ████████╗ ██████╗  ██████╗ ██╗            
\033[1;35m██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║            
\033[1;36m██║  ██║█████╗██║   ██║   ██║██║   ██║██║            
\033[1;37m██║  ██║╚════╝██║   ██║   ██║██║   ██║██║            
\033[1;32m██████╔╝      ██║   ╚██████╔╝╚██████╔╝███████╗       
\033[1;31m╚═════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  

\033[1;97mTool By: \033[1;32mLiggdzut            \033[1;97mPhiên Bản: \033[1;32m4.0
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mGolike - Instagram\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mliggdzut\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m TikTok\033[1;31m   : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/@liggdzut
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞ \033[1;32mhttps://zalo.me/g/ibcydq552\033[1;97m ☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞ \033[1;32mbotsiuvip22\033[1;97m ☜
\033[97m════════════════════════════════════════════════
"""
print(banner)
print("\033[97m════════════════════════════════════════════════")
cookie=input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Cookie TTC :\033[1;33m ')
tokenfb=input(dau+'Nhập Token Fecabook : ')
healogin={
'Host':'tuongtaccheo.com',
'user-agent':'Mozilla/5.0 (Linux; Android 9; Bee 3) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/95.0.244 Mobile Chrome/89.0.4389.244 Mobile Safari/537.36',
'cookie': cookie,
}
hea={
'Host':'tuongtaccheo.com',
'user-agent':'Mozilla/5.0 (Linux; Android 9; Bee 3) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/95.0.244 Mobile Chrome/89.0.4389.244 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'referer':'https://tuongtaccheo.com/kiemtien/',
'cookie': cookie,
}
heanhan={
'Host':'tuongtaccheo.com',
'user-agent':'Mozilla/5.0 (Linux; Android 9; Bee 3) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/95.0.244 Mobile Chrome/89.0.4389.244 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'origin':'https://tuongtaccheo.com',
'referer':'https://tuongtaccheo.com/kiemtien/',
'cookie': cookie,
}
b= requests.get(f'https://tuongtaccheo.com/home.php', headers=healogin)
u = b.text.split('soduchinh">')[1]
xu = u.split('</strong>')[0]
print(dau+'Xu Hiện Tại: ',xu)

while (True):
 a = requests.get(f'https://tuongtaccheo.com/kiemtien/getpost.php', headers=hea)
 x = a.text.split('idpost":"')[1]
 idlike = x.split('","link')[0]
 print('🌸Đang Like ID: ',idlike) 
 urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
 datalike="access_token="+tokenfb
 da={
'id':idlike,
}
 like=requests.post(urllike, data=datalike)
 nhan=json.loads(requests.post('https://tuongtaccheo.com/kiemtien/nhantien.php',headers=heanhan,data=da).text)
 print(nhan)
 sleep(10)