from ReadWriteMemory import ReadWriteMemory
import Offset
import Animal
import time

def health(stop_event):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
    process.open()

    while not stop_event.is_set():
        process.write(Offset.Health, 6)   
        process.write(Offset.p2Health, 6)
        process.write(Offset.p3Health, 6)
        process.write(Offset.p4Health, 6)

        process.write(Animal.dog1Health, 6)
        process.write(Animal.dog2Health, 6)
        process.write(Animal.dog3Health, 6)
        process.write(Animal.dog4Health, 6)

        process.write(Animal.cat1Health, 6)
        process.write(Animal.cat2Health, 6)
        process.write(Animal.cat3Health, 6)
        process.write(Animal.cat4Health, 6)

        process.write(Animal.mooseHealth, 6)
        process.write(Animal.pigHealth, 6)
        process.write(Animal.smallAnimalHealth, 6)
        process.write(Animal.goatHealth, 6)
        process.write(Animal.beaverHealth, 6)

        time.sleep(0.1)