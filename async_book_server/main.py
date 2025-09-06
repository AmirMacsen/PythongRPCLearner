import asyncio
import datetime

import grpc

from async_book_server import book_pb2, book_pb2_grpc


class BookService(book_pb2_grpc.BookServiceServicer):
    def List(self, request, context):
        page = request.page
        page_size = request.page_size

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
    server = grpc.aio.server()
    book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('localhost:50051')
    await server.start()
    print("Server started at localhost:50051")
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(main())