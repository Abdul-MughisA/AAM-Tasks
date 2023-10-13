student1t = ("Dave", "Bloggs", 18, True)
student2t = ("Fred", "Smith", 16, False)

class StudentRecord():
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0
        self.registered = False
    #end def
#end class

def addone(x):
    x = x + 1
    return x
#end def

student1 = StudentRecord()
student1.firstname = "Dave"
student1.lastname = "Bloggs"
student1.age = 18
student1.registered = True

student2 = StudentRecord()
student2.firstname = "Fred"
student2.lastname = "Smith"
student2.age = 16
student2.registered = False

newage = addone(student2.age)
print(newage)

print(student1.age, student1.lastname)
print(student1.age)
print(student1t[2])