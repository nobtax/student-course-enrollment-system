# Student Course Enrollment Manager

A Python desktop application built with **Tkinter** and object-oriented programming.

## Requirements
- Python 3.10+ (Tkinter included in standard Windows Python installations)
- No external packages required

## Run
Open PowerShell in this folder:

```powershell
python main.py
```

## Features
- **Students:** add and list students (ID, name, email)
- **Courses:** add and list courses (ID, title, instructor)
- **Enrollments:** select a student and course from dropdowns, enroll, and list all relationships
- **Show All Records:** combined read-only overview
- **Validation:** required fields, positive numeric IDs, duplicate student/course IDs and duplicate enrollments
- **Remove:** select a row to delete it; removing a student or course also removes associated enrollments
- **Automatic saving:** `enrollment_data.json` is created alongside `main.py` after the first change and loaded at startup

## Code structure
- `models.py`: `Student`, `Course`, `Enrollment`, and `EnrollmentSystem` classes
- `main.py`: Tkinter user interface and JSON file persistence
- `test_system.py`: unit tests for the OOP system

## Test
```powershell
python -m unittest -v
```

## Demonstration
1. Add student `101`, `Alex Lee`, `alex@example.com`.
2. Add course `201`, `Introduction to Python`, `Professor Smith`.
3. Open **Enrollments**, select both records, and click **Enroll Student**.
4. Open **Show All Records** to see students, courses, and their enrollments.
5. Close and reopen the app to confirm records were saved.

> The data file is generated automatically; it does not need to be uploaded for the program to run.
