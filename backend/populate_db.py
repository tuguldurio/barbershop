from database import db
import argparse
from datetime import datetime, timedelta
from random import random

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--delete', default=False, action='store_true')
args = parser.parse_args()



if args.delete:
    db.get_collection('bookings').delete_many({})
    print('Documents deleted')
else:
    count = 0
    for i in range(31):
        date = datetime.now().replace(hour=0, minute=0, second=0)

        if random() < 0.7:
            for j in range(10, 18):
                if random() < 0.8:
                    adding_date = date + timedelta(days=i, hours=j)

                    if db.get_collection('bookings').count_documents({'date': adding_date}) > 0:
                        continue
                    
                    db.get_collection('bookings').insert_one({
                        'date': adding_date,
                        'booking': None
                    })
                    count += 1
    print(f'{count} documents added to the db')
    # bookings.append({
    #     'date': date,
    #     'booking': None
    # })


# db.get_collection('bookings').insert_many()