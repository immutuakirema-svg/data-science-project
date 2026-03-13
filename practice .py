#variable 
name = "brandon mutua"
mark = int( "80")
age = 16
if mark >=80:
        grade = "A"
elif mark >=70:
      grade= "B"
elif mark >=50:
          grade = "c"
else :
        grade = "fail"
students=["brandon" , 'nathan' ,'peter', 'kimani'] 
for _, student in enumerate(students,start=1):
        print(_,student)

class student:
         def __init__(self ,name,age ,mark):
                 self.name= name
                 self.age= age
                 self.mark=mark
         def get_grade(self):
                 if self.mark >=80:
                         return 'A'
                 elif  self.mark >=70:
                         return 'B'
                 elif  self.mark >=50:
                         return 'C'
                 else :
                         return  'fail'
         def display(self):
                 print("name:", self.name)
                 print("age:" , self.age)
                 print("mark:", self.mark)
                 print("grade",self.get_grade())
                 print("------")
s1=student('brandon mutua.' ,18, 80)
s2=student("mike mwambia." ,19,70)
s3=student("ian mwenda",21,40)
students =[s1, s2, s3]
for s in students:
        s.display()

name =input("enter you name..")  
print(name)     
s4=student("timothy" ,int("18"),78)
students.append(s4)
for s in students:
        s.display()

# inheritance and polymophism 

class cars:
        def __init__(self,type,model,price):
                self.type=type
                self.model=model
                self.price=price
                pass
        def sound(self):
                pass
        def display(self):
                print(self.type)
                print(self.model)
                print(self.price)
                print("----------")

class BMW(cars):
        def __init__ (self ,type ,model,price):
         super(). __init__ (type,model,price)
car1=BMW('suv','x5',8000)
car1.display()
                


             

                 

                
