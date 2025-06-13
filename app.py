from flask import Flask, render_template, request #, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/body/")
def body():
    return render_template('body.html')

@app.route("/profile/")
def profile():
    return render_template('profile.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/form5")
def feb():
    return render_template('form5.html')

@app.route("/form6")
def form6():
    return render_template('form6.html')

@app.route("/index")
def index():
    return render_template('index.html')


# Factorial App function
@app.route("/calculate/<int:score>")
def factorial(score):
    return f"<h1>Calculated score is: {+score}</h1>"

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        result = int(request.form["Enter your number"])

        num = 1
        for i in range(1,result+1):
            num = i * num 
        return render_template('form.html',score=f"You entered '{result}' and the Factorial is: {num}")

# Fibonacci app function    
@app.route("/fpp/<int:fibonacci>")
def fibonacci(fibonacci):
    return f"<h1> Calculated score is: {+fibonacci}</h1>"

@app.route("/form2", methods=["GET","POST"])
def form2():
    if request.method=="GET":
        return render_template("form2.html")
    else:
        fibonacci_sequence = int(request.form["Enter your number"])
        febo = []
        n1=0
        n2=1
        for i in range(fibonacci_sequence):
            n3 = n1 + n2
            febo.append(n3)
            n1 = n2
            n2 = n3
        return render_template('form2.html',fibonacci=f"You entered '{fibonacci_sequence}' and the Fibonacci Sequence is: {febo}")

# Prime numbers
@app.route("/high/<int:value>")
def high(value):
    return f"<h5>Value is very high: {+value}</h5>"

@app.route("/body/", methods=['GET','POST'])
def result():
    if request.method=='GET':
        return render_template("body/.html")
    else:
        number = int(request.form["Enter your number"])
        prime = []
        for i in range(2,number):
            for j in range(2,number):
                if i%j==0:
                    break
            if i==j:
                prime.append(i)
                # print(i,end=' ')
        return render_template('body.html',value=f"You entered '{number}' and the Prime numbers are: {prime}")

# Longest word from text 
@app.route("/fe/<num>")
def word(num):
    return f"<h1> Calculated score is: {str(num)}</h1>"

@app.route("/form3", methods=["GET","POST"])
def form3():
    if request.method=="GET":
        return render_template("form3.html")
    else:
        word = request.form["Enter your number"]
        
        # dic = {}
        lenght = 0
        largest = ''
        for i in word.split():
            if len(i)>lenght:
                lenght = len(i)
                largest = i
        # dic[largest] = lenght
        return render_template('form3.html',num=f"You entered '{word}' and the Longest word is: '{largest}'")

# reverse numbers
@app.route("/low/<int:rever>")
def low(rever):
    return f"<h2>Low Value: {+rever}</h2>"

@app.route("/profile/", methods=['GET','POST'])
def reverse():
    if request.method=='GET':
        return render_template('profile.html')
    else:
        your_num = int(request.form['Enter your number'])
        d= your_num
        reverse = 0
        while your_num>0:
            new = your_num%10
            reverse = new + reverse * 10
            your_num = your_num//10
        return render_template('profile.html',rever=f"You entered '{d}' and the Reversed number is: '{reverse}'")

# Even or Odd
@app.route("/find/<int:put>")
def find(put):
    return f"<h3>num is:{+put}</h3>"

@app.route("/form4",methods=['GET','POST'])
def form4():
    if request.method=='GET':
        return render_template("form4.html")
    else:
        input_value = int(request.form['Enter your number'])
        if input_value%2==0:
            return render_template('form4.html',put=f"You entered '{input_value}' and your number is: Even")
        else:
            return render_template('form4.html',put=f"You entered '{input_value}' and your number is: Odd")

#BMI Checker
@app.route("/bmi/<int:data>")
def bmi(data):
    return f"<h3>bmi is {+data}</h3>"

@app.route("/form5", methods=['GET','POST'])
def form5():
    if request.method=='GET':
        return render_template("form5.html")
    else:
        weight = int(request.form['weight'])
        feet = float(request.form['hight'])

        hight = feet/3.28
        bmi = weight/(hight**2)
        if bmi>=30:
            return render_template("form5.html",data= f"Your weight is '{weight}' and your hight is '{feet}', So you belong to Obese category bcoz your BMI is: {bmi:.1f}")
        elif bmi>=25 and bmi<29.9:
            return render_template("form5.html",data= f"Your weight is '{weight}' and your hight is '{feet}', So you belong to Overweight category bcoz your BMI is: {bmi:.1f}")
        elif bmi>=18.5 and bmi<24.9:
            return render_template("form5.html",data= f"Your weight is '{weight}' and your hight is '{feet}', So you belong to Normal category bcoz your BMI is: {bmi:.1f}")
        elif bmi<18.5:
            return render_template("form5.html",data= f"Your weight is '{weight}' and your hight is '{feet}', So you belong to underweight category bcoz your BMI is: {bmi:.1f}")
        
# armstrong number
@app.route("/api/<int:dt>")
def arm(dt):
    return f"<h3>Dt of page is {dt}</h3>"

@app.route("/index", methods=['GET','POST'])
def armstrong():
    if request.method=='GET':
        return render_template("index.html")
    else:
        input_num = int(request.form['Enter your number'])
        n = 0
        sum = 0
        while n<len(str(input_num)):
            nu = int(str(input_num)[n])
            sum = sum + (nu)**3
            n = n + 1
        if input_num==sum:
            return render_template("index.html",dt=f"You entered '{input_num}' and your number is: 'Armstrong number'")
        else:
            return render_template("index.html",dt=f"You entered '{input_num}' and your number is: 'Not-Armstrong number'")
        
# Pelindrome checker
@app.route("/pe/<int:pen>")
def pelin(pen):
    return f"pen number is{pen}"

@app.route("/form6",methods=['GET','POST'])
def pelindrome():
    if request.method=='GET':
        return render_template("form6.html")
    else:
        pen_value = request.form['Enter your number']
        check = pen_value.lower()
        if check==check[::-1]:
            return render_template("form6.html",pen=f"You entered '{pen_value}' and it is a: 'Pelindrome'")
        else:
            return render_template("form6.html",pen=f"You entered '{pen_value}' and it is a: 'Non-Pelindrome'")

if __name__ == "__main__":
    # app.run(debug=True, port=8000)
    app.run()