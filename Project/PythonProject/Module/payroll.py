def calculate_bonus(salary):
    return salary*10/100

def calculate_allowance(salary):
    return salary *1.5

def gross_salary(salary,bonus,allowance):
    return salary +bonus+allowance

def net_salary(salary):
    tax=salary+0.5
    return salary-tax

