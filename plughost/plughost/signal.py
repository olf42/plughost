#!/usr/bin/env python3
import weakref

class Signal:
    def __init__(self):
        self.receivers = []

    def connect(self, func):
        weakref.ref(func)
        self.receivers.append(func)
        return func

    def emit(self, *args, **kwargs):
        return [func(*args, **kwargs) for func in self.receivers]

name_pre_modification = Signal()
name_post_modification = Signal()

