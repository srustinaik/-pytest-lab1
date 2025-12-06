from employee import employee_details
def test_employee_details():
    expected output=(
        "Employee Name:srusti\n"
        "Employee ID:E1001\n"
        "Department:IT\n"
        "salary:55000"
   )
  assert employee_details("srusti","E1001","IT",55000)==expected_output
