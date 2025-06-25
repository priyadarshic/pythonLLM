from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human",
         "{input}"),
    ]
)

chain = prompt | llm

translation = chain.invoke(
    {
        "input_language": "English",
        "output_language": "Russian",
        "input": "I am an expert trainer in Programming.",
    }
)

print(translation.content)
