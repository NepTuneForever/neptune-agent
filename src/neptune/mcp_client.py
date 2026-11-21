import asyncio
from agno.tools.mcp import MCPTools

async def main():
    async with MCPTools(url="https://docs.agno.com/mcp") as mcp:
        for tool in mcp.functions:
            print(tool)
            

asyncio.run(main())