from typing import Optional

# variables
x: int = 1
name: str = "name"
is_true: bool = True


# functions
def add(a: int, b: int) -> None:
    print(a + b)


add(1, 2)


numbers: list[int] = [1, 2, 3, 4, 5, 6]
user_info: dict[str, str] = {"name": "name", "age": "30"}


def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "name"
    else:
        return None


def process(value: int | str) -> str:
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return value
    else:
        return "unknown"
