import tkinter as tk
from data import confidant_list

# global shit
schedule_array = [[[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[]]]

remarks_array = []
remarks_pointer = 10

label_catch = ""

def create_table(root, rows, columns):
    global schedule_array
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == 2:
                if i == 0:
                    cell_value = "Morning"
                else:
                    cell_value = "Evening"
                label = tk.Label(root, text=cell_value, borderwidth=1, relief="solid", width=90, height=2, background="orange")
                label.grid(columnspan=7, sticky="ew")
                break
            else:
                if i == 1:
                    sched_row = 0
                else:
                    sched_row = 1
                
                cell_value=schedule_array[sched_row][j]
                
                if cell_value == []:
                    bg_color = "darkred"
                else:
                    bg_color = "white"
                label = tk.Label(root, text=cell_value, borderwidth=1, relief="solid", width=30, height=10, bg=bg_color)
                label.grid(row=i, column=j, sticky="ew")

def update_sched():
    global schedule_array
    
    # per row (morning and evening)
    for i in range(2):
        # per day (sunday to saturday)
        for j in range(7):
            catch_string = ""
            # per person (makoto to kasumi)
            for k in schedule_array[i][j]:
                print(i,j,k)
                if k is []:
                    break
                catch_string += k
            if catch_string == "":
                label = tk.Label(root, text="", borderwidth=1, relief="solid", width=30, height=10,bg="darkred")
            else:
                label = tk.Label(root, text=catch_string, borderwidth=1, relief="solid", width=30, height=10,bg="white")
            if i == 0:
                row_val = 1
            else:
                row_val = 3
            label.grid(row=row_val, column=j, sticky="ew")
    root.update()
                    

def change_sched(confidant,value):
    # Global variable
    global schedule_array
    global remarks_array
    global confidant_list
    global label_catch
    
    current = confidant_list[confidant]
    days = current["schedule"]
    if value:
        for i in days:
            schedule_array[current["day"]][i].append(current["label"]+"\n")
        if current["remarks"] != "":
            remarks_array.append(current["remarks"]+"\n")
    else:
        for i in days:
            schedule_array[current["day"]][i].remove(current["label"]+"\n")
        if current["remarks"] != "":
            remarks_array.remove(current["remarks"]+"\n")
    update_sched()
    
    string_catch = ""
    for i in remarks_array:
        string_catch += i
    
    string_result = tk.StringVar()
    string_result.set(string_catch)
    
    label = tk.Label(root, textvariable=string_result,anchor="nw",bg="white")
    
    if label_catch == "":
        label_catch = label
    else:
        label_catch.destroy()
        label_catch = label
    label.grid(columnspan=4,rowspan=10,row=10, column=3, sticky="nw")

def create_checklist(root):
    global schedule_array
    # checkbox variables
    conf_makoto = tk.BooleanVar()
    conf_haru = tk.BooleanVar()
    conf_yusuke = tk.BooleanVar()
    conf_sojiro = tk.BooleanVar()
    conf_ann = tk.BooleanVar()
    conf_ryuji = tk.BooleanVar()
    conf_akechi = tk.BooleanVar()
    conf_futaba = tk.BooleanVar()
    conf_chihaya = tk.BooleanVar()
    conf_takemi = tk.BooleanVar()
    conf_iwai = tk.BooleanVar()
    conf_kawakami = tk.BooleanVar()
    conf_ohya = tk.BooleanVar()
    conf_oda = tk.BooleanVar()
    conf_hifumi = tk.BooleanVar()
    conf_mishima = tk.BooleanVar()
    conf_yoshida = tk.BooleanVar()
    conf_maruki = tk.BooleanVar()
    conf_kasumi = tk.BooleanVar()
    
    """mon_may = tk.BooleanVar()
    mon_june = tk.BooleanVar()
    mon_july = tk.BooleanVar()
    mon_aug = tk.BooleanVar()
    mon_sept = tk.BooleanVar()
    mon_oct = tk.BooleanVar()
    mon_nov = tk.BooleanVar()
    mon_dec = tk.BooleanVar()
    mon_jan = tk.BooleanVar()"""


    # Labels
    label = tk.Label(root, text="Confidants", borderwidth=1, relief="solid", width=90, height=2, background="orange")
    label.grid(columnspan=3, row=7, column=0,sticky="ew")
    
    """label = tk.Label(root, text="Month", borderwidth=1, relief="solid", height=2, background="orange")
    label.grid(columnspan=1, row=7, column=3, sticky="ew")"""
    
    label = tk.Label(root, text="Requirements", borderwidth=1, relief="solid", height=2, background="lightblue")
    label.grid(columnspan=4, row=7, column=3, sticky="ew")

    # Checkbox Column 1
    cb_makoto = tk.Checkbutton(root, text="Makoto [Priestess]", variable=conf_makoto, anchor="w", command=lambda: change_sched("makoto", conf_makoto.get()))
    cb_makoto.grid(row=8, column=0, columnspan=2, sticky="ew")
    cb_haru = tk.Checkbutton(root, text="Haru [Empress]", variable=conf_haru, anchor="w",command=lambda: change_sched("haru", conf_haru.get()))
    cb_haru.grid(row=9, column=0, columnspan=2, sticky="ew")
    cb_yusuke = tk.Checkbutton(root, text="Yusuke [Emperor]", variable=conf_yusuke, anchor="w",command=lambda: change_sched("yusuke", conf_yusuke.get()))
    cb_yusuke.grid(row=10, column=0, columnspan=2, sticky="ew")
    cb_sojiro = tk.Checkbutton(root, text="Sojiro [Hierophant]", variable=conf_sojiro, anchor="w",command=lambda: change_sched("sojiro", conf_sojiro.get()))
    cb_sojiro.grid(row=11, column=0, columnspan=2, sticky="ew")
    cb_ann = tk.Checkbutton(root, text="Ann [Lovers]", variable=conf_ann, anchor="w",command=lambda: change_sched("ann", conf_ann.get()))
    cb_ann.grid(row=12, column=0, columnspan=2, sticky="ew")
    cb_ryuji = tk.Checkbutton(root, text="Ryuji [Chariot]", variable=conf_ryuji, anchor="w",command=lambda: change_sched("ryuji", conf_ryuji.get()))
    cb_ryuji.grid(row=13, column=0, columnspan=2, sticky="ew")
    cb_akechi = tk.Checkbutton(root, text="Akechi [Justice]", variable=conf_akechi, anchor="w",command=lambda: change_sched("akechi", conf_akechi.get()))
    cb_akechi.grid(row=14, column=0, columnspan=2, sticky="ew")
    cb_futaba = tk.Checkbutton(root, text="Futaba [Hermit]", variable=conf_futaba, anchor="w",command=lambda: change_sched("futaba", conf_futaba.get()))
    cb_futaba.grid(row=15, column=0, columnspan=2, sticky="ew")
    cb_chihaya = tk.Checkbutton(root, text="Chihaya [Fortune]", variable=conf_chihaya, anchor="w",command=lambda: change_sched("chiyaya", conf_chihaya.get()))
    cb_chihaya.grid(row=16, column=0, columnspan=2, sticky="ew")
    
    # Checkbox Column 2
    
    cb_takemi = tk.Checkbutton(root, text="Takemi [Death]", variable=conf_takemi, anchor="w",command=lambda: change_sched("takemi", conf_takemi.get()))
    cb_takemi.grid(row=8, column=1, columnspan=2, sticky="ew")
    cb_iwai = tk.Checkbutton(root, text="Iwai [Hanged Man]", variable=conf_iwai, anchor="w",command=lambda: change_sched("iwai", conf_iwai.get()))
    cb_iwai.grid(row=9, column=1, columnspan=2, sticky="ew")
    cb_kawakami = tk.Checkbutton(root, text="Kawakami [Temperance]", variable=conf_kawakami, anchor="w",command=lambda: change_sched("kawakami", conf_kawakami.get()))
    cb_kawakami.grid(row=10, column=1, columnspan=2, sticky="ew")
    cb_ohya = tk.Checkbutton(root, text="Ohya [Devil]", variable=conf_ohya, anchor="w",command=lambda: change_sched("ohya", conf_ohya.get()))
    cb_ohya.grid(row=11, column=1, columnspan=2, sticky="ew")
    cb_oda = tk.Checkbutton(root, text="Oda [Tower]", variable=conf_oda, anchor="w",command=lambda: change_sched("oda", conf_oda.get()))
    cb_oda.grid(row=12, column=1, columnspan=2, sticky="ew")
    cb_hifumi = tk.Checkbutton(root, text="Hifumi [Star]", variable=conf_hifumi, anchor="w", command=lambda: change_sched("hifumi", conf_hifumi.get()))
    cb_hifumi.grid(row=13, column=1, columnspan=2, sticky="ew")
    cb_mishima = tk.Checkbutton(root, text="Mishima [Moon]", variable=conf_mishima, anchor="w", command=lambda: change_sched("mishima", conf_mishima.get()))
    cb_mishima.grid(row=14, column=1, columnspan=2, sticky="ew")
    cb_yoshida = tk.Checkbutton(root, text="Yoshida [Sun]", variable=conf_yoshida, anchor="w", command=lambda: change_sched("yoshida", conf_yoshida.get()))
    cb_yoshida.grid(row=15, column=1, columnspan=2, sticky="ew")
    cb_maruki = tk.Checkbutton(root, text="Maruki [Councilor]", variable=conf_maruki, anchor="w", command=lambda: change_sched("maruki", conf_maruki.get()))
    cb_maruki.grid(row=16, column=1, columnspan=2, sticky="ew")
    cb_kasumi = tk.Checkbutton(root, text="Kasumi [Faith]", variable=conf_kasumi, anchor="w", command=lambda: change_sched("kasumi", conf_kasumi.get()))
    cb_kasumi.grid(row=16, column=1, columnspan=2, sticky="ew")
    
    """# Months 
    
    cb_may = tk.Checkbutton(root, text="May", variable=person2, anchor="w")
    checkbox.grid(row=8, column=3, sticky="ew")
    checkbox = tk.Checkbutton(root, text="Check me", variable=person1, anchor="w")
    checkbox.grid(row=9, column=3,  sticky="ew")
    checkbox = tk.Checkbutton(root, text="No, Check me", variable=person2, anchor="w")
    checkbox.grid(row=10, column=3, sticky="ew")
    checkbox = tk.Checkbutton(root, text="Check me", variable=person1, anchor="w")
    checkbox.grid(row=11, column=3, sticky="ew")
    checkbox = tk.Checkbutton(root, text="No, Check me", variable=person2, anchor="w")
    checkbox.grid(row=12, column=3, sticky="ew")
    checkbox = tk.Checkbutton(root, text="Check me", variable=person1, anchor="w")
    checkbox.grid(row=13, column=3, sticky="ew")
    checkbox = tk.Checkbutton(root, text="No, Check me", variable=person2, anchor="w")
    checkbox.grid(row=14, column=3, sticky="ew")
    checkbox = tk.Checkbutton(root, text="Check me", variable=person1, anchor="w")
    checkbox.grid(row=15, column=3, sticky="ew")"""
    
    # Requirements
    label = tk.Label(root, text="The Fool (Igor), Magician (Morgana), Judgement (Sae), and The World are all progressed through the story",anchor="w")
    label.grid(columnspan=4,row=8, column=3, sticky="ew")
    label = tk.Label(root, text="Strength (The Twins) can be progressed through following their requests in the velvet room",anchor="w")
    label.grid(columnspan=4,row=9, column=3, sticky="ew")

# Create the main window
root = tk.Tk()
root.title("P5R Calendar Manager")

# Specify the number of rows and columns in the table
num_rows = 4
num_columns = 7

# Create the table
create_table(root, num_rows, num_columns)

people_label = tk.Label(root, text="Inclusion Checklist", borderwidth=1, relief="solid", width=90, height=2, background="lightblue")
people_label.grid(row=6, column=0, columnspan=7, sticky="ew")  # Use grid for positioning

create_checklist(root)

# Run the Tkinter event loop
root.mainloop()
