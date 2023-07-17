import tool
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime



url1 = "https://www.science.org/action/doSearch?field1=AllField&text1=t-test&field2=AllField&text2=n%3D3&field3" \
       "=AllField&text3=&publication=&Ppub=&AfterMonth=1&AfterYear=2017&BeforeMonth=12&BeforeYear=2017"
url2 = "https://www.biomedcentral.com/search?query=t-test&searchType=publisherSearch"
url3 = "https://www.science.org/doi/10.1126/sciadv.1700521"
article6_1 = "https://www.science.org/doi/10.1126/science.aag1417"
article6_20 = "https://www.science.org/doi/10.1126/scisignal.aan8355"
article7_1 = "https://www.science.org/doi/10.1126/science.aam6512"
text = r'<div role="doc-footnote">(T test <b>A</b> to <b>H</b>) Immunofluorescent images from brain deep white matter and graph (<b>I</b>) showing number of blood vessels (CD34<sup>+</sup>, red) with claudin-5–positive tight junctions (TJs, green) in DM rats (B and D) compared to controls (A and C), as well as in diseased human brains (F and H) compared to controls (E and G). Arrows indicate blood vessels without claudin-5–positive TJs. (C), (D), (G), and (H) show enlarged images of the white boxes in (A), (B), (E), and (F), respectively. (<b>J</b> to <b>O</b>) Number of OPCs (Olig2<sup>+</sup> Nogo-A<sup>−</sup>; indicated by arrows) per square millimeter (J and N) and mature oligodendrocytes (Olig2<sup>+</sup> Nogo-A<sup>+</sup>) (K and O) in DM rats and in diseased human brains compared to controls [Olig2, all oligodendroglia (green); Nogo-A, mature oligodendrocytes (red)]. (<b>P</b>) Number of proliferating OPCs (Olig2<sup>+</sup> PCNA<sup>+</sup>) per square millimeter in DM rats and in the diseased human brains compared to controls [mean ± SEM; *<i>P</i> &lt; 0.05 and **<i>P</i> &lt; 0.01, two-way analysis of variance (ANOVA) with Tukey’s post hoc tests; 3 weeks, <i>n</i> ≥ 4 animals; 4 weeks, <i>n</i> ≥ 3 animals; 5 weeks, (P) <i>n</i> = 3 animals; others, <i>n</i> = 10 animals and <i>n</i> = 5 humans]. Scale bars, 25 μm. PCNA, proliferating cell nuclear antigen.</div>'

# print(tool.regex_keyword("antigen"))
# print(tool.find_min_distance_between_regex_matches(text, "antigen"))
date1 = datetime.strptime('Jan 2017', '%b %Y')
date2 = datetime.strptime('Jan 2018', '%b %Y')
delta = (date2 - date1).days
print(delta)
