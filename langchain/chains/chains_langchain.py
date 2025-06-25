# from langchain.chains import LLMChain
# from langchain_google_genai import ChatGoogleGenerativeAI
#
# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# # Create a chain that first generates text based on a prompt and then summarizes it
# generate_text_chain = LLMChain(llm=llm, prompt="Generate a short story about a cat.")
# summary_chain = LLMChain(llm=llm, prompt="Summarize this: {input}")
#
#
# # Execute the chain
# story = generate_text_chain.run()
# summary = summary_chain.run(input=story)
# print(story)
# print(summary)
#
#
#

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
            "You are a helpful assistant that summarizes story from {story} to {summary}.",
        ),
        ("human",
         "{input}"),
    ]
)

chain = prompt | llm

summary = chain.invoke(
    {
        "story": "English",
        "summary": "English",
        "input": "Generate a short story about a Dog.",
    }
)

print(summary.content)

