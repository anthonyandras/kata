import sys
import os
from rich import print
from rich.columns import Columns

if __name__ == '__main__':
    # print("[italic red]Hello World![/italic red]")
    if len(sys.argv) < 2:
        print("Usage: python pretty.py DIRECTORY")
    else:
        directory = os.listdir(sys.argv[1])
        columns = Columns(directory, equal=True, expand=True)
        print(columns)
