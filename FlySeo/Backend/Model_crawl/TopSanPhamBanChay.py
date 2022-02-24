# thư viện requests đọc dữ liệu khi crawl về
import requests
# jsson chuyển file lấy từ web về đọc dữ liệu
import json
from bs4 import BeautifulSoup
#url = 'https://shopee.vn/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=9&limit=60&offset=0'


url=" https://shopee.vn/api/v4/recommend/recommend?bundle=top_products_landing_page&intentionid=VN_BITL0_157&limit=200&section=best_selling_sec"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': '',
}    
r = requests.get(url, headers=headers)
data = r.json()  


# lấy all sản phẩm theo key tìm kiếm hàng đầu
i=0;
y = 0;
for item in data['data']['sections'][0]['data']['top_product'][0]['list']['data']['item']:
    i+=1
    print("sl",i)
    print(item['name'])
    print(item['image'])
    price=item['price']
    print("giá sản phẩm",price/10000)
    print(item['price_max'])
    print(item['discount'])
    print("doanh số",item['count'])

    #shop đó
    print("tên shop",item['shop_name'])
    print("Điểm đánh giá shop",item['shop_rating'])
# chỗ này lấy phân loại sản phẩm
    while y<i:
        for item in data['data']['sections'][0]['data']['top_product'][0]['list']['data']['item'][y]['tier_variations']:
            print(item['name'])
            print(item['options'])
            print(item['images'])
        y+=1