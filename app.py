from flask import *
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import pickle
import plotting_subject_values as psv
import time

# Load review file

# load the model from disk
filename = 'performance.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('transform.pkl','rb'))
app = Flask(__name__)
app.secret_key = "abc"  
sum =0
flag= 0 
@app.route('/')  
def index():  
    return render_template("index.html")  

@app.route('/front')
def front():
    global flag
    
    print('I am in front val {}'.format(flag))
    if flag == 0 :  
        return render_template("login.html") 
    if flag == 1:
        flag = 0 
        return render_template("front_page.html")
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/member')
def member():
    return render_template('perform.html')



@app.route('/login',methods = ["GET","POST"])  
def login():
    global flag
    error = None;  
    if request.method == "POST": 
        flag = 1 
        if request.form['pass'] != '1234' and request.form['email'] != 'a@g.com':  
            error = "invalid password or userId"  
        else:  
            #flash("you are successfuly logged in")
           #time.sleep(2)  
            return redirect(url_for('front'))  
    return render_template('login.html',error=error) 

@app.route('/predict',methods=['POST'])
def predict():
    global sum
#	df= pd.read_csv("spam.csv", encoding="latin-1")
#	df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
#	# Features and Labels
#	df['label'] = df['class'].map({'ham': 0, 'spam': 1})
#	X = df['message']
#	y = df['label']
#	
#	# Extract Feature With CountVectorizer
#	cv = CountVectorizer()
#	X = cv.fit_transform(X) # Fit the Data
#    
#    pickle.dump(cv, open('tranform.pkl', 'wb'))
#    
#    
#	from sklearn.model_selection import train_test_split
#	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#	#Naive Bayes Classifier
#	from sklearn.naive_bayes import MultinomialNB
#
#	clf = MultinomialNB()
#	clf.fit(X_train,y_train)
#	clf.score(X_test,y_test)
#    filename = 'nlp_model.pkl'
#    pickle.dump(clf, open(filename, 'wb'))
    
	#Alternative Usage of Saved Model
	# joblib.dump(clf, 'NB_spam_model.pkl')
	# NB_spam_model = open('NB_spam_model.pkl','rb')
	# clf = joblib.load(NB_spam_model)
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
        fin_pred = int(my_prediction)
        sum += fin_pred

        psv.Plot(sum)
    return render_template('home.html',prediction = my_prediction)
        
        
if __name__ == '__main__':
	app.run(debug=True)