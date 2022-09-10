from estudent.data_generator import generate_students
import os
def run_example():
    students = generate_students()

    students_data_file_path = os.path.join("data", "students.txt")
    with open(students_data_file_path, mode="w") as students_file:
        for student in students:
            students_file.write(str(student))
            students_file.write("\n")

    new_students = generate_students()
    with open(students_data_file_path, mode="a") as students_file:
        students_file.write("Dodatkowo dopisalismy jeszcze:\n")
        for student in new_students:
            students_file.write(str(student))
            students_file.write("\n")


if __name__ == '__main__':
    run_example()