import sys
import csv
import re


student = "students.csv"
staff = "staf.csv"

def main():
    """
        :Collect student to this variable
        :using while True to unify all my funtion here
        :verify student
        :if student verified Print the name of student and break the loop
    """
    student_no = verify_student(input("Enter Student Number:"))
    while True:
        if student_no :
            with open(student, "r") as student_file:
                student_dict = csv.DictReader(student_file)
                for row in student_dict:
                    if row["studentno"] == student_no:
                        name = row['name'].strip()
                        surname = row['surname'].strip()
                        print(f"{name} {surname}")
                break
        # If the student is not registered the staff can add him
        # Enter Y if you want register a student else Enter N
        # verify staff with verify funtion if the staff verified then registered a student
        #if staff is not verify exit the programm with sys,exit
        elif not student_no:
            register = input("You are not registered Student, Do you want register Y/N: ").upper()
            if register == "Y":
                staf_id = input("Only staf can register a student, Enter a staf Id: ")
                is_verify_staff = verify_staff(staf_id)
                if is_verify_staff== True:
                    student_no_new = input("Enter student No, Student number mus start with 10 and not end with 0: ")
                    student_name = input("Enter Student Name: ")
                    student_surname = input("Enter Student Surname: ")
                    register_student(student_no_new,student_name,student_surname)
                    break
                elif is_verify_staff == False:
                    sys.exit("You are not staf")
            elif register == "N":
                sys.exit("You are not student and you didn't want register")

"""
    :using this function to verify students ID
    :access student csv file with global
    :open it and read-only if student number is valid return it
    :if it not valid the funtion will return None
"""
def verify_student(student_number):
    global student
    with open(student, "r") as student_file:
        student_dict = csv.DictReader(student_file)
        for row in student_dict:
            if row["studentno"] == student_number:
                return row["studentno"]


"""
    :Using this function to verify the staff Id
    :access staff id from the staff csv file
    :if staff Id is valid return True
    :If staff Id is not Valid return False
"""
def verify_staff(staff_id):
    global staff
    with open(staff, "r") as staf_file:
        staf_dict = csv.DictReader(staf_file)
        for row in staf_dict:
            if staff_id == row["stafid"]:
                return True
        return False

"""
    :register student if the student is not registered
    :acces student csv file with global
    :the student number must start with '10' and not end with '0'
    :if Id is not Valid inform the user
    :using re library to validate the valid student number
"""
def register_student(new_id,name,surname):
    global student
    valid_id = re.search(r"^10[0-9]{7}[^0]",new_id)
    if not valid_id:
        print("Invalid student Number")
    elif valid_id:
        with open(student, "a") as file:
            header = ["studentno","name","surname"]
            student_dict = csv.DictWriter(file, fieldnames = header)
            if file.tell() == 0:
                student_dict.writeheader()
            student_dict.writerow({"studentno":new_id,"name":name,"surname":surname})
            print("New Student Registered")
            return True


if __name__ == "__main__":
    main()
