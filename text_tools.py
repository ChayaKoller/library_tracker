def truncate(text: str, max_len: int) -> str:
    """Cut text so the result (including '...') is at most max_len characters."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."


def word_count(text: str | None) -> int:
    """Number of words; empty or missing text has 0 words."""
    return len(text.split())


def title_case(text: str) -> str:
    small = {"of", "the", "and", "a", "in"}
    words = text.lower().split()
    return " ".join(
        w if (i > 0 and w in small) else w.capitalize() for i, w in enumerate(words)
    )
