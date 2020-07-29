import grpc
from services.definitions import car_sale_pb2_grpc, car_sale_pb2

def add_advertisement(stub):
    return stub.AddAdvertisement(car_sale_pb2.AddAdvertisementRequest(
        uc=car_sale_pb2.UserCredential(username='ali', password='12345'),
        title="momhad",
        description="dash mamal",
        car_name='momhaad',
        car_model='1367',
        min_price=0,
    ))

def get_ads_list(stub):
    return stub.GetAdsList(car_sale_pb2.AdsListRequest())


def add_offer(stub):
    return stub.AddOffer(car_sale_pb2.AddOfferRequest(
        uc=car_sale_pb2.UserCredential(username='akbar', password='12345'),
        advertisement=2,
        price=245,
    ))

if __name__ == "__main__":
    channel = grpc.insecure_channel('localhost:50051')
    stub = car_sale_pb2_grpc.CarSaleStub(channel)
    response = add_offer(stub)
    # response = get_ads_list(stub)
    print(response)
