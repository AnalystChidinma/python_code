student_name = input("Enter your name: ")   
grade = input("Enter your grade: ")
if 3.5 <= float(grade) and float(grade) <= 4.0:
    print("First Class Honours")
elif 3.0 <= float(grade) and float(grade) <= 3.49:
    print("Second Class Honours (Upper Division)")
elif 2.0 <= float(grade) and float(grade) <= 2.99:
    print("Second Class Honours (Lower Division)")
elif 1.0 <= float(grade) and float(grade) <= 1.99:
    print("Third Class Honours")
else:
    print(" Grade Not available")