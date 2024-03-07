# ffuzer
A powerful python script for fuzzing admin panel and subdomain quick and safe, on this script we consider method of bypass firewall detection.

We attached a file with name of (admin_panel_lists) with over 7000 🪙 admin panel lists and filename subdomain_lists with over 800 well known subdomain lists for our purpose that can be used as a wordlist in your fuzzing process.

This script works very well with both version of python2 and python3 without any problem

We use multithreading method for increase speed of fuzzing process

Every success links in your fuzzing process will be logged in a seprate filename "output" that will generate during a execution of script

-------------------------------

<img src="https://github.com/p3ym4nmhp/python-admin-finder/assets/161972215/3622a097-e8b6-42b5-a688-31115fa387e8" alt="python admin finder">

-------------------------------

🔥 Requirements:

This script only works with python2, then you should install python2 on your machine with pip, with below instruction you can install both requirements under 1 minute

1. install python2:

 - apt install -y python

2. install pip:

 - apt install -y pip

😟 Dont worry, rest of libraries and dependencies will install during a execute python script

----------------------------

📌 How to Launch ?

 cd python-admin-finder
 
 python admin_finder.py -u targer_url -w wordlist
