# -*- coding: utf-8 -*-

import pytest
from algo.ch3.stacks import FixedCapacityStack


def test_fixed_capacity_stack():
    cap = 10
    stack = FixedCapacityStack(cap=cap)
    assert len(stack) == 0

    sample = "abbreviation"

    for i, c in enumerate(sample):
        if i < cap:
            stack.push(c)
            assert len(stack) == i + 1
        else:
            with pytest.raises(IndexError):
                stack.push(c)

    for i in range(cap):
        c = stack.pop()
        assert c == sample[cap - 1 - i]
