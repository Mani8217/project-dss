import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'bookstore.settings'  # نام پروژه خود را وارد کنید
django.setup()

from itemadapter import ItemAdapter
import mysql.connector
from django.conf import settings

class BookScraperPipeline:
    def process_item(self, item, spider):
        return item


class SaveToMySQLPipeline:
    def open_spider(self, spider):
        # اتصال به پایگاه داده MySQL
        self.conn = mysql.connector.connect(
            host=settings.DATABASES['default']['HOST'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            database=settings.DATABASES['default']['NAME']
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            # درج داده‌ها در جدول 'books_book'
            self.cursor.execute("""
                INSERT INTO books_book (title, price, availability, url)
                VALUES (%s, %s, %s, %s)
            """, (item["title"], float(item["price"][1:]), item["availability"], item["url"]))
            
            self.conn.commit()
        except mysql.connector.Error as err:
            spider.logger.error(f"Error inserting item: {err}")
        return item

    def close_spider(self, spider):
        # بستن اتصال پایگاه داده
        self.cursor.close()
        self.conn.close()
