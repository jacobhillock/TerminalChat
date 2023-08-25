from src.size import get_size
from src.args import get_args
from src.config import Config
from src.format_message import format_message
from src.generate_box import message
from src.print_message import print_message

config = Config(1, 2, 1)

if __name__ == '__main__':
    args = get_args()
    terminal_size = get_size()
    
    h_padding = config.H_EXTERNAL + config.H_INTERNAL + 1
    available_width = terminal_size.columns - h_padding*2
    
    message_lines = format_message(args.message, available_width, h_padding)
    filled_message = message(config, message_lines)
    print_message(filled_message, config)
