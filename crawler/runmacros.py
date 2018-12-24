def macros(filename):
	from win32com.client import Dispatch
	import time
	import pythoncom
	import os
	pythoncom.CoInitialize()

	#filename = r'D:/Users/andptasi/Desktop/templates/Uploads/350.XLSM'
	
	xlApp = Dispatch("Excel.Application")
	xlApp.Visible = 0
	print ('RUNMACROSFILE')
	print (filename)
	xlApp.Workbooks.Open(os.path.abspath(filename))
	print ('running upload macro')
	xlApp.Application.Run("ThisWorkbook.UPLOAD")
	print ("Created upload sheet")
	#time.sleep(5)
	xlApp.Application.Run("ThisWorkbook.TESTTEST")
	print ("Created testtest")
	#time.sleep(5)
	xlApp.ActiveWorkbook.Close(False)
	xlApp.Quit()
	#xl.Workbooks.Close()
	#xl.Run(r'BHARWA')