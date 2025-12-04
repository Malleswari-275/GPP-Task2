from crypto_utils import load_private_key, decrypt_seed, generate_totp_code, verify_totp_code

# Load encrypted seed
with open("encrypted_seed.txt", "r") as f:
    encrypted = f.read().strip()

# Load private key
private_key = load_private_key("student_private.pem")

# Decrypt seed
hex_seed = decrypt_seed(encrypted, private_key)
print("Decrypted Seed:", hex_seed)

# Generate current TOTP
totp_code = generate_totp_code(hex_seed)
print("Current TOTP Code:", totp_code)

# Verify TOTP (should return True)
is_valid = verify_totp_code(hex_seed, totp_code)
print("Verification:", is_valid)
