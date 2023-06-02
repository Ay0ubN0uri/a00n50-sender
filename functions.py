from colorama import Style, init, Fore
import re
from datetime import datetime


def filter_emails(mail_list):
    valid_emails = []
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    for email in mail_list:
        if re.fullmatch(pattern, email.strip()):
            valid_emails.append(email.strip())

    return valid_emails


def render_error(msg):
    print(
        f'{Fore.RED}{Style.BRIGHT}[-] \033[4m{datetime.now().strftime("%I:%M:%S %p")}\033[0m{Fore.RED}{Style.BRIGHT} [-] {msg}{Style.RESET_ALL}')


def render_success(msg):
    print(
        f'{Fore.GREEN}{Style.BRIGHT}[+] \033[4m{datetime.now().strftime("%I:%M:%S %p")}\033[0m{Fore.GREEN}{Style.BRIGHT} [+] {msg}{Style.RESET_ALL}')


def banner():
    init(autoreset=True)
    custom_red_color = (236, 1, 1)
    custom_blue_color = (5, 161, 247)
    custom_green_color = (71, 212, 185)
    custom_purple_color = (128, 0, 128)

    color1 = f"\x1b[38;2;{custom_red_color[0]};{custom_red_color[1]};{custom_red_color[2]}m"
    color2 = f"\x1b[38;2;{custom_blue_color[0]};{custom_blue_color[1]};{custom_blue_color[2]}m"
    color3 = f"\x1b[38;2;{custom_green_color[0]};{custom_green_color[1]};{custom_green_color[2]}m"
    color4 = f"\x1b[38;2;{custom_purple_color[0]};{custom_purple_color[1]};{custom_purple_color[2]}m"
    print(f'/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_')
    print(f'{color1}               AAA            {Style.RESET_ALL}{color2}     000000000          000000000     {Style.RESET_ALL}{color1}NNNNNNNN        NNNNNNNN{Style.RESET_ALL}{color3}555555555555555555      000000000     ')
    print(f'{color1}              A:::A           {Style.RESET_ALL}{color2}   00:::::::::00      00:::::::::00   {Style.RESET_ALL}{color1}N:::::::N       N::::::N{Style.RESET_ALL}{color3}5::::::::::::::::5    00:::::::::00   ')
    print(f'{color1}             A:::::A          {Style.RESET_ALL}{color2} 00:::::::::::::00  00:::::::::::::00 {Style.RESET_ALL}{color1}N::::::::N      N::::::N{Style.RESET_ALL}{color3}5::::::::::::::::5  00:::::::::::::00 ')
    print(f'{color1}            A:::::::A         {Style.RESET_ALL}{color2}0:::::::000:::::::00:::::::000:::::::0{Style.RESET_ALL}{color1}N:::::::::N     N::::::N{Style.RESET_ALL}{color3}5:::::555555555555 0:::::::000:::::::0')
    print(f'{color1}           A:::::::::A        {Style.RESET_ALL}{color2}0::::::0   0::::::00::::::0   0::::::0{Style.RESET_ALL}{color1}N::::::::::N    N::::::N{Style.RESET_ALL}{color3}5:::::5            0::::::0   0::::::0')
    print(f'{color1}          A:::::A:::::A       {Style.RESET_ALL}{color2}0:::::0     0:::::00:::::0     0:::::0{Style.RESET_ALL}{color1}N:::::::::::N   N::::::N{Style.RESET_ALL}{color3}5:::::5            0:::::0     0:::::0')
    print(f'{color1}         A:::::A A:::::A      {Style.RESET_ALL}{color2}0:::::0     0:::::00:::::0     0:::::0{Style.RESET_ALL}{color1}N:::::::N::::N  N::::::N{Style.RESET_ALL}{color3}5:::::5555555555   0:::::0     0:::::0')
    print(f'{color1}        A:::::A   A:::::A     {Style.RESET_ALL}{color2}0:::::0 000 0:::::00:::::0 000 0:::::0{Style.RESET_ALL}{color1}N::::::N N::::N N::::::N{Style.RESET_ALL}{color3}5:::::::::::::::5  0:::::0 000 0:::::0')
    print(f'{color1}       A:::::A     A:::::A    {Style.RESET_ALL}{color2}0:::::0 000 0:::::00:::::0 000 0:::::0{Style.RESET_ALL}{color1}N::::::N  N::::N:::::::N{Style.RESET_ALL}{color3}555555555555:::::5 0:::::0 000 0:::::0')
    print(f'{color1}      A:::::AAAAAAAAA:::::A   {Style.RESET_ALL}{color2}0:::::0     0:::::00:::::0     0:::::0{Style.RESET_ALL}{color1}N::::::N   N:::::::::::N{Style.RESET_ALL}{color3}            5:::::50:::::0     0:::::0')
    print(f'{color1}     A:::::::::::::::::::::A  {Style.RESET_ALL}{color2}0:::::0     0:::::00:::::0     0:::::0{Style.RESET_ALL}{color1}N::::::N    N::::::::::N{Style.RESET_ALL}{color3}            5:::::50:::::0     0:::::0')
    print(f'{color1}    A:::::AAAAAAAAAAAAA:::::A {Style.RESET_ALL}{color2}0::::::0   0::::::00::::::0   0::::::0{Style.RESET_ALL}{color1}N::::::N     N:::::::::N{Style.RESET_ALL}{color3}5555555     5:::::50::::::0   0::::::0')
    print(f'{color1}   A:::::A             A:::::A{Style.RESET_ALL}{color2}0:::::::000:::::::00:::::::000:::::::0{Style.RESET_ALL}{color1}N::::::N      N::::::::N{Style.RESET_ALL}{color3}5::::::55555::::::50:::::::000:::::::0')
    print(f'{color1}  A:::::A               A:::::A{Style.RESET_ALL}{color2}00:::::::::::::00  00:::::::::::::00 {Style.RESET_ALL}{color1}N::::::N       N:::::::N{Style.RESET_ALL}{color3} 55:::::::::::::55  00:::::::::::::00 ')
    print(f'{color1} A:::::A                 A:::::A {Style.RESET_ALL}{color2}00:::::::::00      00:::::::::00   {Style.RESET_ALL}{color1}N::::::N        N::::::N{Style.RESET_ALL}{color3}   55:::::::::55      00:::::::::00   ')
    print(f'{color1}AAAAAAA                   AAAAAAA  {Style.RESET_ALL}{color2}000000000          000000000     {Style.RESET_ALL}{color1}NNNNNNNN         NNNNNNN{Style.RESET_ALL}{color3}     555555555          000000000     ')
    print(f"{color4}                                                      o                               o              ")
    print(f"{color4}                                                  o  O                               O               ")
    print(f"{color4}                                                     o                               o               ")
    print(f"{color4}                                                     O                               o               ")
    print(f"{color4}                            .oOo. `oOOoOO. .oOoO' O  o        .oOo  .oOo. 'OoOo. .oOoO  .oOo. `OoOo. ")
    print(f"{color4}                            OooO'  O  o  o O   o  o  O        `Ooo. OooO'  o   O o   O  OooO'  o     ")
    print(f"{color4}                            O      o  O  O o   O  O  o            O O      O   o O   o  O      O     ")
    print(f"{color4}                            `OoO'  O  o  o `OoO'o o' Oo       `OoO' `OoO'  o   O `OoO'o `OoO'  o     ")
    print(f'/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_/~~~~~~~\_\n\n')
