import math

def find_area(numb, length) :
    apofema = length/(2*(math.tan(math.pi/numb)))
    perimeter = length*numb

    area = (perimeter/2)*apofema
    print(area)

find_area(6,25)