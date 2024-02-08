def solution(phone: str):
    for char in ('(', ')', '-', ' '):
        phone = phone.replace(char, '')
    return phone.isnumeric()


assert True == solution("5555555555")
assert True == solution("555555555")
assert True == solution("555-5555")
assert True == solution("(555) 555-5555")
assert True == solution("(555) 555-555")
assert True == solution("(555) 555-555-5555")
assert False == solution("(555) 555a-555-5555")
assert False == solution("555*-555-5555")
assert False == solution("55a-555-5555")
assert True == solution("55-55-55")
assert True == solution("55 55 55")
