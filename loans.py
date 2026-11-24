from datetime import date

from dateutil.relativedelta import relativedelta


def due_date(start: date, months: int = 1) -> date:
    """Loan due date: same day of month, `months` later (clipped to month end)."""
    return start + relativedelta(months=months)


def is_overdue(due: date, today: date) -> bool:
    """A book returned on the due date itself is not overdue."""
    return today > due


def days_late(due: date, today: date) -> int:
    """Number of days after the due date (0 if not late)."""
    return max(0, (today - due).days)


def late_fee(due: date, today: date, daily_rate: float = 1.5, max_fee: float = 30.0) -> float:
    """Fee grows per late day, but never above max_fee."""
    return min(days_late(due, today) * daily_rate, max_fee)
