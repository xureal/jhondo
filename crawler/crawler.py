import os
import openpyxl
import hasher
import runmacros
import win32api
import os.path
import genericvalidate_slim14
import genericvalidate_slim_citi15
import genericvalidatezenith_slim14
import genericvalidate_slim_tca
import genericvalidateadidas
import genericvalidatevisa
import genericvalidate_samsung
import genericvalidate_samsung_crown
import genericvalidatekering_slim15
import shutil
import time

rootDir = r'C:\Users\andptasi\Documents\Temp'
serviceAccountKey = r'C:\Users\andptasi\Documents\scripts\crawler\service_account_key.json'
ts_count = 0
run_count = 0
check_found = 0

# for root, dirs, files in os.walk(rootDir, topdown=True):
# 	if len(files)>0:
# 		for name in files:
# 			tsfilepath = root+'\\'+'Trafficking-template.xlsm'
# 			tsfileloc = tsfilepath.replace('\\','/')
# 			if not os.path.isfile(tsfileloc):
# 				try:
# 					shutil.rmtree(root)
# 					print '\n'
# 					print "Found a folder without a trafficking sheet"
# 					print "The folder location is " + root
# 					print "The folder has been deleted"
# 					print '\n'
# 				except:
# 					continue


for root, dirs, files in os.walk(rootDir, topdown=True):
	if len(files)>0:
		for name in files:
			checkfilepath = root +'\\'+ 'checked.txt'
			checkfileloc = checkfilepath.replace('\\','/')
			if not os.path.isfile(checkfilepath):
				if name.endswith('.xlsm') or name.endswith('.XLSM'):
					#path to the file - windows style
					filepath = root +'\\'+ name
					#path to the check file (that's how the script know that the template has already been processed) - windows style
					checkfilepath = root +'\\'+ 'checked.txt'
					resultsfilepath = root +'\\'+ 'TS_results.txt'
					
					#FOR FILEPATH REFERENCE USE THE 'LOC' variables below instead of the 'PATH' variable above
					
					#path to file converted
					fileloc= filepath.replace('\\','/')
					#path to check file converted
					checkfileloc= checkfilepath.replace('\\','/')			
					pubHash = hasher.pubHash(fileloc)
					#starcom/mediavest template
					if pubHash == '98371f82a3ab0be6876e397ec49cf368':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Starcom template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('THIS IS AN OLD TEMPLATE PLEASE RESUBMIT SHEET ON A NEW TEMPLATE')
						#vResults = genericvalidate.gvalidate(fileloc, root)
						print ('Finished running validation')
						check_found = 1
					#starcom/mediavest template 'lite version'
					if pubHash == '7ad21190b432d2c1889f9514ac4a1c1d':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Starcom SLIM template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('THIS IS AN OLD TEMPLATE PLEASE RESUBMIT SHEET ON A NEW TEMPLATE')
						#vResults = genericvalidate_slim.gvalidate(fileloc, root)
						print ('Finished running validation')
						check_found = 1
					#starcom/mediavest template 'lite version' (version 1.4 with device)
					if pubHash == 'ff39a96cdd74242073222fc89b69ac53':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Starcom SLIM 1.4 template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidate_slim14.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1
					#citi template 'lite version'
					if pubHash == '13b6f5131acb31197ccf8dc33f29d77a':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Citi SLIM template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('THIS IS AN OLD TEMPLATE PLEASE RESUBMIT SHEET ON A NEW TEMPLATE')
						#vResults = genericvalidate_slim_citi.gvalidate(fileloc, root)
						print ('Finished running validation')
						check_found = 1					
					#citi template 'lite version'
					if pubHash == 'fd57bad5d68280d7a81de6fdfeb14626':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('CITI Slim 1.5 template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidate_slim_citi15.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1
					#zenith template
					elif pubHash == 'b4c64b04b47182d53ac09ef76118ff2f':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Zenith template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('THIS IS AN OLD TEMPLATE PLEASE RESUBMIT SHEET ON A NEW TEMPLATE')
						#vResults = genericvalidatezenith.gvalidate(fileloc, root)
						print ('Finished running validation')
						check_found = 1
					#Zenith slim template	
					if pubHash == '3cd113e5d8155537101d4d71b5860507':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Zenith SLIM template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('THIS IS AN OLD TEMPLATE PLEASE RESUBMIT SHEET ON A NEW TEMPLATE')
						#vResults = genericvalidatezenith_slim.gvalidate(fileloc, root)
						print ('Finished running validation')
						check_found = 1			
					#Zenith slim template (version 1.4 with device)
					if pubHash == '68852dcb96e7608240b901712c4c7160':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Zenith SLIM 1.4 template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidatezenith_slim14.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1								
					#TCA slim template	
					if pubHash == 'afee2fcb35dfb198c914acd1d9ab9229':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('TCA Slim template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidate_slim_tca.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1
						
					#visa template
					elif pubHash == '8040d4cd1ab4169e4d037e3cacc4a898':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('VISA template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidatevisa.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
					#adidas template
					#elif pubHash == '902ac1b810dd4d7e51e749bc63c17295': #old hash - delete once new is confirmed.
					#elif pubHash == '59f820d1896c873711498cfa74a5e2bc': #old hash - delete once new is confirmed.
					elif pubHash == '35d895313cd6adaa5d6684957a228224':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Adidas template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidateadidas.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1
					#samsung template
					elif pubHash == '01a3f2b6009de16a6655c15d818e848b':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Samsung template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidate_samsung.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1
					#samsung crown template
					elif pubHash == '41e805f8d06f786d4174afd756316345':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Samsung crown template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidate_samsung_crown.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1
					#kering template (v1.5)
					elif pubHash == 'adcfaa3ae8d7f240b67adf2a0933a5da':
						ts_count += 1
						print ('\n')
						print ('=================')
						print ('Kering template found')
						print ('The file location is: '+fileloc)
						print ('The file hash is: '+pubHash)
						print ('Running validation')
						vResults = genericvalidatekering_slim15.gvalidate(fileloc, root, serviceAccountKey)
						print ('Finished running validation')
						check_found = 1
						
					elif check_found == 0:
						print ('The file location is: '+fileloc)
						print ('Didn\'t find a rule for this template')
						print ('Experienced the Carine error - check the headers of the trafficking sheet, something has been changed.')
						
					try:
						if vResults[0] == 1:
							print ('## There is an error ##')
							print ('## Please check the folder for results of validation ##')
							print ('## Macros have NOT been ran ##')
						else:
							try:
								print ('There are no errors')
								f = open(checkfileloc,'w')
								f.close()
								print ('Created checked file')
								print ('Starting to run macros')
								print (fileloc)
								runmacros.macros(fileloc)
								print ('Finished running macros')
								for files in os.walk(root):
									for filename in files[2]:
										print (filename)
										if 'MK~' in filename or 'adidas' in filename:
											uploadsheetpath = root + '\\' + filename
											uploadsheetname = filename
									print (uploadsheetpath)
								testtestpath = root + '\\' + 'testtest.xlsx'
								run_count += 1
								print ('=================')
								print ('\n')
							except:
								print ('Something went wrong when running macros, check the trafficking sheet before submitting again')
					except Exception as e:
						e_msg = win32api.FormatMessage(-2147352565)
						print (e_msg)
						#print e_msg.decode('CP1251')
						print (e)
					os.system("taskkill /f /im Excel.exe")
			elif name.endswith('.xlsm'):
				ts_count += 1
print ("Found a total of " + str(ts_count) + " trafficking sheets on the drive")
print ("Ran the macros for " + str(run_count) + " out of " + str(ts_count) + " sheets")
				# print '================='
					# print 'Trafficking template found'
					# print 'Macros have already been ran for this template or template is invalid'
					# print '================='
					# print '\n'