# Install
# python -m pip install --upgrade pip
# python -m pip install grpcio
# python -m pip install grpcio-tools
# python -m pip install googleapis-common-protos

# Protocol Buffer Compile
# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello_world.proto

from concurrent import futures
import time

import grpc

import hello_world_pb2
import hello_world_pb2_grpc


class Greeter(hello_world_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_world_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()