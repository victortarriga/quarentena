import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def primoss():
    primos = ""
    for num in range(1,542):  #contador dos 100 primeiros números primos!
        count = 0
        for numb in range(1,num+1):  #aqui é pra ver quantas vezes é dividido até chegar nele mesmo.
            if num % numb == 0:     # se ele for divisivel conta 1
                count += 1
        if count ==2:        #pra um número ser primo, só pode ser divisel 2x
            primos += str(num) + ', '   
    return (primos [0:len(primos)-2])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)