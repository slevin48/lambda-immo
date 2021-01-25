from flask import Flask,request,jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/')
def dvf_home():
    # render dataframe as html
    code_commune = 75114

    # return "<a href='http://127.0.0.1:5000/dvf?code_commune="+str(code_commune)+"'>http://127.0.0.1:5000/dvf?code_commune="+str(code_commune)+"</a>"
    
    # For local test

    # import urllib
    # import json    
    # try:
    #     url = "http://127.0.0.1:5000/dvf?code_commune="+str(code_commune)
    #     response = urllib.request.urlopen(url)
    #     html = response.read()
    #     json_data = json.loads(html)
    # except urllib.error.URLError:
    #         print("Erreur")

    import json
    with open(str(code_commune)+".json") as json_file:
        json_data = json.load(json_file)
    
    df = pd.DataFrame.from_dict(json_data)
    html = df.to_html()
    return(html) 

@app.route('/ls')
def dvf_ls():
    import os
    return jsonify(os.listdir())

@app.route('/dvf')
def dvf_commune():
    # # Fetch data from S3
    # s3 = boto3.client('s3')
    # bucket = "zappa-54ckqvw8t"
    # filename = "75.csv"
    # s3.download_file(bucket, filename,filename)

    # Read the official data 
    df = pd.read_csv("75.csv")
    df.code_commune = df.code_commune.astype(int)
    df_dict = df[df.code_commune == eval(request.args.get("code_commune"))].to_dict()
    # import json
    # with open("75114.json",'w') as outfile:
    #     json.dump(df_dict, outfile,indent=4)
    return jsonify(df_dict)

@app.route('/dvf2')
def dvf2():
    
    # Read the official data 
    df = pd.read_csv("75.csv")
    df.code_commune = df.code_commune.astype(int)
    df2 = df[df.code_commune == 75114]
    html = df2.to_html()
    return(html) 

@app.route('/dvf3')
def dvf3():
    return request.args.get("code")

# We only need this for local development
if __name__ == '__main__':
    app.run()