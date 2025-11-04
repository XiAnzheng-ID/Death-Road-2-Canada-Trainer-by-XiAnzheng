from ReadWriteMemory import ReadWriteMemory
import Offset
import time

def stats(stop_event):
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("prog.exe") #change the process name to what version u use
    process.open()

    while not stop_event.is_set():
        process.write(Offset.statblock1, 101058049)
        process.write(Offset.statblock2, 101058051)
        process.write(Offset.statblock3, 101058054)
        process.write(Offset.fitness, 774)

        process.write(Offset.p2Statblock1, 101058049)
        process.write(Offset.p2Statblock2, 101058051)
        process.write(Offset.p2Statblock3, 101058054)
        process.write(Offset.p2Fitness, 774)
        
        process.write(Offset.p3Statblock1, 101058049)
        process.write(Offset.p3Statblock2, 101058051)
        process.write(Offset.p3Statblock3, 101058054)
        process.write(Offset.p3Fitness, 774)

        process.write(Offset.p4Statblock1, 101058049)
        process.write(Offset.p4Statblock2, 101058051)
        process.write(Offset.p4Statblock3, 101058054)
        process.write(Offset.p4Fitness, 774)
        time.sleep(0.1)
