class ListQueryResult(object):
    """This is duck class behaving like a Django QuerySet"""

    class query:
        select_related = True
        where = False

    def __init__(self, value=None):
        if value is None:
            self.value = []
        else:
            self.value = value

    def count(self):
        return len(self)

    def iterator(self):
        for v in self.value:
            yield v

    def _clone(self):
        return type(self)(list(self.value))

    def __len__(self):
        return len(self.value)

    def __getitem__(self, s):
        if isinstance(s, slice):
            return self.value.__getitem__(s)
        else:
            return self.value[s]
