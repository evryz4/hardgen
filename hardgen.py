import string
import random
import colorama

chartypes = {
    '1': string.ascii_lowercase,
    '2': string.ascii_uppercase,
    '3': string.digits,
    '4': string.punctuation
}

# CONFIG
def display(code, without_filter=False):
    # OPTIONAL | FILTER THAT RETURNS TRUE IF CODE IS CORRECT
    if (True) or without_filter:
        return f'{code}'
    return False

# REQUIRED
codesamount = 10
charminamount = 8
charmaxamount = 8
chartypesinpass = '1234'

# OPTIONAL
expect = ''
extra_availaible_chars = ''
filename = ''
show_failed_generates = False

availaible_chars = ''.join([chartypes[i] for i in chartypesinpass]) + extra_availaible_chars
for i in expect:
    if expect in availaible_chars:
        availaible_chars.replace(expect, '')

codes = []

for i in range(codesamount):
    code = ''
    for _ in range(random.randint(charminamount, charmaxamount)):
        code += random.choice(availaible_chars)
    while code in codes or not display(code):
        if show_failed_generates:
            print(f'{colorama.Fore.RED} {code in codes and 'already exists' or 'failed filter'} | {display(code, without_filter=True)}{colorama.Fore.WHITE}')
                    
        code = ''
        for _ in range(random.randint(charminamount, charmaxamount)):
            code += random.choice(availaible_chars)
    
    codes.append(code)
    print(f'#{i+1} {' '*(len(str(codesamount))-len(str(i+1)))}| {display(code)}')

if filename:
    with open(filename, mode='w') as file:
        file.write('\n'.join(codes))