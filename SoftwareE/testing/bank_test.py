from bank import BankAccount
import pytest
@pytest.fixture
def account(tmp_path):
    log= tmp_path/"transactions@test.log"
    account= BankAccount(balance=777,log_file=str(log))
    yield account
def test_positive_deposite(account,):
    amount=333
    result = account.deposit(333)
    account._log_transaction(f"a deposit of {amount}has been done , new balance {result}")
    assert result==1110
def test_negative_deposite(account):
    amount=-333
    balance=account.get_balance()
    result = account.deposit(-333)
    account._log_transaction(f"a deposit of {amount}has been try , new balance {result}")
    assert result==balance
def test_enougth_withdraw(account):
    amount=7
    balance=account.get_balance()
    result = account.withdraw(amount)
    account._log_transaction(f"a withdraw of {amount}has been done , new balance {result}")
    assert result==balance-amount

def test_withdraw_too_much(account):
    amount=123456789
    with pytest.raises(ValueError):
        account.withdraw(amount)
def test_logfile_written(account):
    with open(account.log_file )as file:
        text=file.read()
    assert "creada" in text

    

