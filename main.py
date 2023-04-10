import os
import sys
import moviepy
import filetype
import requests
import json
from dotenv import load_dotenv;load_dotenv()



OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
input_file=sys.argv[1]
if os.path.isdir('outputs')==False:
   os.mkdir('outputs')
   
try:
    with open("prompt_instructions/instructions.txt",'r') as f:
         PROMPT=format(f.read())
except Exception as ex:
       print(ex)

def check_file():
    extensions=["3gp","mp4", "m4v", "mkv", "webm", "mov", "avi", "wmv", "mpg", "flv"]
    
    if os.path.isfile(input_file):
       file_ext=filetype.guess(input_file).extension
       if file_ext in extensions:
          pass
       else:
            print(f"Error: not a video: {input_file}")
            sys.exit()
    else:
         print(f"Error: can't open file: {input_file}")
         sys.exit()



def get_code(action):
    
    payload = {"model": "gpt-3.5-turbo", "messages": [

    {"role": "system", "content": "I will always check for errors in the code before write it and i will provide the fixed code"},
    {"role": "user", "content": f"Print some python code that uses moviepy to do the following stuff at video in path {input_file} and save output video to ./outputs using same filename as input: {action}\nEnclose the code block inside ::CODE_START:: and ::CODE_END:: tags. Pay attention to the Attribute 'duration' not set error"}
    
    
    ]}

    r = requests.post('https://api.openai.com/v1/chat/completions', headers = {'Content-Type': 'application/json','Authorization':f'Bearer {OPENAI_API_KEY}'}, data= json.dumps(payload))
    if r.ok:
       response=json.loads(r.text)["choices"][0]['message']['content']
       code=response[response.find("::CODE_START::")+14:response.find("::CODE_END::")].replace("`","").replace("python","")
       return 1,code
    else:
         return 0,json.loads(r.text)['error']['message']

check_file()
res=get_code(input("What you would like to do with this video?\n\n> "))
if res[0]==1:
   try:
       print(res[1])
       exec(res[1])
   except Exception as ex:
          print(ex)
else:
     print(res[1])

    

