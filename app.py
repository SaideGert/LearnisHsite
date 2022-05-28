from flask import Flask, render_template, redirect, url_for
from github import Github

app = Flask(__name__)
g = Github('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').get_user().get_repo('LearnisH')


@app.route('/')
@app.route('/home')
@app.route('/house')
@app.route('/homepage')
def home():
    return render_template('index.html')


@app.route('/download')
def down():
    with open(mode='r', file='peoples.txt') as file:
        people = file.read()
        if people == '':
            people = 12493
    with open(mode='w+', file='peoples.txt') as file:
            file.write(str(people))
    return render_template('down.html', message=people)


@app.route('/starting_download')
def write():
    with open(mode='r', file='peoples.txt') as file:
        people = int(file.read())
    with open(mode='w', file='peoples.txt') as file:
        file.write(str(people+1))
    return redirect('https://github.com/SaideGert/LearnisHAppData/raw/main/InstallerLearnisH.exe')


@app.route('/learn_more')
def more():
    news = g.get_contents('news.txt').decoded_content.decode()
    ask = g.get_contents('ask.txt').decoded_content.decode().split('\n')
    ask1 = []
    new = []
    raw = {}
    for j in news.split('\n'):
        if len(j.split(':')) == 1:
            new.append(raw)
            raw = {}
            continue
        i = j.split(':')
        if i[0]=='date':
            raw['date'] = i[1]
        elif i[0] == 'title':
            raw['title'] = i[1]
        elif i[0] == 'little':
            raw['little'] = i[1]
        elif i[0] == 'id':
            raw['id'] = i[1]
        else:
            raw['text'] = i[1]
    paw = []
    for i in range(len(ask)):
        if (i+1)%2==1:
            paw.append(ask[i])
        else:
            paw.append(ask[i])
            ask1.append(paw)
            paw = []
    print(ask1)
    return render_template('more.html', new=new, len=len(new), ask=ask1)


@app.route('/news/<id>')
def news(id):
    news = g.get_contents('news.txt').decoded_content.decode()
    new = []
    raw = {}
    for j in news.split('\n'):
        if len(j.split(':')) == 1:
            new.append(raw)
            raw = {}
            continue
        i = j.split(':')
        if i[0] == 'date':
            raw['date'] = i[1]
        elif i[0] == 'title':
            raw['title'] = i[1]
        elif i[0] == 'little':
            raw['little'] = i[1]
        elif i[0] == 'id':
            raw['id'] = i[1]
        else:
            raw['text'] = i[1]
    res = []
    for i in new:
        if int(i['id']) == int(id):
            res = i
    return render_template('news.html', res=res)


@app.route('/about')
def contact():
    ask = g.get_contents('about.txt').decoded_content.decode().split('\n')
    return render_template('cont.html', res=ask)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
