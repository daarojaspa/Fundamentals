#%%import libraries 
import json
import os 
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI 
load_dotenv()


#%%function_call definition 
def listLocalFiles(directory="."):
    try:
        files=os.listdir(directory)
        for f in files:
            print(f)
        return {"files":files}
    except Exception as e:
        return{"error":str(e)}
    
Tools = [
    {
        "type": "function",
        "function": {
            "name": "listlocalfiles",
            "description": "list files in directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "directory from which it will list files"
                    }
                },
                "required": []
            }
        }
    }
]
##%%memory and validations
cache=[
    {
        "role":"user",
        "content":"your answers most be less than 300 tockens"
    }
]
def validations(user_input):
    if user_input.lower() in ["sayonara","exit","by"]:
        print("suerte socio")
        exit(
            
        )
def cache_management(user_input,user):
        cache.append(
            {
                "role":user,
                "content":user_input
            })


#%%main loop 
client=OpenAI()
while True :
    userInput=None
    while  userInput==None:
        userInput=input("sr:").strip()
    validations(userInput)
    cache_management(userInput,user="user")
    #gpt api already defines valid users
    responses=client.responses.create(
        model="gpt-5-nano-2025-08-07",
        input=cache,
        tools=Tools
    )
    dumboy=responses.output_text
    cache_management(dumboy,"assistant")
    for output in responses.output:
        if output.type=="function_calling":
            fn_name=output.name
            args=json.loads(output.arguments)
            print(f"the model conciders to call {fn_name}")
        elif output.type=="message":
            print(f"dummy:{output.content}")
# %%
