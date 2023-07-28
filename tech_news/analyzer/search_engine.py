from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news_by_title]


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news_by_date = search_news({"timestamp": date})
        return [(new["title"], new["url"]) for new in news_by_date]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news_by_category = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return [(new["title"], new["url"]) for new in news_by_category]
