# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request

class ScrapyCodePipeline:
    def open_spider(self,spider):
        self.fp = open('book.json','w',encoding="utf8")
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    def close_spider(self,spider):
        self.fp.close()

class DangDangDownload:
    a = 1
    def process_item(self,item,spider):
        src_img = item.get("src")
        urllib.request.urlretrieve(url=src_img,filename="../img/"+str(DangDangDownload.a)+'.jpg')
        DangDangDownload.a += 1

class DyttDownload:
    a = 1
    def process_item(self,item,spider):
        src_img = item.get("src")
        urllib.request.urlretrieve(url=src_img,filename="../img/"+str(DyttDownload.a)+'.jpg')
        DyttDownload.a += 1


class DuShuDownload:
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding="utf8")
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    def close_spider(self, spider):
        self.fp.close()
from scrapy.utils.project import get_project_settings
import pymysql
class MySqlPipelines:
    a = 1
    def open_spider(self,spider):
        settings = get_project_settings()
        db = settings.get('MYSQL_DB_NAME', 'spider')   # 找不到就用后面的值代替
        host = settings.get('MYSQL_HOST', 'localhost')
        port = settings.get('MYSQL_PORT', 3306)
        user = settings.get('MYSQL_USER', 'root')
        passwd = settings.get('MYSQL_PASSWORD', 'root')
        self.db_conn = pymysql.connect(host=host,port=port,db=db,user=user,password=passwd,charset="utf8")
        self.db_cur = self.db_conn.cursor()
    def process_item(self,item,spider):
        self.insert_db(item)
        pass
    def insert_db(self,item):
        value = (
            item.get('name'),
            item.get('src'),
        )
        MySqlPipelines.a += 1
        sql = 'insert into book(name,src) values("%s","%s")'
        self.db_cur.execute(sql,value)
    def close_spider(self,spider):
        self.db_conn.commit()
        self.db_cur.close()
        self.db_conn.close()