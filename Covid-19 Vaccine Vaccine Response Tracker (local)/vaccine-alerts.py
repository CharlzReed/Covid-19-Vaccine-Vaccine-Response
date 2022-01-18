# Vaccine Alerts (Vaccine Alerts.py)
# Charlie Reed
# 4/10/2021
#========================

# Imports
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from random import randint
from time import sleep
import pyautogui as f
import datetime
import discord
import sys


###########################################################################################################################################################################################################################################################################################


def search():
	# the url of the websites


	options = [
		'https://ca.apm.activecommunities.com/yorkregion/Activity_Search?detailskeyword=&IsAdvanced=True&ddlSortBy=Simple+Date&ActivityCenterID=12&ActivityTypeID=25&SearchFor=2&SearchLevelID=2&NumberOfItemsPerPage=100&IsSearch=true', 
		'https://ca.apm.activecommunities.com/yorkregion/Activity_Search?detailskeyword=&IsAdvanced=True&ddlSortBy=Simple+Date&ActivityCenterID=71&ActivityTypeID=25&SearchFor=2&SearchLevelID=2&NumberOfItemsPerPage=100&IsSearch=true',
		'https://ca.apm.activecommunities.com/yorkregion/Activity_Search?detailskeyword=&IsAdvanced=True&ddlSortBy=Simple+Date&ActivityCenterID=75&ActivityTypeID=25&SearchFor=2&SearchLevelID=2&NumberOfItemsPerPage=100&IsSearch=true',
		'https://ca.apm.activecommunities.com/yorkregion/Activity_Search?detailskeyword=&IsAdvanced=True&ddlSortBy=Simple+Date&ActivityCenterID=73&ActivityTypeID=25&SearchFor=2&SearchLevelID=2&NumberOfItemsPerPage=100&IsSearch=true'
	]
	# Georgina Ice Palace
	# Richmond Green Sports Centre
	# Aaniin Community Centre
	# Maple Community Centre

	for links in options:
		sleep(.5)

		try:
			# urlopen is what allows us to read the html from the website
			webPage = urlopen(links)

			# reads the webpage
			html_page = webPage.read()

			# parses the html
			daSoup = soup(html_page, 'html.parser')

			id_1_2_3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ,'10']

			for i in id_1_2_3:
				for x in daSoup.find_all('span', attrs = {'id': 'ctl05_ctlSearchLayout_ctl01_ctl01_ctlIPGridView_GridViewRow{nums}_Label_name_{numz}'.format(nums = i, numz = i)}):
					day = x.find_all(string=True)
					day = day[0]+'.'
					sleep(.5)
				for x in daSoup.find_all('span', attrs = {'id': 'ctl05_ctlSearchLayout_ctl01_ctl01_ctlIPGridView_GridViewRow{nums}_Label_numberopenings_{numz}'.format(nums=i, numz=i)}):
					num = x.find_all(string=True)
					num = int(num[0])
					if num <= 2:
						num = 0
					print('{day}\n\nSpots available: {num}\n\nClick Here---> {link}'.format(day=day, num=num, link=links))
					print()
					print()
					print()
					print()
					if num >= 3:
						return 	'```{day}\n\nSpots available: {num}\n\n```Click Here---> {link}'.format(day=day, num=num, link=links)


		except:
			return '\nAn error occurred :('


###########################################################################################################################################################################################################################################################################################


# Client for discord
client = discord.Client()

# Calling a cleint event when bot goes online and printing message
@client.event
async def on_ready():
	# Tells the bot which channel to read and send messages to
	chat = client.get_channel(830179043084337185)
	
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=' for vaccines!')) # Status message

	alerts_left = 100
	im_still_here_btw = 0
	while True:

		noises = ['sneeze', 'cough', 'sniffle', 'yawn']
		im_still_here_btw += 1
		print(im_still_here_btw)
		if im_still_here_btw % 45 == 0: # Every 45 minutes
			await chat.send(noises[randint(0,3)]) # Broadcasting message

		link = search()
		if link != None:
			await chat.send('{link}'.format(link=link), tts = False) # Broadcasting message

			alerts_left -= 1
			if alerts_left <= 0:
				sleep(5)
				await chat.send('_ _\n\n\n\n\n\n\n\n\n\nYou got 100 possible chances.....   no more alerts for you.') # Broadcasting message
				sleep(1)
				sys.exit()
		sleep(60)

# Client ID for the bot
client.run('ODMwMTgwMDkwMzg1NzkzMDk0.YHC7dQ.70HnldkyChyEfj97yN5HKtOU7rM')


################################################################################################################################################################################################
