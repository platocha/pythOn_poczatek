from estudent.data_generator import generate_students
from estudent.school import School
def run_example():
    students = generate_students(number_of_students=250)
    school = School(name="Mala szkola", students=[])
    school.students = students


if __name__ == '__main__':
    run_example()