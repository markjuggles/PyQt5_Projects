# PyQt5_Projects


## Prerequisites

A version of Python 3.x.x. Version 3.10 did not work for PyQt5 on my system but version 3.9.10 was fine.  
Of course at some point, some 3.10.xx version will probably be fine.

Install PyQt5 with: pip install pyqt5

Install PyQt5 Tools with: pip install pyqt5-tools

## Path

You need to find the install directory of the Python whose pip use used to install.

At a Windows or Linux command prompt, use this command:  where python

This will return the full path to Python.  Starting at the directory (and ignoring the executable filename)
append this path:  \Lib\site-packages\qt5_applications\Qt\bin

Use forward slashes on Linux.  This is the path to the PyQt5 "designer" application.


## PyQt5 Designer

The "designer" command runs the UI designer program.  The output is a ".ui" file.

## PyQt5 Compiler
<p>
pyuic5 -x project.ui -o project_ui.py
<p>
The purpose for the "_ui" in the output filename is to make it clear which code is created by designer and pyuic5.
<p>
Then the main application can import the "project_ui" to complete the implementation of the solution without
modifying the tools' output which may change as the project is developed.

## References

"PyQt5 Tutorial - Setup and a Basic GUI Application" by Tech With Tim on Youtube.
"PyQt5 Tutorial - How to Use Qt Designer"

by "Tech With Tim" on YouTube.

https://www.youtube.com/watch?v=Vde5SH8e1OQ










