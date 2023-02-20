class Debt:
    def __init__(self):
        self.debt = 10000 # here i must put link with database

    def counter(self):
        self.debt += 10000
        return self.debt

    def counter_with_changes(self, new_amount):
        self.debt += new_amount
        return self.debt


def main():
    debt = Debt()
    print(debt.counter_with_changes(5000))
    print(debt.counter())


if __name__ == '__main__':
    main()
