from celery import Celery

app = Celery(
    "src.main",
    broker="redis://:password@localhost:6379/0",
    backend="redis://:password@localhost:6379/0",
)


@app.task
def slow_fibonacci(n):
    if n in {0, 1}:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


if __name__ == "__main__":
    while True:
        n = int(input("Calc the Fibonacci of (input int): "))
        result = slow_fibonacci.delay(n)
        print(result.get())  # timeout=2
