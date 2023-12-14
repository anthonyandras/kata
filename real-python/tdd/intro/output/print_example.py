from rich import print as rprint
from rich import inspect
import rich

if __name__ == "__main__":
    nums_list = [1, 2, 3, 4]
    rprint(nums_list)

    nums_tuple = (1, 2, 3, 4)
    rprint(nums_tuple)

    nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
    rprint(nums_dict)

    bool_list = [True, False]
    rprint(bool_list)

    inspect(rich)  # excellent for debugging
