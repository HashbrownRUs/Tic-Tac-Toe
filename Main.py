import re
import sys

print("X goes first")
winner = False
currentValues = [[" "," "," "],[" "," "," "],[" "," "," "]]


while (not winner):
    try:
        userInput = input("Coordinates ")
        coordinates =  [int(x) for x in re.split('[^0-9]',userInput)]
        if ((len(coordinates) != 2) or (coordinates[0] >= 3) or (coordinates[1] >= 3) or (coordinates[0] < 0) or (coordinates[1] < 0)):
            raise TypeError    
    except KeyboardInterrupt:
        sys.exit()
    except:
        print("invald input")
        continue
    print(coordinates)

print(
"""
 _ _ _ _ 
| {} {} {} |
| {} {} {} |
| {} {} {} |
 ‾ ‾ ‾ ‾ 
""" 
.format(
    currentValues[0][2],currentValues[1][2],currentValues[2][2],
    currentValues[0][1],currentValues[1][1],currentValues[2][1],
    currentValues[0][0],currentValues[1][0],currentValues[2][0]
    )
)