from tech_news.database import db


# Requisito 10
def top_5_categories():
    categories = db.news.aggregate(
        [
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
        ]
    )
    return [category["_id"] for category in categories][:5]
