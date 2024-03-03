#!/usr/bin/python2
# -*- coding: utf8 -*-
######################################################################
# Author = 'peyman mohammadpour' 
# Telegram ID = '@p3ym4n_mhp'
# Githubc= 'https://github.com/p3ym4nmhp'
# Comment = 'Admin Panel Version 1.1'
######################################################################
import sys
import os
import random
import time
import math
start_script = time.time()
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

print ("""

░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
███████║██║░░██║██╔████╔██║██║██╔██╗██║  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
""")

user_agents = ["Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15", "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0", "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"]

if len(sys.argv) <= 4:
	print ('Usage: ' + sys.argv[0] + ' ' + '-u' + ' ' + 'target_url' + ' ' + '-w' + ' ' + 'wordlist')
else:
	if sys.argv[1] == '-u':
		url = sys.argv[2]
	else:
		 print ('Usage: ' + sys.argv[0] + ' ' + '-u' + ' ' + 'target_url' + ' ' + '-w' + ' ' + 'wordlist')
		 sys.exit(0)
	if not url.startswith("http://") and not url.startswith("https://"):
		print ("Error! Please Enter URL Correctly")
		sys.exit(0)
	else:
		if url.endswith("/"):
			print ("Error! Please Enter URL Correctly")
			sys.exit(0)
	session = requests.Session()
	headers = {'User-Agent':random.choice(user_agents)}
	url_check = session.get(url,headers=headers)
	status = url_check.status_code
	try:
		if status == 200:
			pass
	except requests.exceptions.ConnectionError as e:
		print ("Website Not Available!")
		sys.exit(0)
	if sys.argv[3] == '-w':
		wordlist = sys.argv[4]
	else:
		print ('Usage: ' + sys.argv[0] + ' ' + '-u' + ' ' + 'target_url' + ' ' + '-w' + ' ' + 'wordlist')
		sys.exit(0)
	try:
		read_file = open(wordlist,'r').read().split()
		for item in read_file:
			url2 = url + '/' + item
			headers2 = {'User-Agent':random.choice(user_agents)}
			final_req = requests.get(url2,headers=headers2,timeout=5)
			status2 = final_req.status_code
			if status2 == 200:
				print (Fore.WHITE + '['+ Fore.GREEN + 'OK' + Fore.WHITE + ']' + ' ' + Fore.WHITE + 'Admin Panel: => ' + Fore.GREEN + url2)
				print(Fore.RESET + '')
			else:
				print (Fore.WHITE + '['+ Fore.RED + 'NOT' + Fore.WHITE + ']' + ' ' + Fore.WHITE + 'Login Error: => ' + Fore.RED + url2)
				print(Fore.RESET + '')
	except Exception as e:
		print ("Wordlist Not Found")
end_script = math.ceil(time.time() - start_script)

print (Fore.WHITE + '[' + Fore.BLUE + 'END' + Fore.WHITE +']' + ' '  + 'Script Finished: => ' + str(end_script) + ' seconds')
print(Fore.RESET)
