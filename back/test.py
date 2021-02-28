from functools import cached_property


class aaa:

    a = 3
    b = 4

    @cached_property
    def d(self):
        return self.a+self.b

if __name__ == '__main__':
    c = aaa()
    print(c.d)
    print(c.__dict__)