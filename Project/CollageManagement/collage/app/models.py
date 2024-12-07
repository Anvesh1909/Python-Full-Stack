from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Teachers(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.CASCADE) # many teachers one department

    def __str__(self):
        return self.name

class TeacherProfile(models.Model):
    name = models.OneToOneField(Teachers,on_delete=models.CASCADE)
    phone = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.CASCADE) # many student one department

    def __str__(self):
        return self.name

class StudentSubjects(models.Model):
    Subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    Student = models.ForeignKey(Students,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Library(models.Model):
    book = models.CharField(max_length=255)
    student = models.ForeignKey(Students,on_delete=models.CASCADE) 
    date = models.DateField(auto_now=True, auto_now_add=False)
    returned = models.BooleanField()


    def __str__(self):
        return self.name


    