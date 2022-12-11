# GOTA: REST API CRUD

GOTA is a REST API that can manage recipes that supports these operations:

Create a new recipe
Retrieve a recipe
Modify a recipe

For this project I've used:

- python 3
- serverless framework (https://www.serverless.com/) to deploy app in AWS as a Lambda service
- DynamoDB to storage data, in AWS
- API Gateway (AWS)

Authentication: API Key that must be sent in the Header.

## Included in this project:

- serverless.yml: configuration for serverless framework to deploy application to AWS cloud
- requirements.txt: python libraries required for project
- get_layer_packages: script to generate a layer with the required libraries to attach to the lambda
- lambda_function.py: code of the application
- client.py: example calls to the API


# Schema
The schema of the object Recipe is the following:

    {
       "id":"57c01182-78d3-11ed-9722-d628f40f689b",
       "title":"Biscuits and Gravy",
       "description":"Here\u2019s a classic Southern biscuits and gravy recipe you won\u2019t forget. Make biscuits are with real butter and creamy buttermilk, then simmer gravy with pork sausage and drippings. This is comfort food at its best.",
       "servings":10.0,
       "minutes":35.0,
       "steps":[
          {
             "number":1.0,
             "step":"Preheat the oven"
          },
          {
             "number":2.0,
             "step":"Whisk the flour, sugar and salt"
          }
       ],
       "ingredients":[
          {
             "ingredient":"sugar",
             "quantity":2.0,
             "meassurement":"teaspoons"
          },
          {
             "ingredient":"buttermilk",
             "quantity":1.0,
             "meassurement":"cup"
          }
       ],

       "updatedAt":"1670708462.3991892",
       "createdAt":"1670708462.3991756",
    }


# Deployment
I've deployed the project on AWS. The API url is: https://fle2oy1e8j.execute-api.eu-west-1.amazonaws.com/dev/

# API endpoints:
In the client.py file there are examples of the API calls.

#### Retrieve the recipe with the specified id 

```/recipes/<id> ``` (GET)

Required query request params: 
 `id=[string]`

Required Header param:
`x-api-key=[string]`


Example: 	
```
curl https://fle2oy1e8j.execute-api.eu-west-1.amazonaws.com/dev/recipes?id=57c01182-78d3-11ed-9722-d628f40f689b -H "x-api-key:iqzRWNMiA18H4M4NAJkiI1u3xaLoEWgY5v3taKqd"

```


#### Add an recipe the database

```/recipes ``` (POST)

Request data params (not mandatory): 
 `title=[string]`
 `description=[string]`
 `servings=[int]`
 `minutes=[int]`
 `ingredients=[array of string]`
 `steps=[array of string]`

Required Header param:
`x-api-key=[string]`

 Example: 
 ```
curl -X POST https://fle2oy1e8j.execute-api.eu-west-1.amazonaws.com/dev/recipes -H "x-api-key:iqzRWNMiA18H4M4NAJkiI1u3xaLoEWgY5v3taKqd" -d '{"title":"Biscuits and Gravy","description":"Here’s a classic Southern biscuits and gravy recipe you won’t forget. Make biscuits are with real butter and creamy buttermilk, then simmer gravy with pork sausage and drippings. This is comfort food at its best.","minutes":35,"servings":10,"ingredients":[{"ingredient":"sugar","quantity":2,"meassurement":"teaspoons"},{"ingredient":"buttermilk","quantity":1,"meassurement":"cup"}],"steps":[{"step":"Preheat the oven","number":1},{"step":"Whisk the flour, sugar and salt","number":2}]}'  -H "x-api-key:iqzRWNMiA18H4M4NAJkiI1u3xaLoEWgY5v3taKqd"


  ```
  

#### Update an existing recipe
    
```/recipes/<id> ``` (PUT)

Required request data params: 
 `id=[string]`
 `key=[string]`
 `value=[string]`

where key is the field to change

Required Header param:
`x-api-key=[string]`

Example:
```
curl -X PUT https://fle2oy1e8j.execute-api.eu-west-1.amazonaws.com/dev/recipes -H "x-api-key:iqzRWNMiA18H4M4NAJkiI1u3xaLoEWgY5v3taKqd" -d '{"id":"024ed9c6-7988-11ed-8375-fe74f40dcf60","key":"title","value":"title_modified"}'

  ```  
