import grpc

from async_book_client import book_pb2_grpc, book_pb2


async def main():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)
        # 异步调用不是with_call
        call = stub.List(
            book_pb2.BookRequest(
                page=1, page_size=10
            ),
            metadata=(
                ("token", "xxxxxxxxxxxxxxxxxxxxx"),
            )
        )

        # 获取响应结果
        response = await call
        print(response)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())