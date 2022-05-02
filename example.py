#####################################################
#   Author: Safia Guellil                           #
#   Date: April 2022                                #
#   Version: 1.1                                    #             
#   Descriptio:                                     #
#####################################################    
    
import tkinter as tk
import os					
from tkinter import ttk

cmd = 'ls -l'
os.system(cmd)

root = tk.Tk()
root.title("AirPI")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Monitorizar')
tabControl.add(tab2, text ='Rendimiento')
tabControl.add(tab3, text ='Auditar')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1,
		text ="Monitorizar RED").grid(column = 0,
							row = 0,
							padx = 30,
							pady = 30)
ttk.Label(tab2,
		text ="Tests de Rendimiento").grid(column = 0,
									row = 0,
									padx = 30,
									pady = 30)
ttk.Label(tab3,
		text ="Auditar Red").grid(column = 0,
									row = 0,
									padx = 30,
									pady = 30)


root.mainloop()

