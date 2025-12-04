from crypto_utils import load_private_key, decrypt_seed

# Load encrypted seed
with open("encrypted_seed.txt", "r") as f:
    encrypted = f.read().strip()

# Load private key
private_key = load_private_key("student_private.pem")

# Decrypt
seed = decrypt_seed(encrypted, private_key)

print("Decrypted Seed:", seed)
