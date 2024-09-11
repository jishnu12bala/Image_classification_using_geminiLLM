import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
 model="claude-3-opus-20240229",
 max_tokens=1000,
 temperature=0.0,
 system="Respond in short and clear sentences.",
 messages=[
 {
 "role": "user",
 "content": "Can you explain the concept of neural networks?"
 }
 ]
)

print(message.content)