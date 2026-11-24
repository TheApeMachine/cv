import hashlib, hmac, json, requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Daniel Owen van Dommelen",
    "email": "daniel.van.dommelen@gmail.com",
    "resume": "https://github.com/TheApeMachine/cv/blob/2d0b97a81cb843db20b7851ab5fcd8eaacc7f2e3/Daniel%20Owen%20van%20Dommelen%20-%20resume%20-%202026.pdf",       # URL to your resume
    "location": "Rome, Italy",
    "linkedin": "https://www.linkedin.com/in/theapemachine",
    "codeLink": "https://github.com/TheApeMachine/cv/blob/b51dbe200d352ff3e73b1f52297b315608557eed/howgood.py",
    "yearsPython": 10,
    "yearsDjango": 5,
}

body = json.dumps(payload)
signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()

resp = requests.post(
    endpoint,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-HMAC-Signature": signature,
    },
)
print(resp.status_code, resp.json())