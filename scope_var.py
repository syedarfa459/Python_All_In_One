# local and global variables in python
                                                #PROGRAM # 01
# x = 20 # a global variable

# def incX():
#     x = 10 # a local variable
#     x += 1
#     return x
# # here when incX is called, the compiler first try to find the variable in local scope i.e inside the function
# # hence it finds x=10 which is inside the function so the output would be 11
# print(incX())

                                                #PROGRAM #02

# x = 100 # Global

# def incX():
#     # x += 1 # this line will throw an error since we dont have permissions to change the value of global variable directly
#     global x
#     x += 1 # this is the correct way to take permissions from python to use a global variable
#     return x
# print(incX())

                                                #PROGRAM #03
'''whenever you use a value of a variable, the compiler first looks it in local scope if it couldn't find it in
local scope then it looks for it in the global scope
'''
# global_val = 10
# def fun1():
#     val = int(input("Enter number: "))
#     #here first the compiler will look the global variable i.e global_val inside fun1() since there's no global_val inside fun1() so it will look outside the function.
#     if val == global_val:
#         print("Matched!!")
#     else:
#         print("Not matched!!")
# fun1()

                                                #PROGRAM #04
'''Whenever you are working with nested functions, you must remember that the global variable is always that
variable that is declared all the way outside of both the functions
'''
mynum = 50
def outsideFun():
    num = 10 #this is still a local variable
    global mynum
    mynum += 10
    def nestedFun():
        print(f"Local variable {num} + 1 = ", num+1)
        print(f"Local variable {mynum} + 1 = ", mynum+1)
    nestedFun()
outsideFun()

