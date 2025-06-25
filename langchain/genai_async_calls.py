from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


async def run_async_calls():
    # Async invoke
    result_ainvoke = await llm.ainvoke("Why is the sky blue?")
    print("Async Invoke Result:", result_ainvoke.content[:70] + "...")

    # Async stream
    print("\nAsync Stream Result:")
    async for chunk in llm.astream(
        "Write a short poem about asynchronous programming."
    ):
        print(chunk.content, end="", flush=True)
    print("\n")

    # Async batch
    results_abatch = await llm.abatch(["What is 1+1?", "What is 2+2?"])
    print("Async Batch Results:", [res.content for res in results_abatch])


async def main():
    await run_async_calls()

asyncio.run(main())

