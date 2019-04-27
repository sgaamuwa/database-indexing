from django.core.management.base import BaseCommand
from database.models import User, Address
import json

class Command(BaseCommand):

    def create_addresses(self):
        with open('database\seeds\dataApr-26-2019.json', encoding="utf8") as address_json:
            data = json.load(address_json)
            counter = 1
            for address in data:
                address_object = Address(counter, address['street'], address['city'], address['postal_code'], address['country'])
                address_object.save()
                counter += 1

    def handle(self, *args, **options):
        self.create_addresses()