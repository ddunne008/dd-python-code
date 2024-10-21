times_table = int(input("Enter the times table number: "))


if times_table <= 0 or times_table <= 12:
    times_table = abs(times_table)

    for b in range(12, -1, -1):
        print(f"{b} * {times_table} = {b * times_table}")
else:
    if 0 <= times_table <= 12:
        for b in range(13):
            print(f"{b} * {times_table} = {b * times_table}")
    else:
        print("Please enter a number between 0 or 12")