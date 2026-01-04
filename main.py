import random
from fastmcp import FastMCP

mcp = FastMCP(name='Demo Server')

@mcp.tool
def roll_dice(sides: int = 6) -> int:
    """Roll a dice with the given number of sides."""
    return random.randint(1, sides)

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

if __name__ == '__main__':
    mcp.run(transport="http", host="0.0.0.0", port=8000)