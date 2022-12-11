import requests as requests
from decouple import config
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
url = config('API_URL')
headers = {"x-api-key":config('API_KEY')}

def retrieveRecipe(queryStringParams):
    try:
        response = requests.get(url+"?"+queryStringParams,headers=headers)
        return(response.status_code,response.json()) 
    except requests.exceptions.RequestException as e:
        return(e) 

def modifyRecipe(body):
    try:
        response = requests.put(url,headers=headers,json=body)
        return(response.status_code,response.json()) 
    except requests.exceptions.RequestException as e:
        return(e) 

def createRecipe(body):
    try:
        response = requests.post(url,headers=headers,json=body)
        return(response.status_code,response.json()) 
    except requests.exceptions.RequestException as e:
        return(e) 


body_update = {"id":"610f146a-72f0-11ed-b454-16b3889a1874","key":"title","value":"modified"}

body_create = {"title":"Biscuits and Gravy","description":"Here’s a classic Southern biscuits and gravy recipe you won’t forget. Make biscuits are with real butter and creamy buttermilk, then simmer gravy with pork sausage and drippings. This is comfort food at its best.","minutes":35,"servings":10,
    "ingredients":[{"ingredient":"sugar","quantity":2,"meassurement":"teaspoons"},{"ingredient":"buttermilk","quantity":1,"meassurement":"cup"}],"steps":[{"step":"Preheat the oven","number":1},{"step":"Whisk the flour, sugar and salt","number":2}]}

if __name__ == "__main__":
    #print(retrieveRecipe("id=57c01182-78d3-11ed-9722-d628f40f689b"))
    print(modifyRecipe(body_update))
    #print(createRecipe(body_create))
