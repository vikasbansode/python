#!/usr/bin/python3

######################################################################
#															         #
# Python Program to print Diamond Shape						         # 
# Created on : 05/04/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################


print("""
*********************************************
* Example 1 : USING FOR LOOP (HALF DIAMOND)	 	
*********************************************
""")

def pyramid(rows):
	for i in range(rows):
		print(''*(rows-i-1)+'*'*(i+1))
	for j in range(rows-1,0,-1):
		print(''*(rows-j)+'*'*(j))

pyramid(10)


######################################################################

print("""
*********************************************
* Example 2 : USING FOR LOOP	 	
*********************************************
""")


rows = input("Enter the number of rows: ")
rows = int (rows)
for i in range (0, rows):
  for j in range(0, i + 1):
    print("*", end = ' ')
  print()

for i in range (rows, 0, -1):
  for j in range(0, i -1):
    print("*", end = ' ')
  print()
  
  
######################################################################

print("""
*********************************************
* Example 3 : SOLID FULL DIAMOND USING FOR LOOP	 	
*********************************************
""")

rows = int(input("Enter The Number Of Rows: "))
print()
columns = 2*rows -1
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( (columns//2)-i <= j <= (columns//2)  +i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1
    
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( i <= j <= columns-1 -i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1


######################################################################

print("""
*********************************************
* Example 4 : HOLLOW DIAMOND USING FOR LOOP	 	
*********************************************
""")

n=int(input("Please enter the numbers of rows: "))-1
print()
j=n-1
print(' '*(n)+'*')
for i in range(1, 2*n):
    if i>n:
        print(' '*(i-n)+'*'+' '*(2*j-1)+'*')
        j-=1
    else:
        print(' '*(n-i)+'*'+' '*(2*i-1)+'*')
if n>1:
    print(' '*n+'*')
            