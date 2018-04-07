regex_pattern = r""	# Do not delete 'r'.
import re
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')

import re
print("\n".join(re.split(regex_pattern, input())))
