from ratings import stars_label, top_rated


def test_stars_label():
    assert stars_label(4.8) == "excellent"
    assert stars_label(3.5) == "good"
    assert stars_label(2.0) == "ok"
    assert stars_label(1.0) == "poor"


def test_top_rated():
    books = [{"t": "a", "rating": 3}, {"t": "b", "rating": 5}, {"t": "c", "rating": 4}]
    assert [b["t"] for b in top_rated(books, 2)] == ["b", "c"]
