import tool


def search_science(start_time, end_time, keyword):
    """
    :param start_time: "01 Jan 2017"
    :param end_time: "31 Dec 2017"
    :param keyword: "n = 3" (the user must input space beside special symbols such as "=")
    :return: result:
            {'diagram':{'2017-05': 1, '2017-11': 2, '2017-02': 1, '2017-04': 2, '2017-10': 2},
             'articles':{'BMP8A sustains spermatogenesis by activating both SMAD1/5/8 and SMAD2/3 in spermatogonia':
                            {'title': 'BMP8A sustains spermatogenesis by activating both SMAD1/5/8 and SMAD2/3 in spermatogonia',
                             'url': '/doi/10.1126/scisignal.aal1910',
                             'authors': 'by Fang-Ju Wu, Ting-Yu Lin, Li-Ying Sung, Wei-Fang Chang, Po-Chih Wu, Ching-Wei Luo',
                             'published time': '02 May 2017'},
                         'Arabidopsis ATXR2 deposits H3K36me3 at the promoters of LBD genes to facilitate cellular dedifferentiation':
                            {'title': 'Arabidopsis ATXR2 deposits H3K36me3 at the promoters of LBD genes to facilitate cellular dedifferentiation',
                            'url': '/doi/10.1126/scisignal.aan0316',
                            'authors': 'by Kyounghee Lee, Ok-Sun Park, Pil Joon Seo',
                            'published time': '28 Nov 2017'}, ...
                         }
            }
    """
    url = tool.generate_url(start_time, end_time, keyword)
    html = tool.handle_http_requests2(url)
    articles = tool.get_articles_info_in_one_page(html)
    diagram = tool.generate_diagram('01 Jan 2017', '31 Dec 2017', articles)
    result = tool.merge_diagram_articles(diagram, articles)
    return result


# print(search_science("01 Jan 2017", "31 Dec 2017", "n = 3"))
