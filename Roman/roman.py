regex_pattern = r""	# Do not delete 'r'.
from roman import fromRoman

try:
    if 0<fromRoman(input())<4000:
        print(True)
    else:
        print(False)
except:
    print(False)
    
import re
print(str(bool(re.match(regex_pattern, input()))))
