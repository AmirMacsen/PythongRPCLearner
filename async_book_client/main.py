import grpc
from grpc import intercept_channel

from async_book_client import book_pb2_grpc, book_pb2

## 客户端拦截器 异步版本
class MyInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    # 实现这个方法
    async def intercept_unary_unary(self, continuation, client_call_details, request):
        print("interceptor")
        return await continuation(client_call_details, request)


async def main():
    # 客户端拦截器
    async with grpc.aio.insecure_channel('localhost:50051', interceptors=(MyInterceptor(),)) as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)
        # 异步调用不是with_call
        call = stub.List(
            book_pb2.BookRequest(
                page=1, page_size=10
            ),
            metadata=(
                ("token", "xxxxxxxxxxxxxxxxxxxxx1"),
            )
        )

        # 获取响应结果
        response = await call
        print(response)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())