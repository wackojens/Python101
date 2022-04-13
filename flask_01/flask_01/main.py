from flask import Flask

# we maken een object met de naam app van de Flask module
app = Flask(__name__)

@app.route('/')  # dit leidt onze webpagina naar de juiste functie
def home():    
    return \
        """
        <center>
            <h1 style="font-size:4em;">
                Jens</h1>
            <hr>
            <h2 style="font-size:3em;margin-block-start:4em;">
                <a href='/Data'>Data</a></h2>
            <h2 style="font-size:3em;margin-block-start:3em;">
                <a href='/Hobbies'>Hobbies</a></h2>
        </center>
        <div style="position:fixed;bottom:0px;width:100%;text-align:center;word-spacing:20px">
            <h5><a href='/'>Home</a>
            <a href='/Data'>Data</a>
            <a href='/Hobbies'>Hobbies</a></h5>
        </div>
        """

@app.route('/Data')
def data():
    return \
        """
        <center>
            <h1 style="font-size:4em;">
                Data</h1>
            <hr>
            <h2 style="font-size:2.5em;margin-block-start:4em;">
                Voornaam: Jens</h2>
            <h2 style="font-size:2.5em;margin-block-start:1em;">
                Achternaam: Coomans</h2>
            <h2 style="font-size:2.5em;margin-block-start:1em;">
                Leeftijd: 32</h2>
            <h2 style="font-size:2.5em;margin-block-start:1em;">
                Woonplaats: Hechtel-Eksel</h2>
        </center>
        <div style="position:fixed;bottom:0px;width:100%;text-align:center;word-spacing:20px">
            <h5><a href='/'>Home</a>
            <a href='/Data'>Data</a>
            <a href='/Hobbies'>Hobbies</a></h5>
        </div>
        """

@app.route('/Hobbies')
def hobbies():
    return \
        """
        <center>
            <h1 style="font-size:4em;">
                Hobbies</h1>
            <hr>
            <h2 style="font-size:3em;margin-block-start:4em;">
                <a href='/Hobbies/Gaming'>Gaming</a></h2>
            <h2 style="font-size:3em;margin-block-start:3em;">
                <a href='/Hobbies/Reizen'>Reizen</a></h2>
        </center>
        <div style="position:fixed;bottom:0px;width:100%;text-align:center;word-spacing:20px">
            <h5><a href='/'>Home</a>
            <a href='/Data'>Data</a>
            <a href='/Hobbies'>Hobbies</a></h5>
        </div>
        """

@app.route('/Hobbies/Gaming')
def gaming():
    return \
        """
        <body style=" margin-right: 0px;margin-left: 0px;margin-bottom: 0px;>
            <center>
                <h1 style="font-size:4em;">
                    Gaming</h1>
                <hr>
                <div style="display: flex">
                    <div style="flex:50%;">
                        <img src="/static/valheim.jpg"; style="width:100%">
                    </div>
                    <div style="flex:50%;">
                        <img src="/static/ark.jpg"; style="width:100%">
                    </div>
                </div>
                <div style="display: flex;">
                    <div style="flex:50%;">
                        <img src="/static/razerSetup.jpg"; style="width:100%;height:100%;">
                    </div>
                    <div style="flex:50%;">
                        <img src="/static/league.jpg"; style="width:100%;">
                    </div>
                </div>
            </center>
            <div style="position:fixed;bottom:0px;width:100%;text-align:center;word-spacing:20px">
                <h5><a href='/' style="color:#ffffff">Home</a>
                <a href='/Data' style="color:rgba(255,255,255,1)">Data</a>
                <a href='/Hobbies' style="color:white">Hobbies</a></h5>
            </div>
        </body>
        """



@app.route('/Hobbies/Reizen')
def reizen():
    return \
        """
        <center>
            <h1 style="font-size:4em;">
                Reizen</h1>
            <hr>
        </center>
        <div style="position:fixed;bottom:0px;width:100%;text-align:center;word-spacing:20px">
            <h5><a href='/'>Home</a>
            <a href='/Data'>Data</a>
            <a href='/Hobbies'>Hobbies</a></h5>
        </div>
        """


if __name__ == "__main__":
    app.run(debug=True, port=8080)




# <a href="https://duckduckgo.com "> Duck Duck Go</a>
# <a href="www.hln.be"> www.hln.be</a>

# <a href="/id/Ismael">Ismael</a></br>
