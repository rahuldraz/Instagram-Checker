#!/usr/bin/python3
#Github https://github.com/rahudraz

import json,requests

cookie=str(input("Enter Cookie:"))
cookie_list=cookie.split(';')
user_id= list(filter(lambda x: "ds_user_id=" in x, cookie_list))[0].split('ds_user_id=')[1]
print ('''
 ___ _   _ ____ _____  _       ____ _               _             
|_ _| \ | / ___|_   _|/ \     / ___| |__   ___  ___| | _____ _ __ 
 | ||  \| \___ \ | | / _ \   | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | || |\  |___) || |/ ___ \  | |___| | | |  __/ (__|   <  __/ |   
|___|_| \_|____/ |_/_/   \_\  \____|_| |_|\___|\___|_|\_\___|_|   

''')

print("[+]Starting")

headers={'Accept':'*/*',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'X-Ig-App-Id': '936619743392459',
'X-Asbd-Id': '198387',
'Origin': 'https://www.instagram.com',
'Referer': 'https://www.instagram.com/',
'Pragma': 'no-cache',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
'Cookie':cookie}
	
try:
    following_data=requests.get("https://i.instagram.com/api/v1/friendships/"+user_id+"/following/?count=0",headers=headers)
    followers_data=requests.get("https://i.instagram.com/api/v1/friendships/"+user_id+"/followers/?count=999999999",headers=headers)
except:
	print("[-]Authentication Failed.\nCheck Cookie\nCookie Must Contain csrf,mid,ds_user_id,rur,sessionid,shbid\n\n")
	exit()

following_data_json=json.loads(following_data.text)
followers_data_json=json.loads(followers_data.text)
followers=[]
following=[]

print("[+]Calculating")

for i in following_data_json['users']:
    following.append(i['username'])
    #print(i['username'])
for i in followers_data_json['users']:
    followers.append(i['username'])
    #print(i['username'])

following.sort
followers.sort

print("[+] Total Following-"+str(len(following)))
print("[+] Total Followers-"+str(len(followers)))


_not_following_back = set(following) - set(followers)

_user_dont_follow = set(followers) - set(following)



print("------------\nThese People Won't Follow You Back\n-----------")
print("[+]Count"+str(len(_not_following_back)))
print(*_not_following_back,sep='\n')




print("------------\nThese People You Won't Follow Back\n------------")
print("[+]Count"+str(len(_user_dont_follow)))
print(*_user_dont_follow,sep='\n')

