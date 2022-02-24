from flask import Flask

# we maken een object met de naam app van de Flask module
app = Flask(__name__)

@app.route('/')  # dit leidt onze webpagina naar de juiste functie
def home():    
    return \
        """
        <center>
            <h1>Jens</h1>
            <hr>
            <a href='/Data'><h2>Data</h2></a> 
            <a href='/Hobbies'><h2>Hobbies</h2></a>
        </center>
        """

@app.route('/Data')
def data():
    return \
        """
        <h1>Data</h1>
        
        """

@app.route('/Hobbies')
def hobbies():
    return "<h1>Hobbies</h1>"





if __name__ == "__main__":
    app.run(debug=True, port=8080)




# <a href="https://duckduckgo.com "> Duck Duck Go</a>
# <a href="www.hln.be"> www.hln.be</a>

# <a href="/id/Ismael">Ismael</a></br>
