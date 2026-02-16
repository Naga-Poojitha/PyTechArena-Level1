# Team name : Codepy
# Team Name: Codepy

def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    if age >= 65:
        return 10
    if is_student:
        return 12
    return 15
