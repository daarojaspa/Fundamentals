from curl_cffi import requests

URL= "https://books.toscrape.com/"
#simple request
response=requests.get(URL)
if response.status_code==200:
    print("header",response.headers)
    print("text",response.text)
else:
    print(response.status_code)
    
    
