import json
from django.core.management.base import BaseCommand
from requests.models import PurchaseRequest, RequestLine

class Command(BaseCommand):
    help = 'Loads data from JSON into the database'

    def handle(self, *args, **kwargs):
        # Load Purchase Requests
        with open('purchase_requests.json', 'r') as file:
            data = json.load(file)
            for item in data:
                pr = PurchaseRequest.objects.create(
                    requester=item['requester'],
                    description=item['description'],
                    date=item['date'],
                    type=item['type'],
                    status=item['status']
                )
                self.stdout.write(self.style.SUCCESS(f'Loaded PurchaseRequest {pr.id}'))

        # Load Request Lines
        with open('request_lines.json', 'r') as file:
            data = json.load(file)
            for item in data:
                pr = PurchaseRequest.objects.get(id=item['purchase_request_id'])
                rl = RequestLine.objects.create(
                    purchase_request=pr,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price'],
                    currency=item['currency']
                )
                self.stdout.write(self.style.SUCCESS(f'Loaded RequestLine {rl.id}'))
