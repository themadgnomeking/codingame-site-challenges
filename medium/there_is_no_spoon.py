#The program must first read the initialization data from standard input. Then, provide to the standard output one line per instruction.
#Initialization input
#Line 1: one integer width for the number of cells along the x axis.

#Line 2: one integer height for the number of cells along the y axis.

#Next height lines: A string  line  containing  width  characters. A dot . represents an empty cell. A zero 0 represents a cell containing a node.

#Output for one game turn
#One line per node. Six integers on each line:   x1  y1  x2  y2  x3  y3

#Where:
#(x1,y1) the coordinates of a node
#(x2,y2) the coordinates of the closest neighbor on the right of the node
#(x3,y3) the coordinates of the closest bottom neighbor
#If there is no neighbor, the coordinates should be -1 -1.
#Constraints
#0 < width ≤ 30
#0 < height ≤ 30
#0 ≤ x1 < width
#0 ≤ y1 < height
#-1 ≤ x2, x3 < width
#-1 ≤ y2, y3 < height
#Alloted response time to first output line ≤ 1s.
#Response time between two output lines ≤ 100ms

#starter code
import sys
import math

# Don't let the machines win. You are humanity's last hope...
def there_is_no_spoon():
    width = int(input())  # the number of cells on the X axis
    height = int(input())  # the number of cells on the Y axis
    for i in range(height):
        line = input()  # width characters, each either 0 or .

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)



    # Three coordinates: a node, its right neighbor, its bottom neighbor
    print("0 0 1 0 0 1")


