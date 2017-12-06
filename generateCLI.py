


#creates a range of floors for each building 
def build_floors(low,high): 
	"""
	Creates lists of integers. Depends on the range fed into it
	"""
	l = []
	for f in range(low,high+1):
		l.append(f) 
	return l

#list of building abbrivations 
bld_abbr = ["MCL","PTK","SMT","BRD","SHP","FLT","CEN","GPL","EPL","WPL","MPL","EDC"] 

#function generates an rf profile name for 802.11b/g only 
def generate_rf_profile_a(floor_num,bld_abbr):
	"""
	Takes a floor number (list) and a building abbr (string) and returns a list of RF profile names based on the number of floors
	"""
	rf_profile_a = []
	for y in floor_num:
		rf_profile_a.append("%s-floor-%s-rf-802.11a" %(bld_abbr,y))
	return rf_profile_a
	
def generate_rf_profile_b(floor_num,bld_abbr):
	"""
	Takes a floor number (list) and a building abbr (string) and returns a list of RF profile names based on the number of floors
	"""
	rf_profile_b = []
	for y in floor_num:
		rf_profile_b.append("%s-floor-%s-rf-802.11bg" %(bld_abbr,y))
	return rf_profile_b

	
#feed the build_floors() the number of floors each building has. Build a list for it. 
McClure_Floors = build_floors(0,7)
Patrick_Floors = build_floors(0,6)
Smith_Floors = build_floors(0,5)
Baird_Floors = build_floors(1,7)
Shep_Floors = build_floors(1,6) 
Fletcher_Floors = build_floors(1,3)
Engineering_Floors = build_floors (1,4)
Garden_Floors = build_floors(2,2)
East_Floors = build_floors(1,5)
West_Floors = build_floors(1,5)
Middle_Floors = build_floors(1,5)
Education_Floors = build_floors(2,2)

#creates two empty lists
rf_profile_list_a = []
rf_profile_list_b = []

#passes the building abbr and the floor number into the generate_rf_profile() 
rf_profile_list_a.append(generate_rf_profile_a(McClure_Floors,bld_abbr[0]))
rf_profile_list_a.append(generate_rf_profile_a(Patrick_Floors,bld_abbr[1]))
rf_profile_list_a.append(generate_rf_profile_a(Smith_Floors,bld_abbr[2]))
rf_profile_list_a.append(generate_rf_profile_a(Baird_Floors,bld_abbr[3]))
rf_profile_list_a.append(generate_rf_profile_a(Shep_Floors,bld_abbr[4]))
rf_profile_list_a.append(generate_rf_profile_a(Fletcher_Floors,bld_abbr[5]))
rf_profile_list_a.append(generate_rf_profile_a(Engineering_Floors,bld_abbr[6]))
rf_profile_list_a.append(generate_rf_profile_a(Garden_Floors,bld_abbr[7]))
rf_profile_list_a.append(generate_rf_profile_a(East_Floors,bld_abbr[8]))
rf_profile_list_a.append(generate_rf_profile_a(West_Floors,bld_abbr[9]))
rf_profile_list_a.append(generate_rf_profile_a(Middle_Floors,bld_abbr[10]))
rf_profile_list_a.append(generate_rf_profile_a(Education_Floors,bld_abbr[11]))

#passes the building abbr and the floor number into the generate_rf_profile() 
rf_profile_list_b.append(generate_rf_profile_b(McClure_Floors,bld_abbr[0]))
rf_profile_list_b.append(generate_rf_profile_b(Patrick_Floors,bld_abbr[1]))
rf_profile_list_b.append(generate_rf_profile_b(Smith_Floors,bld_abbr[2]))
rf_profile_list_b.append(generate_rf_profile_b(Baird_Floors,bld_abbr[3]))
rf_profile_list_b.append(generate_rf_profile_b(Shep_Floors,bld_abbr[4]))
rf_profile_list_b.append(generate_rf_profile_b(Fletcher_Floors,bld_abbr[5]))
rf_profile_list_b.append(generate_rf_profile_b(Engineering_Floors,bld_abbr[6]))
rf_profile_list_b.append(generate_rf_profile_b(Garden_Floors,bld_abbr[7]))
rf_profile_list_b.append(generate_rf_profile_b(East_Floors,bld_abbr[8]))
rf_profile_list_b.append(generate_rf_profile_b(West_Floors,bld_abbr[9]))
rf_profile_list_b.append(generate_rf_profile_b(Middle_Floors,bld_abbr[10]))
rf_profile_list_b.append(generate_rf_profile_b(Education_Floors,bld_abbr[11]))

#some random stuff I stole from the Internet to strip out some formatting
translation_table = dict.fromkeys(map(ord, '[]'), None)

#this just strips off the [] and dumps everything back into a list
clean_a = []
for line in rf_profile_list_a:
	for line2 in line:
		clean_a.append(line2.translate(translation_table))
clean_b = []
for line in rf_profile_list_b:
	for line2 in line:
		clean_b.append(line2.translate(translation_table))

#iterates back through the clean list and generates this cli code 
for i in clean_a:
	print("config rf-profile create 802.11a %s" %(i))
	print("config rf-profile description %s" %(i))
	print("config rf-profile data-rates 802.11a mandatory 12 %s" %(i))
	print("config rf-profile data-rates 802.11a mandatory 24 %s" %(i))
	print("config rf-profile data-rates 802.11a disabled 6 %s" %(i))
	print("config rf-profile data-rates 802.11a disabled 9 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 18 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 36 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 48 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 54 %s" %(i))
	print("config rf-profile tx-power-min 10 %s" %(i))
	print("config rf-profile coverage data -70  %s" %(i))
	print("config rf-profile coverage voice -65  %s" %(i))
	
for i in clean_b:
	print("config rf-profile create 802.11a %s" %(i))
	print("config rf-profile description %s" %(i))
	print("config rf-profile data-rates 802.11a mandatory 12 %s" %(i))
	print("config rf-profile data-rates 802.11a mandatory 24 %s" %(i))
	print("config rf-profile data-rates 802.11a disabled 6 %s" %(i))
	print("config rf-profile data-rates 802.11a disabled 9 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 18 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 36 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 48 %s" %(i))
	print("config rf-profile data-rates 802.11a supported 54 %s" %(i))
	print("config rf-profile tx-power-min 10 %s" %(i))
	print("config rf-profile coverage data -70  %s" %(i))
	print("config rf-profile coverage voice -65  %s" %(i))
