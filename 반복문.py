'''

              *
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
'''
i = 0
j = 0
'''
while i<5:
    i=i+1
    j=0
    print()
    while j<9:
        j=j+1
        if j > 4+i or i<6-j:
            print(" ", end=" ", )
        else:
            print("*", end=" ", )
'''

while i<5:
    i=i+1
    j=0
    print()
    while j<9:
        j=j+1
        if i<=5-j:
            print(" ", end=" ", )
        else:
            print("*", end=" ", )