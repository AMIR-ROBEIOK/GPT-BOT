#Bot Gpt
from pyrubi import Bot
from re import findall
import json
import requests
import random
import shutil

guid =input("گوید گپ : ")
guid_ch=input("گوید چنل : ")

bot = Bot=input("اوت اکانت : ")

ekhtar = []

def zzz():
	return f'''🔸 کاربر @@{name}@@({us_guid}) برای استفاده از ربات باید حتما در کانال زیر عضو شوید

https://rubika.ir/member_rubiza

 " اگر قبلا عضو شده اید و با این پیام مواجه شدید یک بار لفت بدین و دوباره عضو بشین "'''

def ek_k():
	try:
		ekhtar.append(update.author_id())
		coun = int(ekhtar.count(update.author_id()))
		if coun == 1:
			bot.send_text(guid,f"کاربر @@{name}@@({us_guid}) شما 1 اخطار از 3 اخطار را دریافت کرده اید ♦️",message_id=msg_id)
			print(bot.delete_message(guid,[msg_id]))
		elif coun == 2:
			bot.send_text(guid,f"کاربر @@{name}@@({us_guid}) شما 2 اخطار از 3 اخطار را دریافت کرده اید ♦️",message_id=msg_id)
			print(bot.delete_message(guid,[msg_id]))
		elif coun == 3:
			bot.send_text(guid,f"کاربر @@{name}@@({us_guid}) شما 3 اخطار دریافت کرده اید پس اکنون از گروه حذف میشوید ♦️",message_id=msg_id)
			print(bot.delete_message(guid,[msg_id]))
			bot.ban_chat_member(guid,us_guid)
	except:pass

for update in bot.on_message():
    try:
    	if update.chat_id() == guid:
    		msg_id = update.message_id()
    		text = update.text()
    		us_guid = update.author_id()
    		name = update.author_title()
    		print(text)
    		if findall(r"@",text) or findall(r"http",text) or findall(r"https",text) or findall(r"rubika.ir",text) or findall(r"www",text):
    			ek_k()
    		if text.startswith("+"):
    			if not us_guid in bot.get_chat_members(guid_ch):
    				bot.send_text(guid,zzz(),message_id=msg_id)
    			else:
    				if findall(r"کیر",text) or findall(r"کص",text) or findall(r"واژن",text) or findall(r"آلت",text) or findall(r"جق",text) or findall(r"جنده",text) or findall(r"کون",text) or findall(r"ساک",text) or findall(r"سکس",text) or findall(r"جنس",text) or findall(r"حامله",text) or findall(r"بچه",text) or findall(r"باردار",text) or findall(r"ارضا",text):
    					ek_k()
    				else:
    					bot.send_text(guid,f"کاربر @@{name}@@({us_guid}) در حال پردازش سوال شما . . .",message_id=msg_id)
    					n = text.split("+")[1]
    					print(n)
    					p = n.replace(" ","‌")
    					lo = requests.get(f"https://nahanabzar.ir/ai?text={p}").text
    					print(lo)
    					gptext = json.loads(lo)['answer']
    					print(gptext)
    					u=bot.send_text(guid,f"جواب سوال کاربر @@{name}@@({us_guid}) :\n\n" + '" ' + gptext + ' "',message_id=msg_id)
    					print(u)
    		elif text.startswith("logo"):
    			if not us_guid in bot.get_chat_members(guid_ch):
    				bot.send_text(guid,zzz(),message_id=msg_id)
    			else:
    				if findall(r"kir",text) or findall(r"kos",text) or findall(r"fuck",text) or findall(r"alt",text):
    					ek_k()
    				else:
    					bot.send_text(guid,f"کاربر @@{name}@@({us_guid}) لطفاً صبور باشید . . .",message_id=msg_id)
    					svc = text.split("logo ")[1]
    					xcz = str(random.randint(1,138))
    					poo = svc.replace(" ","‌")
    					getimg = requests.get(f"http://haji-api.ir/ephoto360?type=text&id={xcz}&text={poo}", stream = True)
    					with open("Rasoul.png",'wb') as f:
    						shutil.copyfileobj(getimg.raw, f)
    						bot.send_image(guid,"Rasoul.png",caption=f"کاربر @@{name}@@({us_guid}) لوگو شما آماده شد 😍🖼️",message_id=msg_id)
    except:pass
