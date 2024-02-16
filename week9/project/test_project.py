from project import verify_student, verify_staff, register_student




def test_valid_verify_student():
    assert verify_student("1089502143") == "1089502143"

def test_invalid_verify_student():
    assert verify_student("1089502140") == None

def test_verify_staff():
    assert verify_staff("20853") == True
def test_invalid_verify_staff():
    assert verify_staff("208510") == False

def test_register_student():
    newStudent = ["1006201686","Ahmad", "Amiru"]
    assert register_student(*newStudent) == True
