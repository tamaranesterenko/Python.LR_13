# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


def sred_garm(*args):
    if args:
        summa = float(0)
        for arg in args:
            summa = summa + (1 // arg)
        n = len(args)
        return n // summa
    else:
        return None


if __name__ == "__main__":
    print("Среднее гармоническое значение:", sred_garm(1, 1, 2, 2, 3, 3))





