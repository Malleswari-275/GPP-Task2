# totp_utils.py
import base64
import pyotp

def generate_totp_code(hex_seed: str) -> str:
    """
    Generate a 6-digit TOTP code from a 64-character hex seed.
    """
    # Convert hex seed to bytes
    seed_bytes = bytes.fromhex(hex_seed)
    # Base32 encode (pyotp requires base32)
    base32_seed = base64.b32encode(seed_bytes).decode("utf-8")
    # Create TOTP object (SHA1, 30s, 6 digits by default)
    totp = pyotp.TOTP(base32_seed)
    return totp.now()

def verify_totp_code(hex_seed: str, code: str, valid_window: int = 1) -> bool:
    """
    Verify a TOTP code with ±valid_window periods.
    """
    seed_bytes = bytes.fromhex(hex_seed)
    base32_seed = base64.b32encode(seed_bytes).decode("utf-8")
    totp = pyotp.TOTP(base32_seed)
    return totp.verify(code, valid_window=valid_window)
