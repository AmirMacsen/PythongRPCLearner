import asyncio

import grpc

from async_client import article_pb2_grpc, article_pb2


async def main():
    async with grpc.aio.insecure_channel('localhost:50052') as channel:
        stub = article_pb2_grpc.ArticleServiceStub(channel)
        request = article_pb2.ArticleDetailRequest(pk=1)
        response = await stub.Detail(request)
        print(response)


if __name__ == '__main__':
    asyncio.run(main())