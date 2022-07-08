# CSYS convert utility

The script is used to convert dimensional values between two rotated coordinate systems in CNC program.<br>
If you set coordinates of the "input point", angle values which say how much coordinate system's axes rotate and sequence in which order axes rotate, you get set of coordinates of the point in rotated coordinate system.
CNC milling machine operator can easy set dimm corrections into machine using the script.
<br><br>
# Using of the script
- Define rotation of coordinate system. Here are three possibilities:
    - Direct set angle in [+-360] degree values into entry boxes A, B, C. <br>Box A is rotation about axis X, B is rotation about Y and C is rotation about Z.<br> Don't forget to direct set of rotation sequence from drop-down menu, it define order in which each axes rotate.
    - Copy and paste Siemens CYCLE800 rotation cycle into upper text field and hit `SET` button. Angle values and axes rotation sequence fill automatically.
    - Choose predefined angle values and rotation sequence by checking radiobutton of operation 10 or 20
- Set input coordinates into entry boxes X, Y, Z,
- hit `GO!` button to provide calculation,
- see result rotated coordinates in bottom output boxes.
- The `NULL` button delete input coordinates
<br><br>
## linux
Python 3.9+, only standard modules required on linux.<br>
Make the script executable:<br>
`$ chmod +x ./grob02.py`<br>
have file `transform.py` in the same folder.

Run the script:<br>
`$ ./grob02.py`
<br><br>
## windows
When python 3.9+ installed, using is the same as on linux system.

Or when python is not available on your win system, use the standalone executable `grob02_vx.x.x.exe`.<br>