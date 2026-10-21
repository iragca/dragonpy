from pytest import raises
from dragonpy.utils import merge_url


def test_merge_url():
    base = "https://api.dragonfi.ph/api/v2/Securities"

    assert merge_url(base, "GetStockProfile") == (
        "https://api.dragonfi.ph/api/v2/Securities/GetStockProfile"
    )
    assert merge_url(base + "/", "GetStockProfile") == (
        "https://api.dragonfi.ph/api/v2/Securities/GetStockProfile"
    )


def test_merge_url_multiple_paths():
    assert (
        merge_url(
            "https://api.dragonfi.ph/api/v2", "Securities", "GetStockProfile"
        )
        == "https://api.dragonfi.ph/api/v2/Securities/GetStockProfile"
    )

    assert (
        merge_url(
            "https://api.dragonfi.ph/api/v2/",
            "Securities/",
            "GetStockProfile",
        )
        == "https://api.dragonfi.ph/api/v2/Securities/GetStockProfile"
    )


def test_merge_url_long_list_of_str_paths():
    paths = ["https://example.com/api"] + [
        f"segment{i}" for i in range(1, 101)
    ]
    expected = "https://example.com/api/" + "/".join(
        f"segment{i}" for i in range(1, 101)
    )
    assert merge_url(*paths) == expected


def test_merge_url_has_input():
    with raises(ValueError):
        merge_url()
