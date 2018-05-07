import argparse
from oauth2client import file, client, tools
from apiclient.discovery import build
from httplib2 import Http
import config
import dictionaries
import xlrd
import os
from datetime import datetime
import sys

############stupid shit to get started##################

parser = argparse.ArgumentParser(parents=[tools.argparser])
flags = parser.parse_args()

CLIENT_SECRET = 'client_secret.json' # downloaded JSON file
SCOPES = ('https://www.googleapis.com/auth/dfareporting','https://www.googleapis.com/auth/dfatrafficking')

store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    creds = tools.run_flow(flow, store, flags)

DFA = build('dfareporting', 'v3.0', http=creds.authorize(Http()))

print('Connected to Google servers')

##############end stupid shit##########################

#Initialize all of the required variables
rootDir = config.temp_folder
advertiser_name = input("Advertiser Name: ")
sdates_string = []
sdates_date = []
edates_string = []
edates_date = []

#Check if the entered advertiser is in the alias dict of the config file or the main advertiser dict, if not then exit the program
if advertiser_name in config.alias:
    advertiser_id = dictionaries.advertisers(config.alias[advertiser_name])[0]
    campaign_url = dictionaries.advertisers(config.alias[advertiser_name])[1]
    profile_id = dictionaries.advertisers(config.alias[advertiser_name])[2]
elif dictionaries.advertisers(advertiser_name) != 0:
    advertiser_id = dictionaries.advertisers(advertiser_name)[0]
    campaign_url = dictionaries.advertisers(advertiser_name)[1]
    profile_id = dictionaries.advertisers(advertiser_name)[2]
else:
    print('Advertiser doesn\'t exist, please add the advertiser to the dictionary to proceed')
    print('Terminating...')
    sys.exit()


#Go through the temp directory and find the upload sheet, then go through all of the start and end date and add to list
for root, dirs, files in os.walk(rootDir, topdown=True):
	if len(files)>0:
		for name in files:
			if name.endswith('.xls'):
				filepath = root+'\\'+name
				filename = name
				wb = xlrd.open_workbook(filename=filepath)
				sheet = wb.sheet_by_name('Campaign Spreadsheet')
				for i in range(1, sheet.nrows, 1):
					sdate_cell_value = sheet.cell(rowx=i,colx=11).value
					if sdate_cell_value != '':
						sdates_string.append(sdate_cell_value)					
					edate_cell_value = sheet.cell(rowx=i,colx=12).value
					if edate_cell_value != '':
						edates_string.append(edate_cell_value)

#Change the dates from string to date format that is required in DCM
for j in range(0,len(sdates_string),1):
	sdate_object = datetime.strptime(sdates_string[j], '%m/%d/%y').date()
	sdates_date.append(sdate_object)
for k in range(0,len(sdates_string),1):
	edate_object = datetime.strptime(edates_string[k], '%m/%d/%y').date()
	edates_date.append(edate_object)

#Pick the earliest start date and the latest end date from the list of dates
sdate = str(min(sdates_date))
edate = str(max(edates_date))

#Change the filename is using the adidas taxonomy (they have forward slashes in their naming)
if 'adidas' in filename:
	campaign_name = filename[:-9]+'/'+cname[-5:]
else:
    campaign_name = filename[:-4]

create_campaign = DFA.campaigns().insert(body={'advertiserId':advertiser_id,'name':campaign_name,'startDate':sdate,'endDate':edate,'defaultLandingPageId':campaign_url},profileId=profile_id).execute()
print('\n')
print('====CREATED CAMPAIGN====')
print('User profile: '+ str(profile_id))
print('Advertiser ID: '+ str(advertiser_id))
print('Campaign Name: '+ campaign_name)
print('Start Date: '+ sdate)
print('End Date: '+ edate)
print('Default URL ID: '+ str(campaign_url))