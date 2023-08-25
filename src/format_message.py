def format_message(message, available_width, padding=0):
    message_split: list[str] = message.split(' ')
    message_lines: list[str] = []
    current_line: str = message_split[0]
    for word in message_split[1:]:
        if len(current_line) + len(word) > available_width:
            message_lines.append(current_line)
            current_line = word
        current_line += ' ' + word
    message_lines.append(current_line)

    max_line_length = max([len(line) for line in message_lines])
    message_lines = [
        line.ljust(max_line_length, ' ')
        for line in message_lines
    ]
    return message_lines