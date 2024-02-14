class job:
  name = None
  salary = None
  hours = None

  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def printDetails(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")

class doctor(job):
  specialty = None
  yearsExperience = None

  def __init__(self,salary,hours,specialty,yearsExperience):
    self.name = "Doctor"
    self.salary = salary
    self.hours = hours
    self.specialty = specialty
    self.yearsExperience = yearsExperience

  def printDetails(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Specialty: {self.specialty}")
    print(f"Years of experience: {self.yearsExperience}")

class teacher(job):
  subject = None
  position = None

  def __init__(self,salary,hours,subject,position):
    self.name = "Teacher"
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position
  
  def printDetails(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}")

print("🌟Jobs Jobs Jobs!🌟")

lawyer = job("Lawyer","$500k","60")
teach = teacher("$35k","50","Computer Science","Lecture Hall")
doc = doctor("$500k","60","Pediatric","7")

lawyer.printDetails()
print()
teach.printDetails()
print()
doc.printDetails()

exit()
