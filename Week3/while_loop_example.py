""" We now have seen and used a lot of examples of for loops. There is another type of loop we can also use, called a while loop. The while loop performs a set of code until some condition is reached.

While loops can be used to iterate through lists, just like for loops:

dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1
Every time the condition of the while loop (in this case, index < len(dog_breeds)) is satisfied, the code inside the while loop runs.

While loops can be useful when you don’t know how many iterations it will take to satisfy a condition.

Instructions
1.
You are adding students to a Poetry class, the size of which is capped at 6. While the length of the students_in_poetry list is less than 6, use .pop() to take a student off the all_students list and add it to the students_in_poetry list.

2.
Print the students_in_poetry list . """

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []
while len(students_in_poetry) < 6:
  studs = all_students.pop()
  students_in_poetry.append(studs)
  print(students_in_poetry)