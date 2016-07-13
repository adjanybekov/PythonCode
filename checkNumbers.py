n = input()
s = input()

up    = len([i for i in ['1', '2', '3'] if i in s]) ==  0 # true if s does not contains one of these
right = len([i for i in ['3', '6', '9', '0'] if i in s]) == 0
left  = len([i for i in ['1', '4', '7', '0'] if i in s]) == 0
down  = len([i for i in ['7', '9', '0'] if i in s]) == 0

ok = not(up or right or left or down) #if the is at least one true then it is not uniqe and print NO
                                        #if all of them are 0 then not 0 == true and print YES
if ok:
    print("YES")
else: #not ok
    print("NO")
