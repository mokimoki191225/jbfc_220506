
import pandas as pd

def getBooksDF(books):

    ret_df = pd.DataFrame()

    title = list()
    published_data = list()
    publisher = list()
    pages = list()
    recommendation = list()

    column_name = ['title', 'published_data', 'publisher', 'pages', 'recommendation']

    for book in books:
        title.append(book[0])
        published_data.append(book[1])
        publisher.append(book[2])
        pages.append(book[3])
        recommendation.append(book[4])

    data = {'title' : title,
            'published_data' : published_data,
            'publisher' : publisher,
            'pages': pages,
            'recommendation': recommendation}

    ret_df = pd.DataFrame(data, columns=column_name)

    return ret_df




