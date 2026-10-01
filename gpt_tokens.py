from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
text = "I love python and transformer"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print("original text:", text)
print("tokens:", tokens)
print("token ids:", token_ids)
encoded = tokenizer(text)
print("Encoded Output:", encoded)

decoded_text = tokenizer.decode(token_ids)
print("Decoded Text:", decoded_text)