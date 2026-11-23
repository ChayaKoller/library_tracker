from datetime import date

from loans import days_late, due_date, is_overdue, late_fee


def test_due_date_month_end():
    assert due_date(date(2024, 1, 31)) == date(2024, 2, 29)


def test_not_overdue_on_due_date():
    assert is_overdue(date(2024, 3, 10), date(2024, 3, 10)) is False


def test_overdue_after_due_date():
    assert is_overdue(date(2024, 3, 10), date(2024, 3, 11)) is True


def test_days_late():
    assert days_late(date(2024, 3, 10), date(2024, 3, 14)) == 4
    assert days_late(date(2024, 3, 10), date(2024, 3, 1)) == 0


def test_late_fee_small():
    assert late_fee(date(2024, 3, 10), date(2024, 3, 12)) == 3.0


def test_late_fee_capped():
    assert late_fee(date(2024, 3, 10), date(2024, 5, 10)) == 30.0
