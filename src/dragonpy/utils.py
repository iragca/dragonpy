from urllib.parse import urljoin


def _join_two(left: str, right: str) -> str:
    base = left if left.endswith("/") else left + "/"
    return urljoin(base, right)


def merge_url(*paths) -> str:
    """Join paths regardless of the ending slash existing or not."""
    if not paths:
        raise ValueError("At least one path is required")

    paths = list(paths)
    url = paths.pop(0)

    while paths:
        url = _join_two(url, paths.pop(0))

    return url
