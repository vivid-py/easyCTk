# easyCTk
/EasyCTk - is a small framework based on ``CustomTkinter``, to make creation of a simple python GUI app a lot more easier. The main goal of this framework, to make developers focus on developing project's logic more, and concentrate on UI less.

##Key Features
 - **Easy Initializing** - easily initialize basic UI widgets, like buttons, labels and switches
 - **Easy syntax** - very simple and easy to learn and use our product, create window, labels, entries, in a really short amount of lines

## Quick Start

ʼʼʼpython
from easyCTk import *

#Initialize window
window = App()

#start creating widgets, for example, label
window.label(text="Simple Label")

#entry
window.entry(placeholder_text="Entry")

#button
window.button(text="Button")

#checkbox
window.checkbox(text="Checkbox")

#switch
window.switch(text="Switch")

#Start the window!
window.run()
ʼʼʼ
![App preview](img.png)