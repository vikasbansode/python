#!/usr/bin/python3

######################################################################
#															         #
# Python Program to print Alphabet shapes					         # 
# Created on : 05/04/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : USING FOR LOOP (A Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP (B Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if(col == 0) or (col==4 and (row != 0 and row != 3 and row != 6)) or ((row == 0 or row==3 or row==6) and (col > 0 and col < 4)):
			print("*",end="")
		else:
			print(end=" ")
	print()
	
######################################################################

print("""
*********************************************
* Example 3 : USING FOR LOOP (C Shape)	 	
*********************************************
""")

for row in range(7):
    for col in range(5):
        if(col == 0 and (row != 0 and row != 6)) or  ((row == 0 or row == 6) and (col > 0)):
            print("*",end="")
        else:
            print(end=" ")
    print()

######################################################################

print("""
*********************************************
* Example 4 : USING FOR LOOP (D Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if (col == 0 ) or (col==4 and (row != 0 and row != 6)) or ((row == 0 or row == 6)  and (col > 0 and col < 4)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 5 : USING FOR LOOP (E Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if (col == 0) or ((row == 0 or row == 3 or row == 6) and (col > 0)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 6 : USING FOR LOOP (F Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if (col == 0) or ((row == 0 or row == 3) and (col > 0)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 7 : USING FOR LOOP (G Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(6):
		if (col == 0 or col == 4  and (row != 1 and row != 2)) or ((row == 0 or row == 6) and (col > 0 and col < 4))or ((row == 3) and (col==3 or col == 5)):
			print("*",end="")
		else:
			print(end=" ")
	print()
######################################################################

print("""
*********************************************
* Example 8 : USING FOR LOOP (H Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if (col == 0 or col == 4) or (row ==3 and (col > 0 and col < 4)):
			print("*",end="")
		else:
			print(end=" ")
	print()
	
######################################################################

print("""
*********************************************
* Example 9 : USING FOR LOOP (I Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if col == 2 or ((row == 0 or row == 6) and col != 2):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 10 : USING FOR LOOP (J Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if col == 2 or (row == 0 and col != 2) or (row==5 and col < 1) or (row==6 and col < 1):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 11 : USING FOR LOOP (K Shape)	 	
*********************************************
""")

i=0
j=4

for row in range(7):
	for col in range(5):
		if col == 0 or (row == col+2 and col > 1):
			print("*",end="")
		elif (row == i and col == j):
			print("*",end="")
			i=i+1
			j=j-1
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 12 : USING FOR LOOP (L Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if col == 0 or (row == 6 and col > 0):
			print("*",end="")
		else:
			print(end=" ")
	print()
	
	
######################################################################

print("""
*********************************************
* Example 13 : USING FOR LOOP (M Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(7):
		if (col == 0 or col == 6) or ((row == col) and (col > 0 and col < 4)) or (row == 1 and col == 5) or (row == 2 and col==4):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 14 : USING FOR LOOP (N Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(7):
		if (col == 0 or col == 6) or ((row == col) and (col > 0 and col < 6)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 15 : USING FOR LOOP (O Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if ((col == 0 or col == 4) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)):
			print("*",end="")
		else:
			print(end=" ")
	print()
	
	
######################################################################

print("""
*********************************************
* Example 16 : USING FOR LOOP (P Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if (col == 0 or col == 4 and (row == 1 or row == 2)) or (row == 0 or row == 3) and (col > 0 and col < 4):
			print("*",end="")
		else:
			print(end=" ")
	print()
	
	
######################################################################

print("""
*********************************************
* Example 17 : USING FOR LOOP (Q Shape)	 	
*********************************************
""")

for row in range(8):
	for col in range(5):
		if ((col == 0 or col == 4) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)) or (row ==5 and col == 1) or (row ==7 and col == 4):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 18 : USING FOR LOOP (R Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if col == 0 or (col == 4 and (row != 0 and row != 3)) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 19 : USING FOR LOOP (S Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)) or (col == 0 and (row > 0 and row < 3)) or (col == 4 and (row > 3 and row < 6)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 20 : USING FOR LOOP (T Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if col == 2 or (row == 0 and col != 2):
			print("*",end="")
		else:
			print(end=" ")
	print()
	
######################################################################

print("""
*********************************************
* Example 21 : USING FOR LOOP (U Shape)	 	
*********************************************
""")

for row in range(7):
	for col in range(5):
		if ((col == 0 or col == 4) and row != 6) or (row == 6 and (col > 0 and col <4)):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 22 : USING FOR LOOP (V Shape)	 	
*********************************************
""")
i=0
j=6

for row in range(4):
	for col in range(7):
		if (row == col):
			print("*",end="")
		elif row==i and col == j:
			print("*",end="")
			i=i+1
			j=j-1
		else:
			print(end=" ")
	print()



######################################################################

print("""
*********************************************
* Example 23 : USING FOR LOOP (W Shape)	 	
*********************************************
""")
i=0
j=3
for row in range(4):
	for col in range(7):
		if col == 0 or col == 6 or (col == 5  and row == 2) or (col == 4 and row == 1):
			print("*",end="")
		elif row==i and col==j:
			print("*",end="")
			i=i+1
			j=j-1
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 24 : USING FOR LOOP (X Shape)	 	
*********************************************
""")
i=0
j=4
for row in range(5):
	for col in range(5):
		if row == i and col == j :
			print("*",end="")
			i = i + 1
			j = j - 1
		elif row == col:
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 25 : USING FOR LOOP (Y Shape)	 	
*********************************************
""")

for row in range(5):
	for col in range(5):
		if (col == 2 and row > 1) or (col ==  row and col < 2) or (row == 0 and col == 4) or (row == 1 and col == 3):
			print("*",end="")
		else:
			print(end=" ")
	print()

######################################################################

print("""
*********************************************
* Example 26 : USING FOR LOOP (Z Shape)	 	
*********************************************
""")
i=1
j=4
for row in range(0,6):
	for col in range(0,6):
		if row == 0 or row == 5:
			print("*",end="")
		elif row == i and col == j:
			print("*",end="")
			i=i+1
			j=j-1
		else:
			print(end=" ")
	print()