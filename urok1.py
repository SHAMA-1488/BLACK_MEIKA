from huggingface_hub import InferenceClient

client = InferenceClient(model="Qwen/Qwen2.5-72B-Instruct", token="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")

response = client.chat_completion(
    messages=[{"role": "user", "content": "Привет, кто ты?"}],
    max_tokens=100,
)

print(response["choices"][0]["message"]["content"])