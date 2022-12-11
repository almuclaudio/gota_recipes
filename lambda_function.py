import json
import time
import uuid
from decouple import config
import boto3
import logging
from botocore.exceptions import ClientError
from custom_encoder import CustomEncoder


class Recipes:

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        dynamodb = boto3.resource('dynamodb', region_name=config('DYNAMODB_REGION'))
        self.table = dynamodb.Table(config('RECIPES_TABLE'))

    def retrieveRecipe(self,id):
        try:
            result = self.table.get_item(
                Key={
                    'id': id
                }
            )
            if 'Item' in result:
                return self.getResponse(200,result['Item'])
            else:
                return self.getResponse(404,{'Message':'Recipe: %s not found' % id})
        except ClientError as e:
            self.logger.exception(e.response['Error']['Message'])
            exit(-1)

    def createRecipe(self,body):  
        item = {
            'id': str(uuid.uuid1()),
            'createdAt': str(time.time()),
            'updatedAt': str(time.time())
        }
        
        if 'title' in body.keys():
            item['title']=body['title']
        if 'description' in body.keys():
            item['description']=body['description']
        if 'minutes' in body.keys():
            item['minutes']=body['minutes']
        if 'servings' in body.keys():
            item['servings']=body['servings']
        if 'steps' in body.keys():
            item['steps']=body['steps']
        if 'ingredients' in body.keys():
            item['ingredients']=body['ingredients']
        
        try:
            self.table.put_item(Item=item)
            return self.getResponse(200,json.dumps(item, cls=CustomEncoder))
        except ClientError as e:
            self.logger.exception(e.response['Error']['Message'])
            exit(-1)       

    

    def modifyRecipe(self,id,key,value):
        UpdateExpression='SET #key = :value, #key2 = :value2'
        try:
            result = self.table.update_item(
                UpdateExpression=UpdateExpression,
                Key={
                'id': id,
                },
            ExpressionAttributeNames={
                '#key': key,
                '#key2': "updatedAt"
    
            },
            ExpressionAttributeValues={
                ':value': value,
                ':value2': str(time.time())
    
            },
            ReturnValues="UPDATED_NEW"
            )
            
            
            return self.getResponse(200,json.dumps(result['Attributes'], cls=CustomEncoder)) 
            
        except ClientError as e:
            self.logger.exception(e.response['Error']['Message'])
            exit(-1) 


    def getResponse(self,statusCode,body=None):
        response = {
            'statusCode': statusCode
        }
    
        if body is not None:
            response['body'] = json.dumps(body, cls=CustomEncoder)
        return response

def lambda_handler(event, context):

    if event:
        recipes =  Recipes()
        if event['httpMethod']=='GET':
            id = event['queryStringParameters']['id']
            response = recipes.retrieveRecipe(id)
        elif event['httpMethod']=='POST':
            body = json.loads(event['body'])
            response = recipes.createRecipe(body)
        elif event['httpMethod']=='PUT':
            body = json.loads(event['body'])
            response = recipes.modifyRecipe(body['id'],body['key'],body['value'])
        else:
            response = recipes.getResponse(404,'Not Found')
        
        return response
        

