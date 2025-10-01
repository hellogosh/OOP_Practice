from main import BankAccount, SavingsAccount, CheckingAccount
import pytest

def test_balance_positive():
    acc = SavingsAccount("Test")
    acc.deposit(500)
    acc.withdraw(100)
    acc.apply_interest()
    assert acc.get_balance() > 0
def test_deposit_positive(): #Попытка депозита положительной суммы увеличивает баланс.
    acc = BankAccount("Test")
    acc.deposit(100)
    assert acc.get_balance() == 100
def test_deposite_negative(): #Попытка депозита отрицательной суммы вызывает ValueError.
    acc = BankAccount('Test')
    with pytest.raises(ValueError):
        acc.deposit(-10)
def test_deposit_positive_with_iterations(): #Поэтапное пополнение суммы корректно увеличивает баланс.
    acc = BankAccount("Test")
    acc.deposit(100)
    assert acc.get_balance() == 100
    acc.deposit(100)
    assert acc.get_balance() == 200
def test_withdraw(): #Поэтапное снятие суммы в пределах доступного баланса корректно уменьшает баланс.
    acc = BankAccount("Test")
    acc.deposit(100)
    assert acc.get_balance() == 100
    acc.withdraw(50)
    assert acc.get_balance() == 50
def test_withdraw_unlimit(): #Попытка снять сумму больше баланса вызывает ValueError.
    acc = BankAccount("Test")
    acc.deposit(100)
    assert acc.get_balance() == 100
    with pytest.raises(ValueError):
        acc.withdraw(101)
def test_apply_interest(): #Применение процентов к балансу
    acc = SavingsAccount("Test")
    acc.deposit(100)
    acc.apply_interest()
    assert acc.get_balance() == 105
def test_withdraw_excess_limit(): #снимает средства даже если сумма превышает баланс
    acc = CheckingAccount("Test")
    acc.deposit(100)
    acc.withdraw(101)
    assert acc.get_balance() == -1
