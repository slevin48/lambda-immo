from flask import Flask,request,jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/dvf')
def dvf_commune():
    # Read the official data 
    df = pd.read_csv("75.csv")
    df.code_commune = df.code_commune.astype(int)
    df_dict = df[df.code_commune == eval(request.args.get("code_commune"))].to_dict()
    return jsonify(df_dict)

# We only need this for local development
if __name__ == '__main__':
    app.run()