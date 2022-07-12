class Details:

    def __init__(self, name):
        self.name = name


# Car
class Car(Details):
    SPEED_LIMIT = 40
    __meta__ = {"class_name": "Maruti Car"}

    def __init__(self, name):
        super().__init__(name)

    def get_details(self):
        print(f'Car name: {self.name}')

    class Meta:
        name = 'Maruti'

    @classmethod
    def show_speed(cls):
        print(cls.SPEED_LIMIT)

    @staticmethod
    def print_text():
        print('The quick brown fox jumps over the lazy dog')


def factorial(n):
    if (n == 1):
        return n
    return n * factorial(n - 1)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)

n1.next = n2

print(n1.data)
print(n1.next)
print(n1.next.data)
print(n1.next.next)

print(id(factorial))
