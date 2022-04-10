from lxml import etree
tree = etree.parse("../html/demo.html")
li_list1 = tree.xpath('//body/ul/li')    # 获得body下的ul下的li的所有标签
print(len(li_list1))
print(li_list1)
li_list2 = tree.xpath('//body/ul/li[@id="l1"]/text()')  # 获取ul标签下的li的id属性为l1的文本内容
print(li_list2)
li_list3 = tree.xpath('//body/ul/li[@id]/@class')  # 获得带有id属性的class的属性名
print(li_list3)
li_list4 = tree.xpath('//body/ul/li[@class="l1"]/text()')#获得class属性值l1的标签信息
print(li_list4)
li_list5 = tree.xpath('//body/ul/li[starts-with(@id,"l")]/text()')
print(li_list5)
li_list6 = tree.xpath('//body/ul/li[@id][1]/text()')#还带有索引的性质
print(li_list6)
li_list7 = tree.xpath('//body/ul')[0]
print(li_list7)
print(li_list7.xpath('string(.)'))# 获得对应标签下的嵌套内容
li_list8 = tree.xpath('//body/ul/li')[0]
print(li_list8)
print(li_list8.xpath('string(.)'))#获得li的第一个内容值
li_list9 = tree.xpath('//body/ul/li')[0]
print(li_list9)
print(li_list9.xpath('string(..)'))#获得li上一级目录的所有内容值