from openai import OpenAI 
from dotenv import load_dotenv
import numpy as np 
import pandas as pd
import json 
load_dotenv()
client = OpenAI()
cache=[
    {
        "role":"user",
        "content":"answers max length is  400 tokens "
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

    
def s_tool (operation,csvfile,column):

    df = pd.read_csv(csvfile)
    
    # Get the column data
    col_data = df[column]
    print (f"stool call , reading paper, finding de column")    
    # Perform operation based on input
    try:
        if operation == "average":
            result = np.mean(col_data)
        elif operation == "median":
            result = np.median(col_data)
        elif operation == "std":
            result = np.std(col_data)
        elif operation == "sum":
            result = np.sum(col_data)
        elif operation == "min":
            result = np.min(col_data)
        elif operation == "max":
            result = np.max(col_data)
        else:
            return "Don't understand that operation"
        return result
    except Exception as e:
        return f"Error: {e}" 
tools=[
    { #function calling documentation openAI 
        "type":"function",
        "function":{
            "name":"s_tool",
            "description":"performs statistical operations on a csv file",
            "parameters":{
                "type":"object",
                "properties":{
                    "operation":{
                        "type":"string",
                        "description":"operation to perform on the csv file",
                        "enum":["average","median","std","sum","min","max"]
                    },
                    "csvfile":{
                        "type":"string",
                        "description":"csv file to perform the operation on"
                    },
                    "column":{
                        "type":"string",
                        "description":"column to perform the operation on"
                    }
                },
                "required":["operation","csvfile","column"]
            }
        }
    }
]    

while True:
    
    user_input=input("expresámelo:"). strip()
    validations(user_input)
    responses= client.responses.create(
        model="gpt-5-nano-2025-08-07",
        input= user_input,
        tools=tools
        #tool_choice="auto"
    )
    #print(f"asistonto:{responses.output_text}")
    cache+= responses.output
    for output in responses.output:
        if output.type=="function_call" :
            fn_name=output.name
            args=json.loads(output.arguments)
            if fn_name=="s_tool":
               # result=s_tool(**args)
               
                print(f"should i call {fn_name}")
        elif output.type=="message":
            print(f"asistente{output.content}")