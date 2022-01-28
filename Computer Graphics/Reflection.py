import matplotlib.pyplot as plt
import math
plt.xlim((-10, 30))
plt.ylim((-10, 30))
reflection_line_x=[]
reflection_line_y=[]
rows,cols=(3,3)
translation_reflection_arr=[[0 for i in range(cols)] for j in range(rows)]
translation_antirotation_arr=[[0 for i in range(cols)] for j in range(rows)]
rotation_antitranslation_arr=[[0 for i in range(cols)] for j in range(rows)]
x_original=int(input('Enter first point x coordinate: '))
y_original=int(input('Enter first point y coordinate: '))
print("1. Reflect the point on Y-axis")
print("2. Reflect the point on X-axis")
print("3. Reflect the point on an axis perpendicular to xy plane and passes through the coordinate origin")
print("4. Reflect the point on a line y=mx+c")
i=int(input("Select your option: "))
if i==1:
	reflection_line_x.append(0)
	reflection_line_y.append(0)
	reflection_line_x.append(0)
	reflection_line_y.append(30)
	translation_reflection_arr[0][0]=-1
	translation_reflection_arr[0][1]=0
	translation_reflection_arr[0][2]=0
	translation_reflection_arr[1][0]=0
	translation_reflection_arr[1][1]=1
	translation_reflection_arr[1][2]=0
	translation_reflection_arr[2][0]=0
	translation_reflection_arr[2][1]=0
	translation_reflection_arr[2][2]=1
	reflect_x=translation_reflection_arr[0][0]*x_original+translation_reflection_arr[0][1]*y_original+translation_reflection_arr[0][2]*1
	reflect_y=translation_reflection_arr[1][0]*x_original+translation_reflection_arr[1][1]*y_original+translation_reflection_arr[1][2]*1
elif i==2:
	reflection_line_x.append(0)
	reflection_line_y.append(0)
	reflection_line_x.append(30)
	reflection_line_y.append(0)
	translation_reflection_arr[0][0]=1
	translation_reflection_arr[0][1]=0
	translation_reflection_arr[0][2]=0
	translation_reflection_arr[1][0]=0
	translation_reflection_arr[1][1]=-1
	translation_reflection_arr[1][2]=0
	translation_reflection_arr[2][0]=0
	translation_reflection_arr[2][1]=0
	translation_reflection_arr[2][2]=1
	reflect_x=translation_reflection_arr[0][0]*x_original+translation_reflection_arr[0][1]*y_original+translation_reflection_arr[0][2]*1
	reflect_y=translation_reflection_arr[1][0]*x_original+translation_reflection_arr[1][1]*y_original+translation_reflection_arr[1][2]*1
elif i==3:
	reflection_line_x.append(0)
	reflection_line_y.append(0)
	translation_reflection_arr[0][0]=-1
	translation_reflection_arr[0][1]=0
	translation_reflection_arr[0][2]=0
	translation_reflection_arr[1][0]=0
	translation_reflection_arr[1][1]=-1
	translation_reflection_arr[1][2]=0
	translation_reflection_arr[2][0]=0
	translation_reflection_arr[2][1]=0
	translation_reflection_arr[2][2]=1
	reflect_x=translation_reflection_arr[0][0]*x_original+translation_reflection_arr[0][1]*y_original+translation_reflection_arr[0][2]*1
	reflect_y=translation_reflection_arr[1][0]*x_original+translation_reflection_arr[1][1]*y_original+translation_reflection_arr[1][2]*1
elif i==4:
	m=float(input("Enter the slope(m): "))
	y_intercept=float(input("Enter the y-intercept: "))
	x_intercept=((-1)*y_intercept)/m
	line_point1=(30-(-1)*y_intercept)/m
	radian=math.atan(m)
	angle=math.degrees(radian)
	reflection_line_x.append(x_intercept)
	reflection_line_y.append(0)
	reflection_line_x.append(line_point1)
	reflection_line_y.append(30)
	translation_antirotation_arr[0][0]=round(math.cos(math.radians((-1)*angle)),3)
	translation_antirotation_arr[0][1]=round((-1)*math.sin(math.radians((-1)*angle)),3)
	translation_antirotation_arr[0][2]=round((-1*x_intercept)*math.cos(math.radians((-1)*angle)),3)
	translation_antirotation_arr[1][0]=round(math.sin(math.radians((-1)*angle)),3)
	translation_antirotation_arr[1][1]=round(math.cos(math.radians((-1)*angle)),3)
	translation_antirotation_arr[1][2]=round((-1*x_intercept)*math.sin(math.radians((-1)*angle)),3)
	translation_antirotation_arr[2][0]=0
	translation_antirotation_arr[2][1]=0
	translation_antirotation_arr[2][2]=1		
	reflecting_x=translation_antirotation_arr[0][0]*x_original+translation_antirotation_arr[0][1]*y_original+translation_antirotation_arr[0][2]*1
	reflecting_y=translation_antirotation_arr[1][0]*x_original+translation_antirotation_arr[1][1]*y_original+translation_antirotation_arr[1][2]*1
	translation_reflection_arr[0][0]=1
	translation_reflection_arr[0][1]=0
	translation_reflection_arr[0][2]=0
	translation_reflection_arr[1][0]=0
	translation_reflection_arr[1][1]=-1
	translation_reflection_arr[1][2]=0
	translation_reflection_arr[2][0]=0
	translation_reflection_arr[2][1]=0
	translation_reflection_arr[2][2]=1
	reflecting_x=translation_reflection_arr[0][0]*reflecting_x+translation_reflection_arr[0][1]*reflecting_y+translation_reflection_arr[0][2]*1
	reflecting_y=translation_reflection_arr[1][0]*reflecting_x+translation_reflection_arr[1][1]*reflecting_y+translation_reflection_arr[1][2]*1
	rotation_antitranslation_arr[0][0]=round(math.cos(math.radians(angle)),3)
	rotation_antitranslation_arr[0][1]=round((-1)*math.sin(math.radians(angle)),3)
	rotation_antitranslation_arr[0][2]=x_intercept
	rotation_antitranslation_arr[1][0]=round(math.sin(math.radians(angle)),3)
	rotation_antitranslation_arr[1][1]=round(math.cos(math.radians(angle)),3)
	rotation_antitranslation_arr[1][2]=0
	rotation_antitranslation_arr[2][0]=0
	rotation_antitranslation_arr[2][1]=0
	rotation_antitranslation_arr[2][2]=1			
	reflect_x=rotation_antitranslation_arr[0][0]*reflecting_x+rotation_antitranslation_arr[0][1]*reflecting_y+rotation_antitranslation_arr[0][2]*1
	reflect_y=rotation_antitranslation_arr[1][0]*reflecting_x+rotation_antitranslation_arr[1][1]*reflecting_y+rotation_antitranslation_arr[1][2]*1
else:
	print("Enter valid input!!!")
if i==1 or i==2 or i==3 or i==4:
	original_text=x_original,y_original
	reflect_text=round(reflect_x),round(reflect_y)
	plt.plot(x_original,y_original,'bo',label=f'Original Point {original_text}')
	plt.plot(round(reflect_x),round(reflect_y),'ro',label=f'Reflected Point {reflect_text}')
	plt.plot(reflection_line_x, reflection_line_y, 'g--', label='Reflection Line')
	plt.xlabel('<----X-AXIS---->')
	plt.ylabel('<----Y-AXIS---->')
	plt.title('REFLECTION')
	plt.gca().set_aspect('equal', adjustable='box')
	plt.legend()
	plt.show()
