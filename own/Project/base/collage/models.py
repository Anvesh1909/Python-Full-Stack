from django.db import models

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    head = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Lecturer Model
class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='lecturers')  # One-to-Many

    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')  # One-to-Many
    mentor = models.OneToOneField(Lecturer, on_delete=models.SET_NULL, null=True, blank=True, related_name='mentored_student')  # One-to-One

    def __str__(self):
        return self.name

# Many-to-Many relationship between Student and Lecturer
class StudentLecturer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_lecturers')
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name='lecturer_students')
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.name} - {self.lecturer.name} ({self.subject})"
