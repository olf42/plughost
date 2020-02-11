#!/usr/bin/env python3

from plughost.signal import name_pre_modification


@name_pre_modification.connect
def print_name_pre_mod(name):
    raise ValueError("lol!")
    return f"{name}_Obst"
