import config, re, openpyxl, os, shutil, sys, clear
from PIL import Image


#Initizlize all of the required variables
workbook = openpyxl.load_workbook(config.feed_path)
sheet = workbook.get_sheet_by_name(config.feed_sheet)
sizePattern = re.compile("[0-9]{2,4}(x|X)[0-9]{2,4}")
row_count = 0
error_flag = 0
all_flag = 0
issues_flag = 0
tracking_flag = 0
creative_set = set()
size_set = set()
found_set = set()
notfound_set = set()
issues_set = set()

clear.cleanup() # Clear out the upload folder before doing anything

for i in range(1,sheet.max_row,1): #Find the total number of non-empty rows in the testtest sheet
    if sheet['A'+str(i)].value!=None and sheet['A'+str(i)].value!='':
        row_count += 1

for j in range(2,row_count+1,1): #Go through all of the creatives on testtest and add the creative names to a set
    for k in range(2,8,2):
        creative_name = sheet.cell(row=j,column=k).value
        if creative_name != 'Tracking' and creative_name !='' and creative_name != None:
            creative_set.add(creative_name)
        elif creative_name == 'Tracking':
            tracking_flag = 1



for creative in creative_set: #Go through all of the creatives in the set and check if they match the size regex (used for the default creative later)
    try:
        match = re.search(sizePattern, creative).group()
        size_set.add(match)
    except AttributeError:
        #error_flag = 1
        print('Couldn\'t find the size for the following creative - ' + str(creative))

if error_flag == 0: #Check if all of the creative names on testtest have a correct size
    if len(size_set) != 0:
        print('\n')
        print('Found the following sizes:')
        print(size_set)
    print('\n')
else:
    print('Some creatives are missing sizes, please fix the filenames and re-run the script')
    print('Terminating...')
    sys.exit()

for creative in creative_set: #Go through the creative folder and copy all matching filenames into the upload folder
    found_check = 0
    for root, dirs, files in os.walk(config.creative_folder, topdown=True):
        if len(files)>0:
            for name in files:
                if creative in name:
                    found_check += 1
                    found_set.add(creative)
                    shutil.copyfile(config.creative_folder+'\\'+name, config.upload_folder+'\\'+name)
    if found_check == 0:
        all_flag = 1
        notfound_set.add(creative)

for root, dirs, files in os.walk(config.upload_folder, topdown=True): #Go through the upload folder and check the dimensions of the files + create the necessary default creatives
    if len(files)>0:
        for name in files:
            if not name.lower().endswith('.zip') and not name.lower().endswith('.mp4'):
                with Image.open(config.creative_folder+'\\'+name) as im:
                    width, height = im.size
                    match = re.search(sizePattern, name).group()
                    if 'x' in match:
                        dimensions = str(width) + 'x' + str(height)
                    else:
                        dimensions = str(width) + 'X' + str(height)
                    if match != dimensions:
                        print('The dimensions are not matching the label for ' + str(name))
                        issues_set.add(name)
                        issues_flag = 1
                    else:
                        shutil.copyfile(config.upload_folder+'\\'+name, config.upload_folder+'\\'+dimensions+'_default.jpg')

if issues_flag == 1:
    print('\n')
    print('There are issues with the below creatives, please fix the creatives and re-run the script')
    for creatives in issues_set:
        print(creatives)
    print('\n')
    print('Terminating...')
    sys.exit()

if all_flag == 0: #If all the creatives were found and all the labels and dimensions are matching
    print('All creatives found and defaults created, campaign ready to be trafficked')
    if tracking_flag == 1:
        print('There are tracking creatives on the trafficking sheet, make sure to create those before trafficking the campaign')
else: #If some creatives were missing
    print('Found:') #Print out the found set
    for creatives in found_set:
        print(creatives)
    print('\n')

    print('Not Found:') #Print out the not found set
    for creatives in notfound_set:
        print(creatives)

