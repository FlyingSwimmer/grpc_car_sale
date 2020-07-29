import grpc
from concurrent import futures
from services.definitions import car_sale_pb2_grpc
from services.implementations.car_sale import CarSaleServicer
from database import connection
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    car_sale_pb2_grpc.add_CarSaleServicer_to_server(CarSaleServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()