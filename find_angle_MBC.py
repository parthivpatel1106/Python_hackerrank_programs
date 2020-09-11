import math
import cmath
ab=int(input())
bc=int(input())
angle=math.degrees(cmath.phase(complex(bc,ab)))
print(round(angle),"\u00b0",sep="")
