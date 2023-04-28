import tool
from bs4 import BeautifulSoup
from selenium import webdriver


url1 = "https://www.science.org/action/doSearch?field1=AllField&text1=t-test&field2=AllField&text2=n%3D3&field3" \
       "=AllField&text3=&publication=&Ppub=&AfterMonth=1&AfterYear=2017&BeforeMonth=12&BeforeYear=2017"
url2 = "https://www.biomedcentral.com/search?query=t-test&searchType=publisherSearch"
url3 = "https://www.science.org/doi/10.1126/sciadv.1700521"
article6_1 = "https://www.science.org/doi/10.1126/science.aag1417"
article6_20 = "https://www.science.org/doi/10.1126/scisignal.aan8355"
article7_1 = "https://www.science.org/doi/10.1126/science.aam6512"

# html = tool.handle_http_requests2("https://www.science.org/doi/10.1126/scitranslmed.aag2809")
print(tool.is_related(article7_1, 'n = 3'))

# print(tool.find_min_distance_between_regex_matches(html, 'n = 3'))
# print(tool.is_related(url3, 'n = 3'))
# print(type(tool.get_last_page(html)))
# print(distance)

# print(tool.get_all_related_article("01 Jan 2017", "31 Dec 2017", "n = 3", {"page": "3", "article": "https://"}))

# print(tool.generate_url("01 Jan 2017", "31 Dec 2017", "n = 3"))

# articles = tool.get_only_related_articles_info(html, {'page': '1', 'article': 'https://www.science.org/doi/10.1126/sciimmunol.aam8929'})
# articles = tool.get_articles_info_in_one_page(html)
# diagram = tool.generate_diagram('01 Jan 2017', '31 Dec 2017', articles)
# result = tool.merge_diagram_articles(diagram, articles)
# print(result)


