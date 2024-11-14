import email.utils
import re

no_of_email = int(input())
email_regex = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'

for _ in range(no_of_email):
    
    name, email_addr = input().split()
    
    if re.match(email_regex, email_addr):
        
        #print(name, email_addr)
        
        parsed_addr = f"{name} {email_addr}"
        name, email = email.utils.parseaddr(parsed_addr)
        print(f"{name} <{email}>")
        