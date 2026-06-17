from mcp.server.fastmcp import FastMCP
from snowflake_tools import employee_lookup, department_summary, employee_count, average_salary, employees_by_department, highest_salary_employee, generate_hr_report

mcp = FastMCP("employee-agentic-assistant-mcp")


@mcp.tool()
def get_employee(emp_id: int):
    """
    Returns employee details from Snowflake.
    """
    return employee_lookup(emp_id)

@mcp.tool()
def get_department_summary():
    """
    Returns department summary from Snowflake.
    """
    return department_summary()

@mcp.tool()
def get_employee_count():
    """
    Returns the total number of employees from Snowflake.
    """
    return employee_count()

@mcp.tool()
def get_average_salary():
    """
    Returns the average salary of employees from Snowflake.
    """
    return average_salary()

@mcp.tool()
def get_employees_by_department(department: str):
    """
    Returns a list of employees in a specific department from Snowflake.
    """
    return employees_by_department(department)

@mcp.tool()
def get_highest_salary_employee():
    """
    Returns the employee with the highest salary from Snowflake.
    """
    return highest_salary_employee()

@mcp.tool()
def generate_hr_report():
    """
    Generates a comprehensive HR report from Snowflake.
    """
    return generate_hr_report()

if __name__ == "__main__":
    mcp.run()