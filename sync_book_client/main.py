import grpc

from sync_book_client import book_pb2_grpc, book_pb2


def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)
        # 同步调用使用with_call 返回两个参数
        response, call = stub.List.with_call(
            book_pb2.BookRequest(
                page=1, page_size=10
            ),
            metadata=(
                ("token", "xxxxxxxxxxxxxxxxxxxxx"),
            )
        )

        print(response)

        for key, value in call.trailing_metadata():
            print(
                "Greeter client received trailing metadata: key=%s value=%s"
                % (key, value)
            )

if __name__ == '__main__':
    main()
