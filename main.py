from flask import Flask, render_template, url_for, request, redirect,jsonify

app = Flask(__name__)
import dayguesser
import random
import math

paramVars = {
        'month':0,
        'day': 1,
        'year': 1,
        'calendar_day':"0/0/0",
        'score':0,
        'streak':0,
        'alert_type':'success',
        'result_msg':'no_message'
    }
start = True
invalid = False
setDifficulty = 1

def numToDay(num):
    weekdays = {
    0:"sunday",1:"monday",2:"tuesday",3:"wednesday",
    4:"thursday",5:"friday",6:"saturday"}
    return weekdays[num]
def dayToNum(day):
    weekdays = {
    "sunday":0,"monday":1,"tuesday":2,"wednesday":3,
    "thursday":4,"friday":5,"saturday":6}
    if(day in weekdays.keys()):
        return weekdays[day]
    else:
        return -1

@app.route('/')
@app.route('/home',methods=["GET","POST"])
def home(): 
    global paramVars
    if(not invalid):
        paramVars['month'],paramVars['day'],paramVars['year']= dayguesser.genNewDate(setDifficulty)
        paramVars['calendar_day']=str(paramVars['month'])+"/"+str(paramVars['day'])+"/"+str(paramVars['year'])
    print("PARAM VARS FROM HOME")
    print(paramVars)
    difficulty_text = {1:'Easy',2:'Medium',3:'Hard'}
    return render_template("home.html",params=paramVars,start=start,invalid=invalid,difficulty=difficulty_text[setDifficulty])

@app.route('/about')
def about():
    return render_template("about.html",title = "About")

@app.route('/learn')
def learn():
    return render_template("learn.html", title = "Learn Da Way")

@app.route('/easy_difficulty')
def one_year():
    global setDifficulty
    setDifficulty = 1
    return redirect(url_for('home'))

@app.route('/medium_difficulty')
def one_century():
    global setDifficulty
    setDifficulty = 2
    return redirect(url_for('home'))

@app.route('/answer_submitted',methods=["POST"])
def answer_submitted():
    global start, paramVars, invalid
    start = False
    response = request.form['answer'].lower()
    correctAnswer = dayguesser.findDayOfTheWeek(paramVars)
    givenAnswer = dayToNum(response)
    if(givenAnswer == -1):
        invalid = True
        return redirect(url_for('home'))
    else:
        invalid = False

    if(correctAnswer == givenAnswer):
        paramVars["alert_type"]='success'
        paramVars['streak']+=1
        newPoints = random.randint(1,math.ceil(math.sqrt(paramVars['streak'])))
        paramVars['result_msg']="(+"+str(newPoints)+") You are correct! The answer was "+response
        paramVars['score']+=newPoints
    else:
        print("====INCORRECT====")
        print(paramVars)
        paramVars['score']-=1
        paramVars["alert_type"]='danger'
        paramVars['result_msg']="(-1) That is incorrect. You answered "+response+", the answer was "+numToDay(correctAnswer)
        paramVars['streak']=0
    
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)