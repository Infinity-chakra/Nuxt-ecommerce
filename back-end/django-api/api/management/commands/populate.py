from django.core.management.base import BaseCommand
import pandas as pd
from api.models import Item


class Command(BaseCommand):
    help = 'Populates Item Database from csv file'

    def handle(self, *args, **kwargs):
        
        df = pd.read_csv('data/myntra.csv')

        result = df.head(10)

        for index, row in df.iterrows():
            try:
                current_item = Item(
                    product_id=row[0],
                    title=row[1],
                    link=row[10],
                    price=row[4],
                    mrp=row[5],
                    brand=row[9],
                    rating=row[6],
                    totalRating=row[7],
                    discount=row[8],
                )
                current_item.save()
                print('Data saved for ', row[9])
            except Exception as err:
                print('Could not save data for this item ', err)
        