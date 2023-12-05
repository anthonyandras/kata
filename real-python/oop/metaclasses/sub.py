import subprocess


class Action:
    def __init__(self, actions):
        self.actions = actions

    def __call__(self, *args, **kwargs):
        for action in self.actions:
            subprocess.run(action)


if __name__ == "__main__":
    hellos = Action([['echo', 'hello_world'], ['echo', 'bonjour le monde']])
    hellos()
