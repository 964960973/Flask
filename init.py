import functools


def func_1(x: str) -> None:
    """
    function
    :return: None
    """
    print("func_1", x)


@functools.wraps(func_1)
def demo():
    """
    demo
    :return: None
    """
    print("demo")

print("demo name:", demo.__name__)
print("demo doc:", demo.__doc__)
print("demo annotations:", demo.__annotations__)
demo()
print("func_1 is demo's wrap:", func_1 is demo.__wrapped__)
print(demo.__wrapped__)
