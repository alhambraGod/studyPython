# -*- coding: utf-8 -*-
###########################################
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('template_home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('template_form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '456':
        return render_template('template_signin-ok.html', username = username)
    return render_template('template_form.html', message = 'Bad username or password', username = username)

if __name__ == '__main__':
    app.run()



###############################
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320129740415df73bf8f81e478982bf4d5c8aa3817a000
# 比如循环输出页码：
# {% for i in page_list %}
#     <a href="/page/{{ i }}">{{ i }}</a>
# {% endfor %}
# 如果page_list是一个list：[1, 2, 3, 4, 5]，上面的模板将输出5个超链接。
# 除了Jinja2，常见的模板还有：
# Mako：用<% ... %>和${xxx}的一个模板；
# Cheetah：也是用<% ... %>和${xxx}的一个模板；
# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
