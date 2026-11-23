def normalize_email(member: dict) -> str | None:
    """Lower-cased, stripped email, or None if the member has no email."""
    return member.get("email").strip().lower()


def full_name(member: dict) -> str:
    first = member.get("first", "").strip()
    last = member.get("last", "").strip()
    return f"{first} {last}".strip()


def find_member(members: list[dict], member_id: int) -> dict | None:
    for m in members:
        if m.get("id") == member_id:
            return m
    return None
