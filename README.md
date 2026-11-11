# Student Course Enrollment System

This is my Student, Course, and Enrollment project using Python and object-oriented programming (OOP). The program allows users to add students, create courses, enroll students in courses, and view all the records.

I made two versions of the project: a desktop version using Tkinter and a web version using HTML, CSS, JavaScript, and Flask.

## Features

- Add new students with their ID, name, and email
- Add courses with course ID, title, and instructor
- Enroll students in available courses
- View all students, courses, and enrollments
- Remove students, courses, or enrollments
- Check for duplicate records
- Save records so they are still available after closing the program

## Project Files

```text
student-course-enrollment-system/
├── README.md
├── desktop-version/
│   └── student_course_enrollment/
│       ├── main.py
│       ├── models.py
│       ├── test_system.py
│       └── README.md
└── web-version/
    └── student_enrollment_web/
        ├── app.py
        ├── models.py
        ├── test_system.py
        ├── requirements.txt
        ├── README.md
        ├── templates/
        └── static/
```

## Desktop Version

This version uses Python Tkinter for the interface. It has different sections for students, courses, and enrollments.

To run it, open the terminal in the main project folder and enter:

```bash
cd desktop-version/student_course_enrollment
python main.py
```

## Web Version

This version runs in a web browser. I used HTML and CSS for the page, JavaScript for the interactive features, and Python Flask for the backend.

To run it, open a terminal in the main project folder and enter:

```bash
cd web-version/student_enrollment_web
python -m pip install -r requirements.txt
python app.py
```

Then open this address in your browser:

http://127.0.0.1:5000

## OOP Classes

I used the following classes:

- **Student:** Stores student ID, name, and email.
- **Course:** Stores course ID, title, and instructor.
- **Enrollment:** Connects a student to a course.
- **EnrollmentSystem:** Handles adding students, courses, and enrollments.

## Testing

I included a `test_system.py` file in both versions to test the main functions.

To run the tests, go into either version's folder and enter:

```bash
python -m unittest -v
```

## Requirements

- Python 3.10 or newer
- Tkinter for the desktop version (included with most Python installations)
- Flask for the web version (installed using `requirements.txt`)

Both versions work separately and save their own data.
