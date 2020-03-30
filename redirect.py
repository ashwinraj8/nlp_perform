from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)
counter = 100  

@app.route('/')
def home():
    return render_template('home.html')

    #return redirect(url_for('member'))



@app.route('/member')
def member():
    return render_template('perform.html')
if __name__ =='__main__':
    app.run(debug=True)