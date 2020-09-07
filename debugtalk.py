# coding=utf-8
from configs.on_off import skips


def is_skip(case):
    if skips[case] == 1:
        return True
    else:
        return False
