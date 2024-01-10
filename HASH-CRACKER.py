import os
from os import system
try:
        import webbrowser as web
except ImportError: os.system("python2 -m pip install webbrowser")
try:
        import hashlib
except ImportError: os.system("python2 -m pip install hashlib")
try:
        import datetime
except ImportError:system("python2 -m pip install datetime")
from time import sleep
import time as t
try:
        import pyfiglet
except ImportError:system("python2 -m pip install pyfiglet")
try:
        from tqdm import tqdm
except ImportError:os.system("python2 -m pip install tqdm")
import sys
import subprocess
try:
        from colorama import *
except ImportError:os.system("python2 -m pip install colorama")
try:
        import platform
except ImportError:
        os.system("python2 -m pip install platform")

class color:
        end      = '\033[0m'
        red      = '\033[91m'
        green    = '\033[92m'
        white    = '\033[97m'
        dgreen   = '\033[32m'
        yellow   = '\033[93m'
        back     = '\033[7;91m'
        run      = '\033[97m[~]\033[0m'
        que      = '\033[94m[?]\033[0m'
        bad      = '\033[91m[-]\033[0m'
        info     = '\033[93m[!]\033[0m'
        good     = '\033[92m[+]\033[0m'
POROMT = Fore.RED+"/root"+Fore.BLUE+"@kali"+Fore.RED+"~#"+Fore.RESET+""
run_script = raw_input(color.green+" Do you want the script to run >> [yes/no] ? ")

if run_script == "no" or run_script == "n" or run_script == "No" or run_script == "N":sys.exit()
elif run_script == "yes" or run_script == "y" or run_script == "Yes" or run_script=="Y":
        pass

def clear_page():
        SYSTEM_Name = name = platform.uname()[0]
        if SYSTEM_Name == 'Windows':os.system("cls")
        elif SYSTEM_Name !='Windows':system("clear")
        t.sleep(1); print ('\n')

def Banner_Tool():
        if os.name=="nt":
                try:
                        print Fore.MAGENTA+"_____________________________________________________________________________________"
                        ban = pyfiglet.figlet_format("\tHASH    KILLER");t.sleep(0.1)
                        print color.green+"";print Style.BRIGHT+""
                        print ban ;print color.end+""
                        print Fore.MAGENTA+"_____________________________________________________________________________________"
                except :
                        for error in range(3):
                                print Fore.RED,Style.BRIGHT+"\a[!] Error in Install or update pyfiglet !!! please install pyfiglet and try agin ... "
                        sys.exit()
        elif platform.uname()[0]=="Linux":
                print Fore.RED,Style.BRIGHT+""
                os.system("jp2a --colors 0.jpg")
                print "\n"
        print Fore.MAGENTA+"\t\t_______________________________________"
        print Fore.CYAN+"\t\t << SCRIPT BY BLACK WOLVES TEAM >> "
        print Fore.RED+"\t\t << We Do Not Forget , We Do Not Forgive >> "
        print Fore.YELLOW+"\t\t << Script Cracker Hash >> "
        print Fore.BLUE+"\t\t << Telegram : t.me/BlackWolves_Team >> "
        print Fore.MAGENTA+"\t\t_______________________________________\n"

clear_page()
Banner_Tool()
DATE_TIME = datetime.datetime.now()
print Style.BRIGHT+""
print POROMT+Fore.CYAN+"[time_date]"+Fore.BLUE+">>: "+Fore.RESET+str(DATE_TIME)
Follow_Us = raw_input(POROMT+Fore.CYAN+"[ Do you want to follow us? yes/no ]"+Fore.BLUE+">>: "+Fore.RESET+"")
if Follow_Us == "yes" or Follow_Us == "Yes" or Follow_Us == "y" or Follow_Us == "Y" or Follow_Us == "YES":
        if os.name=="nt":
                os.system("open https://t.me/BlackWolves_Team")
        elif platform.uname()[0]=="Linux":
                system("xdg-open https://t.me/BlackWolves_Team")
if Follow_Us == "no" or Follow_Us == "No" or Follow_Us == "n" or Follow_Us == "N" or Follow_Us == "NO":
        pass
GET_HASH = raw_input(POROMT+Fore.CYAN+"[Enter Hash]"+Fore.BLUE+">>: "+Fore.RESET+"")
GET_WORD_LIST = raw_input(POROMT+Fore.CYAN+"[Enter Word-List]"+Fore.BLUE+">>: "+Fore.RESET+"")
t.sleep(2)
def TYPE_hash():
        if len(GET_HASH) == 32:
                TYPE_HASH = POROMT+Fore.CYAN+"[TYPE HASH]"+Fore.BLUE+":>> "+Fore.RESET+"MD5"
                print TYPE_HASH
        if len(GET_HASH) == 40:
                TYPE_HASH = POROMT+Fore.CYAN+"[TYPE HASH]"+Fore.BLUE+":>> "+Fore.RESET+"SHA1"
                print TYPE_HASH
        if len(GET_HASH) == 64:
                TYPE_HASH = POROMT+Fore.CYAN+"[TYPE HASH]"+Fore.BLUE+":>> "+Fore.RESET+"SHA256"
                print TYPE_HASH
        if len(GET_HASH) == 96:
                TYPE_HASH = POROMT+Fore.CYAN+"[TYPE HASH]"+Fore.BLUE+":>> "+Fore.RESET+"SHA384"
                print TYPE_HASH
        if len(GET_HASH) == 128:
                TYPE_HASH = POROMT+Fore.CYAN+"[TYPE HASH]"+Fore.BLUE+":>> "+Fore.RESET+"SHA512"
                print TYPE_HASH
TYPE_hash()
t.sleep(2)
TYPE_HASH = raw_input(POROMT+Fore.CYAN+"[Enter Type Hash]"+Fore.BLUE+">>: "+Fore.RESET+"")
TYPE_HASH = TYPE_HASH.lower()
def crack_hash():
        print Style.BRIGHT+""
        Wordlist = open(GET_WORD_LIST,"r").readlines()
        for password in Wordlist:
                password = password.strip()
                if TYPE_HASH == "md5" or TYPE_HASH == "MD5":
                        hash_cracked = hashlib.md5(password).hexdigest()
                elif TYPE_HASH == "sha1" or TYPE_HASH == "SHA1":
                        hash_cracked = hashlib.sha1(password).hexdigest()
                elif TYPE_HASH == "sha224" or TYPE_HASH == "SHA224":
                        hash_cracked = hashlib.sha224(password).hexdigest()
                elif TYPE_HASH == "sha256" or TYPE_HASH == "SHA256":
                        hash_cracked = hashlib.sha256(password).hexdigest()
                elif TYPE_HASH == "sha384" or TYPE_HASH == "SHA384":
                        hash_cracked = hashlib.sha384(password).hexdigest()
                elif TYPE_HASH == "sha512" or TYPE_HASH == "SHA512":
                        hash_cracked = hashlib.sha512(password).hexdigest()
                if GET_HASH == hash_cracked:
                        print color.green+"+ [YES]"+Fore.BLUE,Style.BRIGHT+">> "+Fore.CYAN+"[HASH CRACKED] : "+Fore.GREEN+"{Password Found}"+Fore.BLUE+"->> : ",color.dgreen+password,"\r",
                        print "\n\n\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a" ; break
                else:
                        print color.red+"- [NOT]"+Fore.BLUE,Style.BRIGHT+">> "+Fore.CYAN+"[Password Not Found]"+Fore.BLUE+"->> : ",color.red+password,"\r",
crack_hash()
