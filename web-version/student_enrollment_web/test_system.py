import unittest
from models import EnrollmentSystem


class EnrollmentSystemTests(unittest.TestCase):
    def setUp(self):
        self.system = EnrollmentSystem()
        self.system.add_student(1, 'Alex Lee', 'alex@example.com')
        self.system.add_course(101, 'Database Systems', 'Dr. Kim')

    def test_create_and_enroll(self):
        self.assertEqual(self.system.students[1].name, 'Alex Lee')
        self.assertEqual(self.system.courses[101].title, 'Database Systems')
        self.system.enroll(1, 101)
        self.assertEqual(len(self.system.enrollments), 1)

    def test_duplicate_student(self):
        with self.assertRaises(ValueError):
            self.system.add_student(1, 'Another', 'another@example.com')

    def test_duplicate_course(self):
        with self.assertRaises(ValueError):
            self.system.add_course(101, 'Other', 'Teacher')

    def test_missing_student(self):
        with self.assertRaises(ValueError):
            self.system.enroll(999, 101)

    def test_duplicate_enrollment(self):
        self.system.enroll(1, 101)
        with self.assertRaises(ValueError):
            self.system.enroll(1, 101)


if __name__ == '__main__':
    unittest.main()
