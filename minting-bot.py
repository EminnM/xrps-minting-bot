import json
import requests
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import Memo
from xrpl.constants import CryptoAlgorithm
from datetime import datetime
import pwinput
from xrpl.transaction import submit_and_wait
from xrpl.models.requests import LedgerCurrent
from xrpl.models.requests.account_info import AccountInfo

ascii =r'''

,--.   ,--.,------. ,------.  ,---.      ,--.   ,--.,--.,--.  ,--.,--------.,------.,------.
 \  `.'  / |  .--. '|  .--. ''   .-'     |   `.'   ||  ||  ,'.|  |'--.  .--'|  .---'|  .--. '
  .'    \  |  '--'.'|  '--' |`.  `-.     |  |'.'|  ||  ||  |' '  |   |  |   |  `--, |  '--'.'
 /  .'.  \ |  |\  \ |  | --' .-'    |    |  |   |  ||  ||  | `   |   |  |   |  `---.|  |\  \
'--'   '--'`--' '--'`--'     `-----'     `--'   `--'`--'`--'  `--'   `--'   `------'`--' '--'

'''

print(ascii)
#to get your private key https://secret-numbers-to-family-seed.xumm.dev/ enter your xaman wallet numbers here to get your secret key, not affiliated, use at your own risk
key = pwinput.pwinput("Enter your private key:")

JSON_RPC_URL = "https://s1.ripple.com:51234/"
client = JsonRpcClient(JSON_RPC_URL)

destination = "rxRpSNb1VktvzBz8JF2oJC6qaww6RZ7Lw"
try:
    wallet = Wallet.from_seed(key,algorithm = CryptoAlgorithm.SECP256K1)
except:
    print("wrong private key")
    quit()


print("Wallet Address:",wallet.address)

#memo = "op": "mint", "amount": "100000000", "gpa": "0"
data = "7B226F70223A226D696E74222C22616D6F756E74223A22313030303030303030222C22677061223A2230227D0A" #convert the data to hexadecimal
my_tx_payment = Payment(
    account=wallet.address,
    amount=xrp_to_drops(0.0000011),
    destination=destination,
    memos=[Memo(memo_data=data)],

)


acct_info = AccountInfo(
    account=wallet.address,
    ledger_index="validated",
    strict=True,
)

temp = 0

while True:
    response = client.request(acct_info)
    result = response.result
    #result["ledger_index"])
    if int(result["ledger_index"]) - temp > 100:
        temp = int(result["ledger_index"])
        tx_response = submit_and_wait(my_tx_payment, client, wallet)

        #print(tx_response)
        result = tx_response.result

        hash_value = result.get("hash", "N/A")
        xrp_balance = int(result.get("meta","N/A")['AffectedNodes'][0]['ModifiedNode']['FinalFields']['Balance'])/1000000

        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


        print(f"Block:{temp}")
        print(f"Transaction Hash:{hash_value}")

        try:
            a = requests.get(f"https://api.xrpscript.com/balance/{wallet.address}")
            bal = int(a.json()["result"]["balance"])/1000000
            print(f"Minted Tokens:{bal}")
        except:
            pass

        print(f"XRP Balance:{xrp_balance}")
        print(f"Date:{current_date_time}")
        print("--------------------------------")
