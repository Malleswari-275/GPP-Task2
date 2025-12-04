from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crypto_utils import decrypt_seed
from cryptography.hazmat.primitives import serialization

app = FastAPI()

# Pydantic model for request body
class SeedRequest(BaseModel):
    encrypted_seed: str

# Load private key once at startup
try:
    with open("student_private.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
except Exception as e:
    print("Failed to load private key:", e)
    private_key = None

@app.post("/decrypt-seed")
def decrypt_seed_endpoint(request: SeedRequest):
    if private_key is None:
        raise HTTPException(status_code=500, detail="Private key not loaded")

    try:
        decrypted = decrypt_seed(request.encrypted_seed, private_key)
        return {"decrypted_seed": decrypted}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
