#!/usr/bin/python3
from abc import ABC, Abstractmethond


class Repository(ABC):
    @abstractmethond
    def add(self, obj):
        pass

    @abstractmethond
    def get(self, obj_id):
        pass

    @abstractmethond
    def update(self, obj_id, data):
        pass

    @abstractmethond
    def delete(self, obj_id):
        pass

    @abstractmethond
    def get_by_attribute(self, attr_name, attr_value):
        pass

class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]
    
    def get_by_attribute(self, attr_name, attr_value):
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
