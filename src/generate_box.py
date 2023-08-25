from src.config import Config
from src.message import Message

def message(config: Config, message_lines: list[str]) -> Message:
    message = Message()
    max_line_length = max([len(line) for line in message_lines])

    message.start_line = ' '*config.H_EXTERNAL + '|' + '-'*(max_line_length + config.H_INTERNAL*2) + '|'
    message.end_line = message.start_line
    message.padding_line = ' '*config.H_EXTERNAL + '|' + ' '*(max_line_length + config.H_INTERNAL*2) + '|'
    message.message_body = [
        ' '*config.H_EXTERNAL + '|' + ' '*config.H_INTERNAL + line + ' '*config.H_INTERNAL + '|'
        for line in message_lines
    ]

    return message
