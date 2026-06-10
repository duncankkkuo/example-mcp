"""Example MCP server for the KKday MCP Platform.

- 用官方 mcp SDK 的 FastMCP，streamable-http transport（預設掛在 /mcp）。
- 監聽 $PORT（Cloud Run 會給，預設 8080），host 0.0.0.0。
- 不做任何驗證：平台的 JWT 驗證在 Apigee 那層做，這裡是被保護的後端。
"""

import os
import random
import uuid
from datetime import datetime, timezone

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("example-mcp")


@mcp.tool()
def echo(text: str) -> str:
    """Echo back the given text unchanged."""
    return text


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a (a - b)."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Errors if b is zero."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


@mcp.tool()
def current_time() -> str:
    """Return the current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


@mcp.tool()
def random_number(minimum: int = 0, maximum: int = 100) -> int:
    """Return a random integer between minimum and maximum (inclusive)."""
    return random.randint(minimum, maximum)


@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse the given text."""
    return text[::-1]


@mcp.tool()
def word_count(text: str) -> int:
    """Count the number of whitespace-separated words in the text."""
    return len(text.split())


@mcp.tool()
def to_uppercase(text: str) -> str:
    """Convert the text to uppercase."""
    return text.upper()


@mcp.tool()
def bmi(weight_kg: float, height_m: float) -> float:
    """Calculate Body Mass Index from weight (kg) and height (m)."""
    return round(weight_kg / (height_m**2), 2)


@mcp.tool()
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


@mcp.tool()
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@mcp.tool()
def generate_uuid() -> str:
    """Generate and return a random UUID4 string."""
    return str(uuid.uuid4())


# streamable-http ASGI app（FastMCP 預設掛在 /mcp）
app = mcp.streamable_http_app()


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
