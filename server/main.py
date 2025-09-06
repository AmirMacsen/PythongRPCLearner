import datetime
from concurrent import futures

import grpc

from server import article_pb2, article_pb2_grpc


class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    def List(self, request, context):
        page = request.page
        page_size = request.page_size
        response = article_pb2.ArticleListResponse()

        articles = []
        for i in range(page*page_size):
            articles.append(article_pb2.Article(
                    id=i,
                    title="title %d" % i,
                    content="content %d" % i,
                    create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ))

        response.articles.extend(articles)

        return response


    def Detail(self, request, context):
        article = article_pb2.Article(
            id=request.id,
            title="title %d" % request.id,
            content="content %d" % request.id,
            create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        return article

def main():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), grpc_server)
    # 使用不安全的通讯，开发阶段，如果使用安全服务还需要公钥和密钥
    grpc_server.add_insecure_port('localhost:50051')
    grpc_server.start()
    print("server start")
    # 循环等待关闭
    grpc_server.wait_for_termination()

if __name__ == '__main__':
    main()