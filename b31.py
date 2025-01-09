import requests
import time
from datetime import datetime, timedelta
import os
import sys
from itertools import cycle

STATUS_URL = "https://raw.githubusercontent.com/emptyskill/braintree1/refs/heads/main/server.txt"
USER_LIST_URL = "https://raw.githubusercontent.com/emptyskill/braintree1/refs/heads/main/users.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/emptyskill/checker/refs/heads/main/stripe.py"
IP_CHECK_URL = "https://www.studynotesaba.com/"

RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

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

def clear_terminal():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def fetch_url_content(url, description="resource"):
    """Fetch content from a given URL with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"{RED}[ERROR]{RESET} Unable to fetch {description}: {e}")
        return None

def check_ip_region():
    print(f"{CYAN}[INFO]{RESET} Initiating IP and region verification...\n")

    try:
        print(f"{CYAN}[INFO]{RESET} Fetching your public IP address...")
        ip_response = requests.get("https://api.ipify.org?format=json", timeout=10)
        ip_response.raise_for_status()
        ip_data = ip_response.json()
        user_ip = ip_data.get("ip", "Unavailable")
        print(f"{GREEN}[SUCCESS]{RESET} Your public IP: {WHITE}{user_ip}{RESET}\n")

        print(f"{CYAN}[INFO]{RESET} Verifying server availability in your region...")
        region_check = requests.get(IP_CHECK_URL, timeout=10)
        region_check.raise_for_status()

        if region_check.status_code == 200:
            print(f"{GREEN}[SUCCESS]{RESET} Server is operational in your region.\n")
            print(f"{CYAN}[INFO]{RESET} You can proceed with your IP: {WHITE}{user_ip}{RESET}.\n")
            return True
        else:
            print(f"{RED}[WARNING]{RESET} Server might be facing issues in your region. Please try again later.\n")
            return False

    except requests.exceptions.Timeout:
        print(f"{RED}[ERROR]{RESET} Request timed out. Please check your internet connection and try again.\n")
        return False

    except requests.exceptions.ConnectionError:
        print(f"{RED}[ERROR]{RESET} Unable to connect to the server. Please ensure you are online.\n")
        return False

    except requests.exceptions.HTTPError as http_err:
        print(f"{RED}[ERROR]{RESET} HTTP error occurred: {http_err}\n")
        return False

    except requests.exceptions.RequestException as req_err:
        print(f"{RED}[ERROR]{RESET} An unexpected error occurred: {req_err}\n")
        return False

    except Exception as e:
        print(f"{RED}[ERROR]{RESET} An unforeseen error occurred: {e}\n")
        return False

def is_status_on():
    print(f"{CYAN}[INFO]{RESET} Initiating system status check...")

    try:
        print(f"{CYAN}[INFO]{RESET} Retrieving status information from the server...")
        status = fetch_url_content(STATUS_URL, "system status")

        if status is None:
            print(f"{RED}[ERROR]{RESET} Unable to retrieve status. The server might be unreachable or the status file is missing.")
            return None

        status_upper = status.upper()
        if status_upper == "ON":
            print(f"{GREEN}[SUCCESS]{RESET} The system is currently {WHITE}ON{RESET}.")
            return True
        elif status_upper == "OFF":
            print(f"{YELLOW}[WARNING]{RESET} The system is currently {WHITE}OFF{RESET}.")
            return False
        else:
            print(f"{RED}[ERROR]{RESET} Unexpected status value received: {WHITE}{status}{RESET}. Please verify the status file.")
            return None

    except Exception as e:
        print(f"{RED}[ERROR]{RESET} An error occurred while checking the system status: {e}")
        return None

def is_user_registered(user_id):
    print(f"{CYAN}[INFO]{RESET} Initiating user validation process...\n")

    try:
        print(f"{CYAN}[INFO]{RESET} Retrieving registered user list...")
        user_data = fetch_url_content(USER_LIST_URL, "registered user list")
        if not user_data:
            return False, f"{RED}[ERROR]{RESET} Unable to fetch user data. Please try again later."

        for line in user_data.splitlines():
            try:
                registered_id, expiration_date, expiration_time = [item.strip() for item in line.split(",")]

                if str(user_id) == registered_id:
                    expiration_datetime = datetime.strptime(f"{expiration_date} {expiration_time}", "%d/%m/%y %I:%M %p")
                    now = datetime.now()
                    time_left = expiration_datetime - now

                    print(f"{CYAN}[DEBUG]{RESET} Current datetime: {WHITE}{now.strftime('%d/%m/%y %I:%M %p')}{RESET}")
                    print(f"{CYAN}[DEBUG]{RESET} Expiration datetime: {WHITE}{expiration_datetime.strftime('%d/%m/%y %I:%M %p')}{RESET}")
                    print(f"{CYAN}[DEBUG]{RESET} Time left: {WHITE}{time_left}{RESET}")

                    if time_left > timedelta(0):
                        days = time_left.days
                        hours, remainder = divmod(time_left.seconds, 3600)
                        minutes = remainder // 60
                        return True, (f"{GREEN}[SUCCESS]{RESET} Subscription valid for "
                                      f"{BOLD}{CYAN}{days} days{RESET}, {BOLD}{CYAN}{hours} hours{RESET}, "
                                      f"and {BOLD}{CYAN}{minutes} minutes{RESET}.")
                    else:
                        return False, (f"{RED}[ERROR]{RESET} Subscription expired on "
                                       f"{BOLD}{YELLOW}{expiration_datetime.strftime('%d/%m/%y %I:%M %p')}{RESET}. "
                                       f"Contact admin to renew.")

            except ValueError as parse_error:
                print(f"{RED}[ERROR]{RESET} Failed to parse line: {YELLOW}{line}{RESET}. Error: {RED}{parse_error}{RESET}")
                continue

        return False, (f"{RED}[ERROR]{RESET} User ID not found. Please contact admin to register.\n"
                       f"{MAGENTA}TIP{RESET}: Ensure you have entered a valid user ID.")

    except Exception as e:
        return False, f"{RED}[ERROR]{RESET} An unexpected error occurred: {e}"

def fetch_and_execute_script():
    print(f"{CYAN}[INFO]{RESET} Attempting to retrieve the main script from the server...\n")

    try:
        script_content = fetch_url_content(SCRIPT_URL, "main script")
        if not script_content:
            print(f"{RED}[ERROR]{RESET} Failed to fetch the main script. Retrying in 10 seconds...\n")
            return False

        print(f"{GREEN}[SUCCESS]{RESET} Main script retrieved successfully. Preparing to execute...\n")

        loading_animation = cycle([
            f"{MAGENTA}●{RESET}",
            f"{CYAN}●{RESET}",
            f"{GREEN}●{RESET}",
            f"{YELLOW}●{RESET}",
        ])
        print(f"{CYAN}[INFO]{RESET} Initializing script execution:\n")
        for _ in range(6):
            sys.stdout.write(f"\r{next(loading_animation)} {RESET} Loading...")
            sys.stdout.flush()
            time.sleep(0.3)
        print("\n")

        try:
            exec(script_content, globals())
            print(f"{GREEN}[SUCCESS]{RESET} Script executed successfully!\n")
            return True
        except Exception as execution_error:
            print(f"{RED}[ERROR]{RESET} Script execution failed: {execution_error}. Retrying in 10 seconds...\n")
            return False

    except Exception as fetch_error:
        print(f"{RED}[ERROR]{RESET} An unexpected error occurred while fetching the script: {fetch_error}\n")
        return False

def print_header():
    clear_terminal()

    loading_animation = cycle([
        f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}", f"{MAGENTA}★{RESET}", f"{CYAN}★{RESET}", f"{GREEN}★{RESET}", f"{YELLOW}★{RESET}", f"{RED}★{RESET}"
    ])
    print("\n")
    for _ in range(30):
        sys.stdout.write(f"\r{next(loading_animation)} {RESET} Loading Header...")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")
    clear_terminal()
    print(LOGO)

    print(f"{CYAN}{BOLD}Welcome to the {UNDERLINE}Secure Script Executor{RESET}{CYAN}!{RESET}\n")
    print(f"{YELLOW}★ {BOLD}Your one-stop solution for safe and reliable script execution.{RESET}\n")
    print(f"{YELLOW}{UNDERLINE}Ensure you read all prompts carefully and follow instructions for optimal use.{RESET}\n")

    print(f"{GREEN}{'-'*50}{RESET}\n")

def sleep_accurately(seconds):
    if seconds <= 0:
        raise ValueError("The sleep duration must be a positive value.")
    
    start_time = time.perf_counter()
    end_time = start_time + seconds

    while time.perf_counter() < end_time:
        time.sleep(0.1)

    elapsed_time = time.perf_counter() - start_time
    return elapsed_time

def main():
    print_header()

    user_id = input(f"{CYAN}🔑 Enter your registered Telegram UserID: {RESET}").strip()

    while True:
        ip_status = check_ip_region()
        if not ip_status:
            print(f"{RED}[ERROR]{RESET} Your region is unable to access the server. Retrying in 30 seconds...\n")
            sleep_accurately(30)
            continue

        status = is_status_on()
        if status is None:
            print(f"{RED}[ERROR]{RESET} Unable to determine system status. Retrying in 10 seconds...\n")
            sleep_accurately(10)
            continue
        if not status:
            print(f"{YELLOW}[MAINTENANCE]{RESET} The system is currently under maintenance. Retrying in 30 seconds...\n")
            sleep_accurately(30)
            continue

        print(f"{GREEN}[SUCCESS]{RESET} System is online.\n")

        is_registered, message = is_user_registered(user_id)
        if not is_registered:
            print(f"{RED}[ERROR]{RESET} {message}. Retrying in 10 seconds...\n")
            sleep_accurately(10)
            continue

        print(f"{GREEN}[SUCCESS]{RESET} User ID verified successfully.\n")

        if fetch_and_execute_script():
            print(f"{GREEN}[INFO]{RESET} Script executed successfully. Waiting 10 seconds before retrying...\n")
            sleep_accurately(10)
        else:
            sleep_accurately(10)

if __name__ == "__main__":
    main()
