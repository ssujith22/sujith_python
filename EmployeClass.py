import datetime
today = datetime.date.today()
year = today.year
#print


class company:
    def __init__(self,cname):
        self._cname=cname #instance variable
    def displaycname(self):
        print("company name: ",self._cname)
    def address(self):
        return "Technopark phase 2 trivendrum";
"""
c1 = company("UST")
c2 = company("BMW")
c1.displaycname()
c2.displaycname()
"""
class Employee(company):
    ismarried = True
    empcount = 0
    def __init__(self,cname,fname,lname,designation,yob):
        self._cname = cname;       
        self._fname = fname;
        self._lname = lname;
        self._designation = designation;
        self._age= year - yob;
        Employee.empcount +=1 #class level empcount
    def getempdetails(self):
        self.displaycname()
        print("Fullname: ",self._fname," ",self._lname)
        print("Yob: ",self._age)
        print("Designation: ",self._designation)
        print("Marital Status: ",self.ismarried)
        print("Employee count: ",self.empcount)
    def address(self):
        print("Company address: ", super().address())
        print("Employee address: Ginger hotel technopark phase1")
        
e1 = Employee("UST","Parag", "Joshi","HR",1984)
e1.ismarried = False
e1.empcount=8; #instance level empcount
e1.getempdetails()
e1.address()
"""
e2 = Employee("ajay", "kumar","HR",2000)
e2.getempdetails()
e3 = Employee("venkat", "r","software",1988)
e3.getempdetails()
e4 = Employee("sugumar", "b","HR",2002)
e4.getempdetails()

print(Employee.empcount)
"""
