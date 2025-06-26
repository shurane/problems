from typing import Any
from io import StringIO

SHIFT=" "
def pp(s: StringIO, data: Any, indent: str = "", skip: bool = False) -> None:
    def indentured():
        nonlocal skip
        if skip:
            skip = False
            return ""
        return indent

    match data:
        case int() | float() | str() | bool():
            s.write(f"{indentured()}{data}")
        case list() | tuple() as lst if not lst:
            s.write(f"{indentured()}[]")
        case list() | tuple() as lst:
            s.write(f"{indentured()}[\n")
            for val in lst[:-1]:
                pp(s, val, indent=indent + SHIFT, skip=skip)
                skip=False
                s.write(",\n")
            pp(s, lst[-1], indent=indent + SHIFT, skip=skip)
            s.write("\n")
            s.write(f"{indentured()}]")
        case dict() as d if not d:
            s.write(f"{indentured()}{{}}")
        case dict() as d:
            s.write(f"{indentured()}{{\n")
            for key, val in d.items():
                pp(s, key, indent=indent + SHIFT)
                s.write(": ")
                pp(s, val, indent=indent + SHIFT, skip=True)
                s.write(",\n")
            s.write(f"{indentured()}}}")

        case _:
            raise ValueError(data)


for value in (1, 50, 100, 3.14159, "quickbrownfox", True, False):
    with StringIO() as s:
        pp(s, value)
        print(f"original: {value}, pprint: {s.getvalue()}")

for lst in [[], [1,2], (1,2,3), list(range(10)), [[1]], [[1],[[1,2]],[[[1,2,3]]]]]:
    with StringIO() as s:
        print(f"pprint: {lst}")
        pp(s, lst)
        print(s.getvalue())

def create_nested_dict(n: int):
    if n == 0:
        return {}

    return {n: n, n-1: create_nested_dict(n-1)}

def create_tree_dict(n: int):
    if n == 0:
        return {}

    result = {}
    for i in range(n):
        result[i] = i
    result[n] = create_tree_dict(n-1)

    return result

for d in [{1:1}, {1:1, 2:2}, {1: {}, 2: {2: 2}, 3: {3: {3: 3}}}, create_nested_dict(10), create_tree_dict(5)]:
    with StringIO() as s:
        print(f"pprint: {d}")
        pp(s, d)
        print(s.getvalue())
