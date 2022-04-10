from bs4 import BeautifulSoup
soup = BeautifulSoup(open('../html/demo.html','r',encoding="utf8"),'lxml')
print(soup.select('li[class="l2"]')[0].name)  # 选择li中class的属性值为l2的标签
