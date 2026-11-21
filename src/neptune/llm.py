import httpx

def generate(prompt:str)->None:
    response=httpx.post("http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5-coder:0.5b",
        "prompt": prompt,
        "stream": False
    },
    timeout=120
    )

    data = response.json()

    print(data["response"])

