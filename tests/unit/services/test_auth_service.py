from dragonpy.services import AuthorizationService


def test_enc_password():
    password = "baba123"
    encrypted = (
        "0QzBx7IoGPc7E9bCBPLDJQ=="  # taken from dragonfi.ph failed test login
    )
    result = AuthorizationService._encrypt_password(
        password,
        b"$Dr@gonF!C0rP_Phil1ppin3s@2023#$",
        enc_iv=b"0000000000000000",
    )
    assert result == encrypted
