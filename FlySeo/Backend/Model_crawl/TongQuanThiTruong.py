import requests
import json
from bs4 import BeautifulSoup
import requests
from flask import jsonify
import numpy as np

def getdatamarket():
    url = "https://api.shopeeanalytics.com/vn/products/"
    payload={
    '_saToken': 'q9keazaxfu8s04kwcg0c8o0k4ss88o0',
    'tp': 'products',
    'products_action': 'products_search',
    'products_search': 'product_search_sp_title=&product_search_sp_cat=&product_check_buff=on'}
    headers = {
    'Cookie': 'PHPSESSID=k12vujsiu0vqugd2p38mm14hb4'
    }
    response = requests.request("POST", url, headers=headers,  data=payload)
    data = response.json()
    
    print(data['statistical']['view_month'])

    aDict = { "revenue_month": data['statistical']['revenue_month'],   "sold_month":data['statistical']['sold_month'],"view_month":data['statistical']['view_month'],
    "sold_total":data['statistical']['sold_total'],
    "revenue_total":data['statistical']['revenue_total'],
    }
    # jsonString = json.dumps(aDict)
    # jsonFile = open("data.json", "w")
    # jsonFile.write(jsonString)
    # jsonFile.close()
    return  aDict
    

    # return response.json()
def getdatachartmaket():
    try:
        url ="https://www.shopeeanalytics.com/vn/search/market"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = str(soup)
        item = (data[26000:34000])
        a1 = item.find("backgroundColor: '#FF6384',")
        a2 = item.find("  label: 'Trước đó',")
        end = item.find("</script>")
        #data doanh thu 30 ngày
        datadoanhthu =  item[a1:a2].split(",");
        a3 =datadoanhthu[1].split("data: [")
        a4 = datadoanhthu[10].split("]")
        #print("DoanhThu",a3[1],datadoanhthu[2],datadoanhthu[3],datadoanhthu[4],datadoanhthu[5],datadoanhthu[6],datadoanhthu[7],datadoanhthu[8], datadoanhthu[9])
    
        # trước đó 30 ngày

        datadoanhthutruocdo = item[a2+142:a2+220].split(",");
        a5 = datadoanhthutruocdo[0].split("data: [");
        a6 = datadoanhthutruocdo[9].split("]")
       
        print(a5[1],a6[0])

        

        #data lượt bán 30 ngày

        b1 = item.find("backgroundColor: '#36A2EB',");
        dataluotban = item[b1:b1+3000].split(",");
        b2 = dataluotban[1].split("data: [");
        b3 = dataluotban[10].split("]")
        #print("LuotBan",b2[1],dataluotban[2],dataluotban[3],dataluotban[4],dataluotban[5],dataluotban[6],dataluotban[7],dataluotban[8],dataluotban[8],dataluotban[9])
    

        # data luotxem
        c1= item.find("backgroundColor: '#4BC0C0',");
        dataluotxem = item[c1:c1+3000].split(",");
        c2 = dataluotxem[1].split("data: [");
        c3 = dataluotxem[10].split("]")
        #print("luotxem",c2[1],dataluotxem[2],dataluotxem[3],dataluotxem[4],dataluotxem[5],dataluotxem[6],dataluotxem[7],dataluotxem[8],dataluotxem[9])
    
        #data ti le chuyen doi

        d1 = item.find("backgroundColor: '#282C34',")
        datatyle = item[d1:d1+3000].split(",")
        d2 = datatyle[1].split("data: [");
        d3 = datatyle[10].split("]")
        #print("tyle",d2[1],datatyle[2],datatyle[3],datatyle[4],datatyle[5],datatyle[6],datatyle[7],datatyle[8],datatyle[9])

        aDict = {
            "DoanhThu":[a3[1],datadoanhthu[2],datadoanhthu[3],datadoanhthu[4],datadoanhthu[5],datadoanhthu[6],datadoanhthu[7],datadoanhthu[8], datadoanhthu[9],a4[0]],
            "LuotBan":[b2[1],dataluotban[2],dataluotban[3],dataluotban[4],dataluotban[5],dataluotban[6],dataluotban[7],dataluotban[8],dataluotban[8],b3[0]], 
            "LuotXem":[c2[1],dataluotxem[2],dataluotxem[3],dataluotxem[4],dataluotxem[5],dataluotxem[6],dataluotxem[7],dataluotxem[8],dataluotxem[9],c3[0]],
            "TyLe":[d2[1],datatyle[2],datatyle[3],datatyle[4],datatyle[5],datatyle[6],datatyle[7],datatyle[8],datatyle[9],d3[0]]
        }

       
    except:
        print("Error")
    return aDict

getdatachartmaket()