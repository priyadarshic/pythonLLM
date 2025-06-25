from google.ai.generativelanguage_v1beta.types import Tool as GenAITool
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
resp = llm.invoke(
    "What is 5!, use python",
    tools=[GenAITool(code_execution={})],
)
print(resp.content)

for c in resp.content:
    if isinstance(c, dict):
        if c["type"] == "code_execution_result":
            print(f"Code execution result: {c['code_execution_result']}")
        elif c["type"] == "executable_code":
            print(f"Executable code: {c['executable_code']}")
    else:
        print(c)
