class User:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def revert_friends(user):
        user.friends = []
        return user

    def __repr__(self):
        return f'{self.name}'


user = User('main')
friend = User('1')
friend.friends = [User('1.1'), User('1.2'), User('1.3')]
user.friends = [friend]


class Maybe:
    def __init__(self, value):
        self.value = value

    @classmethod
    def unit(cls, value):
        return cls(value)

    def bind(self, f):
        if self.value is None:
            return self

        result = f(self.value)
        if isinstance(result, Maybe):
            return result
        return Maybe(result)

    def __getattr__(self, name):
        field = hasattr(self.value, name) and getattr(self.value, name) or None
        if not callable(field):
            return self.bind(lambda _: field)
        return lambda *args, **kwargs: self.bind(lambda _: field(*args, **kwargs))


def first_value(values):
    if len(values) > 0:
        return values[0]
    return None


friends = (
    Maybe.unit(user).
    friends.
    bind(first_value).
    friends.
    value
)
print(friends)
