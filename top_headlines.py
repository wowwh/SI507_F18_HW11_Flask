from flask import Flask, render_template
import secrets
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'

@app.route('/<nm>')
def hello_name(nm):
    baseurl='https://api.nytimes.com/svc/search/v2/articlesearch.json'
    params={
        'api-key': secrets.api_key,
        'q': "technology",
        'fl': "web_url,headline"
    }
    ls=requests.get(baseurl,params).text
    ls=json.loads(ls)['response']['docs']
    result=[]
    i=0
    for l in ls:
        i+=1
        if i >5:
            break
        result.append(l['headline']['main']+' ('+l['web_url']+')')
    return render_template('user.html', name=nm, list=result)

if __name__ == '__main__':
    app.run(debug=True)