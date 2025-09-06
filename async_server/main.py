import asyncio
import datetime

import grpc

from async_server import article_pb2_grpc, article_pb2


class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    async def List(self, request, context):
        page = request.page
        page_size = request.page_size
        ### 模拟异步io
        await asyncio.sleep(1)

        response = article_pb2.ArticleListResponse()
        articles=[]

        for i in range(page*page_size):
            article = article_pb2.Article(
                id=i,
                title="title %s" % i,
                content="content %s" % i,
                create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )

            articles.append(article)

        response.articles.extend(articles)
        return response

    async def Detail(self, request, context):
        article_id = request.pk
        ### 模拟异步io
        await asyncio.sleep(1)

        article = article_pb2.Article(
            id=article_id,
            title="title %s" % article_id,
            content="content %s" % article_id,
            create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        return article


async def main():
    server = grpc.aio.server()
    article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), server)
    server.add_insecure_port('localhost:50052')
    await server.start()
    print("Server started at localhost:50052")
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(main())

