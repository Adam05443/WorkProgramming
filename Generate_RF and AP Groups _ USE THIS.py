import re
import os 
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

def generate_ap_group(floor_num,bld_abbr):
	ap_group = []
	for y in floor_num:
		ap_group.append("%s-floor-%s-apg" %(bld_abbr,y))
	return ap_group
	
#feed the build_floors() the number of floors each building has. Build a list for it. 
McClure_Floors = build_floors(0,7)
Patrick_Floors = build_floors(0,6)
Smith_Floors = build_floors(0,6)
Baird_Floors = build_floors(0,7)
Shep_Floors = build_floors(1,6) 
Fletcher_Floors = build_floors(2,5)
Engineering_Floors = build_floors (1,4)
Garden_Floors = build_floors(2,2)
East_Floors = build_floors(1,6)
West_Floors = build_floors(1,6)
Middle_Floors = build_floors(0,5)
Education_Floors = build_floors(2,2)

#creates two empty lists
rf_profile_list_a = []
rf_profile_list_b = []
ap_group_list = [] 
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

#passes the building abbr and the floor number into the ap_groups() 
ap_group_list.append(generate_ap_group(McClure_Floors,bld_abbr[0]))
ap_group_list.append(generate_ap_group(Patrick_Floors,bld_abbr[1]))
ap_group_list.append(generate_ap_group(Smith_Floors,bld_abbr[2]))
ap_group_list.append(generate_ap_group(Baird_Floors,bld_abbr[3]))
ap_group_list.append(generate_ap_group(Shep_Floors,bld_abbr[4]))
ap_group_list.append(generate_ap_group(Fletcher_Floors,bld_abbr[5]))
ap_group_list.append(generate_ap_group(Engineering_Floors,bld_abbr[6]))
ap_group_list.append(generate_ap_group(Garden_Floors,bld_abbr[7]))
ap_group_list.append(generate_ap_group(East_Floors,bld_abbr[8]))
ap_group_list.append(generate_ap_group(West_Floors,bld_abbr[9]))
ap_group_list.append(generate_ap_group(Middle_Floors,bld_abbr[10]))
ap_group_list.append(generate_ap_group(Education_Floors,bld_abbr[11]))


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

clean_ap_group = []
for line in ap_group_list:
	for line2 in line:
		clean_ap_group.append(line2.translate(translation_table))
backout_script = open(os.path.join('\MyDocuments\Python Scripts','backout.txt'), "w")
#iterates back through the clean list and generates this cli code 
print("!!!!!!!!!!!!!!!!!!!!!!!802.11a RF profiles!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i in clean_a:
	backout_script.write("config rf-profile delete %s \n" %(i))
	print("config rf-profile create 802.11a %s" %(i))
	print("config rf-profile description %s %s" %(i,i))
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
	
	
print("!!!!!!!!!!!!!!!!!!!!!!!802.11bg RF profiles!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i in clean_b:
	backout_script.write("config rf-profile delete %s \n" %(i))
	print("config rf-profile create 802.11b %s" %(i))
	print("config rf-profile description %s %s" %(i,i))
	print("config rf-profile data-rates 802.11b mandatory 12 %s" %(i))
	print("config rf-profile data-rates 802.11b mandatory 24 %s" %(i))
	print("config rf-profile data-rates 802.11b disabled 6 %s" %(i))
	print("config rf-profile data-rates 802.11b disabled 9 %s" %(i))
	print("config rf-profile data-rates 802.11b supported 18 %s" %(i))
	print("config rf-profile data-rates 802.11b supported 36 %s" %(i))
	print("config rf-profile data-rates 802.11b supported 48 %s" %(i))
	print("config rf-profile data-rates 802.11b supported 54 %s" %(i))
	print("config rf-profile tx-power-min 10 %s" %(i))
	print("config rf-profile coverage data -70  %s" %(i))
	print("config rf-profile coverage voice -65  %s" %(i))
	
print("!!!!!!!!!!!!!!!!!!!!!!!access-point-groups!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i in clean_ap_group:
	backout_script.write("config wlan apgroup delete %s \n" %(i))
	print("config wlan apgroup add %s" %(i))
	print("config wlan apgroup interface-mapping add %s 50 wan_clinical_psk" %(i))
	print("config wlan apgroup interface-mapping add %s 17 guest_go_nowhere" %(i))
	print("config wlan apgroup interface-mapping add %s 15 w_testnetwork" %(i))
	print("config wlan apgroup interface-mapping add %s 51 mc_famcd1" %(i))
	print("config wlan apgroup interface-mapping add %s 20 mc_famobile2" %(i))
	print("config wlan apgroup interface-mapping add %s 22 mchv_acc_ivpump" %(i))
	print("config wlan apgroup interface-mapping add %s 23 mchv_acc_clinical_psk" %(i))
	print("config wlan apgroup interface-mapping add %s 25 cast_nowhere" %(i))
	print("config wlan apgroup interface-mapping add %s 75 fah_famobile2" %(i))
	
backout_script.close()	

#this creates the mappings of ap group to rf group. 
generate_mappings = []
for i in clean_ap_group:
	generate_mappings = i.split("-")
	print("config wlan apgroup profile-mapping add %s %s-%s-%s-rf-802.11a " %(i,generate_mappings[0],generate_mappings[1],generate_mappings[2]))
	print("y\n")
	print("config wlan apgroup profile-mapping add %s %s-%s-%s-rf-802.11bg " %(i,generate_mappings[0],generate_mappings[1],generate_mappings[2]))
	print("y\n")
	generate_mappings.clear()

report_of_aps = open(os.path.join('\MyDocuments\Python Scripts','ap-report.txt'), "w")

with open(os.path.join('\MyDocuments\Python Scripts','fresh-list'), "r") as r:
	for line in r:
		r_list = list(line)
		ap_name_4 = r_list[0] + r_list[1] + r_list[2] + r_list[3]
		ap_name_5 = r_list[0] + r_list[1] + r_list[2] + r_list[3] + r_list[4]
		if ap_name_4 == "bd1w":
			print ("config ap group-name BRD-floor-1-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "bd2w":
			print ("config ap group-name BRD-floor-2-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "bd2w" or ap_name_4 == "bscw":
			print ("config ap group-name BRD-floor-2-apg %sy" %(line))
			r_list.clear()			
		elif ap_name_4 == "bd3w":
			print ("config ap group-name BRD-floor-3-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "bd4w":
			print ("config ap group-name BRD-floor-4-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "bd5w":
			print ("config ap group-name BRD-floor-5-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "bd6w":
			print ("config ap group-name BRD-floor-6-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "bd7w":
			print ("config ap group-name BRD-floor-7-apg %sy" %(line))
			r_list.clear()	
		elif ap_name_5 == "brd07":
			print ("config ap group-name BRD-floor-7-apg %sy" %(line))
			r_list.clear()					
		elif ap_name_4 == "bdbw":
			print ("config ap group-name BRD-floor-0-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "cp1w" or ap_name_4 == "en1w":
			print ("config ap group-name CEN-floor-1-apg %sy" %(line))
			r_list.clear()			
		elif ap_name_4 == "cp2w" or ap_name_4 == "en2w":
			print ("config ap group-name CEN-floor-2-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "cp3w" or ap_name_4 == "en3w":
			print ("config ap group-name CEN-floor-3-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "cp4w" or ap_name_4 == "en4w":
			print ("config ap group-name CEN-floor-4-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "ed2w":
			print ("config ap group-name EDC-floor-2-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "ep1w":
			print ("config ap group-name EPL-floor-1-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "ep2w":
			print ("config ap group-name EPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "ep3w":
			print ("config ap group-name EPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "ep4w":
			print ("config ap group-name EPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "ep5w":
			print ("config ap group-name EPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "ep6w":
			print ("config ap group-name EPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_5 == "epl03":
			print ("config ap group-name EPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "fl2w":
			print ("config ap group-name FLT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "fl3w":
			print ("config ap group-name FLT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "fl4w":
			print ("config ap group-name FLT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "fl5w":
			print ("config ap group-name FLT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "gp2w":
			print ("config ap group-name GPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "mc1w":
			print ("config ap group-name MCL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()			
		elif ap_name_4 == "mc2w":
			print ("config ap group-name MCL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "mc3w":
			print ("config ap group-name MCL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "mc4w":
			print ("config ap group-name MCL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "mc5w":
			print ("config ap group-name MCL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "mc6w":
			print ("config ap group-name MCL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "mc7w":
			print ("config ap group-name MCL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "mclw":
			print ("config ap group-name MCL-floor-0-apg %sy" %(line))
			r_list.clear()	
		elif ap_name_4 == "md1w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "md2w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()			
		elif ap_name_4 == "mdbw":
			print ("config ap group-name PTK-floor-0-apg %sy" %(line))
			r_list.clear()
		elif ap_name_4 == "mp1w":
			print ("config ap group-name MPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "mp2w":
			print ("config ap group-name MPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "mp3w":
			print ("config ap group-name MPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "mp4w":
			print ("config ap group-name MPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "mp5w":
			print ("config ap group-name MPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "mpl0":
			print ("config ap group-name MPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "pt1w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "pt2w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "pt3w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "pt4w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "pt5w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "pt6w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "pt7w":
			print ("config ap group-name PTK-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()				
		elif ap_name_4 == "ptbw":
			print ("config ap group-name PTK-floor-0-apg %sy" %(line))
			r_list.clear()	
		elif ap_name_4 == "sh1w":
			print ("config ap group-name SHP-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "sh2w":
			print ("config ap group-name SHP-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "sh3w":
			print ("config ap group-name SHP-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "sh4w":
			print ("config ap group-name SHP-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "sh5w":
			print ("config ap group-name SHP-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "sh6w":
			print ("config ap group-name SHP-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "sm1w":
			print ("config ap group-name SMT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "sm2w":
			print ("config ap group-name SMT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "sm3w":
			print ("config ap group-name SMT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()			
		elif ap_name_4 == "sm4w":
			print ("config ap group-name SMT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "sm5w":
			print ("config ap group-name SMT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		elif ap_name_4 == "sm6w":
			print ("config ap group-name SMT-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()				
		elif ap_name_4 == "smbw":
			print ("config ap group-name SMT-floor-0-apg %sy" %(line))
			r_list.clear()						
		elif ap_name_4 == "wp1w" or ap_name_4 == "jmcw":
			print ("config ap group-name WPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()
		elif ap_name_4 == "wp2w":
			print ("config ap group-name WPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "wp3w":
			print ("config ap group-name WPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "wp4w":
			print ("config ap group-name WPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "wp5w":
			print ("config ap group-name WPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()		
		elif ap_name_4 == "wp6w":
			print ("config ap group-name WPL-floor-%s-apg %sy" %(r_list[2],line))
			r_list.clear()	
		else: 
			report_of_aps.write(line)
		
			