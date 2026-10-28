from urllib.parse import urljoin


def _join_two(left: str, right: str) -> str:
    """Join two URL paths regardless of the ending slash 
    existing or not.

    Parameters
    ----------
    left : str
        The `left` part of the combined URL, where the `right` part
        will be appended to regardless if there is an ending slash
        (`"/"`).
    right : str
        The path to append to the `left` URL path.

    Returns
    -------
    str
        The combined URL path.

    Examples
    --------
    ```
    _join_two("https://github.com/", "path")
    >>> "https://github.com/path"

    _join_two("path", "https://github.com/")
    >>> "https://github.com/"
    ```
    """
    base = left if left.endswith("/") else left + "/"
    return urljoin(base, right)


def merge_url(*paths: str) -> str:
    """Join multiple paths regardless of the ending slash
    existing or not.

    Parameters
    ----------
    *paths : str
        The paths to merge into a single url.
        Merging starts from the left.

    Returns
    -------
    str
        The combined URL paths.

    Raises
    ------
    ValueError
        If there are no `paths` supplied.

    Examples
    --------
    ```
    merge_url("https://github.com/", "path", "url")
    >>> "https://github.com/path/url"

    merge_url("path", "https://github.com/")
    >>> "https://github.com/"
    ```
    """
    if not paths:
        raise ValueError("At least one path is required")

    remaining = list(paths)
    url = remaining.pop(0)

    while remaining:
        url = _join_two(url, remaining.pop(0))

    return url
