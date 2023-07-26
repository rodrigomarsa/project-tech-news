from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url: str) -> str | None:
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
    return urls


# Requisito 3
def scrape_next_page_link(html_content: str) -> str | None:
    selector = Selector(html_content)
    link = selector.css("a.next.page-numbers::attr(href)").get()
    return link


# Requisito 4
def scrape_news(html_content: str) -> dict:
    selector = Selector(html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("li.meta-author a::text").get()
    reading_time = int(
        selector.css("li.meta-reading-time::text").re(r"\d+")[0]
    )
    paragraph = selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()
    summary = "".join(paragraph).strip()
    category = selector.css(".label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
