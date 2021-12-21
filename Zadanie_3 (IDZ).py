# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


def summ_null(*args):
    if args:
        summa = float(0)
        args = reversed(args)
        for arg in args:
            if arg != 0:
                summa += arg
            else:
                break
        return summa
    else:
        return None


if __name__ == "__main__":
    print("Сумма чисел после последнего нуля:",
          summ_null(1, 1, 2, 2, 3, 3, 0, 0, 1, 0, 5, 5))






