from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name:srusti\n"
        "Employee ID:E1001\n"
        "Department:IT\n"
        "salary:550000"
    )
    assert employee_details("srusti", "E1001", "IT", 550000) == expected_output
