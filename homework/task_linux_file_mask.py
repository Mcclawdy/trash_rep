class MaskItem(object):
    def __init__(self, mask=0):
        self.mask = mask

    def is_readable(self):
        return bool(self.mask // 4)

    def is_writable(self):
        return bool((self.mask % 4) // 2)

    def is_executable(self):
        return bool(self.mask % 2)

    def __str__(self):
        r = 'r' if self.is_readable() else '-'
        w = 'w' if self.is_writable() else '-'
        x = 'x' if self.is_executable() else '-'

        return r + w + x

    def __repr__(self):
        return 'MaskItem(0b{0:03b})'.format(self.mask) if self.mask > 0 else 'MaskItem()'


class Mask(object):
    def __init__(self, author, group, other):
        self.author = author
        self.group = group
        self.other = other

    def __str__(self):
        r = str(self.author)
        w = str(self.group)
        x = str(self.other)

        return r + w + x

    def __repr__(self):
        return f'Mask({self.author}, {self.group}, {self.other})'