#!/usr/bin/env python
# -*- coding: utf8 -*-
######################################################################
# TELEGRAM_ID = '@p3ym4n_mhp'
# _GITHUB = 'https://github.com/p3ym4nmhp'
__AUTHOR__ = 'Peyman Mohammadpour' 
__COMMENT__ = 'ffuzzer version 2.0'
######################################################################
import sys
import os
import random
import time
import threading
#----------------------------------------------------------------------
# import requests
#----------------------------------------------------------------------
try:
	import requests
except:
	os.system('pip install requests')
#---------------------------------------------------------------------
# import colorama
#---------------------------------------------------------------------
try:
	import colorama
except:
	os.system('pip install colorama')
from colorama import Fore,Back
#--------------------------------------------------------------------
# import math
#--------------------------------------------------------------------
try:
	import math
except:
	os.system('pip install python-math')
#--------------------------------------------------------------------
# import dnspython
#--------------------------------------------------------------------
try:
	import dns.resolver
except:
	os.system('pip install dnspython')

print ("""
  ______  ______  _    _  ______ ______ ______  _____  
 |  ____||  ____|| |  | ||___  /|___  /|  ____||  __ \ 
 | |__   | |__   | |  | |   / /    / / | |__   | |__) |
 |  __|  |  __|  | |  | |  / /    / /  |  __|  |  _  / 
 | |     | |     | |__| | / /__  / /__ | |____ | | \ \ 
 |_|     |_|      \____/ /_____|/_____||______||_|  \_\

""")
help = """
Usage: ffuzzer.py [-u] target [-w] wordlist [-s]

Options:
  -v | --version             Show program's version number and exit
  -h             	     Show help message and exit
  -u			     Target URL
  -w	       		     Wordlist for fuzzing
  -s             	     Subdomain fuzzing (Optional)
  -A			     Author name of script
"""

user_agents = ["Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15", "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0", "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"]
if len(sys.argv) == 1:
	print (Fore.WHITE + '[' + Fore.RED + 'Error!' + Fore.WHITE + ']' + ' ' + 'Usage: ' + sys.argv[0] + ' ' + '-u' + ' ' + 'target_url' + ' ' + '-w' + ' ' + 'wordlist')
	sys.exit()
if (len(sys.argv) <= 4) and (sys.argv[1] != '-h') and (len(sys.argv) <= 4) and (sys.argv[1] != '-v') and (len(sys.argv) <= 4) and (sys.argv[1] != '--version') and (len(sys.argv) <= 4) and (sys.argv[1] != '-A'): 
	print (Fore.WHITE + '[' + Fore.RED + 'Error!' + Fore.WHITE + ']' + ' ' + 'Usage: ' + sys.argv[0] + ' ' + '-u' + ' ' + 'target_url' + ' ' + '-w' + ' ' + 'wordlist')
	sys.exit()
if sys.argv[1] == '-u':
	url = sys.argv[2]
elif sys.argv[1] == '-h':
	print (help)
	sys.exit()
elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
	print (Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']' + ' ' +  __COMMENT__)
	print (Fore.RESET + '')
	sys.exit()
elif sys.argv[1] == '-A':
	print (Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']' + ' ' + 'Coded By' + ' ' + __AUTHOR__)
	print (Fore.RESET + '')
	sys.exit()
else:
	print ('Usage: ' + sys.argv[0] + ' ' + '-u' + ' ' + 'target_url' + ' ' + '-w' + ' ' + 'wordlist')
	sys.exit(0)
if not url.startswith("http://") and not url.startswith("https://"):
	print (Fore.WHITE + '[' + Fore.RED + "Error!" + Fore.WHITE + ']' + ' ' + "Please Enter URL Correctly")
	sys.exit(0)
if url.endswith("/"):
	print (Fore.WHITE + '[' + Fore.RED + "Error!" + Fore.WHITE + ']' + ' ' + "Please Enter URL Correctly")
	sys.exit(0)
if sys.argv[3] == '-w':
	wordlist_raw = sys.argv[4]
	if os.path.exists(wordlist_raw):
		wordlist = sys.argv[4]
	else:
		print(Fore.WHITE + '[' + Fore.RED + 'Error!' + Fore.WHITE + ']' + ' ' + 'Wordlist Not Available!')
		sys.exit()
else:
	print ('Usage: ' + sys.argv[0] + ' ' + '-u' + ' ' + 'target_url' + ' ' + '-w' + ' ' + 'wordlist')
	sys.exit(0)

try:
	session = requests.Session()
	headers = {'User-Agent':random.choice(user_agents)}
	url_check = session.get(url,headers=headers,timeout=5)
	status = url_check.status_code
	if status == 200:
		pass
except requests.exceptions.ConnectionError as e:
	print (Fore.WHITE + '[' + Fore.RED + 'Error!' + Fore.WHITE + ']' + ' ' + Fore.WHITE + 'Website Not Available OR You have been blocked by WAF!')
	print (Fore.RESET +'')
	sys.exit(0)

if len(sys.argv) == 6:
		if not sys.argv[5] == '-s':
			print (Fore.WHITE + '[' + Fore.RED + 'Error!' + Fore.WHITE + ']' + ' ' + "Not Acceptable Swith => just use (-s)")
		elif sys.argv[5] == '-s':
			if not os.path.exists('output'):
				os.system('touch output')
			if url.find('www.'):
				url_replace = url.replace('www.','')
				url_split = url_replace.split("//")
			else:
				url_split = url.split("//")
			wordlist_lines = open(wordlist,'r').read().split()
			list_1 = wordlist_lines[:len(wordlist_lines)//5]
			list_2 = wordlist_lines[len(wordlist_lines)//5:len(wordlist_lines)//4]
			list_3 = wordlist_lines[len(wordlist_lines)//4:len(wordlist_lines)//3]
			list_4 = wordlist_lines[len(wordlist_lines)//3:len(wordlist_lines)//2]
			list_5 = wordlist_lines[len(wordlist_lines)//2:len(wordlist_lines)]
			def sub_scanner(path):
				for item in path:
					url2 = item + '.' + url_split[1]
					try:
						ip = dns.resolver.query(url2,'A')
						if ip:
							print (Fore.WHITE + '['+ Fore.GREEN + 'OK' + Fore.WHITE + ']' + ' ' + Fore.WHITE + 'Subdomain Found: => ' + Fore.GREEN + url2)
							open('output','a').write('Subdomain Found: => ' + url2 + '\n')
							print(Fore.RESET + '')
					except:
						print (Fore.WHITE + '['+ Fore.RED + 'NOT' + Fore.WHITE + ']' + ' ' + Fore.WHITE + 'Subdomain Not Exists: => ' + Fore.RED + url2)
						print(Fore.RESET + '')

elif len(sys.argv) == 5:
	read_file_list = open(wordlist,'r').read().split()
	list1 = read_file_list[:len(read_file_list)//5]
	list2 = read_file_list[len(read_file_list)//5:len(read_file_list)//4]
	list3 = read_file_list[len(read_file_list)//4:len(read_file_list)//3]
	list4 = read_file_list[len(read_file_list)//3:len(read_file_list)//2]
	list5 = read_file_list[len(read_file_list)//2:len(read_file_list)]
	if not os.path.exists('output'):
		os.system('touch output')
	def scanner(paths):
		for item in paths:
			url2 = url + '/' + item
			headers2 = {'User-Agent':random.choice(user_agents)}
			try:
				final_req = requests.get(url2,allow_redirects=True,headers=headers2,timeout=5)
				status2 = final_req.status_code
				if status2 == 200:
					print (Fore.WHITE + '['+ Fore.GREEN + 'OK' + Fore.WHITE + ']' + ' ' + Fore.WHITE + 'Directory Found: => ' + Fore.GREEN + url2)
					open('output','a').write('Directory Found: => ' + url2 + '\n')
					print(Fore.RESET + '')
				else:
					print (Fore.WHITE + '['+ Fore.RED + 'NOT' + Fore.WHITE + ']' + ' ' + Fore.WHITE + 'Directory Not Found: => ' + Fore.RED + url2)
					print(Fore.RESET + '')
			except ConnectionError as e:
				print ("Error Connection")
try:
	if len(sys.argv) == 6:
		thread1 = threading.Thread(target=sub_scanner,args=(list_1,))
		thread2 = threading.Thread(target=sub_scanner,args=(list_2,))
		thread3 = threading.Thread(target=sub_scanner,args=(list_3,))
		thread4 = threading.Thread(target=sub_scanner,args=(list_4,))
		thread5 = threading.Thread(target=sub_scanner,args=(list_5,))
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
		thread5.start()
	elif len(sys.argv) == 5:
		thread1 = threading.Thread(target=scanner,args=(list1,))
		thread2 = threading.Thread(target=scanner,args=(list2,))
		thread3 = threading.Thread(target=scanner,args=(list3,))
		thread4 = threading.Thread(target=scanner,args=(list4,))
		thread5 = threading.Thread(target=scanner,args=(list5,))
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
except NameError as e:
	pass

