                                                #loops
                                                #PROGRAM # 01

# starti = int(input("Enter the start you want for the loop: "))
# endi = int(input("Enter the end you want for the loop: "))
# for i in range(starti,endi,2):
#     print(i)
                                                #lists
                                                #PROGRAM # 02

# mylist = ['arfa','rafay','afraz','saad','sameed','irtiza','munhib']
# for name in mylist:
#     print(name)

                                                #nested list
                                                #PROGRAM # 03

# mylist = [['arfa','rafay','afraz'],['saad','sameed'],['irtiza','munhib']]

# # for names in mylist:
# #     print(names)
# for names in mylist:
#     for name in names:
#         print(names.index(name))

                                                #tuple(immutable)
                                                #PROGRAM # 04

# tup1 = ('C++', 'Java','Python')
# for item in tup1:
#     print(item)

                                                #strings
                                                #PROGRAM # 05

# mystr = '''this is me, Arfa
# a software engineer from UET'''

# print(mystr.replace(' is ', ' was '))
# print(mystr)
# print(mystr.find('Arfa'))
# print(mystr.capitalize())
# print(mystr.split())
# print(mystr.upper())
# print(mystr.lower())
# print(mystr.startswith('this'))
# print(mystr.endswith('arfa'))
# print(mystr.splitlines())


                                                #functions
                                                #PROGRAM # 06

#fn to calculate no of chrs in string

# def calcChars(eString):
#     count=0
#     for chr in eString:
#         count = count + 1
#     print("The number of characters in your string are: ", count)
# calcChars("HelloSyed")

                                                #PROGRAM # 07
#fn to calculate no of items in list and sub list

# def calcListItem(ls):
#     maincount = 0
#     subcount = 0
#     if ls:
#         for items in ls:
#             maincount += 1
#             for item in items:
#                 subcount += 1
#         print("The number of items in main list are: ", maincount, " and sub list are: ", subcount)
#     else:
#         print('Please pass a nested list...')
# calcListItem([['arfa','rafay','afraz'],['saad','sameed'],['irtiza','munhib']])

                                                #dictionary
                                                #PROGRAM # 08

# mydict = {'farrukh':('arfa','rafay','afraz'), 'jaffer':('irtiza','munhib'), 'shoaib':('saad','sameed')}
# # print('Sons of Farrukh: ', mydict.get('farrukh'))
# # print('Sons of Jaffer: ', mydict.get('jaffer'))
# # print('Sons of Shoaib: ', mydict.get('shoaib'))
# #2nd way of doing using loop(slows performance)
# for name in mydict.get('farrukh'):
#     print(name)

                                                #working with external files
                                                #PROGRAM # 09

#writing content to a text file
# myfile = open('Arfa.txt', 'wb') #wb stands for writing mode
# print(myfile.name)
# print(myfile.mode)
# myfile.write(bytes("hello this is me, Arfa a software engineer!","UTF-8"))
# myfile.close()

# #reading content from a text file
# myfile = open('Arfa.txt','r+') #r+ stands for read and write
# content = myfile.read()
# print(content)
# myfile.close()

# #appendiing content to textfile
# myfile = open('Arfa.txt','a')
# myfile.write(' \nthis text is appended in a new line.')
# myfile.close()


                                                #object oriented programming
                                                #PROGRAM # 10

#double underscore shows member variable as a private variable which cant be accessed outside the class
# class Student:
#     __name = None
#     __age = 0
#     __course = None
#     __marks = 0

#     #constructor
#     # def __init__(self, name, age, course, marks):
#     #     self.__name = name
#     #     self.__age = age
#     #     self.__course = course
#     #     self.__marks = marks

#     #getters and setters
#     def setStudent(self, name, age, course, marks):
#         self.__name = name
#         self.__age = age
#         self.__course = course
#         self.__marks = marks

#     def getStudent(self):
#         print("Name is: ", self.__name," \nAge is: ", self.__age, " \nCourse is: ", self.__course, " \nMarks are: ", self.__marks)

#     #static method(directly called by a class without creating any instance)
#     @staticmethod
#     def mystatic():
#         return "hello this is static method of Student class"

# # std1 = Student('Wajih Rehman', 22, 'Operating System', '95')
# #dict returns a dictionary that shows the member variables & functions of class or an object
# print(Student.__dict__)
# # std1.setStudent('Syed Arfa', 22, 'Operating System', '90') 
# # std1.getStudent()
# #call to static method without object
# print(Student.mystatic())
# #call to static method by an instance of class
# staticobj = Student()
# print(staticobj.mystatic())

                                                #Single Inheritance
                                                #PROGRAM # 11

# class University:
#     __name = None
#     __since = None
#     __ranking = None

#     def __init__(self, name, since, ranking):
#         self.__name = name
#         self.__since = since
#         self.__ranking = ranking
    
#     def getUniDetails(self):
#         print(f"University -> {self.__name} since -> {self.__since} ranked -> {self.__ranking}")

# class Department(University):
#     __deptname = None
#     __chairperson = None

#     def __init__(self, name, since, ranking, dept, cp):
#         super().__init__(name, since, ranking)
#         self.__deptname = dept
#         self.__chairperson = cp

#     def getFullDetails(self):
#         self.getUniDetails()
#         print(f"Department -> {self.__deptname} Chairperson {self.__chairperson}")

# first_obj = Department("UET",1975,"5th","Software Engg","Engr Ali")
# sec_obj = Department("NUST",1956,"2nd","Mech Engg","Engr Muzafar")
# first_obj.getFullDetails()
# sec_obj.getFullDetails()
# sec_obj.getUniDetails()

                                                #Multiple Inheritance
                                                #PROGRAM # 12

#A Programmer can be a student as well as gamer at the same time 
# class Student:
#     def __init__(self, name, age, dept):
#         self.name = name
#         self.age = age
#         self.dept = dept
#     def getStudent(self):
#         print(f"Student -> {self.name} age -> {self.age} dept -> {self.dept}")

# class Gamer:
#     def __init__(self, game, player_level):
#         self.game = game
#         self.player_level = player_level
#     def getGamer(self):
#         print(f"Game -> {self.game} Level -> {self.player_level}")


# class Programmer(Student,Gamer):
#     def __init__(self, name, age, dept, game, level, complanguage, experience):
#         Student.__init__(self, name, age, dept)
#         # super().__init__(name, age, dept)
#         # super().__init__(game,level)
#         Gamer.__init__(self, game, level)
#         self.complanguage = complanguage
#         self.experience = experience
#     def getDetails(self):
#         self.getStudent()
#         self.getGamer()
#         print(f"Programming Language -> {self.complanguage} and experience -> {self.experience}")

# progobj = Programmer('Syed Arfa', 22, 'Software', 'PUBG', '76', 'Python', '2 years')
# progobj.getDetails()
# progobj2 = Programmer('Syed Abdullah', 23, 'Software', 'GTA-5', '97', 'Kotlin', '5 years')
# progobj2.getDetails()
# # progobj.getStudent()