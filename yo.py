


#creates a range of floors for each building 
def build_floors(low,high): 
	l = []
	for f in range(low,high+1):
		l.append(f) 
	return l
	
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
Floor = [McClure_Floors,Patrick_Floors]
#test print
"""
print (McClure_Floors)
print (Garden_Floors)
print (McClure_Floors)
print (Patrick_Floors)
print (Smith_Floors)
print (Baird_Floors)
print (Shep_Floors )
print (Fletcher_Floors)
print (Engineering_Floors)
print (Garden_Floors)
print (East_Floors)
print (West_Floors)
print (Middle_Floors)
print (Education_Floors)
"""

#make floor names 
def completeFloors():
	building_abbr = ["MCL","PTK","SMT","BRD","SHP","FLT","CEN","GPL","EPL","WPL","MPL","EDC"] 
	for x in building_abbr:
		for y in Floor:
			print(x+str(y))
	return
yay = completeFloors()
print (yay)
