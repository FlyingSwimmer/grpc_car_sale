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
