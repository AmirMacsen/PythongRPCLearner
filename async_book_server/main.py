import asyncio
import datetime

import grpc

from async_book_server import book_pb2, book_pb2_grpc

"""
元数据： 类似http请求中的header，可以上下文中获取或者添加元数据，实现权限校验或者客户端服务端一些特殊数据的传递

拦截器：通过继承grpc  实现对请求的拦截
"""

class BookServiceInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(self, continuation, handler_call_details):
        print("进入第一个拦截器...")
        next_handler = await continuation(handler_call_details)
        print("离开第一个拦截器...")
        return next_handler

class BookServiceInterceptor2(grpc.aio.ServerInterceptor):
    async def intercept_service(self, continuation, handler_call_details):
        print("进入第二个拦截器...")
        next_handler = await continuation(handler_call_details)
        print("离开第二个拦截器...")
        return next_handler

class AuthenticateInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(self, continuation, handler_call_details):
        print("进入权限拦截器...")
        print()
        # 获取元数据 token
        token = dict(handler_call_details.invocation_metadata).get("token", "")
        if token and token == "xxxxxxxxxxxxxxxxxxxxx":
                return await continuation(handler_call_details)
        else:
            # 需要中断请求，并返回消息
            def method_handler(request, context):
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details("Invalid token")
                return
            return grpc.unary_unary_rpc_method_handler(
                method_handler
            )


class BookService(book_pb2_grpc.BookServiceServicer):
    def List(self, request, context):
        page = request.page
        page_size = request.page_size

        # 打印客户端带过来的元数据
        for key, value in context.invocation_metadata():
            print("metadata: [%s] %s" % (key, value))


        # 服务端设置元数据 元组
        context.set_trailing_metadata((
            ("server", "grpc"),
            ("framework", "grpc-python")
        ))

        books = []
        for i in range(page*page_size):
            books.append(book_pb2.Book(
                id=i,
                title="Book %d" % i,
                author="Author %d" % i,
                description="Description %d" % i,
                book_type=book_pb2.BookType.ART,
                publish_date=datetime.datetime.now().strftime("%Y-%m-%d"),
                tags={"java": 1, "python": 2},
                book_url="https://www.google.com",
            ))

        response = book_pb2.BookListResponse(books=books)
        response.books.extend(books)
        return response

async def main():
    server = grpc.aio.server(interceptors=[BookServiceInterceptor(), BookServiceInterceptor2(), AuthenticateInterceptor()])
    book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('localhost:50051')
    await server.start()
    print("Server started at localhost:50051")
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(main())