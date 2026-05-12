from flask import Flask

app = Flask(__name__)

@app.route('/')
def explicacao():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
     <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Decorator</title>
     </head>   
     <body>
        <h2> O que é o decorator? </h2>
        <p> O decorator é usado para implementar classes e/ou funções de modo fácil ao seu código</p>
     </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)