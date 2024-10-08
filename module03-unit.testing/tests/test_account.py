"""
CUT: Class Under Test
MUT: Method Under Test
     withdraw, deposit
     __init__
     __str__

     Unit Test Phases:
     1. Test Fixture/Setup
     2. call exercise method
     3. verification
     4. Teardown
"""
import pytest

from banking.account import Account, InsufficientBalanceException, AccountStatus

withdraw_failure_amounts = [
    100_000.10,
    100_001.00,
    100_001.10
]

withdraw_negative_amounts = [
    0.0,
    -1.00,
    -0.10
]


@pytest.fixture
def an_active_account():
    # 1. Test Fixture/Setup
    return Account("TR290006222359813456984831", 100_000)


@pytest.fixture
def an_closed_account():
    # 1. Test Fixture/Setup
    return Account("TR290006222359813456984831", 100_000, AccountStatus.CLOSED)


@pytest.mark.parametrize("amount", withdraw_negative_amounts)
def test_withdraw_with_wrong_amount_should_raise_exception(an_active_account, amount):
    with pytest.raises(ValueError):  # 3. verification
        # 2. call exercise method
        an_active_account.withdraw(amount)
    # 4. Teardown


def test_deposit_positive_amount_should_success(an_active_account):
    balance = an_active_account.deposit(1)
    assert balance == 100_001
    assert an_active_account.status == AccountStatus.ACTIVE


def test_withdraw_from_closed_account_should_raise_exception(an_closed_account):
    with pytest.raises(ValueError):  # 3. verification
        # 2. call exercise method
        an_closed_account.withdraw(1.0)
    # 4. Teardown


@pytest.mark.parametrize("amount", withdraw_failure_amounts)
def test_withdraw_with_amount_larger_than_balance_should_raise_exception(an_active_account, amount):
    with pytest.raises(InsufficientBalanceException):  # 3. verification
        # 2. call exercise method
        an_active_account.withdraw(amount)
    # 4. Teardown


def test_withdraw_all_balance_should_success(an_active_account):
    # 2. call exercise method
    an_active_account.withdraw(100_000)
    # 3. verification
    assert an_active_account.balance == 0
    assert an_active_account.status == AccountStatus.ACTIVE
    # 4. Teardown
