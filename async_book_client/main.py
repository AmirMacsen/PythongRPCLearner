import grpc

from async_book_client import book_pb2_grpc, book_pb2


async def main():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)
        request = book_pb2.BookRequest(
            page=1,
            page_size=10
        )
        response = await stub.List(request)
        print(response)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())