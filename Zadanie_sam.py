# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import sys


def printartist(owner, **track_info):
    print(f"Owner Name: {owner}")
    for track_info, name in track_info.items():
        print(f"{track_info}: {name}")


if __name__ == "__main__":
    printartist("Bach", title="The Passion according to Matthew", year="1727")

