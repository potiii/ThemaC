class Fib:
    def fibonacchi(self, n):
        if n <= 2:
            return 1
        else:
            return self.fibonacchi(n - 2) + self.fibonacchi(n - 1)

    def prints(self, n):
        print(self.fibonacchi(n))


def main():
    fib = Fib()
    fib.prints(20)


if __name__ == '__main__':
    main()
