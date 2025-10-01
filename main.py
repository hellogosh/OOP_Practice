"""
### Шаги для выполнения:
1. **Определение базового класса `BankAccount`:**
    - Атрибуты: **`owner`** (владелец счета, строка), **`__balance`** (баланс счета, изначально 0, приватный).
    - Методы:
        - Конструктор **`__init__(self, owner, balance=0)`**
        - **`deposit(self, amount)`**: добавляет сумму к балансу, если сумма положительная, иначе выбрасывает **`ValueError`**
        - **`withdraw(self, amount)`**: снимает сумму с баланса, если на счету достаточно средств, иначе выбрасывает **`ValueError`**
        - **`get_balance(self)`**: возвращает текущий баланс.
"""
import pytest as pytest


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError('Сумма должна быть положительной')
        return self.__balance
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError('Средств недостаточно')
        return self.__balance
    def get_balance(self):
        return self.__balance

"""
 2. **Создание класса `SavingsAccount` (наследуется от `BankAccount`):**
    - Дополнительный атрибут: **`interest_rate`** (процентная ставка 0.05).
    - Метод **`apply_interest(self)`**: начисляет проценты на остаток по счету.
"""


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0,interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return self.get_balance()

"""3. **Создание класса `CheckingAccount` (наследуется от `BankAccount`):**
    - Переопределение метода **`withdraw(self, amount)`**: позволяет снимать средства без ограничений по балансу.
    После создания структуры необходимо:
    1. создать экземпляр класса `SavingsAccount`
    2. внести депозит 500
    3. списать с него 100
    4. применить начисление процентов
    5. написать тест с использованием pytest, что сумма > 0

"""
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self._BankAccount__balance -= amount
        return self.get_balance()

if __name__ == "__main__":
    account = SavingsAccount("Джордж")
    account.deposit(500)
    account.withdraw(100)
    account.apply_interest()
    print(account.get_balance())
