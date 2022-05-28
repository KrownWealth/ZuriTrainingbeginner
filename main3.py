class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        Student = 'Person'

        self.name=name
        self.age=age
        self.track=track
        self.score=score

#Object of the student class
Adeola=Student('Adeola', 26, 'full time full stack', 60.90)

#printing Adeola details
print('My name is :', Adeola.name)
print('Age : ', Adeola.age)
print('Track :', Adeola.track)
print('Score :', Adeola.score)

#To change the details of Adeola by creating another methods for class "Student"
print("\n")
Adeola.name = input("Enter new student name :")
Adeola.age = int (input("Enter new student  age :"))
Adeola.track = input("Enter newstudent track :")
Adeola.score = (Adeola.score)

print('New student name is :', Adeola.name)
print('New student age is :', Adeola.age)
print('New student track is :', Adeola.track)
print(Adeola.score)


