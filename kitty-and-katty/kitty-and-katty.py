#!/bin/python3

import math
import os
import random
import re
import sys

for n in (int(input()) for _ in range(int(input()))):
    print('Kitty' if n==1 or not (n&1) else 'Katty')
