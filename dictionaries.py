'''
This is the dictionaries file that is used by multiple other python scripts. It stores the profile IDs and the advertiser IDs from all of the networks.

Do not modify this file yourself, if you need to add new advertisers please contact the person managing the list. If you want to change the keys for certain advertisers, you can change them in the config file.
'''
import config

def profiles(x,y):

    choices = {
        'Starcom' : {'Andy': 1937694, 'Varun' : 911682, 'Janani' : 2744611, 'Ali' : 4511530, 'Vlad' : 4774182},
        'Zenith' : {'Andy': 2763125, 'Varun' : 913440, 'Janani' : 2871989, 'Ali' : 4529198, 'Vlad' : 4796317},
        'Visa' : {'Andy': 1970754, 'Varun' : 2871110, 'Janani' : 2795904, 'Ali' : 4541315, 'Vlad' : 4795709},
        'Adidas' : {'Andy': 2649258, 'Varun' : 2654502, 'Janani' : 4044150, 'Ali' : None, 'Vlad' : None},
        'Reebok' : {'Andy': 3038017, 'Varun' : 3033621, 'Janani' : 3034081, 'Ali' : None, 'Vlad' : None},
        'EA' : {'Andy': 2556446, 'Varun' : 2559822, 'Janani' : 4126377, 'Ali' : None, 'Vlad' : None},
        'Kraft' : {'Andy': 4271839, 'Varun' : 4284476, 'Janani' : 4261017, 'Ali' : None, 'Vlad' : None},
        'Etihad' : {'Andy': 1967569, 'Varun' : 1729030, 'Janani' : None, 'Ali' : None, 'Vlad' : None},
        'Citibank' : {'Andy': 2649058, 'Varun' : 2646069, 'Janani' : 2794746, 'Ali' : None, 'Vlad' : None},
        'ALJ' : {'Andy': 2907526, 'Varun' : 2904780, 'Janani' : 2903983, 'Ali' : None, 'Vlad' : None},
        'Net-a-porter' : {'Andy': 2912422, 'Varun' : 2914609, 'Janani' : 2914607, 'Ali' : None, 'Vlad' : None},
        'Nestle' : {'Andy': 4288811, 'Varun' : 4291247, 'Janani' : 4290977, 'Ali' : None, 'Vlad' : None},
        'Mondelez' : {'Andy': 4003138, 'Varun' : 4001486, 'Janani' : 4004266, 'Ali' : 4491075, 'Vlad' : None},
        'Maserati' : {'Andy': 4132905, 'Varun' : 4148575, 'Janani' : None, 'Ali' : None, 'Vlad' : None},
        'Abu Dhabi Tourism' : {'Andy': 4197959, 'Varun' : 4172892, 'Janani' : 4187605, 'Ali' : 4532032, 'Vlad' : 4796900},
        'McDonalds' : {'Andy': 4280186, 'Varun' : 4256139, 'Janani' : 4263925, 'Ali' : 4509106, 'Vlad' : 4795712},
        'Dubai Tourism' : {'Andy': 4007225, 'Varun' : 4113848, 'Janani' : 4097083, 'Ali' : 4532035, 'Vlad' : 4796320},
        'Samsung' : {'Andy': None, 'Varun' : None, 'Janani' : 4337169, 'Ali' : None, 'Vlad' : None},
        'Kering' : {'Andy': None, 'Varun' : 1471107, 'Janani' : None, 'Ali' : None, 'Vlad' : None},
 }
    try:
        profile_id = choices[x][y]
    except:
        print('Profile not found')
        return 0
    return profile_id

def advertisers(x):

    choices = {
        'abu dhabi culture' : [8420115,21552881,profiles('Abu Dhabi Tourism',config.user)],
        'al zahia' : [4527228,4885521,profiles('Starcom',config.user)],
        'acer' : [6634729,9452003,profiles('Zenith',config.user)],
        'adidas brand running' : [6524017,10048595,profiles('Adidas',config.user)],
        'adidas brand football' : [6523076,20361749,profiles('Adidas',config.user)],
        'adidas ecom' : [6524016,20054070,profiles('Adidas',config.user)],
        'aldar malls' : [8416056,21487126,profiles('Starcom',config.user)],
        'alfa telecom' : [3973613,2655472,profiles('Starcom',config.user)],
        'ayla' : [6873611,9841323,profiles('Starcom',config.user)],
        'yas island' : [5238154,6997993,profiles('Starcom',config.user)],
        'ariel' : [4457598,4585192,profiles('Starcom',config.user)],
        'bank audi' : [4092856,20016259,profiles('Starcom',config.user)],
        'beitmisk' : [4079501,2743324,profiles('Starcom',config.user)],
        'bmw parent' : [6355536,None,profiles('Zenith',config.user)],
        'bmw dubai' : [6356828,9481250,profiles('Zenith',config.user)],
        'bmw ksa' : [6355538,9326426,profiles('Zenith',config.user)],
        'bmw abu dhabi' : [6344670,9615179,profiles('Zenith',config.user)],
        'bmw regional' : [6342793,9202283,profiles('Zenith',config.user)],
        'bmw bahrain' : [6344968,22068603,profiles('Zenith',config.user)],
        'bmw qatar' : [6341285,22121234,profiles('Zenith',config.user)],
        'braun pg' : [4458193,4589087,profiles('Starcom',config.user)],
        'bebd' : [8454919,21632350,profiles('Zenith',config.user)],
        'ccf' : [8150373,21197280,profiles('Nestle',config.user)],
        'cipriani' : [5450404,9483570,profiles('Starcom',config.user)],
        'citi' : [6165999,8587611,profiles('Citibank',config.user)],
        'dtcm' : [5481501, 20500064 ,profiles('Dubai Tourism',config.user)],
        'farah experiences' : [8187590,20632788,profiles('Starcom',config.user)],
        'fitness' : [8272415,21080607,profiles('Nestle',config.user)],
        'fwad' : [5310078, 6935152 ,profiles('Starcom',config.user)],
        'gac' : [8114896,21128651,profiles('Starcom',config.user)],
        'ghh pg' : [4788150,6323274,profiles('Starcom',config.user)],
        'gillette pg' : [4456516,4590699,profiles('Starcom',config.user)],
        'google' : [6787442,9707803,profiles('Starcom',config.user)],
        'jazeera' : [2412944,108332,profiles('Zenith',config.user)],
        'liberty' : [4435377,4826474,profiles('Starcom',config.user)],
        'louvre' : [8413322,21552647,profiles('Abu Dhabi Tourism',config.user)],
        'luxury clothing company' : [8029407,20114006,profiles('Starcom',config.user)],
        'maf' : [2531650,96420,profiles('Starcom',config.user)],
        'maf communities' : [8474268,21760737,profiles('Starcom',config.user)],
        'meydan' : [3973441, 2754285, profiles('Starcom',config.user)],
        'mini abu dhabi' : [6678505,20027463,profiles('Zenith',config.user)],
        'mini dubai' : [6678302,10012833,profiles('Zenith',config.user)],
        'rr abu dhabi' : [8592408,22891443,profiles('Zenith',config.user)],
        'rr dubai' : [8899614,22985812,profiles('Zenith',config.user)],
        'mini ksa' : [6678303,20028261,profiles('Zenith',config.user)],
        'mini regional' : [6679901,9484715,profiles('Zenith',config.user)],
        'mini qatar' : [6678304,22187186,profiles('Zenith',config.user)],
        'nbo' : [8141036,20768946,profiles('Zenith',config.user)],
        'nbk' : [8076563,21084166,profiles('Zenith',config.user)],
        'omantel' : [6468900,9143119,profiles('Zenith',config.user)],
        'ooredoo oman' : [5640709,8586068,profiles('Starcom',config.user)],
        'ooredoo kuwait' : [8239298,20858154,profiles('Zenith',config.user)],
        'osn' : [3293958,831457,profiles('Starcom',config.user)],
        'rajhi' : [4290372,4062156,profiles('Starcom',config.user)],
        'royal jordan' : [8374103,21452990,profiles('Starcom',config.user)],
        'samba' : [3238262,503637,profiles('Zenith',config.user)],
        'tca' : [8242965,20877913,profiles('Abu Dhabi Tourism',config.user)],
        'tca master' : [8242311,None,profiles('Abu Dhabi Tourism',config.user)],
        'tca ota' : [8702381,22572600,profiles('Abu Dhabi Tourism',config.user)],
        'virgin mobile' : [6142427,10095060,profiles('Starcom',config.user)],
        'visa ecom' : [5219109,7782121, profiles('Visa',config.user)],
        'visa ecom parent' : [5197399,None, profiles('Visa',config.user)],
        'visa xborder' : [5182297,6864229, profiles('Visa',config.user)],
        'visa brand' : [5260257,8139947, profiles('Visa',config.user)],
        'visa kz brand' : [8307806, 21197770, profiles('Visa',config.user)],
        'varun' : [3349403,482316,profiles('Starcom',config.user)],
        'wb' : [8350519,21370883,profiles('Starcom',config.user)],
        'yas mall' : [8198954,20678914,profiles('Starcom',config.user)],
        'yas marina' : [5452848,9340317,profiles('Starcom',config.user)],
        'ymc' : [4157783,4793721,profiles('Starcom',config.user)],
        'yww' : [5308461,8309033,profiles('Starcom',config.user)],
        'zwz' : [6073556,8798911,profiles('Starcom',config.user)],
        'samsung' : [8379943, 21699157, profiles('Samsung',config.user)],
        'mcdel jed' : [8300924, 21318980, profiles('McDonalds',config.user)],
        'mcdel riy' : [8300609, 21327596, profiles('McDonalds',config.user)],
        'mcdel uae' : [8308266, 21172201, profiles('McDonalds',config.user)],
        'mcdel bah' : [8307993, 21284176, profiles('McDonalds',config.user)],
        'mcdel qat' : [8306964, 21300901, profiles('McDonalds',config.user)],
        'mcdel kuw' : [8312584, 21284194, profiles('McDonalds',config.user)],
        'mcdel jor' : [8872934, 22984538, profiles('McDonalds',config.user)],
        'mcdon jed' : [8313030, 21849108, profiles('McDonalds',config.user)],
        'mcdon riy' : [8315428, 21467787, profiles('McDonalds',config.user)],
        'mcdon uae' : [8318479, 21196933, profiles('McDonalds',config.user)],
        'mcdon bah' : [8318482, 21524276, profiles('McDonalds',config.user)],
        'mcdon qat' : [8315431, 21469569, profiles('McDonalds',config.user)],
        'mcdon kuw' : [8305037, 22173339, profiles('McDonalds',config.user)],
        'mcdon omn' : [8318476, 21512890, profiles('McDonalds',config.user)],
        'mcdon jor' : [8886810, 22987298, profiles('McDonalds',config.user)],
        'rsa' : [2673419, 82667, profiles('Starcom',config.user)],
        'enbd' : [3712847,1172757,profiles('Starcom',config.user)],
        'gucci' : [4569123,5442978,profiles('Kering',config.user)],
        'maggi' : [6619061,9386214,profiles('Nestle',config.user)],
        'nap' : [6206879,9121587,profiles('Net-a-porter',config.user)],
        'cafe najjar' : [5994018,21593623,profiles('Starcom',config.user)],
        'toyota retail' : [8616571,22115836,profiles('ALJ',config.user)],
        'toyota service' : [8920036,23066245,profiles('ALJ',config.user)],
        'siniora' : [8718589,22466140,profiles('Starcom',config.user)],
        'ikea' : [8546187,21872829,profiles('Starcom',config.user)],
        'al tayyar' : [8701908,22428507,profiles('Starcom',config.user)],
        'swatch' : [4408088,4448718,profiles('Starcom',config.user)],
        'cerelac' : [8239055,20831883,profiles('Nestle',config.user)],
        'fasttelco' : [8364424,22781074,profiles('Zenith',config.user)],
        'nescafe' : [6773928,9671254,profiles('Nestle',config.user)],
        'alhosn': [8935053,23069934,profiles('Abu Dhabi Tourism',config.user)],
        'qah': [8947435,23069154,profiles('Abu Dhabi Tourism',config.user)],
        'cultural foundation': [8942209,23069937,profiles('Abu Dhabi Tourism',config.user)],
        'omt': [8948876,23203273,profiles('Starcom',config.user)]
    }
    try:
        aid=choices[x][0]
        url=choices[x][1]
        profile_id = choices[x][2]
    except:
        print('Advertiser not found')
        return 0
    return aid, url, profile_id