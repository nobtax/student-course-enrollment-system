"""Student Course Enrollment Manager - Tkinter desktop interface."""
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import json
from models import EnrollmentSystem

DATA_FILE = Path(__file__).with_name("enrollment_data.json")
BG, PANEL, NAVY, BLUE, TEXT, MUTED = "#f3f6fb", "#ffffff", "#17243b", "#2563eb", "#1e293b", "#64748b"


class EnrollmentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Campus Enrollment | Student & Course Manager")
        self.geometry("1100x720")
        self.minsize(880, 600)
        self.configure(bg=BG)
        self.system = EnrollmentSystem()
        self.load_data()
        self.setup_style()
        self.build_ui()
        self.refresh_all()

    def setup_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", rowheight=31, font=("Segoe UI", 10), background="white",
                        fieldbackground="white", foreground=TEXT, borderwidth=0)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), padding=10,
                        background="#e8eef8", foreground=NAVY)
        style.map("Treeview", background=[("selected", "#dbeafe")], foreground=[("selected", NAVY)])
        style.configure("TCombobox", padding=7, font=("Segoe UI", 10))

    def build_ui(self):
        header = tk.Frame(self, bg=NAVY, height=100)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="CAMPUS  /  ENROLLMENT MANAGER", bg=NAVY, fg="#93c5fd",
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=32, pady=(15, 0))
        tk.Label(header, text="Student & Course Management", bg=NAVY, fg="white",
                 font=("Segoe UI", 21, "bold")).pack(anchor="w", padx=32)
        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True, padx=26, pady=18)
        stats = tk.Frame(container, bg=BG)
        stats.pack(fill="x", pady=(0, 15))
        self.stat_labels = {}
        for key, label in [("students", "TOTAL STUDENTS"), ("courses", "AVAILABLE COURSES"), ("enrollments", "ACTIVE ENROLLMENTS")]:
            box = tk.Frame(stats, bg=PANEL, highlightbackground="#dce5f0", highlightthickness=1)
            box.pack(side="left", expand=True, fill="x", padx=5)
            tk.Label(box, text=label, fg=MUTED, bg=PANEL, font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(11, 0))
            value = tk.Label(box, text="0", fg=NAVY, bg=PANEL, font=("Segoe UI", 23, "bold"))
            value.pack(anchor="w", padx=18, pady=(0, 10))
            self.stat_labels[key] = value

        self.tabs = ttk.Notebook(container)
        self.tabs.pack(fill="both", expand=True)
        self.students_tab = tk.Frame(self.tabs, bg=PANEL)
        self.courses_tab = tk.Frame(self.tabs, bg=PANEL)
        self.enroll_tab = tk.Frame(self.tabs, bg=PANEL)
        self.all_tab = tk.Frame(self.tabs, bg=PANEL)
        for frame, title in [(self.students_tab, "  Students  "), (self.courses_tab, "  Courses  "),
                             (self.enroll_tab, "  Enrollments  "), (self.all_tab, "  Show All Records  ")]:
            self.tabs.add(frame, text=title)
        self.make_students()
        self.make_courses()
        self.make_enrollments()
        self.make_show_all()
        tk.Label(self, text="Records are saved automatically on this computer  •  Select 'Show All Records' for a complete overview",
                 bg=BG, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", padx=32, pady=(0, 12))

    def section(self, parent, title, subtitle):
        tk.Label(parent, text=title, bg=PANEL, fg=NAVY, font=("Segoe UI", 17, "bold")).pack(anchor="w", padx=22, pady=(18, 0))
        tk.Label(parent, text=subtitle, bg=PANEL, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", padx=22, pady=(2, 14))

    def entry_row(self, parent, fields):
        form = tk.Frame(parent, bg=PANEL)
        form.pack(fill="x", padx=22)
        entries = {}
        for i, (key, label) in enumerate(fields):
            cell = tk.Frame(form, bg=PANEL)
            cell.grid(row=0, column=i, sticky="ew", padx=(0, 12))
            form.columnconfigure(i, weight=1)
            tk.Label(cell, text=label, bg=PANEL, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w")
            ent = ttk.Entry(cell, font=("Segoe UI", 11))
            ent.pack(fill="x", pady=(5, 0), ipady=6)
            entries[key] = ent
        return entries

    def button(self, parent, text, command, color=BLUE):
        return tk.Button(parent, text=text, command=command, bg=color, fg="white",
                         activebackground="#1d4ed8", activeforeground="white", relief="flat",
                         cursor="hand2", font=("Segoe UI", 10, "bold"), padx=17, pady=9)

    def make_tree(self, parent, columns, height=9):
        holder = tk.Frame(parent, bg=PANEL)
        holder.pack(fill="both", expand=True, padx=22, pady=(12, 18))
        tree = ttk.Treeview(holder, columns=[key for key, _ in columns], show="headings", height=height)
        for key, label in columns:
            tree.heading(key, text=label)
            tree.column(key, width=150, anchor="w", stretch=True)
        scrollbar = ttk.Scrollbar(holder, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        return tree

    def make_students(self):
        p = self.students_tab
        self.section(p, "Student Directory", "Register students and view their details.")
        self.student_inputs = self.entry_row(p, [("id", "Student ID"), ("name", "Full Name"), ("email", "Email Address")])
        actions = tk.Frame(p, bg=PANEL)
        actions.pack(fill="x", padx=22, pady=(12, 0))
        self.button(actions, "+ Add Student", self.add_student).pack(side="left")
        self.button(actions, "Remove Selected", self.remove_student, "#b45309").pack(side="left", padx=10)
        self.student_tree = self.make_tree(p, [("id", "Student ID"), ("name", "Name"), ("email", "Email")])

    def make_courses(self):
        p = self.courses_tab
        self.section(p, "Course Catalog", "Create and manage courses available for enrollment.")
        self.course_inputs = self.entry_row(p, [("id", "Course ID"), ("title", "Course Title"), ("instructor", "Instructor")])
        actions = tk.Frame(p, bg=PANEL)
        actions.pack(fill="x", padx=22, pady=(12, 0))
        self.button(actions, "+ Add Course", self.add_course).pack(side="left")
        self.button(actions, "Remove Selected", self.remove_course, "#b45309").pack(side="left", padx=10)
        self.course_tree = self.make_tree(p, [("id", "Course ID"), ("title", "Course Title"), ("instructor", "Instructor")])

    def make_enrollments(self):
        p = self.enroll_tab
        self.section(p, "Course Enrollment", "Choose an existing student and course to create an enrollment.")
        form = tk.Frame(p, bg=PANEL)
        form.pack(fill="x", padx=22)
        self.student_combo = None
        self.course_combo = None
        for i, label in enumerate(["Student", "Course"]):
            col = tk.Frame(form, bg=PANEL)
            col.grid(row=0, column=i, sticky="ew", padx=(0, 12))
            form.columnconfigure(i, weight=1)
            tk.Label(col, text=label, bg=PANEL, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w")
            combo = ttk.Combobox(col, state="readonly", font=("Segoe UI", 11))
            combo.pack(fill="x", pady=(5, 0))
            if i == 0:
                self.student_combo = combo
            else:
                self.course_combo = combo
        actions = tk.Frame(p, bg=PANEL)
        actions.pack(fill="x", padx=22, pady=(12, 0))
        self.button(actions, "+ Enroll Student", self.add_enrollment).pack(side="left")
        self.button(actions, "Unenroll Selected", self.remove_enrollment, "#b45309").pack(side="left", padx=10)
        self.enroll_tree = self.make_tree(p, [("student_id", "Student ID"), ("student", "Student"),
                                               ("course_id", "Course ID"), ("course", "Course")])

    def make_show_all(self):
        p = self.all_tab
        self.section(p, "All Records", "Complete overview of students, courses, and enrollment relationships.")
        self.summary = tk.Text(p, wrap="word", bg="#f8fafc", fg=TEXT, font=("Consolas", 10),
                               padx=20, pady=15, relief="flat", state="disabled")
        self.summary.pack(fill="both", expand=True, padx=22, pady=(0, 12))
        self.button(p, "Refresh All Records", self.refresh_all).pack(anchor="w", padx=22, pady=(0, 18))

    def get_id(self, text, label):
        try:
            value = int(text.strip())
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            raise ValueError(f"{label} must be a positive whole number.")

    def add_student(self):
        try:
            v = self.student_inputs
            self.system.add_student(self.get_id(v["id"].get(), "Student ID"), v["name"].get(), v["email"].get())
            self.persist_and_refresh()
            for ent in v.values(): ent.delete(0, "end")
            messagebox.showinfo("Student Added", "Student successfully registered.")
        except ValueError as e:
            messagebox.showerror("Cannot Add Student", str(e))

    def add_course(self):
        try:
            v = self.course_inputs
            self.system.add_course(self.get_id(v["id"].get(), "Course ID"), v["title"].get(), v["instructor"].get())
            self.persist_and_refresh()
            for ent in v.values(): ent.delete(0, "end")
            messagebox.showinfo("Course Added", "Course successfully created.")
        except ValueError as e:
            messagebox.showerror("Cannot Add Course", str(e))

    def add_enrollment(self):
        try:
            sid = self.get_id(self.student_combo.get().split(" — ")[0], "Student ID")
            cid = self.get_id(self.course_combo.get().split(" — ")[0], "Course ID")
            self.system.enroll(sid, cid)
            self.persist_and_refresh()
            messagebox.showinfo("Enrollment Created", "Student enrolled successfully.")
        except ValueError as e:
            messagebox.showerror("Cannot Enroll", str(e))

    def selected(self, tree):
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Select a Record", "Please select a row first.")
            return None
        return tree.item(selected[0], "values")

    def remove_student(self):
        row = self.selected(self.student_tree)
        if row and messagebox.askyesno("Confirm", "Delete this student and their enrollments?"):
            sid = int(row[0])
            del self.system.students[sid]
            self.system.enrollments = [e for e in self.system.enrollments if e.student.student_id != sid]
            self.persist_and_refresh()

    def remove_course(self):
        row = self.selected(self.course_tree)
        if row and messagebox.askyesno("Confirm", "Delete this course and its enrollments?"):
            cid = int(row[0])
            del self.system.courses[cid]
            self.system.enrollments = [e for e in self.system.enrollments if e.course.course_id != cid]
            self.persist_and_refresh()

    def remove_enrollment(self):
        row = self.selected(self.enroll_tree)
        if row and messagebox.askyesno("Confirm", "Remove this enrollment?"):
            sid, cid = int(row[0]), int(row[2])
            self.system.enrollments = [e for e in self.system.enrollments
                                       if not (e.student.student_id == sid and e.course.course_id == cid)]
            self.persist_and_refresh()

    def persist_and_refresh(self):
        self.save_data()
        self.refresh_all()

    def save_data(self):
        data = {
            "students": [vars(s) for s in self.system.students.values()],
            "courses": [vars(c) for c in self.system.courses.values()],
            "enrollments": [{"student_id": e.student.student_id, "course_id": e.course.course_id}
                            for e in self.system.enrollments]
        }
        try:
            DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except OSError as e:
            messagebox.showerror("Save Failed", f"Unable to save records:\n{e}")

    def load_data(self):
        if not DATA_FILE.exists():
            return
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            for s in data.get("students", []):
                self.system.add_student(s["student_id"], s["name"], s["email"])
            for c in data.get("courses", []):
                self.system.add_course(c["course_id"], c["title"], c["instructor"])
            for e in data.get("enrollments", []):
                self.system.enroll(e["student_id"], e["course_id"])
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
            messagebox.showwarning("Load Warning", f"Some saved records could not be loaded:\n{e}")

    def refresh_all(self):
        for tree in (self.student_tree, self.course_tree, self.enroll_tree):
            for item in tree.get_children(): tree.delete(item)
        for s in sorted(self.system.students.values(), key=lambda x: x.student_id):
            self.student_tree.insert("", "end", values=(s.student_id, s.name, s.email))
        for c in sorted(self.system.courses.values(), key=lambda x: x.course_id):
            self.course_tree.insert("", "end", values=(c.course_id, c.title, c.instructor))
        for e in self.system.enrollments:
            self.enroll_tree.insert("", "end", values=(e.student.student_id, e.student.name,
                                                       e.course.course_id, e.course.title))
        self.student_combo["values"] = [f"{s.student_id} — {s.name}" for s in sorted(self.system.students.values(), key=lambda x: x.student_id)]
        self.course_combo["values"] = [f"{c.course_id} — {c.title}" for c in sorted(self.system.courses.values(), key=lambda x: x.course_id)]
        self.student_combo.set("")
        self.course_combo.set("")
        for key, count in [("students", len(self.system.students)), ("courses", len(self.system.courses)),
                           ("enrollments", len(self.system.enrollments))]:
            self.stat_labels[key].configure(text=str(count))
        lines = ["STUDENTS", "─" * 75]
        lines += [f"  {s.student_id:<9} {s.name:<27} {s.email}" for s in self.system.students.values()] or ["  No students registered."]
        lines += ["", "COURSES", "─" * 75]
        lines += [f"  {c.course_id:<9} {c.title:<27} {c.instructor}" for c in self.system.courses.values()] or ["  No courses available."]
        lines += ["", "ENROLLMENTS (STUDENT → COURSE)", "─" * 75]
        lines += [f"  {e.student.name} (#{e.student.student_id})  →  {e.course.title} (#{e.course.course_id})"
                  for e in self.system.enrollments] or ["  No enrollments yet."]
        self.summary.configure(state="normal")
        self.summary.delete("1.0", "end")
        self.summary.insert("1.0", "\n".join(lines))
        self.summary.configure(state="disabled")


if __name__ == "__main__":
    EnrollmentApp().mainloop()
