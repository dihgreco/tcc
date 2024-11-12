from flask import Flask, make_response, request
from utils import *

app = Flask("flask_app")

@app.route("/verify", methods=["POST"])
def verify():
    request_data = request.json

    altura = request_data["altura"]
    peso = request_data["peso"]
    nascimento = request_data["nascimento"]
    genero = request_data["genero"]
    ipaq = request_data["ipaq"]
    parq = request_data["parq"]

    # criar função para calcular a idade 1990-01-20
    idade = calculate_age(nascimento=nascimento)

    # calcular ipaq e parq
    ipaq_result = calculate_ipaq(ipaq)
    parq_result = calculate_parq(parq)

    imc_status, imc_value = calculate_imc(
        genero=genero,
        idade=idade,
        altura=altura,
        peso=peso
    )

    # Casos de Erro
    if not parq_result:
        return make_response({
            "error_message": "Erro ao calcular Parq."
        }, 500)

    # colocar todos os status na funcao
    status = calculate_status(
        idade = idade,
        genero=genero
    )

    return make_response({
        "status": status.value,
        "imc": imc_value,
        "imc_status": imc_status.value,
        "ipaq_result": ipaq_result.value
    }, 200)

@app.route(f"/{Status.SLAUGHTER.value}", methods=["POST"])
def slaughter():
    request_data = request.json

    tricipital = request_data["tricipital"]
    panturrilha = request_data["panturrilha"]

    # CHAMAR FUNCAO DO UTILS
    result = 13.5

    return make_response({
        Status.SLAUGHTER.value: result
    }, 200)

@app.route(f"/{Status.JACK_POL7.value}", methods=["POST"])
def jack_pol7():
    request_data = request.json

    subescapular = request_data["subescapular"]
    tricipital = request_data["tricipital"]
    peitoral = request_data["peitoral"]
    abdominal = request_data["abdominal"]
    suprailiaca = request_data["suprailiaca"]
    coxa = request_data["coxa"]
    axilar_media = request_data["axilar_media"]
    idade = request_data["idade"]

    # CHAMAR FUNCAO DO UTILS
    result = 13.5

    return make_response({
        Status.JACK_POL7.value: result
    }, 200)

@app.route(f"/{Status.TRAN_WEL3.value}", methods=["POST"])
def tram_wel3():
    request_data = request.json

    circunferencia_abdominal = request_data["circunferencia abdominal"]
    circunferencia_quadril = request_data["circunferencia quadril"]
    circunferencia_iliaca = request_data["circunferencia iliaca"]
    peso = request_data["peso"]

    # CHAMAR FUNCAO DO UTILS
    result = 13.5

    return make_response({
        Status.TRAN_WEL3.value: result
    }, 200)

@app.route(f"/{Status.TRAN_WEL2.value}", methods=["POST"])
def tram_wel2():
    request_data = request.json

    circunferencia_abdominal = request_data["circunferencia abdominal"]
    circunferencia_quadril = request_data["circunferencia quadril"]
    altura = request_data["altura"]

    # CHAMAR FUNCAO DO UTILS
    result = 13.5

    return make_response({
        Status.TRAN_WEL2.value: result
    }, 200)

app.run(debug=True, use_reloader=True)
