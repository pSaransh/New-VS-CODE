from mimetypes import init
from pickle import NONE


class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None