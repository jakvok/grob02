#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter
from tkinter import ttk
import sys

root = tkinter.Tk()
root.minsize(400,300)
root.resizable(False, False)
root.title('Coord system rotation')

f0 = ttk.Frame(root)
f0_5 = ttk.LabelFrame(root, text='Input rotation angles')
f1 = ttk.LabelFrame(root, text='Input coordinates')
f2 = ttk.Frame(root)
f3 = ttk.LabelFrame(root, text='Rotated coordinates')

#f0 widgets
radio10 = ttk.Radiobutton(f0, text='Operation 10: G54, G56')
radio20 = ttk.Radiobutton(f0, text='Operation 20: G55, G57')
label_cycle = ttk.Label(f0, text='Insert CYCLE800 here:')
entry_cycle = ttk.Entry(f0, width=60)
button_set = ttk.Button(f0, text='SET')

#f0_5 widgets
label_a_popis = ttk.Label(f0_5, text='A:')
entry_a = ttk.Entry(f0_5)
label_b_popis = ttk.Label(f0_5, text='B:')
entry_b = ttk.Entry(f0_5)
label_c_popis = ttk.Label(f0_5, text='C:')
entry_c = ttk.Entry(f0_5)
label_listbox = ttk.Label(f0_5, text='Rot. sequence:')
sequences = ['X Y Z','Y Z X','Z X Y','Y X Z','Z Y X']
listbox = tkinter.Listbox(f0_5, height=3)
for seq in sequences:
    listbox.insert(tkinter.END, seq)

#f1 widgets
label_x_popis = ttk.Label(f1, text='X:')
entry_x = ttk.Entry(f1)
label_y_popis = ttk.Label(f1, text='Y:')
entry_y = ttk.Entry(f1)
label_z_popis = ttk.Label(f1, text='Z:')
entry_z = ttk.Entry(f1)

#f2 widgets
button_null = ttk.Button(f2, text='NULL')
button_go = ttk.Button(f2, text='GO!')
button_exit = ttk.Button(f2, text='EXIT', command=lambda: sys.exit(0))

#f3 widgets
label_x_out_popis = ttk.Label(f3, text='X:')
entry_x_out = ttk.Entry(f3)
label_y_out_popis = ttk.Label(f3, text='Y:')
entry_y_out = ttk.Entry(f3)
label_z_out_popis = ttk.Label(f3, text='Z:')
entry_z_out = ttk.Entry(f3)


#f0 geometry
label_cycle.grid(column=0, row=0, sticky='w', padx=7, pady=(7,0))
entry_cycle.grid(column=0, row=1, columnspan=3,padx=(7,7), sticky='ew')
radio10.grid(column=0, row=2, pady=7, padx=(7,20))
radio20.grid(column=1, row=2, pady=7, padx=(7,20))
button_set.grid(column=3, row=1)

#f0_5 geometry
label_a_popis.grid(column=0, row=0, padx=(7,0))
entry_a.grid(column=1, row=0, pady=5, padx=(0,7))
label_b_popis.grid(column=2, row=0, padx=(7,0))
entry_b.grid(column=3, row=0, pady=5, padx=(0,7))
label_c_popis.grid(column=4, row=0, padx=(7,0))
entry_c.grid(column=5, row=0, pady=5, padx=(0,7))
listbox.grid(column=3, row=1, pady=7)
label_listbox.grid(column=1, row=1, sticky='nse')

#f1 geometry
label_x_popis.grid(column=0, row=0, padx=(7,0))
entry_x.grid(column=1, row=0, pady=5, padx=(0,7))
label_y_popis.grid(column=2, row=0, padx=(7,0))
entry_y.grid(column=3, row=0, pady=5, padx=(0,7))
label_z_popis.grid(column=4, row=0, padx=(7,0))
entry_z.grid(column=5, row=0, pady=5, padx=(0,7))

#f2 geometry
button_null.grid(column=0, row=0, sticky='', padx=40)
button_go.grid(column=1, row=0, sticky='', padx=40)
button_exit.grid(column=2, row=0, sticky='', padx=40)

#f3 geometry
label_x_out_popis.grid(column=0, row=0, padx=(7,0))
entry_x_out.grid(column=1, row=0, pady=5, padx=(0,7))
label_y_out_popis.grid(column=2, row=0, padx=(7,0))
entry_y_out.grid(column=3, row=0, pady=5, padx=(0,7))
label_z_out_popis.grid(column=4, row=0, padx=(7,0))
entry_z_out.grid(column=5, row=0, pady=5, padx=(0,7))


f0.grid(column=0, row=0, pady=7, padx=7, sticky='we')
f0_5.grid(column=0, row=1, pady=7, padx=7)
f1.grid(column=0, row=2, pady=7, padx=7)
f2.grid(column=0, row=3, pady=7, padx=7, sticky='we')
f3.grid(column=0, row=4, pady=7, padx=7)

root.mainloop()