# Ask for a point 
point1 = input("Please give the first point in the form (x,y)\n")
# Get values from the point
for i in point1:
    if i.isdigit():
        x1 = int(i)
        break

for j in point1:
    if j.isdigit() and j == i:
        y1 = int(j)
# Ask user for another point
point2 = input("Please give the second point in the form (x,y)\n")
# Get values from input string
for p in point2:
    if p.isdigit():
        x2 = int(p)
        break
for q in point2:
    if q.isdigit() and q != p:
        y2 = int(q)
        break
# Calculate the slope
m1 = (y2 - y1)
m2 = (x2 - x1)
# Calculate intercept
if m2 == 0:
    print("The points do not make a function")
else:
    b = (m1//m2)*(-1*x1) + y1
# Print the slope-intercept equation
if m2 == 1:
    print("y = " + str(m1) + "x + " + str(b))
elif m1 == m2:
    print("y = x + " + str(b))
elif m2%m1 == 0:
    m3 = m2 // m1
    print("y = (1/" + str(m3) + ")x + " + str(b))
elif m1%m2 == 0:
    m4 = m1 // m2
    print("y = " + str(m4) + "x + " + str(b))
else:
    print("y = (" + str(m1) + "/" + str(m2) + ")x + " + str(b))