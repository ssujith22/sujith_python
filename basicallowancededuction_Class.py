class Salary:
    def __init__(self,bsal):
        self._bsal=bsal
    def getBasicSalary(self):
        print("Basic Salary: ",self._bsal)

class Allowances(Salary):
    s_allowances= {"HRA":0.4,"DA":0.3,"TA":0.15}
    def calcAllowances(self):
        total_allowances = 0;
        for key in self.s_allowances:
            total_allowances+=self.s_allowances[key]*self._bsal;
        return total_allowances;

class Deductions(Salary):
    s_deductions = {"PF":0.12, "Insurance":5000}
    def calcDeductions(self):
        total_deductions = 0;
        for key in self.s_deductions:
            if type(self.s_deductions[key]) is not int:
                total_deductions += self.s_deductions[key]*self._bsal
            else:
                total_deductions+=self.s_deductions[key]
        return total_deductions

class SalaryCalculator(Allowances,Deductions):
    def __init__(self,bsal):
        self._bsal = bsal;
    def getSalaryDetails(self):
        super().getBasicSalary()
        print("Allowances" , super().calcAllowances())
        print("Deductions" , super().calcDeductions())


s1 = SalaryCalculator(10000)
s1.getSalaryDetails()
