import datetime

from pygooglenews import GoogleNews
import pandas as pd


def get_news(search_word: str,
             country: str,
             start_date: datetime,
             end_date: datetime) -> pd.DataFrame:
    """
    This method gets news articles from google news for given search word and country and date range.
    Here, google sets limit at 100 article per day.
    Args:
        search_word: str, word to search in google news
        country: str, country region for the google news
        start_date: datetime, news from a date
        end_date: datetime, news till a date

    Returns:
        pd.DataFrame with columns title for the article, link and publication dates
    """

    delta = datetime.timedelta(days=1)
    date_list = pd.date_range(start_date, end_date).tolist()

    news_list = []

    for date in date_list[:-1]:
        gn = GoogleNews(country=country)
        result = gn.search(search_word,
                           from_=date.strftime('%Y-%m-%d'),
                           to_=(date + delta).strftime('%Y-%m-%d'))
        news_item = result['entries']

        for item in news_item:
            news = {
                'title': item.title,
                'link': item.link,
                'published': item.published
            }

            news_list.append(news)

    news_dataframe = pd.DataFrame(news_list)

    # format_columns(news_dataframe)

    return news_dataframe


def format_columns(news_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Helper function to format the columns of the input DataFrame
    Args:
        news_dataframe: pd.Dataframe to which the operation is performed

    Returns:
        pd.DataFrame with formatted columns
    """
    news_dataframe['published'] = pd.to_datetime(news_dataframe['published'])


if __name__ == '__main__':
    get_news(search_word='disease',
             country='US',
             start_date=datetime.date(2021, 3, 1),
             end_date=datetime.date(2021, 3, 2))
