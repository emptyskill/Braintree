import requests,time,user_agent,re,base64,random,re,base64,os,sys
from user_agent import *
from colorama import Fore
#---------[COLORS]--------#
Z =  '\033[91m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
LIME = '\033[38;5;10m'
W=Fore.WHITE
L=Fore.BLUE
#-------[CLEAR]--------#
def clear():
    os.system('clear')
#----------LOGO-------------#
logo = ("""
\033[38;2;255;69;0m                       __             __   _ ____
  ___  ____ ___  ____  / /___  _______/ /__(_) / /
 / _ \/ __ `__ \/ __ \/ __/ / / / ___/ //_/ / / / 
/  __/ / / / / / /_/ / /_/ /_/ (__  ) ,< / / / /  
\___/_/ /_/ /_/ .___/\__/\__, /____/_/|_/_/_/_/   
             /_/        /____/             \033[1;93m
\x1b[1;95m┏───────────────────────────────────────────────┓
\x1b[1;94m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘈𝘜𝘛𝘏𝘖𝘙     \x1b[1;97m: \033[38;2;72;209;204memptyskill
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘠𝘗𝘌       \x1b[1;97m: \033[38;2;255;69;0mPAID🔥
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘎𝘐𝘛𝘏𝘜𝘉     \x1b[1;97m: \033[38;2;147;112;219memptyskill
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘖𝘖𝘓       \x1b[1;97m: \033[38;2;0;206;209mPH CHECKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘝𝘌𝘙𝘚𝘐𝘖𝘕    \x1b[1;97m: \033[38;2;255;105;180m1.0
\x1b[1;91m \x1b[1;46m\033[1;91m ✅ NOT JUST A BRAINTREE CHECKER\033[;0m\033[1;91m\033[1;92m
\x1b[1;95m┗───────────────────────────────────────────────┛
""")
def main():
    while True:
        # Display menu
        print("\nPayment Gateway Menu:")
        print("1. Braintree 1")
        print("2. Braintree 2")
        print("3. Stripe Auth")
        print("4. Quit")

        # Get user input
        choice = input("Enter your choice (1-4): ")

        # Handle user input
        if choice == "1":
            os.system("python b31.py")
        elif choice == "2":
            os.system("python b32.py")
        elif choice == "3":
            os.system("python stripe.py")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()