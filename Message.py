from enum  import Enum

class Type(Enum):
    QUERY_LATEST_BLOCK = 0
    QUERY_ALL = 1
    RESPONSE_BLOCKCHAIN = 2


class Message:
    def __init__(self, type, data, addr):
        self.type = type
        self.data = data
        self.addr = addr