# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


def sred_znach(*args):
    if args:
        summa = 0
        for arg in args:
            summa = summa + arg
        n = len(args)
        return summa / n
    else:
        return None


if __name__ == "__main__":
    print("Среднее значение:", sred_znach(1, 1, 2, 5, 1, 0))

    



