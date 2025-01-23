import math 

#What is the length of a side of the square? 5
#The area of the square is: 25.0
#What is the length of rectangle? 6
#What is the width of the rectangle? 7
#The area of the rectangle is: 42.0
#What is the radius of the circle? 5
#The area of the circle is: 78.5


print('Please use cm')
square_side=input('What is the length of a side of the square? ')
square_area=float(square_side)*float(square_side)
squ_area_m=float(square_area)/10000
print('The area of the square in cm is: '+str(square_area))
print('The area of the square in m is: '+str(squ_area_m))

rectangle_length=input('What is the length of rectangle? ')
rec_width=input('What is the width of the rectangle? ')
rec_area=float(rectangle_length)*float(rec_width)
rec_area_m=float(rec_area)/10000
print('The area of the rectangle in cm is: '+str(rec_area))
print('The area of the rectangle in m is: '+str(rec_area_m))

circle_radius=input('What is the radius of the circle? ')
circle_area=math.pi*float(circle_radius)**2
circle_area2=round(circle_area,1)
circle_area3=float(circle_area2)/10000
print('The area of the circle in cm 0is: '+str(circle_area2))
print('The area of the circle in m is: '+str(circle_area3))

#lenth=input('lenth: ')


#circle_area=math.pi*float(lenth)**2
#circle_area2=round(circle_area,1)
#print('The area of the circle is: '+str(circle_area2))

#square_area=float(lenth)*float(lenth)
#print('The area of the square is: '+str(square_area))


