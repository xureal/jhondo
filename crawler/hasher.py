def pubHash(filename):
	import hashlib
	import openpyxl
	# try:
	wb = openpyxl.load_workbook(filename)
	sheet = wb['Media Plan']
	hashString = ''
	for p in range(1,26,1):
		hashString += str(sheet.cell(row=11,column=p).value)
	TSHash = hashlib.md5(hashString.encode('utf-8')).hexdigest()
	return TSHash
	# except:
	# 	return 1