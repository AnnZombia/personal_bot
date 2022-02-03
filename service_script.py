import os
import time
from telethon import TelegramClient, events, sync
from telethon.tl.functions.users import GetFullUserRequest
import subprocess

dis = ''
discord = None
statusdisc = ''
n = 0


api_id = xxxxxxx 
api_hash = 'xxxxxxxxxxxxxxxxxx'
client = TelegramClient('session_name', api_id, api_hash)
client.start()


user='@'+'zzz'
status = 0
disc = 'offline'
while True:
	with TelegramClient('xxx', api_id, api_hash) as client:
     		full = client(GetFullUserRequest(user))
	if status != full.user.status:
		if full.user.status != None:
			with TelegramClient('xxx', api_id, api_hash) as client:
				client.send_message('yyy', 'Unlocked')
			with TelegramClient('xxx', api_id, api_hash) as client:
				client.send_message('yyy', 'Unlocked')
		else:
			with TelegramClient('xxx', api_id, api_hash) as client:
				client.send_message('yyy', 'Locked')
	
	status = full.user.status
	discord = subprocess.check_output('python3 ./discord_status_check.py', shell = True)
	dis = discord.decode('UTF-8')
	statusdisc = dis.find("offline")
	if statusdisc == -1:
		if n == 0:
			with TelegramClient('zzz', api_id, api_hash) as client:
				client.send_message('yyy', 'Status changed')
			n += 1
	else:
		if n > 0:
			with TelegramClient('yyy', api_id, api_hash) as client:
				client.send_message('yyy', 'Back offline')			
			n = 0	
	time.sleep(15)

client.disconnect()
