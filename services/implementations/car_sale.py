from services.definitions import car_sale_pb2_grpc, car_sale_pb2
from database import Session
from database.models import Advertisement, Offer
from services.implementations import mappers
from database.functions import get_user
import grpc

class CarSaleServicer(car_sale_pb2_grpc.CarSaleServicer):

    def GetAdsList(self, request, context):
        session = Session()
        ads = [mappers.advertisement_mapper(ad) for ad in session.query(Advertisement).all()]
        return car_sale_pb2.AdsListResponse(data=ads)

    def AddOffer(self, request, context):
        session = Session()
        uc = request.uc
        user = get_user(session, uc.username, uc.password)
        if user is None:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("authentication error.")
            return car_sale_pb2.AddOfferResponse()

        offer = Offer(
            user_id = user.id,
            advertisement_id=request.advertisement,
            price=request.price
        )
        session.add(offer)
        session.commit()
        print("filaaan: ", offer)
        return car_sale_pb2.AddOfferResponse(data=mappers.offer_mapper(offer))


    def AddAdvertisement(self, request, context):
        session = Session()
        uc = request.uc
        user = get_user(session, uc.username, uc.password)
        if user is None:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("authentication error.")
            return car_sale_pb2.AddAdvertisementResponse()
        ad = Advertisement(
            owner_id=user.id,
            title=request.title,
            description=request.description,
            car_name=request.car_name,
            car_model=request.car_model,
            min_price=request.min_price,
            )

        if request.end_time is not None and str(request.end_time).strip() != '':
            ad.end_time = request.end_time.ToDatetime()
        session.add(ad)
        session.commit()
        return car_sale_pb2.AddAdvertisementResponse(data=mappers.advertisement_mapper(ad))
