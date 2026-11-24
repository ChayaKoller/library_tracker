def stars_label(avg: float) -> str:
    """Label for an average rating between 0 and 5."""
    if avg >= 4.5:
        return "excellent"
    elif avg >= 3:
        return "good"
    elif avg >= 2:
        return "ok"
    return "poor"


def top_rated(books: list[dict], n: int) -> list[dict]:
    """The n books with the highest rating."""
    ranked = sorted(books, key=lambda b: b["rating"], reverse=True)
    return ranked[:n]
