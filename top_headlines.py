from flask import Flask, render_template
import secrets
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'

@app.route('/<nm>/<s>')
def hello_name(nm,s):    
    baseurl='https://api.nytimes.com/svc/topstories/v2/'+ s +'.json'
    params={
        'api-key': secrets.api_key
    }
    ls=requests.get(baseurl,params).text
    ls=json.loads(ls)['results']
    result=[]
    i=0
    for l in ls:
        i+=1
        if i >5:
            break
        result.append(l['title']+' ('+l['url']+')')
    return render_template('user.html', name=nm, list=result, section = s)

if __name__ == '__main__':
    app.run(debug=True)
    