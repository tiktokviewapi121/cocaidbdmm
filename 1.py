from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests, json
import os
import sys
import time
from itertools import cycle
from sys import platform
from time import sleep
from datetime import datetime
from time import strftime

total = 0
may = 'mb' if platform[0:3] == 'lin' else 'pc'

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

def bongoc(so):
	for i in range(so):
		print('════', end = '' )
	print('')
class TraoDoiSub_Api (object):
	def __init__ (self, token):
		self.token = token
	
	def main(self):
		try:
			main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False
	def run(self, user):
		try:
			run = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={user}&access_token={self.token}').json()
			try:
				return run['data']
			except:
				return False
		except:
			return False
	def get_job(self, type):
		try:
			get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}')
			return get
		except:
			return False
	
	def cache(self, id, type):
		try:
			cache = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}').json()
			try:
				cache['cache']
				return True
			except:
				return False
		except:
			return False

	def nhan_xu(self, id, type):
		try:
			nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}')
			try:
				xu = nhan.json()['data']['xu']
				msg = nhan.json()['data']['msg']
				job = nhan.json()['data']['job_success']
				xuthem = nhan.json()['data']['xu_them']
				global total
				total+=xuthem
				bongoc(14)
				print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhận Thành Công {job} Nhiệm Vụ | {msg} | Total {total} Xu | {xu} ')
				bongoc(14)
				if job == 0:
					return 0
			except:
				if '"code":"error","msg"' in nhan.text:
					hien = nhan.json()['msg']; print(red+hien, end = '\r'); sleep(2); print(' '*len(hien), end = '\r')
				else:
					print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mNhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
				return False
		except:
			print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mNhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
			return False
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(f'\033[1;32m[\033[1;31m♤\033[1;32m]'+str(i)+vang+']           ',end='\r')
       sleep(1)
  except:
     sleep(dl)
     print(dl,end='\r')

def chuyen(link, may):
	if may == 'mb':
		os.system(f'xdg-open {link}')
	else:
		os.system(f'cmd /c start {link}')

def main():
	os.system("cls" if os.name == "nt" else "clear")
	dem=0
	banner()
	info()
	while True:
		if os.path.exists('Config_TĐS.txt'):
			with open('Config_TĐS.txt', 'r') as f:
				token = f.read()
			tds = TraoDoiSub_Api(token)
			data = tds.main()
			try:
				print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Giữ Lại Tài Khoản '+vang+ data['user'] )
				print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Nhập Access_Token TĐS Mới')
				chon = input(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mNhập Số \033[1;31m: \033[1;36m')
				if chon == '2':
					os.remove('Config_TĐS.txt')
				elif chon == '1':
					pass
				else:
					print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mLựa Chọn Không Hợp Lệ !');bongoc(14)
					continue 
			except:
				os.remove('Config_TĐS.txt')
		if not os.path.exists('Config_TĐS.txt'):
			token = input(f'\n\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mNhập Access_Token TĐS : \033[1;36m')
			with open('Config_TĐS.txt', 'w') as f:
				f.write(token)
		with open('Config_TĐS.txt', 'r') as f:
			token = f.read()
		tds = TraoDoiSub_Api(token)
		data = tds.main()
		try:
			xu = data['xu']
			xudie = data['xudie']
			user = data['user']
			print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mĐăng Nhập Thành Công !')
			sleep(1.5)
			break
		except:
			print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mAccess Token Không Hợp Lệ, Hãy Thử Lại !')
			os.remove('Config_TĐS.txt')
			continue 
	bongoc(14)
	
	os.system("cls" if os.name == "nt" else "clear")
	banner()
	info()
	print(f'\n\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mTên Tài Khoản : \033[1;36m{user} ')
	print(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mXu Hiện Tại : \033[1;36m{xu}')
	print(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mXu Bị Phạt : \033[1;36m{xudie} ')
	while True:
		ntool=0
		bongoc(14)
		print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Chạy Nhiệm Vụ Tim')
		print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Chạy Nhiệm Vụ Follow')
		print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m3\033[1;32m]\033[1;36m Chạy Nhiệm Vụ Follow Tiktok Now')
		nhiem_vu=input(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mNhập Số Để Chạy Nhiệm Vụ : \033[1;36m')
		dl = int(input(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mNhập Delay: \033[1;36m'))
		while True:
			if ntool == 2:
				break
			ntool = 0
			bongoc(14)
			nv_nhan=int(input(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mSau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu : \033[1;36m'))
			if nv_nhan < 8:
				print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mTrên 8 Nhiệm Vụ Mới Được Nhận Tiền !')
				continue
			if nv_nhan > 15:
				print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mNhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi !')
				continue
			user_cau_hinh=input(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mNhập User Name TikTok Cần Cấu Hình : \033[1;36m')
			cau_hinh=tds.run(user_cau_hinh)
			if cau_hinh != False:
				user=cau_hinh['uniqueID']
				id_acc=cau_hinh['id']
				bongoc(14)
				print(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mĐang Cấu Hình ID : {id_acc} | User : {user} | ')
				bongoc(14)
			else:
				print(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mCấu Hinh Thất Bại User : {user_cau_hinh} ')
				continue 
			while True:
				if ntool==1 or ntool==2:break
				if '1' in nhiem_vu:
					listlike = tds.get_job('tiktok_like')
					if listlike == False:
						print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mKhông Get Được Nhiệm Vụ Like              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listlike.text:
						if listlike.json()['error'] == 'Thao Tác Quá Nhanh, Vui Lòng Chậm Lại':
							coun = listlike.json()['countdown']
							print(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mĐang Get Nhiệm Vụ Like, CountDown : {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listlike.json()['error'] == 'Vui Lòng Ấn Nhận Tất Cả Rồi Sau Đó Tiếp Tục Làm Nhiệm Vụ Để Tránh Lỗi !':
							nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE')
						else:
							print(red+listlike.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listlike = listlike.json()['data']
						except:
							print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mHết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listlike) == 0:
							print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mHết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32mTìm Thấy {len(listlike)} Nhiệm Vụ Like                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listlike:
								id = i['id']
								link = i['link']
								chuyen(link, may)
								cache = tds.cache(id, 'TIKTOK_LIKE_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32m{tg} | Tim | {id} |'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;32m{tg} | {TIM} | {id} |')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE')
										if nhan == 0:
											print('\033[1;32m[\033[1;31m♤\033[1;32m] \033[1;33m➩ \033[1;31mNhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Để Thay Nhiệm Vụ ')
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m2\033[1;32m]\033[1;36m Thay Acc Tiktok ')
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhấn [Enter] Để Tiếp Tục')
											chon=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033[1;36m')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											bongoc(14)
				if ntool==1 or ntool==2:break
				if '2' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == 'Thao Tác Quá Nhanh, Vui Lòng Chậm Lại':
							coun = listfollow.json()['countdown']
							print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Get Nhiệm Vụ Follow, CountDown : {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == 'Vui Lòng Ấn Nhận Tất Cả Rồi Sau Đó Tiếp Tục Làm Nhiệm Vụ Để Tránh Lỗi !':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mHết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mHết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTìm Thấy {len(listfollow)} Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								link = i['link']
								chuyen(link, may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{tg} | Follow | {id} |'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{tg} | {FOLLOW} | {id} |')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Thay Nhiệm Vụ')
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Thay Acc Tiktok ')
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhấn [Enter] Để Tiếp Tục')
											chon=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033[1;36m')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											bongoc(14)
				if ntool==1 or ntool==2:break
				if '3' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == 'Thao Tác Quá Nhanh, Vui Lòng Chậm Lại':
							coun = listfollow.json()['countdown']
							print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mĐang Get Nhiệm Vụ Follow, CountDown : {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == 'Vui Lòng Ấn Nhận Tất Cả Rồi Sau Đó Tiếp Tục Làm Nhiệm Vụ Để Tránh Lỗi !':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mHết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mHết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mTìm Thấy {len(listfollow)} Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								uid = id.split('_')[0] 
								link = i['link']
								que = i['uniqueID']
								if may == 'mb':
									chuyen(f'tiktoknow://user/profile?user_id={uid}', may)
								else:
									chuyen(f'https://now.tiktok.com/@{que}', may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{tg} | Follow TikTok Now | {id} |'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32m{tg} | {FOLLOW_TIKTOK_NOW} | {id} |')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Thay Nhiệm Vụ')
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số \033[1;32m[\033[1;31m1\033[1;32m]\033[1;36m Thay Acc Tiktok ')
											print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhấn [Enter] Để Tiếp Tục')
											chon=input(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Số : \033[1;36m')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											bongoc(14)
main()