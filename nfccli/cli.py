"""Usage:
   nfccli read [--continuous]
   nfccli write --string=<string>
   nfccli -h | --help
   nfccli --version

Options:
   -h --help  Displays this message
   --version  Displays the version number
"""
from . import commands
from docopt import docopt
import nfccli


def run(doc=__doc__):
    arguments = docopt(doc)

    if arguments['--version']:
        print('nfccli v{}'.format(nfccli.__version__))
        return 0

    selected_commands = [
        command
        for command, active in arguments.items()
        if not command.startswith('-') and active
    ]

    command = getattr(commands, selected_commands[0], None)

    if command is None:
        print('Command not yet implemented.')
        return 1

    command(**arguments)

    return 0


if __name__ == '__main__':
    sys.exit(run())
