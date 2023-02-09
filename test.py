from typing import List, Any, Union


class Path:
    def __init__(self, path: str, item: Union[list, dict]):
        self.path = path
        self.item = item


def handle_dict(stack, path, data, result):
    for k, v in data.items():
        if isinstance(v, dict) or isinstance(v, list):
            if path == "":
                spath = k
            else:
                spath = f"{path}.{k}"
            stack.append(Path(path=spath, item=v))
        else:
            if path == "":
                spath = k
            else:
                spath = f"{path}.{k}"
            result[spath] = v


def solution(d: dict):
    stack: List[Path] = []
    result = dict()
    current_path = Path("", d)
    while True:
        value = current_path.item
        if isinstance(value, dict):
            handle_dict(stack, current_path.path, current_path.item, result)
        elif isinstance(value, list):
            pass
        if len(stack) == 0:
            break
        current_path = stack.pop()
    return result


c = {
    "a": 123,
    "b": {
        "12": "12",
        "3": "4",
        1:2,
        "c": {
            "hello": "hi",
            "see": "you"
        }
    }
}

print(solution(c))