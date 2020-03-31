""" Copeland’s Corporate Company also wants to update how they generate temporary passwords for new employees.

Write a function called password_generator that takes two inputs, first_name and last_name and then concatenate the last three letters of each and returns them as a string. """

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  new_pass = first_name[(len(first_name)-1)-2:] + last_name[(len(last_name)-1)-2:]
  return new_pass

temp_password = password_generator(first_name, last_name)