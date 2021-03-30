class PearsBasket:

    def __init__(self, pears: int):
        self._pears = pears

    def __floordiv__(self, other) -> list:
        if other <= 0:
            raise Exception
        pb_pears = self._pears // other
        pb_array = [PearsBasket(pb_pears) for i in range(other)]
        pb_2_pears = self._pears % other
        if pb_2_pears:
            pb_array.append(PearsBasket(pb_2_pears))
        return pb_array

    def __mod__(self, other) -> int:
        return self._pears % other

    def __add__(self, other: "PearsBasket") -> "PearsBasket":
        return PearsBasket(self._pears + other._pears)

    def __sub__(self, other) -> int:
        self._pears -= other
        if self._pears < 0:
            self._pears = 0
        return self._pears

    def __str__(self):
        return f"{self._pears}"

    def __repr__(self):
        return f"PearsBasket({self._pears})"


if __name__ == '__main__':
    pb = PearsBasket(17)
    array = pb // 4
    print(array)
    pb_2 = PearsBasket(13)
    pb_3 = pb + pb_2
    print(pb_3)
    print(pb_3 % 7)
    pb - 2
    print([pb])
