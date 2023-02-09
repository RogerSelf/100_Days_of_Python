import time


def cal_fact(n):
    if n == 1:
        return n
    else:
        return n * cal_fact(n - 1)


def cal_fact2(n):
    if n == 1:
        return n
    else:
        result = 1
        for i in range(2, n + 1):
            result = result * i
        return result


start = time.time()

cal_fact(900)

end = time.time()

time_to_process = end - start

print("\n" + str(time_to_process))