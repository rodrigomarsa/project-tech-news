from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url: str) -> str:
    try:
        response = requests.get(
            url, headers={"User-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        return response.text if response.status_code == 200 else None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content: str) -> list[str]:
    selector = Selector(html_content)
    urls = selector.css(".post-inner h2 a::attr(href)").getall()
    return urls if urls else []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
