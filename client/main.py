import grpc.aio

from client import article_pb2_grpc
from client import article_pb2


def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        # 创建一个 stub
        stub = article_pb2_grpc.ArticleServiceStub(channel)
        # 创建请求对象
        request = article_pb2.ArticleRequest()
        request.page=2
        request.page_size=10
        response = stub.List(request)
        print(response)


if __name__ == '__main__':
    main()

