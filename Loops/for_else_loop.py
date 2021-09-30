# for-else loop

import sys

n = int(input("Enter the size of list:"))
if n <= 0:
    sys.exit(0)

myList = []
i = 0

while i < n:
    element = int(input("Enter the next element: "))
    myList.append(element)
    i = i + 1

flag = False

for x in myList:
    if x % 7 == 0:
        print("Broken out of loop")
        break
    print("x = ", x)
else:
    print("Executed all iterations")

"""
Output :

Enter the size of list:3
Enter the next element: 1
Enter the next element: 2
Enter the next element: 3
x =  1
x =  2
x =  3
Executed all iterations


--------------------

Enter the size of list:5
Enter the next element: 12
Enter the next element: 4
Enter the next element: 14
Enter the next element: 6
Enter the next element: 8
x =  12
x =  4
Broken out of loop

Process finished with exit code 0


"""
