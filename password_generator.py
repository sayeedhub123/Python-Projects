#how to generate password

import random
import string

def gene_pass(length: int=10):
    alpha = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alpha) for i in range(length))
    return password


password = gene_pass()
print(f"Generated Password : {password}")










#THANKS FOR WATCHING...................
