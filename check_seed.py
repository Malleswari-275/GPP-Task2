import base64

with open("encrypted_seed.txt", "r") as f:
    encrypted = f.read().strip()

decoded_bytes = base64.b64decode(encrypted)
print("Decoded bytes length:", len(decoded_bytes))  # Should be 1024 for 8192-bit key
