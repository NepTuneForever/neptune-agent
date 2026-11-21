import asyncio
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.mcp import MCPTools

async def main():
    async with MCPTools(url="https://docs.agno.com/mcp") as mcp:
        agent = Agent(
            model=Ollama(id="llama3.1:8b"),
            tools=[mcp]
        )

        await agent.aprint_response(
            "Use a ferramenta search_docs para pesquisar a documentação do Agno."
        )

asyncio.run(main())