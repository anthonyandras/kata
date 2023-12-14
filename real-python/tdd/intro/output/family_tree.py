from rich.tree import Tree
from rich import print as rprint

tree = Tree("Family Tree")
tree.add("Mom")
tree.add("Dad")
tree.add("Anthony").add("Maya")
tree.add("[blue]Kristie").add("[green]Max")

rprint(tree)
