students = input("Enter amount of students: ")
group_size = input("Enter the required group size: ")

students = float(students)
group_size = float(group_size)

amount_of_groups = (students // group_size)
remaining_students = students % group_size

if remaining_students ==0:
    print(f"there are {amount_of_groups} groups of students")
    print(f"there are {remaining_students} remaining students who are not in a group")
