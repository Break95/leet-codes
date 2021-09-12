#!/usr/bin/env python3
# Slow LRU no double linked list.

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.entries = 0
        self.key_usage = []
        self.mem = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mem:
            self.key_usage.remove(key)
            self.key_usage.append(key)
            return self.mem[key]
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.mem:
            if self.entries == self.capacity:
                self.evict()
                self.mem[key] = value
                self.key_usage.append(key)
            else:
                self.entries += 1
                self.mem[key] = value
                self.key_usage.append(key)
        else:
            self.key_usage.remove(key)
            self.key_usage.append(key)
            self.mem[key] = value

    def evict(self):
        del self.mem[self.key_usage.pop(0)]
