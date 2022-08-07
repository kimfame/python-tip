import functools
from typing import Callable

ComposableFunction = Callable[[float], float]

def compose(*functions):
    return functools.reduce(
        lambda f,
        g: lambda x: g(f(x)),
        functions
    )


def add_one(num: float) -> float:
    return num + 1

def multiple_by_two(num: float) -> float:
    return num * 2

def main() -> None:
    total_func = compose(
        add_one,
        add_one,
        multiple_by_two
    )
    print(total_func(98))

if __name__ == "__main__":
    main()