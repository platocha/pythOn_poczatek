from dataclasses import dataclass
from estudent.subject import Subject

@dataclass
class Grade:
    value: int

    def is_passing(self):
        return self.value > 1

    def __repr__(self):
        return str(self.value)

@dataclass
class FinalGrade(Grade):
    subject: Subject

    def __repr__(self):
        return f"{self.subject.name}: {self.value}"

