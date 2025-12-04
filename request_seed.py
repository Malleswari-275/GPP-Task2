import json
import requests

API_URL = "https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws"

def request_seed(student_id: str, github_repo_url: str):
    # Step 1: Read your student public key
    with open("instructor_public.pem", "r") as f:
        public_key = f.read().strip()   # <-- KEEP ORIGINAL PEM FORMAT

    # Step 2: Create request payload
    payload = {
        "student_id": student_id,
        "github_repo_url": github_repo_url,
        "public_key": public_key      # <-- SEND EXACT PEM
    }

    print("Sending request...")
    response = requests.post(API_URL, json=payload)

    # Step 3: Handle API response
    if response.status_code != 200:
        print("API error:", response.text)
        return

    data = response.json()

    encrypted_seed = data.get("encrypted_seed")
    if not encrypted_seed:
        print("Encrypted seed not found")
        print(data)
        return

    # Step 4: Save encrypted seed
    with open("encrypted_seed.txt", "w") as f:
        f.write(encrypted_seed)

    print("\nSUCCESS!")
    print("Encrypted seed saved to encrypted_seed.txt")

# ---- RUN HERE ----
if __name__ == "__main__":
    request_seed(
        student_id="23A91A6166",
        github_repo_url="https://github.com/Malleswari-275/GPP-Task2"
    )
