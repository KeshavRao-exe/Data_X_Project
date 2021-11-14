from flask import Flask, render_template
from os import environ, getcwd
from matplotlib import pyplot as plt
from mine import mineit
#from crypto_value_prediction_update import forecast
#cmd = getcwd()
#print(cmd)

#preds, targets = forecast()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',title='Home Page')

@app.route('/mining/')
def mining():
    time_taken, hash_val = mineit()
    mining = open('FrontEnd/templates/mining.html').read().format(time_taken = time_taken, hash_val = hash_val)
    return mining
    #return render_template('mining.html', time_taken = time_taken, hash_val = hash_val)

@app.route('/forecast/')
def forecast():
    #plt.plot(preds,targets)
    #plt.scatter(preds,targets)
    #plt.plot(preds, color = 'red', label = 'Predicted Bitcoin Price')
    #plt.plot(targets, color = 'red', label = 'Predicted Cryptocurrency Price')
    #plt.ylabel('Price in USD')
    #plt.xlabel('Date')
    #plt.savefig('Data_X_Project/FrontEnd/static/my_plot.png')
    
    #img =  r'D:\My Projects\Data-X\Cryptoknight-Git\Data_X_Project\FrontEnd\myplot.png'
    return render_template('forecast.html')

@app.route('/about/')
def about():
    return render_template('about.html')    

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug = True)   