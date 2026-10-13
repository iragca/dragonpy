from urllib.parse import urljoin


def _join_two(left: str, right: str) -> str:
    base = left if left.endswith("/") else left + "/"
    return urljoin(base, right)


def merge_url(*paths) -> str:
    """Join paths regardless of the ending slash existing or not.

    Accepts either several positional path strings or a single iterable of
    path strings (e.g. a list) for convenience.
    """

    if len(paths) == 1 and isinstance(paths[0], (list, tuple)):
        paths = tuple(paths[0])

    if len(paths) < 2:
        raise ValueError("merge_url requires at least two paths")

    converted = list(paths)
    total = len(converted)

    # The historical implementation recursed on ``(first two) + rest`` which made
    # deeply nested/long inputs hit Python's recursion limit. Reproduce the same
    # grouping iteratively so behaviour is preserved for any number of paths.
    if total % 2 == 0:
        result = _join_two(converted[-2], converted[-1])
        position = total - 2
    else:
        result = _join_two(_join_two(converted[-3], converted[-2]), converted[-1])
        position = total - 3

    while position > 0:
        position -= 2
        left = _join_two(converted[position], converted[position + 1])
        result = _join_two(left, result)

    return result
