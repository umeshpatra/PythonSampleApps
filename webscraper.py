from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
api = Api(app)

class Googlelinks(Resource):
    def get(self):
        url = "http://www.hubertiming.com/results/2017GPTR10K"
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        all_links = soup.find_all("a")
        links = []
        for link in all_links:
            if len(link) > 0 and link.get("href") is not None: #link  is not None and 
                links.append(link.get("href"))        

        return jsonify(links)

class Googlerows(Resource):
    def get(self):
        url = "http://www.hubertiming.com/results/2017GPTR10K"
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        totalrows = soup.find_all("tr")
        rows = totalrows[:10]
        #rowblob =[]
        textblob =[]
        for row in rows:
            row_td = row.find_all('td')
            if len(row_td) > 0:
                cleantext = BeautifulSoup(str(row_td),'lxml').get_text()
                if cleantext is not None and len(cleantext) > 0:
                    print(row_td)
                    print(cleantext)
                    textblob.append(cleantext)
        list_rows = []
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 0:
                str_cells = str(cells)
                clean = re.compile('<.*?>')
                clean2 = (re.sub(clean, '',str_cells))
                if clean2 is not None and len(clean2) > 0:
                    list_rows.append(clean2)

        return jsonify({'list_rows': list_rows})

api.add_resource(Googlelinks, '/news')
api.add_resource(Googlerows, '/rows')

if __name__ == '__main__':
    app.run(port='5002')