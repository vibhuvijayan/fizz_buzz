import sys
# Cheching versin 2 
# Checking Version 2.3
# added Try block for Exception

default_lowerlimit = 1
default_upperlimit = 100
loop_condition = True
loop_increment = 0

print ("name of the Script is {}".format(sys.argv[0]))

try:
    if len(sys.argv) == 3 and (int(sys.argv[2]) > int(sys.argv[1])):
        upperlimit = int(sys.argv[2])
        lowerlimit = int(sys.argv[1])
        print ("User Entered lowerlinit is {} and upperlimit is {}".format(lowerlimit,upperlimit))
    elif len(sys.argv) == 2 and (int(sys.argv[1]) > 1):
        upperlimit = int(sys.argv[1])
    else:
         while loop_condition :
            loop_increment+=1
            if loop_increment <=3 :
                my_input_lowerlimit = input("LowerLimit :")
                my_input_upperlimit = input("UpperLimit :")
                try:
                    if int(my_input_lowerlimit) < int(my_input_upperlimit):
                         lowerlimit = int(my_input_lowerlimit)
                         upperlimit = int(my_input_upperlimit)
                         loop_condition = False
                    else:
                         print("Upperlimit is Greater than Lowerlimit , please enter again ")
                except ValueError:
                    print('Please Enter Valid Integers')
            else:
                lowerlimit = default_lowerlimit
                upperlimit = default_upperlimit
                loop_condition = False
except ValueError:
    print('Enter parameter not Valid, using Default Values')  
    lowerlimit = default_lowerlimit
    upperlimit = default_upperlimit
    
for x in range(lowerlimit,upperlimit):
    if (x%3 ==0) and (x%5 ==0):
        print("fizz buzz")
    elif (x%3 ==0):
        print("fizz")
    elif (x%5 ==0):
        print("buzz")
    else:
        print(x)
