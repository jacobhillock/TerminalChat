from dataclasses import dataclass, field

@dataclass
class Message:
    start_line: str = ''
    end_line: str = ''
    padding_line: str = ''
    message_body: list[str] = field(default_factory=list)
    figure: str = ''
