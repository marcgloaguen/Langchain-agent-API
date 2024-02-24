from langchain.tools import tool


@tool
def square(x: int) -> int:
    """
    squares a number
    """
    return int(x)**2
