# pip install fastmcp

from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("Kams First MCP Server", "0.1.0")

@mcp.tool()
async def factorial(param1: int) -> str:
    """
    Returns the factorial of a number.
    
    Args:
        param1: The number to calculate the factorial of.
   
    Returns:
        The factorial of the input number as a string.
    """
    if param1 < 0:
        return "Error: Factorial is not defined for negative numbers."
    result = math.factorial(param1)
    return str(result)


mcp.run(transport='stdio')  # Standard input/output transport