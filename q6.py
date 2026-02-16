# Team Name: Codepy

def convert_temperature(value: float, unit: str) -> float | str:
    if unit == 'C':
        return round((value * 9/5) + 32, 1)
    if unit == 'F':
        return round((value - 32) * 5/9, 1)
    return "Invalid Unit"
