import toml

def load():
    with open('config.toml', 'r') as file:
        return toml.load(file)
