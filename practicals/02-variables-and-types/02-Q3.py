students = input("Enter amount of students: ")
group_size = input("Enter the required group size: ")

students = float(students)
group_size = float(group_size)

amount_of_groups = (students // group_size)
remaining_students = students % group_size

if remaining_students ==0:
    print(f"There are {amount_of_groups} groups of students")
    print(f"There are {remaining_students} remaining students")
