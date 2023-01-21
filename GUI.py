import tkinter as tk
from tkinter.ttk import *
from activity import communication

window = tk.Tk()
window.title("Conflict Coach")
window.geometry("350x400")
window.minsize(350, 400)
window.maxsize(350, 400)

greeting = tk.Label(text="Hello, welcome to Conflict Coach")
greeting.place(x=200, y=25, anchor="center")
greeting.grid(row=0, column=0, sticky="n")


def handle_start(event):

    def next_page():
        msg = str(scenario_num["text"])
        value = int(msg.split(" ")[-1])
        next = value + 1
        scenario_num["text"] = f"Scenario {next}"
        if next == 2:
            s1_lbl1["text"] = "At home, your sister Amy is arguing with you.\n"
            s1_lbl2["text"] = "Amy: \nI’m older so I should have control of the remote control!\n"

    def handle_reply():
        starter = s1_lbl2["text"].split(": ")[-1]
        starter_res = communication.get_class(starter)

        reply = entry.get()
        reply_res = communication.get_class(reply)

        final_res = communication.reasonable_answer(starter_res, reply_res)
        
        res_lbl = tk.Label(newWindow,
            text = f"{final_res}" )
        res_lbl.grid(row=2, column=0, padx=5, pady=5)


        s1_lbl1.grid_forget()
        s1_lbl2.grid_forget()
        print("yep")

    newWindow = tk.Toplevel(window)
    newWindow.title("Conflict Simulator")
    newWindow.geometry("350x400")
    newWindow.minsize(350, 400)
    newWindow.maxsize(350, 400)
   
    scenario_num = tk.Label(newWindow,
          text = "Scenario 1")
    scenario_num.grid(row=1, column=0, padx=5, pady=5, sticky='n')

    s1_lbl1 = tk.Label(newWindow,
            text = "In the classroom, \nyour classmate Jason is talking to you.\n" )

    s1_lbl2 = tk.Label(newWindow, 
            text="Jason: \nYou can't even get that answer? You're so dumb!\n")
            
    s1_lbl1.grid(row=2, column=0, padx=5, sticky='n')
    s1_lbl2.grid(row=3, column=0, padx=5, sticky='n')

    entry= Entry(newWindow, width= 25)
    entry.focus_set()
    entry.grid(row=4, column=0, sticky='n')
    
    
    but_sub = tk.Button(
        newWindow,
        text="Reply",
        width=10,
        height=2,
        background='Thistle',
        highlightbackground='Thistle',
        fg="white",
        command=handle_reply
    )
    but_sub.grid(row=6, column=0, padx=5, pady=5)

    but_next = tk.Button(
        newWindow,
        text="Next",
        width=10,
        height=2,
        background='Thistle',
        highlightbackground='Thistle',
        fg="white",
        command=next_page
    )
    but_next.grid(row=7, column=0, padx=5, pady=5)

but_start = tk.Button(
    text="Quick Start",
    width=15,
    height=3,
    background='Thistle',
    highlightbackground='Thistle',
    fg="white",
)
but_start.bind("<Button-1>", handle_start)
but_start.grid(row=1, column=0, padx=5, pady=5)
    

but_peers = tk.Button(
    text="Peers",
    width=15,
    height=3,
    background='Thistle',
    highlightbackground='Thistle',
    fg="white",
)
# but_peers.bind("<Button-1>", handle_peers)
but_peers.grid(row=2, column=0, padx=5, pady=5)

but_parents = tk.Button(
    text="Parents",
    width=15,
    height=3,
    background='Thistle',
    highlightbackground='Thistle',
    fg="white",
)
but_parents.grid(row=3, column=0, padx=5, pady=5)

but_strangers = tk.Button(
    text="Strangers",
    width=15,
    height=3,
    background='Thistle',
    highlightbackground='Thistle',
    fg="white",
)
but_strangers.grid(row=4, column=0, padx=5, pady=5)

window.mainloop()