import threading
import ctypes
import winsound
from ReadWriteMemory import ReadWriteMemory
import customtkinter as ctk

# Trainer Toggle Status
unlimited_loot_status = False
unlimited_ammo_status = False
unlimited_health_status = False
max_stat_status = False

# Trainer Hack
def inject_item():
    item_id_value = int(item_id.get()) 
    quantity_value = int(quantity.get())
    process.write(Offset.inventory_Slot, item_id_value)
    process.write(Offset.item_Quantity, quantity_value)

def background(script, stop_event):
    threading.Thread(target=script, args=(stop_event,)).start()

def create_stop_event():
    return threading.Event()

def toggle_loot():
    global unlimited_loot_status, stop_event_loot
    unlimited_loot_status = not unlimited_loot_status
    if unlimited_loot_status:
        stop_event_loot = create_stop_event()
        background(Loot.loot, stop_event_loot)
    else:
        stop_event_loot.set()

def toggle_ammo():
    global unlimited_ammo_status, stop_event_ammo
    unlimited_ammo_status = not unlimited_ammo_status
    if unlimited_ammo_status:
        stop_event_ammo = create_stop_event()
        background(Ammo.ammo, stop_event_ammo)
    else:
        stop_event_ammo.set()

def toggle_health():
    global unlimited_health_status, stop_event_health
    unlimited_health_status = not unlimited_health_status
    if unlimited_health_status:
        stop_event_health = create_stop_event()
        background(Health.health, stop_event_health)
    else:
        stop_event_health.set()

def toggle_max_stat():
    global max_stat_status, stop_event_stats
    max_stat_status = not max_stat_status
    if max_stat_status:
        stop_event_stats = create_stop_event()
        background(Stats.stats, stop_event_stats)
    else:
        stop_event_stats.set()

# App Function
def on_closing():
    # Stop all Trainer feature on close
    if unlimited_loot_status:
        stop_event_loot.set()
    if unlimited_ammo_status:
        stop_event_ammo.set()
    if unlimited_health_status:
        stop_event_health.set()
    if max_stat_status:
        stop_event_stats.set()
    
    app.destroy()

#check if Entrybox is valid (ignore the unused error)
def validate_entry(*args):
    try:
        item_id_value = int(item_id.get()) #DONT REMOVE THIS
        quantity_value = int(quantity.get()) # DONT REMOVE THIS
        quantity_button.configure(state=ctk.NORMAL)
    except ValueError:
        quantity_button.configure(state=ctk.DISABLED)

# Main UI
try:
    import Ammo
    import Health
    import Loot
    import Stats
    import Offset
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("prog.exe")
    process.open()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.geometry("500x300")
    app.title("DR2C Trainer by XiAnzheng v05.1.2025(Quadriceps Update)")
    app.protocol("WM_DELETE_WINDOW", on_closing)

    # Toggle
    loot_switch = ctk.CTkSwitch(app, text="Unlimited Loot", command=toggle_loot)
    loot_switch.grid(row=0, column=0, padx=20, pady=10)
    
    ammo_switch = ctk.CTkSwitch(app, text="Unlimited Ammo", command=toggle_ammo)
    ammo_switch.grid(row=1, column=0, padx=20, pady=10)
    
    health_switch = ctk.CTkSwitch(app, text="Unlimited Health", command=toggle_health)
    health_switch.grid(row=2, column=0, padx=20, pady=10)
    
    stat_switch = ctk.CTkSwitch(app, text="No Decay & Max Stats", command=toggle_max_stat)
    stat_switch.grid(row=3, column=0, padx=20, pady=10)

    # Manual Editor
    item_id = ctk.CTkEntry(app, placeholder_text="Item ID?")
    item_id.grid(row=0, column=2, padx=10, pady=10)
    item_id.bind("<KeyRelease>", validate_entry)  # validate entry on change

    quantity = ctk.CTkEntry(app, placeholder_text="Quantity?")
    quantity.grid(row=0, column=3, padx=0, pady=10)
    quantity.bind("<KeyRelease>", validate_entry)  # validate entry on change

    quantity_button = ctk.CTkButton(app, text="Inject Item", command=inject_item, state=ctk.DISABLED)
    quantity_button.place(relx=0.66, rely=0.2, anchor=ctk.CENTER)

    app.mainloop()

except Exception as ex:
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    ctypes.windll.user32.MessageBoxW(0, "Does the game running? this Trainer was tested on Steam Version", str(ex), 0x20 | 0x1000)