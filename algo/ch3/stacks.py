# -*- coding: utf-8 -*-

from typing import Any


class FixedCapacityStack:

    def __init__(self, cap: int):
        self.con = [None] * cap
        self.n: int = 0

    def is_empty(self) -> bool:
        return self.n == 0

    def __len__(self) -> int:
        return self.n

    def push(self, item: Any):
        self.con[self.n] = item
        self.n += 1

    def pop(self) -> Any:
        self.n -= 1
        return self.con[self.n]
