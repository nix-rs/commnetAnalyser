from pathlib import Path
import platform
from colorama import Fore, init
import argparse

#- Exclude node_modules folder
#- Accept the Args from terminal
#- Able to parse other language files



# Underlying OS name
sys = platform.system()
init(autoreset=True)

# Commnet lliteral of languages
js = 'js'
ts = 'ts'
py = 'py'



# Here we will take the commented line and then print the usable line
def toPrint(s: str, file: str, line: str):

    # Make sure we get Comment line with some text on it, otherwise return
    if len(s.strip()) <= 2:
        return

    # If there is space between '//' and character i.e. '// XXX'
    if s[2] == " ":
        s = s[3:].strip()

        if s[0:3].lower() == 'fix':
            #print(Back.YELLOW + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.YELLOW + f'({file}) [{line}] {s}')
        elif s[0:7].lower() == 'current':
            #print(Back.GREEN + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.GREEN + f'({file}) [{line}] {s}')
        elif s[0:5].lower() == 'error':
            #print(Back.RED + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.RED + f'({file}) [{line}] {s}')
        elif s[0:4].lower() == 'info':
            #print(Back.BLUE + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.BLUE + f'({file}) [{line}] {s}')
        elif s[0:7].lower() == 'problem':
            #print(Back.BLUE + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.MAGENTA + f'({file}) [{line}] {s}')
    else:
        s = s[2:].strip()

        if s[0:3].lower() == 'fix':
            #print(Back.YELLOW + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.YELLOW + f'({file}) [{line}] {s}')
        elif s[0:7].lower() == 'current':
            #print(Back.GREEN + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.GREEN + f'({file}) [{line}] {s}')
        elif s[0:5].lower() == 'error':
            #print(Back.RED + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.RED + f'({file}) [{line}] {s}')
        elif s[0:4].lower() == 'info':
            #print(Back.BLUE + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.BLUE + f'({file}) [{line}] {s}')
        elif s[0:7].lower() == 'problem':
            #print(Back.BLUE + Fore.WHITE + f'({file}) [{line}] {s}')
            print(Fore.MAGENTA + f'({file}) [{line}] {s}')


# File
for (p, q) in enumerate(Path('.').rglob('*.ts')):
    #print("--->" +q.name)
    if q.is_dir() and q.name.startswith('node_modules'):
        continue
    
    text = q.read_text()

    # Here we are only deciding this is comment or not '//'
    # Line
    for (i, j) in enumerate(text.splitlines()):
        #print(f'~{i}--{j}')
        # Character
        for (k,l) in enumerate(j):
            if l != '/':
                break
            # FIX: this break is unnatural
            else: 
                #print(j)
                toPrint(j, str(q), str(i + 1) )
                break
