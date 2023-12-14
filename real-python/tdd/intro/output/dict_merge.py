from rich.console import Console


def merge_dict(dict1, dict2):
    return dict1 | dict2


if __name__ == '__main__':
    console = Console()
    console.log(merge_dict({'id': 1}, {'name': 'Absutosh'}), log_locals=True)
