""" Define a class Student this will be our data model at Jan van Eyck High School and Conservatory.

2.
Add a constructor for Student. Have the constructor take in two parameters: a name and a year. Save those two as attributes .name and .year.

3.
Create three instances of the Student class:

Roger van der Weyden, year 10
Sandro Botticelli, year 12
Pieter Bruegel the Elder, year 8
Save them into the variables roger, sandro, and pieter.

4.
Create a Grade class, with minimum_passing as an attribute set to 65.

5.
Give Grade a constructor. Take in a parameter score and assign it to self.score.

6.
In the body of the constructor for Student, declare self.grades as an empty list.

7.
Add an .add_grade() method to Student that takes a parameter, grade.

.add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades.

If grade isn’t an instance of Grade then .add_grade() should do nothing.

8.
Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade().

9.
Great job! You’ve created two classes and defined their interactions. This is object-oriented programming! From here you could:

Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
Write a Student method get_average() that returns the student’s average score.
Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values that indicate whether the student attended school that day.
Write your own classes to do whatever logic you want! """



class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))