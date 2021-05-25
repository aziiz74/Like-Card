#
# This Is Free Tool By Mr. Lyrica Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
	import os
	import requests
	import re
	from os import system
	system("title " + "Soud Was Here - @8Y - Soud#5866")
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()
logo = f"""
{Fore.CYAN}         _______   __ 
{Fore.CYAN}   ____ |  _  \ \ / /
{Fore.CYAN}  / __ \ \ V / \ V /
{Fore.CYAN} / / _` |/ _ \  \ /
{Fore.CYAN}| | (_| | |_| | | |
{Fore.CYAN} \ \__,_\_____/ \_/
{Fore.CYAN}  \____/
"""
print(logo)
print(f"{Fore.RED}This Is Free Tool By Mr. Lyrica Alanzi And Not For Sale\n\n{Fore.RESET}{Fore.GREEN}Instagram: @8Y + @_agf\nDiscord: Soud#5866\n")
input("Press Enter To Start\n")
req = requests.get("https://influencer.redeemly.com/influencer/5f7b125e8539127b2e2c617c").text

code = re.compile('{"code":"(.*?)"},').findall(req)[0]

print(f"Like Card Coupon: {Fore.GREEN}{code}\n{Fore.RESET}By {Fore.RED}Mr. Lyrica Alanzi\n")

input("Press Enter To Exit\n")
