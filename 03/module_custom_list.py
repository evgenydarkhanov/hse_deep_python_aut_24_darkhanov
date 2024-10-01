class CustomList(list):

    def __add__(self, other):
        if isinstance(other, int):
            result = [self[i] + other for i in range(len(self))]
            return CustomList(result)

        if isinstance(other, list):
            minimal = min(len(self), len(other))
            result = [self[i] + other[i] for i in range(minimal)]
            if len(self) < len(other):
                for j in range(len(self), len(other)):
                    result.append(other[j])
            else:
                for j in range(len(other), len(self)):
                    result.append(self[j])

            return CustomList(result)

        raise TypeError(f"{other=} must be 'int'/'list'/'CustomList'")

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int):
            result = [self[i] - other for i in range(len(self))]
            return CustomList(result)

        if isinstance(other, list):
            minimal = min(len(self), len(other))
            result = [self[i] - other[i] for i in range(minimal)]
            if len(self) < len(other):
                for j in range(len(self), len(other)):
                    result.append(-other[j])
            else:
                for j in range(len(other), len(self)):
                    result.append(self[j])

            return CustomList(result)

        raise TypeError(f"{other=} must be 'int'/'list'/'CustomList'")

    def __rsub__(self, other):
        if isinstance(other, int):
            result = [other - self[i] for i in range(len(self))]
            return CustomList(result)

        if isinstance(other, list):
            minimal = min(len(self), len(other))
            result = [other[i] - self[i] for i in range(minimal)]
            if len(self) < len(other):
                for j in range(len(self), len(other)):
                    result.append(other[j])
            else:
                for j in range(len(other), len(self)):
                    result.append(-self[j])

            return CustomList(result)

        raise TypeError(f"{other=} must be 'int'/'list'/'CustomList'")

    def __eq__(self, other):
        if isinstance(other, CustomList):
            return sum(self) == sum(other)
        raise TypeError(f"{other=} must be 'CustomList'")

    def __ne__(self, other):
        if isinstance(other, CustomList):
            return sum(self) != sum(other)
        raise TypeError(f"{other=} must be 'CustomList'")

    def __gt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) > sum(other)
        raise TypeError(f"{other=} must be 'CustomList'")

    def __ge__(self, other):
        if isinstance(other, CustomList):
            return sum(self) >= sum(other)
        raise TypeError(f"{other=} must be 'CustomList'")

    def __lt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) < sum(other)
        raise TypeError(f"{other=} must be 'CustomList'")

    def __le__(self, other):
        if isinstance(other, CustomList):
            return sum(self) <= sum(other)
        raise TypeError(f"{other=} must be 'CustomList'")

    def __str__(self):
        out = f"[{', '.join(map(str, self))}], {sum(self)}"
        return out
