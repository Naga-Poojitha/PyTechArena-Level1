# Team Name: Codepy

def calculate_total_bill(amount: float, tip_percent: int) -> float:
    total = float(amount) + (float(amount) * float(tip_percent) / 100)
    return round(total + 1e-9, 2)
