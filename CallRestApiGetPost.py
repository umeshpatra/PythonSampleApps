
import requests
from requests.models import Response

def getdatafromapi():
    url = 'http://localhost:60390/SampleApi/getMergeTags/documentid'
    #postdata = '{"documentids":["doc1","doc2"]}'
    headerdata = '{"Content-Type":"application/json"}'

    responsedata = requests.get(url, headers={"Content-Type":"application/json"})

    print(responsedata)
    docname = responsedata.json()
    print(docname)


def postdataintoapi():
    url = 'http://localhost:60390/SampleApi/mergeTags'
    postdata = '{"documentids":["doc1","doc2"]}'
    headerdata = '{"Content-Type":"application/json"}'

    responsedata = requests.post(url, data=postdata, headers={"Content-Type":"application/json"})

    print(responsedata)


postdataintoapi()

getdatafromapi()
