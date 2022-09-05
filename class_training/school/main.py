from estudent.subject import Subject
from estudent.grade import Grade, FinalGrade
def run_example():
    best_grade = Grade(value=6)
    failing_grade = Grade(value=1)
    print(best_grade)
    print(failing_grade)
    print(best_grade.is_passing())
    print(failing_grade.is_passing())

    math = Subject(identifier=1, name="Matematyka")
    final_grade = FinalGrade(value=4, subject=math)
    print(final_grade)
    math.assign_teacher("Wojciech")
    print(math)


if __name__ == '__main__':
    run_example()