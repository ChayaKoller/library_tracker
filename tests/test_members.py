from members import find_member, full_name, normalize_email


def test_normalize_email():
    assert normalize_email({"email": "  Dan@Example.COM "}) == "dan@example.com"


def test_normalize_email_missing():
    assert normalize_email({"first": "Dan"}) is None


def test_full_name():
    assert full_name({"first": " Dan ", "last": "Levi"}) == "Dan Levi"
    assert full_name({"first": "Dan"}) == "Dan"


def test_find_member():
    ms = [{"id": 1}, {"id": 2}]
    assert find_member(ms, 2) == {"id": 2}
    assert find_member(ms, 3) is None
