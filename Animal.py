from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("prog.exe")
process.open()

#Animal Stat? , Dont know why they have different offset for stats
dog1Health = process.get_pointer(0x9F3B18)
dog2Health = process.get_pointer(0x9F4698)
dog3Health = process.get_pointer(0x9F43B8)
dog4Health = process.get_pointer(0x9F3DF8)
cat1Health = process.get_pointer(0x9F4C58)
cat2Health = process.get_pointer(0x9F54F8)
cat3Health = process.get_pointer(0x9F5218)
cat4Health = process.get_pointer(0x9F4978)
mooseHealth = process.get_pointer(0x9F6BF8)
pigHealth = process.get_pointer(0x9F4F38)
smallAnimalHealth = process.get_pointer(0x9F40D8)
goatHealth = process.get_pointer(0x9EB9B8)
beaverHealth = process.get_pointer(0x9E9CF8)