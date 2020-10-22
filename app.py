from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__, template_folder='templates')
app.secret_key = 'mysecretkey'

@app.route('/')
def introduction():
    return(render_template('intro.html'))


@app.route('/Rules&Regualtions', methods=['GET', 'POST'])
def rules_regulation():
    return(render_template('rules.html'))


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return(render_template('404.html'), 404)

@app.route('/mysteriousbook', methods=['GET', 'POST'])
def index():
    return(render_template('1.html'))


@app.route('/navigation', methods=['GET', 'POST'])
def stage1():
    
    answer = 'ALDOL32'
    wrong_ans = False
    
    if request.method == 'POST':

        user_ans = request.form['user_ans']
        print(user_ans)

        if user_ans.upper() == answer:
            return(render_template('2.html'))
        
        else:
            wrong_ans = True
            return(render_template('1.html', wrong_ans=wrong_ans))

    return(render_template('1.html', wrong_ans=wrong_ans))
        

@app.route('/crypticmessage', methods=['GET', 'POST'])
def stage2():
    
    answer = 'ELEPHANTA ISLAND'
    wrong_ans = False
    
    if request.method == 'POST':

        user_ans = request.form['user_ans']
        print(user_ans)

        if user_ans.upper() == answer:
            return(render_template('3.html'))
        
        else:
            wrong_ans = True
            return(render_template('2.html', wrong_ans=wrong_ans))

    return(render_template('2.html', wrong_ans=wrong_ans))


@app.route('/logo', methods=['GET', 'POST'])
def stage3():
    
    answer = 'CERATANIUM'
    wrong_ans = False
    
    if request.method == 'POST':

        user_ans = request.form['user_ans']
        print(user_ans)

        if user_ans.upper() == answer:
            return(render_template('4.html'))
        
        else:
            wrong_ans = True
            return(render_template('3.html', wrong_ans=wrong_ans))

    return(render_template('3.html', wrong_ans=wrong_ans))
  

@app.route('/crossword', methods=['GET', 'POST'])
def stage4():
    
    answer = 'METALLURGICAL CENTRE'
    wrong_ans = False
    
    if request.method == 'POST':

        user_ans = request.form['user_ans']
        print(user_ans)

        if user_ans.upper() == answer:
            return(render_template('5.html'))
        
        else:
            wrong_ans = True
            return(render_template('4.html', wrong_ans=wrong_ans))

    return(render_template('4.html', wrong_ans=wrong_ans))
  
@app.route('/emojiandbinary', methods=['GET', 'POST'])
def stage5():
    
    answer = 'NATIONAL PARK'
    wrong_ans = False
    
    if request.method == 'POST':

        user_ans = request.form['user_ans']
        print(user_ans)

        if user_ans.upper() == answer:
            return(render_template('6.html'))
        
        else:
            wrong_ans = True
            return(render_template('5.html', wrong_ans=wrong_ans))

    return(render_template('5.html', wrong_ans=wrong_ans))
  

@app.route('/destination', methods=['GET', 'POST'])
def stage6():
    
    answer = 'WORLI FORT'
    wrong_ans = False
    
    if request.method == 'POST':

        user_ans = request.form['user_ans']
        print(user_ans)

        if user_ans.upper() == answer:
            return(render_template('7.html'))
        
        else:
            wrong_ans = True
            return(render_template('6.html', wrong_ans=wrong_ans))

    return(render_template('6.html', wrong_ans=wrong_ans))
  

@app.route('/finale', methods=['GET', 'POST'])
def stage7():
    
    answer = 'POWER UNLOCKED'
    wrong_ans = False
    
    if request.method == 'POST':

        user_ans = request.form['user_ans']
        print(user_ans)

        if user_ans.upper() == answer:
            return(render_template('end.html'))
        
        else:
            wrong_ans = True
            return(render_template('7.html', wrong_ans=wrong_ans))

    return(render_template('7.html', wrong_ans=wrong_ans))
  

if __name__ == "__main__":
    app.run(debug=True)
