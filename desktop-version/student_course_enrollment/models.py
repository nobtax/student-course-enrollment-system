"""Core object-oriented models for the enrollment system."""
from dataclasses import dataclass, field


@dataclass
class Student:
    student_id: int
    name: str
    email: str


@dataclass
class Course:
    course_id: int
    title: str
    instructor: str


@dataclass
class Enrollment:
    student: Student
    course: Course


@dataclass
class EnrollmentSystem:
    students: dict[int, Student] = field(default_factory=dict)
    courses: dict[int, Course] = field(default_factory=dict)
    enrollments: list[Enrollment] = field(default_factory=list)

    def add_student(self, student_id: int, name: str, email: str) -> Student:
        if student_id in self.students:
            raise ValueError('Student ID already exists.')
        if not name.strip() or not email.strip():
            raise ValueError('Name and email cannot be empty.')
        student = Student(student_id, name.strip(), email.strip())
        self.students[student_id] = student
        return student

    def add_course(self, course_id: int, title: str, instructor: str) -> Course:
        if course_id in self.courses:
            raise ValueError('Course ID already exists.')
        if not title.strip() or not instructor.strip():
            raise ValueError('Title and instructor cannot be empty.')
        course = Course(course_id, title.strip(), instructor.strip())
        self.courses[course_id] = course
        return course

    def enroll(self, student_id: int, course_id: int) -> Enrollment:
        if student_id not in self.students:
            raise ValueError('Student ID not found.')
        if course_id not in self.courses:
            raise ValueError('Course ID not found.')
        if any(e.student.student_id == student_id and e.course.course_id == course_id for e in self.enrollments):
            raise ValueError('Student is already enrolled in this course.')
        enrollment = Enrollment(self.students[student_id], self.courses[course_id])
        self.enrollments.append(enrollment)
        return enrollment
