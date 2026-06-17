from fastapi import FastAPI
from snowflake_tools import employee_lookup

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Employee MCP API running"}

@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):
    return employee_lookup(emp_id)

# @app.get("/department-summary")
# def dept_summary():
#     return department_summary()