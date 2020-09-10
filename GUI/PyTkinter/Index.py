import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import Tk, Canvas, Frame, BOTH
import requests

#createting center windows
def center_window(w=700, h=700):
    # get screen width and height
    ws = master.winfo_screenwidth()
    hs = master.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))

master = Tk()
center_window(800, 700) 
master.title("API CHASER")

# Getting API URL from USER

master.resizable(0, 0)
tk.Label(master, text="Drop API ").grid(row=0)

dropapi = tk.Entry(master, bg="white", width=80)
dropapi.grid(row=0, column=1)


data=("GET", "POST", "HEAD", "PUT", "OPTIONS")
cb=Combobox(master, values=data, width=15)
cb.place(x=60, y=150)
cb.grid(row=0, column=2)

submit = tk.Button(text="Submit", width= 20)
submit.grid(row=0, column=3)


#Start Getting Response from API and print here
def headresponse():
    r = requests.head(dropapi)
    print("[+] HEAD Response : " + str(r))
    #print(r)

# print response in Grid box
headerlabel = tk.Label(master, text="HEADER RESPONSE ")
headerlabel.place(x = 10,
        y = 30,
        width=200,
        height=100)

entryExample = tk.Entry(master)
entryExample.place(x = 10,
        y = 90,
        width=350,
        height=300)

# body response

requestlabel = tk.Label(master, text="REQUEST RESPONSE ")
requestlabel.place(x = 400,
        y = 30,
        width=200,
        height=100)

entryExample = tk.Entry(master)
entryExample.place(x = 400,
        y = 90,
        width=350,
        height=300)








    

#Keep Running Application until user close thi window
master.mainloop()

