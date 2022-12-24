from base64 import b64encode, b64decode
from hashlib import sha256
from time import time
from urllib.parse import quote_plus, urlencode
from hmac import HMAC
from decouple import config
import requests

def generate_sas_token(uri, key, policy_name, expiry=3600):
     ttl = time() + expiry
     sign_key = "%s\n%d" % ((quote_plus(uri)), int(ttl))
     print(sign_key)
     signature = b64encode(HMAC(b64decode(key), sign_key.encode('utf-8'), sha256).digest())

     rawtoken = {
         'sr' :  uri,
         'sig': signature,
         'se' : str(int(ttl))
     }

     if policy_name is not None:
         rawtoken['skn'] = policy_name

     return 'SharedAccessSignature ' + urlencode(rawtoken)

def main():
    uri = config("DPS_URI")
    key = config("DPS_DEVICE_KEY")
    expiry = 2592000 #[expiry_in_seconds]
    policy='provisioningserviceowner'
    #policy= 'registration'

    SAS = generate_sas_token(uri, key, policy, expiry)
    print(SAS)
    dps_scopeid = config("DPS_SCOPEID")
    dps_registrationid = config("DPS_REGISTRATIONID")

    api = 'https://global.azure-devices-provisioning.net/{0}/registrations/{1}/register?api-version=2021-06-01'.format(dps_scopeid,dps_registrationid)
    print(api)
    h = {}
    h.update({"Authorization": SAS})
    h.update({"Content-Type":"application/json"})
    h.update({"Content-Encoding": "utf-8"})
    print(h)
    payload = "{{\"registrationid\": \"{0}\"}}".format(dps_registrationid)
    print(payload)

    try:
        r = requests.put(api,headers=h,data=payload)
    except requests.exceptions as e:
        print(e)
    except requests.HTTPError as error:
        print(error)
    finally:
        print("status={0}, reason={1}, content={2}".format(r.status_code, r.reason, r.content))

if __name__ == "__main__":
    main()