#user grade

user_grade = int(input("Pleas enter your grade percentage: "))

if user_grade >= 90:
    letter = "A"
elif user_grade >=80:
    letter = "B"
elif user_grade >=70:
    letter = "C"
elif user_grade >=60:
    letter = "D"
elif user_grade <60:
    letter = "F"
print(f"Your letter grade is: {letter} ")  

#sign
sing = " "
last_digit = user_grade % 10
if last_digit >=7:
    sing = "+"
elif last_digit <=3:
    sing = "-"
else:
    sing = " "
if user_grade >= 93:
    sign = " "
if letter == "F":
    sign = " "

#print
    
print(f"Letter sing = {letter}{sing}")
if user_grade >=70:
    print("Congratularions! You passed the class!")   
elif user_grade <=69:
    print("Sorry, you must take the class again.")
