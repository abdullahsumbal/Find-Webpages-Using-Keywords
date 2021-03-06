from flask import Flask, render_template, flash, redirect, url_for, session, request, make_response
from helper import *
app = Flask(__name__)
app.secret_key = 'hamzaelahgdfgsdfdfgisquash'

@app.route('/')
def index():
    return redirect(url_for('home'))
    # return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if('WebsiteURL' not in request.form or 'Keywords' not in request.form):
        links= {"":("None")}
        return render_template('search.html', links=links, num=len(links))
    else:

        url = request.form['WebsiteURL']
        keywords = request.form['Keywords'].split()

        locNet = urlparse(url).netloc
        sameDomain = True

        visited = []
        current_level = 0
        level_limit = request.form['SelectLevel']

        keywords_pattern = re.compile('|'.join(keywords))
        DFS(url, visited, current_level, level_limit, locNet, sameDomain)
        # print(visited)
        links = filter(visited, keywords_pattern)
        print(links)
        return render_template('search.html', links=links, num=len(links))

if __name__ == '__main__':
   app.run(debug = True)
