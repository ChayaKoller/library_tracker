from text_tools import title_case, truncate, word_count


def test_truncate_short_text_unchanged():
    assert truncate("hello", 10) == "hello"


def test_truncate_respects_max_len():
    result = truncate("abcdefghijkl", 8)
    assert result == "abcde..."
    assert len(result) == 8


def test_word_count():
    assert word_count("one two  three") == 3


def test_word_count_missing():
    assert word_count(None) == 0
    assert word_count("") == 0


def test_title_case():
    assert title_case("the lord of the rings") == "The Lord of the Rings"
