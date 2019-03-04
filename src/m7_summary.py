"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Ruth Hammond.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
#
# DONE: 2.
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:

import rosegraphics as rg
window = rg.TurtleWindow()

#    - Constructs a SimpleTurtle with a  'blue'  Pen.
mike = rg.SimpleTurtle("turtle")
mike.pen = rg.Pen("blue",0)

#    - Makes the SimpleTurtle go straight UP 200 pixels.
mike.left(90)
mike.forward(200)
#    - Makes the SimpleTurtle lift its pen UP
#         (so that the next movements do NOT leave a "trail")
#         HINT: Use the "dot trick" to figure out how to do this.
mike.pen_up()

#    - Makes the SimpleTurtle go to the Point at (100, -40).
point = rg.Point(100,-40)
mike.go_to(point)
#    - Makes the SimpleTurtle put its pen DOWN
#         (so that the next movements will return to leaving a "trail").
mike.pen_down()
#    - Makes the SimpleTurtle's pen have color 'green' and thickness 10.
mike.pen = rg.Pen("green",10)

#    - Makes the SimpleTurtle go 150 pixels straight DOWN.
mike.backward(150)

window.close_on_mouse_click()
#   Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#   As always, test by running the module.
#   As always, COMMIT-and-PUSH when you are done with this module.
#
########################################################################
