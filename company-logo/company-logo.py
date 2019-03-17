#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

[print(*c) for c in OrderedCounter(sorted(s)).most_common(3)]
