from src.config import Config
from src.message import Message

def print_message(message: Message, config: Config):
    print(message.start_line)
    [print(message.padding_line) for _ in range(config.V_INTERNAL)]
    for line in message.message_body:
        print(line)
    [print(message.padding_line) for _ in range(config.V_INTERNAL)]
    print(message.end_line)

    if message.figure:
        print(' '*(config.H_EXTERNAL + config.H_INTERNAL + 1) + message.figure)