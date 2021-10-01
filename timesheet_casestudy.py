class Employee:
    def __init__(self,empid,ename,empsal,empdept):
        self.empid=empid
        self.ename=ename
        self.empsal=empsal
        self.empdept=empdept
    def display(self):
        print(self.empid)
        print(self.ename)
        print(self.empsal)
        print(self.empdept)
class Timesheet(Employee):
    def __init__(self,date,noofhrs,activity,description,status):
        self.date=date
        self.noofhours=noofhrs
        self.activity=activity
        self.description=description
        self.status=status
    def display(self):
        print(self.date)
        print(self.noofhours)
        print(self.activity)
        print(self.description)
        print(self.status)

emp=Employee(20879,"parvathi",20000,"analyst")
emp.display()
t=Timesheet("29-09-2021",8,"training","python training","Approved")
t.display()