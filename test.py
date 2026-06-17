from snowflake_tools import employee_lookup, department_summary, employee_count, average_salary, employees_by_department, highest_salary_employee, generate_hr_report

print(employee_lookup(101))
print(department_summary())
print(employee_count())
print(average_salary())
print(employees_by_department("Sales"))
print(highest_salary_employee())
print(generate_hr_report())