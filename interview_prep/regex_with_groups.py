import re

regex_output = re.search(r'(([a-zA-Z0-9])\2{1,})', input())
#([a-zA-Z0-9]) matches alpha-numeric group,
#\2 matched consecutive character in group two which is nested,
#{1,} matched repetation more than once

if regex_output:
    print(regex_output.group()[0])
else:
    print(-1)
    
#..123456789011121341516171820212223 ==> 1
#hackerrank ==> r
#__commit__ ==> m
#__init__ ==> -1