import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import pyotp

# ----------------------------
# Load Private Key
# ----------------------------
def load_private_key(path="student_private.pem"):
    with open(path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
        )
    return private_key

# ----------------------------
# Decrypt Seed (PKCS1v15, block-wise)
# ----------------------------
def decrypt_seed(encrypted_seed_b64: str, private_key) -> str:
    encrypted_bytes = base64.b64decode(encrypted_seed_b64)
    key_size_bytes = (private_key.key_size + 7) // 8

    decrypted_bytes = b""
    for i in range(0, len(encrypted_bytes), key_size_bytes):
        block = encrypted_bytes[i:i + key_size_bytes]
        decrypted_block = private_key.decrypt(
            block,
            padding.PKCS1v15()
        )
        decrypted_bytes += decrypted_block

    decrypted_seed = decrypted_bytes.hex()
    if len(decrypted_seed) < 64:
        raise ValueError(f"Decrypted data too short: {len(decrypted_seed)}")
    return decrypted_seed[:64]

# ----------------------------
# Generate TOTP
# ----------------------------
def generate_totp_code(hex_seed: str) -> str:
    seed_bytes = bytes.fromhex(hex_seed)
    seed_base32 = base64.b32encode(seed_bytes).decode('utf-8')
    totp = pyotp.TOTP(seed_base32)
    return totp.now()

# ----------------------------
# Verify TOTP
# ----------------------------
def verify_totp_code(hex_seed: str, code: str, valid_window: int = 1) -> bool:
    seed_bytes = bytes.fromhex(hex_seed)
    seed_base32 = base64.b32encode(seed_bytes).decode('utf-8')
    totp = pyotp.TOTP(seed_base32)
    return totp.verify(code, valid_window=valid_window)
