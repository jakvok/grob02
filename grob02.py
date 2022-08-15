#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk, messagebox
import sys
import transform

class Main_window(tkinter.Tk):
    '''
    Class represents point's (vector's) transformator from base coordinate system to rotated coordinate system.
    If you set coordinates of the "input point", set of angles which say how coordinate system's axes rotate and sequence in which order axes rotate,
    you get set of coordinates of the point in rotated coordinate system.
    '''

    def __init__(self):
        super().__init__()
        self.minsize(400,300) # dimmensions of main window
        self.resizable(False, False) # not resizable main window
        self.title('Coord system rotation') # name of app

        # init frames
        self.f0 = ttk.Frame(self)
        self.f0_5 = ttk.LabelFrame(self, text='Input rotation angles')
        self.f1 = ttk.LabelFrame(self, text='Input coordinates')
        self.f2 = ttk.Frame(self)
        self.f3 = ttk.LabelFrame(self, text='Rotated coordinates')
        
        # init variables, styles, widgets and geometry
        self.create_variables()
        self.create_styles()
        self.create_widgets()
        self.create_geometry()


    def create_styles(self):
        # define look styles of some widgets
        style = ttk.Style()
        style.configure('GO.TButton', font=('Sans', '12' ,'bold'), foreground='green')
        style.configure('EXIT.TButton', foreground='red')
        style.configure('OUT.TLabel', width=13 ,background='white' ,font=('Sans','12','bold')) # style of output values


    def create_variables(self):
        # var for rotation axes sequence
        self.sequence = tkinter.StringVar(self)
        self.sequence.set('YXZ')
        
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
        
        # vars for input point (vector) coordinates
        self.input_X = tkinter.DoubleVar(self)
        self.input_X.set(0.0)
        self.input_Y = tkinter.DoubleVar(self)
        self.input_Y.set(0.0)
        self.input_Z = tkinter.DoubleVar(self)
        self.input_Z.set(0.0)

        # vars for output point (vector) coordinates
        self.output_X = tkinter.DoubleVar(self)
        self.output_X.set(0.0)
        self.output_Y = tkinter.DoubleVar(self)
        self.output_Y.set(0.0)
        self.output_Z = tkinter.DoubleVar(self)
        self.output_Z.set(0.0)


    def create_widgets(self):
        # widgets in frame f0
        
        # radiobutton for predefined operation10
        self.radio10 = ttk.Radiobutton(self.f0, text='Operation 10: G54, G56', variable=self.operation, value='op10', command=self.set_input_angles_op10)
        # radiobutton for predefined operation20
        self.radio20 = ttk.Radiobutton(self.f0, text='Operation 20: G55, G57', variable=self.operation, value='op20', command=self.set_input_angles_op20)
        # label and entry field for CYCLE800 direct insertion
        self.label_cycle = ttk.Label(self.f0, text='Insert CYCLE800 here:')
        self.entry_cycle = ttk.Entry(self.f0, width=60, textvariable=self.cycle)
        # button for fire function to find angle values from raw CYCLE800 string
        self.button_set = ttk.Button(self.f0, text='SET', command=self.set_cycle)

        
        # commands for number input validation handling
        vcmd = (self.register(self.check_number), '%P', '%W')
        ivcmd = (self.register(self.bad_number), '%W')
        
        # widgets in frame f0_5
        
        # label and entry field for angle A (X axis)
        self.label_a_popis = ttk.Label(self.f0_5, text='A:')
        self.entry_a = ttk.Entry(self.f0_5, textvariable=self.input_angle_A)
        self.entry_a.configure(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        # label and entry field for angle B (Y axis)
        self.label_b_popis = ttk.Label(self.f0_5, text='B:')
        self.entry_b = ttk.Entry(self.f0_5, textvariable=self.input_angle_B)
        self.entry_b.configure(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        # label and entry field for angle C (Z axis)
        self.label_c_popis = ttk.Label(self.f0_5, text='C:')
        self.entry_c = ttk.Entry(self.f0_5, textvariable=self.input_angle_C)
        self.entry_c.configure(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        # label and menu for axes rotation sequence
        self.label_seq = ttk.Label(self.f0_5, text='Rot. sequence:')
        sequences = ['ZYX', 'YZX', 'ZXY', 'XZY', 'YXZ', 'XYZ']
        self.menu_seq = tkinter.OptionMenu(self.f0_5,self.sequence, *sequences)

        # widgets in frame f1
        
        # label and entry field for X axis of input point (vector)
        self.label_x_popis = ttk.Label(self.f1, text='X:')
        self.entry_x = ttk.Entry(self.f1, textvariable=self.input_X)
        self.entry_x.configure(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        # label and entry field for Y axis of input point (vector)
        self.label_y_popis = ttk.Label(self.f1, text='Y:')
        self.entry_y = ttk.Entry(self.f1, textvariable=self.input_Y)
        self.entry_y.configure(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        # label and entry field for Z axis of input point (vector)
        self.label_z_popis = ttk.Label(self.f1, text='Z:')
        self.entry_z = ttk.Entry(self.f1, textvariable=self.input_Z)
        self.entry_z.configure(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)

        # widgets in frame f2
        
        # button for run function nulling input values
        self.button_null = ttk.Button(self.f2, text='NULL', command=self.nulling)
        # button to run transformation function
        self.button_go = ttk.Button(self.f2, text='GO!', style='GO.TButton', command=self.go_transform)
        # button to quit app
        self.button_exit = ttk.Button(self.f2, text='EXIT', style='EXIT.TButton', command=lambda: sys.exit(0))

        # widgets in frame f3
        
        # label and entry field for X axis of output point (vector)
        self.label_x_out_popis = ttk.Label(self.f3, text='X:')
        self.entry_x_out = ttk.Label(self.f3, textvariable=self.output_X, style='OUT.TLabel')
        # label and entry field for Y axis of output point (vector)
        self.label_y_out_popis = ttk.Label(self.f3, text='Y:')
        self.entry_y_out = ttk.Label(self.f3, textvariable=self.output_Y, style='OUT.TLabel')
        # label and entry field for Z axis of output point (vector)
        self.label_z_out_popis = ttk.Label(self.f3, text='Z:')
        self.entry_z_out = ttk.Label(self.f3, textvariable=self.output_Z, style='OUT.TLabel')


    def create_geometry(self):
        # geometry inside frame f0
        self.label_cycle.grid(column=0, row=0, sticky='w', padx=7, pady=(7,0))
        self.entry_cycle.grid(column=0, row=1, columnspan=3,padx=(7,7), sticky='ew')
        self.radio10.grid(column=0, row=2, pady=7, padx=(7,20))
        self.radio20.grid(column=1, row=2, pady=7, padx=(7,20))
        self.button_set.grid(column=3, row=1)

        # geometry inside frame f0_5
        self.label_a_popis.grid(column=0, row=0, padx=(7,0))
        self.entry_a.grid(column=1, row=0, pady=5, padx=(0,7))
        self.label_b_popis.grid(column=2, row=0, padx=(7,0))
        self.entry_b.grid(column=3, row=0, pady=5, padx=(0,7))
        self.label_c_popis.grid(column=4, row=0, padx=(7,0))
        self.entry_c.grid(column=5, row=0, pady=5, padx=(0,7))
        self.menu_seq.grid(column=3, row=1, pady=7, sticky=tkinter.W)
        self.label_seq.grid(column=1, row=1, sticky='nse')

        # geometry inside frame f1
        self.label_x_popis.grid(column=0, row=0, padx=(7,0))
        self.entry_x.grid(column=1, row=0, pady=5, padx=(0,7))
        self.label_y_popis.grid(column=2, row=0, padx=(7,0))
        self.entry_y.grid(column=3, row=0, pady=5, padx=(0,7))
        self.label_z_popis.grid(column=4, row=0, padx=(7,0))
        self.entry_z.grid(column=5, row=0, pady=5, padx=(0,7))

        # geometry inside frame f2
        self.button_null.grid(column=0, row=0, sticky='', padx=40)
        self.button_go.grid(column=1, row=0, sticky='', padx=40)
        self.button_exit.grid(column=2, row=0, sticky='', padx=40)

        #geometry inside frame f3
        self.label_x_out_popis.grid(column=0, row=0, padx=(7,0))
        self.entry_x_out.grid(column=1, row=0, pady=5, padx=(0,7))
        self.label_y_out_popis.grid(column=2, row=0, padx=(7,0))
        self.entry_y_out.grid(column=3, row=0, pady=5, padx=(0,7))
        self.label_z_out_popis.grid(column=4, row=0, padx=(7,0))
        self.entry_z_out.grid(column=5, row=0, pady=5, padx=(0,7))

        # frames geometry inside main window
        self.f0.grid(column=0, row=0, pady=7, padx=7, sticky='we')
        self.f0_5.grid(column=0, row=1, pady=7, padx=7)
        self.f1.grid(column=0, row=2, pady=7, padx=7)
        self.f2.grid(column=0, row=3, pady=7, padx=7, sticky='we')
        self.f3.grid(column=0, row=4, pady=7, padx=7)


    def set_cycle(self):
        '''
        method to find rotation angles from CYCLE800 string representation
        '''
        try:
            line = self.cycle.get()
            
            # isolate string just between brackets
            a = False
            parameters = ''
            for n in line:
                if n == ')': a = False
                if a: parameters += n
                if n == '(': a = True
            
            # split isolated string by comma char
            parameters = parameters.split(',')
            # fill list of angles by values found at splitted string
            angles = [float(parameters[7]), float(parameters[8]), float(parameters[9])]
            
            # check if angles are in correct range
            for b in angles:
                if b > 360.0 or b < -360.0:
                    self.cycle.set('Angles out of range.')
                    raise Exception()
            
            # fill input angles variables by values in order to sequence found in splitted string
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
        # method to null input point coordinates
        self.input_X.set(0.0)
        self.input_Y.set(0.0)
        self.input_Z.set(0.0)


    def go_transform(self):
        '''
         method to perform "input point" (vector) transformation from base CS to rotated CS
        '''
        a = self.input_angle_A.get()
        b = self.input_angle_B.get()
        c = self.input_angle_C.get()
        x = self.input_X.get()
        y = self.input_Y.get()
        z = self.input_Z.get()
        
        # define transformation object
        t = transform.Transform3D([a,b,c],self.sequence.get())
        # call transformation method
        t_point = t.transform([x, y, z])
        
        # set result into output variables
        self.output_X.set(round(t_point[0], 4))
        self.output_Y.set(round(t_point[1], 4))
        self.output_Z.set(round(t_point[2], 4))
        

    def set_input_angles_op10(self):
        '''
        method to set predefined input values for operation10
        '''
        self.input_angle_A.set(-135.0)
        self.input_angle_B.set(90.0)
        self.input_angle_C.set(180.0)
        self.cycle.set('CYCLE800(0,"TC_GROB",200000,54,0,0,0,90.,-135.,180.,0,0,0,1,0,0)')
        self.sequence.set('YXZ')


    def set_input_angles_op20(self):
        '''
        method to set predefined input values for operation20
        '''
        self.input_angle_A.set(-135.0)
        self.input_angle_B.set(-90.0)
        self.input_angle_C.set(180.0)
        self.cycle.set('CYCLE800(0,"TC_GROB",200000,54,0,0,0,-90.,-135.,180.,0,0,0,1,0,0)')
        self.sequence.set('YXZ')

    def check_number(self, value, widg):
        '''
        function check if entry input is number and returns True if so,
        if not, returns False and pait value to red

        '''
        try:
            float(value)
            self.nametowidget(widg)['foreground'] = 'black' # method points to current widget object
            return True
        except ValueError:
            if value == '':
                self.nametowidget(widg).insert(0, 0.0)
                return True
            self.nametowidget(widg)['foreground'] = 'red'
            return False

    def bad_number(self, widg):
        '''
        when entry input is not valid, shows error message box and change entry value to 0.0
        '''
        messagebox.showerror('Value Error', 'Input value must be a number!')
        self.nametowidget(widg).delete(0, len(self.nametowidget(widg).get())) # delete involved string chars from index 0 to the last srting index
        self.nametowidget(widg).insert(0, 0.0) # insert value 0.0
        self.nametowidget(widg)['foreground'] = 'black'


app = Main_window()
app.mainloop()