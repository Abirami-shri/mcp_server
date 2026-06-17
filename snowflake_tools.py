from dotenv import load_dotenv
import os
import snowflake.connector

load_dotenv()

def get_connection():

    return snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USERNAME'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )

def employee_lookup(emp_id):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM EMPLOYEE_POC.HR.EMPLOYEE_DETAILS
        WHERE EMP_ID=%s
        """,(emp_id,)
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def department_summary():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT department,
               COUNT(*) employee_count
        FROM EMPLOYEE_DETAILS
        GROUP BY department
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def employee_count():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM EMPLOYEE_POC.HR.EMPLOYEE_DETAILS
    """)

    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "total_employees": count
    }

def average_salary():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT ROUND(AVG(SALARY), 2)
        FROM EMPLOYEE_POC.HR.EMPLOYEE_DETAILS
    """)

    avg_salary = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "average_salary": avg_salary
    }

def employees_by_department(department):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT EMP_ID,
               NAME,
               DEPARTMENT,
               SALARY
        FROM EMPLOYEE_POC.HR.EMPLOYEE_DETAILS
        WHERE UPPER(DEPARTMENT) = UPPER(%s)
    """, (department,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def highest_salary_employee():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT EMP_ID,
               NAME,
               DEPARTMENT,
               SALARY
        FROM EMPLOYEE_POC.HR.EMPLOYEE_DETAILS
        ORDER BY SALARY DESC
        LIMIT 1
    """)

    row = cur.fetchone()

    cur.close()
    conn.close()

    return row

def generate_hr_report():

    total = employee_count()
    avg = average_salary()
    top_employee = highest_salary_employee()

    report = f"""
                HR REPORT

                Total Employees: {total['total_employees']}

                Average Salary: {avg['average_salary']}

                Highest Paid Employee:
                ID: {top_employee[0]}
                Name: {top_employee[1]}
                Department: {top_employee[2]}
                Salary: {top_employee[3]}
            """

    return report