import tools
#import tools as t

while(True):
    char=input(" Enter for Area\n"
               "c for circle\n"
               "r for rectangle\n"
               "t for triangle\n"
               "s for Square\n"
               "q for Quit\n")
    if(char=='q' or char=='Q'):
        print("Goodbye")

    if(char not in 'CcSsRrTt'):
        print("Please enter a valid input")
        continue

    if(char=='c' or char=='C'):
        r=float(input("Enter the radius of the circle:"))
        print(tools.area_circle(r))

    if (char == 's' or char == 'S'):
        s =int(input("Enter Number for Square:"))
        print(tools.area_square(s))

    if(char== 'r' or char == 'R'):
        w=int(input("Enter the width of the rectangle:"))
        h=int(input("Enter the height of the rectangle:"))
        print(tools.area_rectangle(w,h))

    if(char=='t' or char == 'T'):
        w=int(input("Enter the width of the triangle:"))
        b=int(input("Enter the breath of the triangle:"))
        print(tools.area_triangle(w,b))
