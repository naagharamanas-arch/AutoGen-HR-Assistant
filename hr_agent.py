
import asyncio
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


async def main():
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini"
    )

    try:
        agent = AssistantAgent(
            name="hr_assistant",
            model_client=model_client,
            system_message="You are an HR assistant."
        )

        await Console(
            agent.run_stream(
                task=(
                    "Write a job description for a Junior Python Developer "
                    "in exactly five bullet points. Use one line per bullet."
                )
            )
        )
    finally:
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
