from makerscamp.db import *
from dataclasses import dataclass

@dataclass
class Message:
    """Class to hold messages"""
    id: str
    user_id: str
    channel_id: str
    message: str
