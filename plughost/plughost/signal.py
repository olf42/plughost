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
        responses = []
        for receiver in self.receivers:
            try:
                response = receiver(*args, **kwargs)
            except Exception as err:
                responses.append((receiver.__name__, err))
            else:
                responses.append((receiver.__name__, response))
        return responses

name_pre_modification = Signal()
name_post_modification = Signal()
