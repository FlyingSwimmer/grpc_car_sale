from services.definitions import car_sale_pb2
from google.protobuf.timestamp_pb2 import Timestamp

def advertisement_mapper(ad):
    end_time = Timestamp()
    end_time.FromDatetime(ad.end_time)
    return car_sale_pb2.Advertisement(
        id=ad.id,
        owner=ad.owner_id,
        title=ad.title,
        description=ad.description,
        car_name=ad.car_name,
        car_model=ad.car_model,
        min_price=ad.min_price,
        end_time=end_time,
    )

def offer_mapper(offer):
    creation_date = Timestamp()
    creation_date.FromDatetime(offer.creation_date)
    return car_sale_pb2.Offer(
        id=offer.id,
        user=offer.user_id,
        advertisement=offer.advertisement_id,
        price=offer.price,
        creation_date=creation_date,
    )