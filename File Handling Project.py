


def is_valid_name(name):
    return name.replace(" ", "").isalpha()

# Main loop
while True:
    print('\n 1 Add Record')
    print('\n 2 Display Records')
    print('\n 3 Update Record')
    print('\n 4 Delete Student Record')
    print('\n 5 Exit')

    n = int(input("Enter Your Choice : "))

    if n == 5:
        break
    elif n == 1:
        print('\nEnter Student Detail\n: ')
        first_name = input("Enter First Name : ")
        surname = input("Enter Surname : ")
        if not (is_valid_name(first_name) and is_valid_name(surname)):
            print("Invalid name. Please enter letters and spaces only.")
            continue

        roll_no = input("Enter Roll-No : ")
        standard = input("Enter Standard : ")
        fees = input("Enter Fees : ")
        percentage = input("Enter Percentage : ")

        with open('Students.txt', 'a') as f:
            f.write(f"{first_name} {surname} {roll_no} {standard} {fees} {percentage}%\n")

    elif n == 2:
        print("\n\nList of Records\n\n")
        with open('Students.txt', 'r') as f:
            data = f.readlines()

        if data:
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("First Name", "Surname", "Roll-No", "Standard", "Fees", "Percentage"))
            for line in data:
                record = line.strip().split()
                if len(record) == 6:  # Ensure data has correct number of elements
                    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(record[0], record[1], record[2], record[3], record[4], record[5]))
        else:
            print("No records found.")

    elif n == 3:
        roll_no = input("Enter Roll-No to update record : ")

        with open('Students.txt', 'r') as f:
            lines = f.readlines()

        found = False

        with open('Students.txt', 'w') as f:
            for line in lines:
                data = line.strip().split()
                if len(data) == 6 and data[2] == roll_no:  # Ensure data has correct number of elements
                    found = True
                    first_name = input("Enter New First Name : ")
                    surname = input("Enter New Surname : ")
                    standard = input("Enter New Standard : ")
                    fees = input("Enter New Fees : ")
                    percentage = input("Enter New Percentage : ")

                    f.write(f"{first_name} {surname} {data[2]} {standard} {fees} {percentage}%\n")
                else:
                    f.write(line)

        if not found:
            print('No record found for Roll-No', roll_no)

    elif n == 4:
        roll_no = input("Enter Roll-No to delete record : ")

        with open('Students.txt', 'r') as f:
            lines = f.readlines()

        found = False

        with open('Students.txt', 'w') as f:
            for line in lines:
                data = line.strip().split()
                if len(data) == 6 and data[2] == roll_no:  # Ensure data has correct number of elements
                    found = True
                else:
                    f.write(line)

        if not found:
            print('No record found for Roll-No', roll_no)

# End of main loop


