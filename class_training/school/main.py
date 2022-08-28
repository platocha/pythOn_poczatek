from estudent import data_generator
from estudent.school import School

def run_example():
    students = data_generator.generate_students()

    students.sort(key=lambda student: student.grades_avg, reverse=True)
    school = School(name="Hogwart", students=students)

    print(f"Najlepszy uczen: {school.best_student}")
    print(f"Oceny najlepszego ucznia: {school.best_student.final_grades}")

if __name__ == '__main__':
    run_example()