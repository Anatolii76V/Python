def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    return max(30, min(600, fee))


def calculate_tax_on_wealth(amount):
    return amount * 0.1


def deposit(balance, amount):
    balance += amount
    return balance, f"Пополнение: +{amount} у.е."


def withdraw(balance, amount):
    if balance >= amount:
        fee = calculate_withdrawal_fee(amount)
        balance -= amount + fee
        return balance, f"Снятие: -{amount} у.е., комиссия: -{fee} у.е."
    else:
        return balance, "Недостаточно средств на счете."


def atm():
    balance = 0
    wealth_tax_threshold = 5000000
    wealth_tax = 0
    operations_count = 0
    transaction_history = []

    while True:
        print(f"Текущий баланс: {balance} у.е.")

        if balance >= wealth_tax_threshold:
            wealth_tax = calculate_tax_on_wealth(balance)
            balance -= wealth_tax

        action = input("Выберите действие (пополнить/снять/выйти): ").lower()

        if action == "пополнить":
            amount = int(input("Введите сумму для пополнения (кратную 50): "))
            if amount % 50 == 0:
                balance, transaction = deposit(balance, amount)
                operations_count += 1
                if operations_count % 3 == 0:
                    balance *= 1.03
                transaction_history.append(transaction)
            else:
                print("Сумма должна быть кратной 50.")
        elif action == "снять":
            amount = int(input("Введите сумму для снятия (кратную 50): "))
            if amount % 50 == 0:
                balance, transaction = withdraw(balance, amount)
                operations_count += 1
                if operations_count % 3 == 0:
                    balance *= 1.03
                transaction_history.append(transaction)
            else:
                print("Сумма должна быть кратной 50.")
        elif action == "выйти":
            break
        else:
            print("Неверное действие. Пожалуйста, повторите.")

        print()

    print("История операций:")
    for transaction in transaction_history:
        print(transaction)


atm()
