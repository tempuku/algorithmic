import json
import sys
from dataclasses import dataclass, asdict


@dataclass
class Offer:
    offer_id: str
    market_sku: int
    price: int


offers = []
for i in range(int(sys.stdin.readline().strip())):
    feed = sys.stdin.readline().strip()
    offers.extend([Offer(**offer) for offer in json.loads(feed)['offers']])

offers.sort(key=lambda x: (x.price, x.offer_id))

result = {
    "offers": [
        asdict(x) for x in offers
    ]
}

print(json.dumps(result))
