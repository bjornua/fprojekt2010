# -*- coding: utf-8 -*-
import Queue

__all__ = ["Pool"]

"""
Thread-safe simple connection pool
"""
class Pool(object):
    def __init__(self, creator, maxsize):
        self.creator = creator
        self.queue = Queue.Queue(maxsize=maxsize)
    
    def take(self):
        try:
            return self.queue.get(block=False)
        except Queue.Empty:
            return self.creator()
    
    def give(self, item):
        try:
            self.queue.put(item=item, block=False)
        except Queue.Full:
            del item
