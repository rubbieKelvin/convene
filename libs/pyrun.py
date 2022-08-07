import toml
import sys 

command = None if len(sys.argv)<2 else sys.argv[1]
if not command: sys.exit(1)

with open('pyproject.toml') as file:
    data = toml.load(file)

scripts = data.get('pyrun', {}).get('scripts', {})

command = command.replace(':', "_") # allows writing "command:subcommand" to map to "command_subcommand"
script = scripts.get(command)

if not script: sys.exit(1)
print(script) # return script to stdout
