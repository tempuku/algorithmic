class Robot:

    def __init__(self, dot: tuple):
        self.location = dot
        self._path = [self.location, ]

    def move(self, arrow: str) -> tuple:
        for direction in arrow:
            location_list = list(self.location)
            if direction == 'N':
                if location_list[1] != 100:
                    location_list[1] += 1
            elif direction == 'S':
                if location_list[1] != 0:
                    location_list[1] -= 1
            elif direction == 'E':
                if location_list[0] != 100:
                    location_list[0] += 1
            elif direction == 'W':
                if location_list[1] != 0:
                    location_list[0] -= 1
            self.location = tuple(location_list)
            self._path.append(self.location)
        if not arrow:
            self._path.append(self.location)
        return self.location

    def path(self) -> list:
        return self._path


if __name__ == '__main__':
    r = Robot((0, 0))
    print(r.move('NENW'))
    print(*r.path())

