def generate_bonus_dict(names, rates, bonuses):
    return {name: rate * float(bonus.rstrip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}


names = ["Алексанлр", "Воладимир", "Михаил"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "5%", "12.5%"]

result_dict = generate_bonus_dict(names, rates, bonuses)
print(result_dict)
