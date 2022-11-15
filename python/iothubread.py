import asyncio
import requests
import base64
import sys
import json

from azure.iot.device.aio import IoTHubDeviceClient

async def main():
    # Fetch the connection string from an environment variable
    if len(sys.argv) == 2:
        requestURL = sys.argv[1]

    # Create instance of the device client using the authentication provider
    response = requests.get(requestURL)
    if response.status_code == 200:
        list = []
        list = response.text.splitlines()
        i = 0
        while i < len(list):
            s = list[i]
            d = json.loads(s)
            print("time = " + d["EnqueuedTimeUtc"])
            print("device = " + d["SystemProperties"]["connectionDeviceId"])
            print("body = {0}".format(base64.b64decode(d["Body"])))
            print("--------------")
            i += 1
    else:
        print("status code = {0}".format(response.status_code))

if __name__ == "__main__":
    asyncio.run(main())