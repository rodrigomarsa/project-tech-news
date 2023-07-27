import pytest
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import Mock, patch


def test_reading_plan_group_news() -> None:
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    mock_db_find_news = Mock(
        return_value=[
            {"title": "Python é a linguagem do momento", "reading_time": 4},
            {
                "title": "Selenium, BS ou Parsel? Entenda as diferenças",
                "reading_time": 3,
            },
            {
                "title": "Pytest + Faker: a combinação poderosa dos testes!",
                "reading_time": 10,
            },
            {
                "title": "FastAPI e Flask: frameworks para APIs em Python",
                "reading_time": 15,
            },
            {
                "title": "A biblioteca Pandas e o sucesso da linguagem Python",
                "reading_time": 12,
            },
        ]
    )

    with patch("tech_news.database.find_news", mock_db_find_news):
        result = ReadingPlanService.group_news_for_available_time(10)

    expected = {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    ("Python é a linguagem do momento", 4),
                    ("Selenium, BS ou Parsel? Entenda as diferenças", 3),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    ("Pytest + Faker: a combinação poderosa dos testes!", 10)
                ],
            },
        ],
        "unreadable": [
            ("FastAPI e Flask: frameworks para APIs em Python", 15),
            ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
        ],
    }
    assert result == expected
