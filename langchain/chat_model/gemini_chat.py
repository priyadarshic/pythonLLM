from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

output = model.invoke("Hello, world!")

print(output.content)

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("I am a a friend from Rome!"),
]

output = model.invoke(messages)
print(output.content)

