# tutorial
employee_file = open("employees.txt","r")
for employee in employee_file.read() :
    print(employee)
employee_file.close()
employee_file = open("employees.txt","a")
for employee in employee_file.write(input("enter an employee name : ")) :
     employee.indert 
employee_file.close()     