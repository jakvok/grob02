#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
import sys
import transform

class Main_window(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.minsize(400,300)
        self.resizable(False, False)
        self.title('Coord system rotation')

        # init frames
        self.f0 = ttk.Frame(self)
        self.f0_5 = ttk.LabelFrame(self, text='Input rotation angles')
        self.f1 = ttk.LabelFrame(self, text='Input coordinates')
        self.f2 = ttk.Frame(self)
        self.f3 = ttk.LabelFrame(self, text='Rotated coordinates')

        self.create_variables()
        self.create_styles()
        self.create_widgets()
        self.create_geometry()


    def create_styles(self):
        style = ttk.Style()
        style.configure('GO.TButton', font=('Sans', '12' ,'bold'), foreground='green')
        style.configure('EXIT.TButton', foreground='red')
        style.configure('OUT.TLabel', width=13 ,background='white' ,font=('Sans','12','bold'))


    def create_variables(self):
        # var for rotation axes sequence
        self.sequence = tkinter.StringVar(self)
        self.sequence.set('YZX')
        
        # var for predefined operation
        self.operation = tkinter.StringVar(self)
        self.operation.set('op10')
        
        # var for cycle800 definition        
        self.cycle = tkinter.StringVar(self)
        self.cycle.set('CYCLE800(0,"TC_GROB",200000,54,0,0,0,90.,-135.,180.,0,0,0,1,0,0)')
        
        # vars for rotation angles
        self.input_angle_A = tkinter.DoubleVar(self)
        self.input_angle_A.set(-135.0)
        self.input_angle_B = tkinter.DoubleVar(self)
        self.input_angle_B.set(90.0)
        self.input_angle_C = tkinter.DoubleVar(self)
        self.input_angle_C.set(180.0)
        
        # vars for input coordinates
        self.input_X = tkinter.DoubleVar(self)
        self.input_X.set(0.0)
        self.input_Y = tkinter.DoubleVar(self)
        self.input_Y.set(0.0)
        self.input_Z = tkinter.DoubleVar(self)
        self.input_Z.set(0.0)

        # vars for output coordinates
        self.output_X = tkinter.DoubleVar(self)
        self.output_X.set(0.0)
        self.output_Y = tkinter.DoubleVar(self)
        self.output_Y.set(0.0)
        self.output_Z = tkinter.DoubleVar(self)
        self.output_Z.set(0.0)


    def create_widgets(self):
        #f0 widgets
        self.radio10 = ttk.Radiobutton(self.f0, text='Operation 10: G54, G56', variable=self.operation, value='op10', command=self.set_input_angles_op10)
        self.radio20 = ttk.Radiobutton(self.f0, text='Operation 20: G55, G57', variable=self.operation, value='op20', command=self.set_input_angles_op20)
        self.label_cycle = ttk.Label(self.f0, text='Insert CYCLE800 here:')
        self.entry_cycle = ttk.Entry(self.f0, width=60, textvariable=self.cycle)
        self.button_set = ttk.Button(self.f0, text='SET', command=self.set_cycle)

        #f0_5 widgets
        self.label_a_popis = ttk.Label(self.f0_5, text='A:')
        self.entry_a = ttk.Entry(self.f0_5, textvariable=self.input_angle_A)
        self.label_b_popis = ttk.Label(self.f0_5, text='B:')
        self.entry_b = ttk.Entry(self.f0_5, textvariable=self.input_angle_B)
        self.label_c_popis = ttk.Label(self.f0_5, text='C:')
        self.entry_c = ttk.Entry(self.f0_5, textvariable=self.input_angle_C)
        self.label_seq = ttk.Label(self.f0_5, text='Rot. sequence:')
        sequences = ['ZYX', 'YZX', 'ZXY', 'XZY', 'YZX', 'XYZ']
        self.menu_seq = tkinter.OptionMenu(self.f0_5,self.sequence, *sequences)

        #f1 widgets
        self.label_x_popis = ttk.Label(self.f1, text='X:')
        self.entry_x = ttk.Entry(self.f1, textvariable=self.input_X)
        self.label_y_popis = ttk.Label(self.f1, text='Y:')
        self.entry_y = ttk.Entry(self.f1, textvariable=self.input_Y)
        self.label_z_popis = ttk.Label(self.f1, text='Z:')
        self.entry_z = ttk.Entry(self.f1, textvariable=self.input_Z)

        #f2 widgets
        self.button_null = ttk.Button(self.f2, text='NULL', command=self.nulling)
        self.button_go = ttk.Button(self.f2, text='GO!', style='GO.TButton', command=self.go_transform)
        self.button_exit = ttk.Button(self.f2, text='EXIT', style='EXIT.TButton', command=lambda: sys.exit(0))

        #f3 widgets
        self.label_x_out_popis = ttk.Label(self.f3, text='X:')
        self.entry_x_out = ttk.Label(self.f3, textvariable=self.output_X, style='OUT.TLabel')
        self.label_y_out_popis = ttk.Label(self.f3, text='Y:')
        self.entry_y_out = ttk.Label(self.f3, textvariable=self.output_Y, style='OUT.TLabel')
        self.label_z_out_popis = ttk.Label(self.f3, text='Z:')
        self.entry_z_out = ttk.Label(self.f3, textvariable=self.output_Z, style='OUT.TLabel')


    def create_geometry(self):
        #f0 geometry
        self.label_cycle.grid(column=0, row=0, sticky='w', padx=7, pady=(7,0))
        self.entry_cycle.grid(column=0, row=1, columnspan=3,padx=(7,7), sticky='ew')
        self.radio10.grid(column=0, row=2, pady=7, padx=(7,20))
        self.radio20.grid(column=1, row=2, pady=7, padx=(7,20))
        self.button_set.grid(column=3, row=1)

        #f0_5 geometry
        self.label_a_popis.grid(column=0, row=0, padx=(7,0))
        self.entry_a.grid(column=1, row=0, pady=5, padx=(0,7))
        self.label_b_popis.grid(column=2, row=0, padx=(7,0))
        self.entry_b.grid(column=3, row=0, pady=5, padx=(0,7))
        self.label_c_popis.grid(column=4, row=0, padx=(7,0))
        self.entry_c.grid(column=5, row=0, pady=5, padx=(0,7))
        self.menu_seq.grid(column=3, row=1, pady=7, sticky=tkinter.W)
        self.label_seq.grid(column=1, row=1, sticky='nse')

        #f1 geometry
        self.label_x_popis.grid(column=0, row=0, padx=(7,0))
        self.entry_x.grid(column=1, row=0, pady=5, padx=(0,7))
        self.label_y_popis.grid(column=2, row=0, padx=(7,0))
        self.entry_y.grid(column=3, row=0, pady=5, padx=(0,7))
        self.label_z_popis.grid(column=4, row=0, padx=(7,0))
        self.entry_z.grid(column=5, row=0, pady=5, padx=(0,7))

        #f2 geometry
        self.button_null.grid(column=0, row=0, sticky='', padx=40)
        self.button_go.grid(column=1, row=0, sticky='', padx=40)
        self.button_exit.grid(column=2, row=0, sticky='', padx=40)

        #f3 geometry
        self.label_x_out_popis.grid(column=0, row=0, padx=(7,0))
        self.entry_x_out.grid(column=1, row=0, pady=5, padx=(0,7))
        self.label_y_out_popis.grid(column=2, row=0, padx=(7,0))
        self.entry_y_out.grid(column=3, row=0, pady=5, padx=(0,7))
        self.label_z_out_popis.grid(column=4, row=0, padx=(7,0))
        self.entry_z_out.grid(column=5, row=0, pady=5, padx=(0,7))


        self.f0.grid(column=0, row=0, pady=7, padx=7, sticky='we')
        self.f0_5.grid(column=0, row=1, pady=7, padx=7)
        self.f1.grid(column=0, row=2, pady=7, padx=7)
        self.f2.grid(column=0, row=3, pady=7, padx=7, sticky='we')
        self.f3.grid(column=0, row=4, pady=7, padx=7)


    def set_cycle(self):
        try:
            line = self.cycle.get()
            a = False
            parameters = ''
            for n in line:
                if n == ')': a = False
                if a: parameters += n
                if n == '(': a = True
            
            parameters = parameters.split(',')
            angles = [float(parameters[7]), float(parameters[8]), float(parameters[9])]
            
            for b in angles:
                if b > 360.0 or b < -360.0:
                    self.cycle.set('Angles out of range.')
                    raise Exception()
            
            if parameters[3] == '54':
                self.input_angle_A.set(float(parameters[8]))
                self.input_angle_B.set(float(parameters[7]))
                self.input_angle_C.set(float(parameters[9]))
                self.sequence.set('YXZ')
            elif parameters[3] == '27':
                self.input_angle_A.set(float(parameters[9]))
                self.input_angle_B.set(float(parameters[8]))
                self.input_angle_C.set(float(parameters[7]))
                self.sequence.set('ZYX')
            elif parameters[3] == '30':
                self.input_angle_A.set(float(parameters[8]))
                self.input_angle_B.set(float(parameters[9]))
                self.input_angle_C.set(float(parameters[7]))
                self.sequence.set('YZX')
            elif parameters[3] == '39':
                self.input_angle_A.set(float(parameters[9]))
                self.input_angle_B.set(float(parameters[7]))
                self.input_angle_C.set(float(parameters[8]))
                self.sequence.set('ZXY')
            elif parameters[3] == '45':
                self.input_angle_A.set(float(parameters[7]))
                self.input_angle_B.set(float(parameters[9]))
                self.input_angle_C.set(float(parameters[8]))
                self.sequence.set('XZY')
            elif parameters[3] == '57':
                self.input_angle_A.set(float(parameters[7]))
                self.input_angle_B.set(float(parameters[8]))
                self.input_angle_C.set(float(parameters[9]))
                self.sequence.set('XYZ')
            else:
                self.cycle.set('Not supported sequence.')                                       

        except:
            self.cycle.set('Not supported format.')


    def nulling(self):
        self.input_X.set(0.0)
        self.input_Y.set(0.0)
        self.input_Z.set(0.0)


    def go_transform(self):
        a = self.input_angle_A.get()
        b = self.input_angle_B.get()
        c = self.input_angle_C.get()
        x = self.input_X.get()
        y = self.input_Y.get()
        z = self.input_Z.get()
        
        t = transform.Transform3D([a,b,c],self.sequence.get())
        t_point = t.transform([x, y, z])
        
        self.output_X.set(round(t_point[0], 4))
        self.output_Y.set(round(t_point[1], 4))
        self.output_Z.set(round(t_point[2], 4))
        

    def set_input_angles_op10(self):
        self.input_angle_A.set(-135.0)
        self.input_angle_B.set(90.0)
        self.input_angle_C.set(180.0)
        self.cycle.set('CYCLE800(0,"TC_GROB",200000,54,0,0,0,90.,-135.,180.,0,0,0,1,0,0)')
        self.sequence.set('YXZ')


    def set_input_angles_op20(self):
        self.input_angle_A.set(-135.0)
        self.input_angle_B.set(-90.0)
        self.input_angle_C.set(180.0)
        self.cycle.set('CYCLE800(0,"TC_GROB",200000,54,0,0,0,-90.,-135.,180.,0,0,0,1,0,0)')
        self.sequence.set('YXZ')


app = Main_window()
app.mainloop()