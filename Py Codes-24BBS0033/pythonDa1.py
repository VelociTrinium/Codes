import math
(r,a)=map(float, input().split())
print(format((((math.pi*r*r)*(a*4))-(r*a))/((math.pi*r*r)+(a*a)),'.2f'))