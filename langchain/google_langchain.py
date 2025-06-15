from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Simple text invocation
result = llm.invoke("Sing a ballad of LangChain.")
print(result.content)

# Multimodal invocation with gemini-pro-vision
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "What's in this image?",
        },
        {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
    ]
)
result = llm.invoke([message])
print(result.content)