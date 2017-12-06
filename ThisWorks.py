


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
def generate_rf_profile(floor_num,bld_abbr):
	"""
	Takes a floor number (list) and a building abbr (string) and returns a list of RF profile names based on the number of floors
	"""
	rf_profile_a = []
	rf_profile_b = []
	for y in floor_num:
		rf_profile_a.append("%s-floor-%s-rf-802.11a" %(bld_abbr,y))
		rf_profile_b.append("%s-floor-%s-rf-802.11b/g" %(bld_abbr,y))
	return rf_profile_a,rf_profile_b
	
	
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

rf_profile_list = []
rf_profile_list.append(generate_rf_profile(McClure_Floors,bld_abbr[0]))
rf_profile_list.append(generate_rf_profile(Patrick_Floors,bld_abbr[1]))
rf_profile_list.append(generate_rf_profile(Smith_Floors,bld_abbr[2]))
rf_profile_list.append(generate_rf_profile(Baird_Floors,bld_abbr[3]))
rf_profile_list.append(generate_rf_profile(Shep_Floors,bld_abbr[4]))
rf_profile_list.append(generate_rf_profile(Fletcher_Floors,bld_abbr[5]))
rf_profile_list.append(generate_rf_profile(Engineering_Floors,bld_abbr[6]))
rf_profile_list.append(generate_rf_profile(Garden_Floors,bld_abbr[7]))
rf_profile_list.append(generate_rf_profile(East_Floors,bld_abbr[8]))
rf_profile_list.append(generate_rf_profile(West_Floors,bld_abbr[9]))
rf_profile_list.append(generate_rf_profile(Middle_Floors,bld_abbr[10]))
rf_profile_list.append(generate_rf_profile(Education_Floors,bld_abbr[11]))
print(*rf_profile_list)
#pass2 =(*pass1)
#print ('\n'.join(rf_profile_list))
"""
for i in range(len(rf_profile_list)):
	print(rf_profile_list[i])
"""	
#print (rf_profile_list)