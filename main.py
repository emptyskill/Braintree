import requests,time,user_agent,re,base64,random,re,base64,os,sys
from user_agent import *
from colorama import Fore

def main():
    while True:
        # Display menu
        print("\nPayment Gateway Menu:")
        print("1. Braintree 1")
        print("2. Braintree 2")
        print("3. Stripe Auth")
        print("3. Bin Generator")
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
