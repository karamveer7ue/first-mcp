# MCP Server with Groq API (via openai API) tool
# pip install fastmcp
import os
import openai

from mcp.server.fastmcp import FastMCP
import math

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
groq_model = "openai/gpt-oss-120b"

mcp = FastMCP("External API on LM Studio", "0.1.0")

@mcp.tool()
async def Groq(prompt: str) -> str:
    """
    Queries Groq API to answer the user query.
    
    Args:
        prompt: The query to send to the Groq API.
   
    Returns:
        The response from the Groq API as a string.
    """

    client = openai.OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=groq_api_key
    )
    response = client.responses.create(
        model=groq_model,
        input=prompt,
    )
    return response.output_text


mcp.run(transport='stdio')  # Standard input/output transport