from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe")
process.open()

#Inventory:
Food = process.get_pointer(0x9E2264)
Gas = process.get_pointer(0x9E2268)
Medkit = process.get_pointer(0x9E226C)
Dolt = process.get_pointer(0x9E2270)
Rifle = process.get_pointer(0x9E2274)
Shotgun = process.get_pointer(0x9E2278)

#P1 Ammo & health:
Health = process.get_pointer(0x9E2718)
gasAmmo = process.get_pointer(0x9E2868)
doltAmmo = process.get_pointer(0x9E2870)
rifleAmmo = process.get_pointer(0x9E2874)
shotgunAmmo = process.get_pointer(0x9E2878)
Battery = process.get_pointer(0x9E2888)

#Stats:
statblock1 = process.get_pointer(0x9E27A0) #Morale, Attitude, Composure on the same address for some reason?
statblock2 = process.get_pointer(0x9E27A4) #Medical, Wits, Loyalty on the same address for some reason?
statblock3 = process.get_pointer(0x9E27A8) #Mechanical, Strength, Shooting, Dexterity on the same address for some reason?
fitness = process.get_pointer(0x9E27AC)

#Inventory
inventory_Slot = process.get_pointer(0x9E2280)
item_Quantity = process.get_pointer(0x9E2284)

#P2-P4 Health:
p2Health = process.get_pointer(0x9E29F8)
p3Health = process.get_pointer(0x9E2CD8)
p4Health = process.get_pointer(0x9E2FB8)

#P2-P4 Ammo Stats
p2Statblock1 = process.get_pointer(0x9E2A80)
p2Statblock2 = process.get_pointer(0x9E2A84)
p2Statblock3 = process.get_pointer(0x9E2A88)
p2Fitness = process.get_pointer(0x9E2A8C)

p3Statblock1 = process.get_pointer(0x9E3320)
p3Statblock2 = process.get_pointer(0x9E3324)
p3Statblock3 = process.get_pointer(0x9E3328)
p3Fitness = process.get_pointer(0x9E332C)

p4Statblock1 = process.get_pointer(0x9E3040)
p4Statblock2 = process.get_pointer(0x9E3044)    
p4Statblock3 = process.get_pointer(0x9E3048)
p4Fitness = process.get_pointer(0x9E304C)

#P2-P4 Ammo
p2d = process.get_pointer(0x9E2B50)
p2r = process.get_pointer(0x9E2B54)
p2s = process.get_pointer(0x9E2B58)
p2g = process.get_pointer(0x9E2B48)
p2b = process.get_pointer(0x9E2B68)

p3d = process.get_pointer(0x9E2E30)
p3r = process.get_pointer(0x9E2E34)
p3s = process.get_pointer(0x9E2E38)
p3g = process.get_pointer(0x9E2E28)
p3b = process.get_pointer(0x9E2E54)

p4d = process.get_pointer(0x9E3110)
p4r = process.get_pointer(0x9E3114)
p4s = process.get_pointer(0x9E3118)
p4g = process.get_pointer(0x9E3108)
p4b = process.get_pointer(0x9E3140)