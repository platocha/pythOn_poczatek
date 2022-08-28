from estudent import data_generator
from estudent.school import School

def run_example():
    students = data_generator.generate_students()

    students.sort(key=lambda student: student.grades_avg, reverse=True)
    school = School(name="Hogwart", students=students)

    new_students = data_generator.generate_students(number_of_students=8)
    school.students = new_students
    print(school)

    # too_many_students = data_generator.generate_students(number_of_students=100)
    # school.students = too_many_students
    # print(school)

if __name__ == '__main__':
    run_example()