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
