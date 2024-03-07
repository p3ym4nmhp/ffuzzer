# ffuzzer
A powerful python script for fuzzing admin panel and subdomain quick and safe, on this script we consider method of bypass firewall detection.

We attached a file with name of (admin_panel_lists) with over 7000 🪙 admin panel lists and filename (subdomain_lists) with over 800 well known subdomain lists for our purpose that can be used as a wordlist in your fuzzing process.

This script works very well with both version of python2 and python3 without any problem

We use multithreading method for increase speed of fuzzing process

Every success links in your fuzzing process will be logged in a seprate filename "output" that will generate during a execution of script

-------------------------------

<img src="https://github.com/p3ym4nmhp/ffuzer/assets/161972215/843d61a9-3e8a-41c3-b183-57ec2c022158" alt="python admin finder">

-------------------------------

🔥 Requirements:

This script works with python2 and python3 then you can install python2 or pyhton3 on your machine with pip or pip3, with below instruction you can install both requirements under 1 minute

1. install python2 or python3:

 - sudo apt install -y python | sudo apt install -y python3

2. install pip or pip3:

 - sudo apt install -y pip | sudo apt install -y pip3

😟 Dont worry, rest of libraries and dependencies will install during a execute python script

----------------------------

📌 How to Launch ?

 cd ffuzer
 
 python ffuzer.py -u targer_url -w wordlist      =>   (For Directory Fuzzing)
 
 python ffuzer.py -u targer_url -w wordlist -s   =>   (For Subdomain Fuzzing)

