def parse_commands(program: str):
    commands = program.split()
    out_commands = list()
    for cmd in commands:
        if 'REPEAT' in cmd:
            command = cmd.replace('REPEAT', '')
            command = command.replace('(', '').replace(')', '')
            command_count = int(command.split(',')[1])
