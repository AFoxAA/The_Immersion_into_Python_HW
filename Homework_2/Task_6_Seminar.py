MULTIPLE = 50
WITHDRAWAL_FREE = 0.015
MINIMUM_WITHDRAWAL = 30
MAXIMUM_WITHDRAWAL = 600
EVERY_THIRD_TRANSACTION = 3
INTEREST_ACCRUAL = 1.03
SURPASSING_SUM = 5_000_000
WEALTH_TAX = 0.1

# Функция проверки на кратность (50)
def validate_amount(amount: int) -> bool:
    if amount % MULTIPLE == 0:
        return True
    else:
        print("Сумма должна быть кратной 50!")
        return False

# Функция расчета начисления процентов на баланс
def apply_interest(balance: float, operations_count: int) -> float:
    if operations_count >= EVERY_THIRD_TRANSACTION:
        balance *= INTEREST_ACCRUAL
        balance = round(balance, 2)
        print("\033[92mНачислены проценты 3%.")
        print("\033[94mОбщий счет после начисления процентов:\033[0m", balance, "y.e.")
    return balance

# Функция определения налога на богатство
def apply_wealth_tax(balance: float) -> float:
    if balance > SURPASSING_SUM:
        wealth_tax: float = balance * WEALTH_TAX  
        wealth_tax = round(wealth_tax, 2)
        balance -= wealth_tax
        print("\033[91mВычтен налог на богатство:\033[0m", wealth_tax, "y.e.")
    return balance

# Функция расчета комиссии за снятие денег
def calculate_withdrawal_fee(withdrawal_sum: float) -> float:
    withdrawal_fee: float = withdrawal_sum * WITHDRAWAL_FREE
    withdrawal_fee = max(withdrawal_fee, MINIMUM_WITHDRAWAL)
    withdrawal_fee = min(withdrawal_fee, MAXIMUM_WITHDRAWAL) 
    return withdrawal_fee

# Функция пополнения счета
def deposit(balance: float, operations_count: int) -> tuple[float, int]:
    amount: int = int(input("\n\033[94mВведите сумму для пополнения (кратную 50): \033[0m"))
    if validate_amount(amount):
        balance += amount
        balance = round(apply_wealth_tax(balance), 2) # Проверяем и вычитаем налог на богатство

        print("\033[92mСчет пополнен на\033[0m", amount, "у.е.")
        print("\033[94mОбщий счет:\033[0m", balance, "y.e.")
        operations_count += 1
        balance = apply_interest(balance, operations_count)
    return balance, operations_count

# Функция снятия со счета
def withdraw(balance: float, operations_count: int) -> tuple[float, int]:
    amount: int = int(input("\n\033[94mВведите сумму для снятия (кратную 50): \033[0m"))
    if validate_amount(amount):
        if amount <= balance:
            balance = apply_wealth_tax(balance)

            withdrawal_fee: float = round(calculate_withdrawal_fee(amount), 2)
            total_withdrawal: float = amount + withdrawal_fee

            if total_withdrawal <= balance:
                balance -= total_withdrawal
                print("\033[91mВы сняли\033[0m", amount, "у.е.")
                print("\033[91mПроцент за снятие:\033[0m", withdrawal_fee, "у.е.")
                print("\033[94mОбщий счет:\033[0m", round(balance, 2), "у.е.")
                operations_count += 1
                balance = apply_interest(balance, operations_count)
            else:
                print("\033[91mНедостаточно средств на счете с учетом комиссии!\033[0m")
        else:
            print("\033[91mНедостаточно средств на счете!\033[0m")
    return balance, operations_count

# Функция выбора пункта меню, запуск программы
def atm():
    balance: float = 0
    operations_count: int = 0

    while True:

        print('\n\033[93m\033[4m-----> МЕНЮ <-----\033[0m')

        print("\n1. Пополнить счет")
        print("2. Снять деньги")
        print("3. Проверить баланс")
        print("4. Выйти")

        user_choice: int = input("\nВыберите действие (1-4): ")

        match user_choice:
            case "1":
                print('Вы выбрали \033[92mпополнение счета\033[0m')
                balance, operations_count = deposit(balance, operations_count)
            case "2":
                print('Вы выбрали \033[91mснятия денег\033[0m')
                balance, operations_count = withdraw(balance, operations_count)
            case "3":
                print('\033[94mТекущий баланс:', round(balance, 2), 'у.е.')
            case "4":
                print("До свидания!")
                break
            case _:
                print("\033[91mНекорректный выбор. Попробуйте еще раз.\033[0m")

atm()