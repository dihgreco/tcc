import gspread
from datetime import datetime
from enum import Enum
from google.oauth2 import service_account

class Status(Enum):
    SLAUGHTER = "slaughter"
    JACK_POL7 = "jack_pol7"
    TRAN_WEL3 = "tran_wel3"
    TRAN_WEL2 = "tran_wel2"
    PETROSKI = "petroski"

class IPAQ(Enum):
    MUITO_ATIVO = "Muito Ativo"
    ATIVO = "Ativo"
    IRREGULARMENTE_ATIVO_A = "Irregularmente Ativo A, realizar avaliação por bioimpiedância é o mais indicado"
    IRREGULARMENTE_ATIVO_B = "Irregularmente Ativo B, realizar avaliação por bioimpiedância é o mais indicado"
    SEDENTARIO = "Sedentário, realizar avaliação por bioimpiedância é o mais indicado"

class IMC(Enum):
    PESO_BAIXO_MG = "Peso baixo Muito Grave"
    PESO_BAIXO_G = "Peso baixo Grave"
    PESO_BAIXO = "Peso baixo"
    EUTROFICO = "Eutrófico"
    NORMAL = "Normal"
    SOBREPESO = "Sobrepeso"
    OBESIDADE = "Obesidade"
    OBESIDADE_1 = "Obesidade Grau 1"
    OBESIDADE_2 = "Obesidade Grau 2"
    OBESIDADE_3= "Obesidade Grau 3"

def imc_elderly (altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 23:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 23.1 and imc_value <= 28:
        imc_status = IMC.NORMAL
    if imc_value >= 28.1 and imc_value <= 30:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_adult (altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 16:
        imc_status = IMC.PESO_BAIXO_MG
    if imc_value > 16 and imc_value <= 16.9:
        imc_status = IMC.PESO_BAIXO_G
    if imc_value > 17 and imc_value <= 18.49:
        imc_status = IMC.PESO_BAIXO_G
    if imc_value >= 18.5 and imc_value <= 24.9:
        imc_status = IMC.NORMAL
    elif imc_value >= 25.0 and imc_value <= 29.9:
        imc_status = IMC.SOBREPESO
    elif imc_value >= 30.0 and imc_value <= 34.9:
        imc_status = IMC.OBESIDADE_1
    elif imc_value >= 35.0 and imc_value <= 39.9:
        imc_status = IMC.OBESIDADE_2
    else:
        imc_status = IMC.OBESIDADE_3

    return imc_status, imc_value

# Crianças de 6 - 19 anos (femiinino)
def imc_teen_f6(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 14.3:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 14.4 and imc_value <= 16.1:
        imc_status = IMC.NORMAL
    if imc_value >= 16.2 and imc_value <= 17.4:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f7(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 14.9:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 15 and imc_value <= 17.1:
        imc_status = IMC.NORMAL
    if imc_value >= 17.2 and imc_value <= 18.9:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f8(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 15.6:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 15.7 and imc_value <= 18.1:
        imc_status = IMC.NORMAL
    if imc_value >= 18.2 and imc_value <= 20.3:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f9(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 16.3:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 16.4 and imc_value <= 19.1:
        imc_status = IMC.NORMAL
    if imc_value >= 19.2 and imc_value <= 21.7:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f10(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 17:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 17.1 and imc_value <= 20.1:
        imc_status = IMC.NORMAL
    if imc_value >= 20.2 and imc_value <= 23.2:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f11(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 17.6:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 17.7 and imc_value <= 21.1:
        imc_status = IMC.NORMAL
    if imc_value >= 21.2 and imc_value <= 24.5:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f12(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 18.3:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 18.4 and imc_value <= 22.1:
        imc_status = IMC.NORMAL
    if imc_value >= 22.2 and imc_value <= 25.9:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f13(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 18.9:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 19 and imc_value <= 23:
        imc_status = IMC.NORMAL
    if imc_value >= 23.1 and imc_value <= 27.7:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f14(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 19.3:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 19.4 and imc_value <= 23.8:
        imc_status = IMC.NORMAL
    if imc_value >= 23.9 and imc_value <= 27.9:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_f15_19(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 19.6:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 19.7 and imc_value <= 24.2:
        imc_status = IMC.NORMAL
    if imc_value >= 24.3 and imc_value <= 28.8:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

# Crianças de 6 - 19 anos (femiinino)
def imc_teen_m6(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 14.5:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 14.6 and imc_value <= 16.6:
        imc_status = IMC.NORMAL
    if imc_value >= 16.7 and imc_value <= 18:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m7(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 15:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 15.1 and imc_value <= 17.3:
        imc_status = IMC.NORMAL
    if imc_value >= 17.4 and imc_value <= 19.1:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m8(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 15.6:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 15.7 and imc_value <= 16.7:
        imc_status = IMC.NORMAL
    if imc_value >= 16.8 and imc_value <= 20.3:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m9(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 16.1:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 16.2 and imc_value <= 18.8:
        imc_status = IMC.NORMAL
    if imc_value >= 18.9 and imc_value <= 21.4:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m10(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 16.7:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 16.8 and imc_value <= 19.6:
        imc_status = IMC.NORMAL
    if imc_value >= 19.7 and imc_value <= 22.5:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m11(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 17.2:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 17.3 and imc_value <= 20.3:
        imc_status = IMC.NORMAL
    if imc_value >= 20.4 and imc_value <= 23.7:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m12(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 17.8:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 17.9 and imc_value <= 21.1:
        imc_status = IMC.NORMAL
    if imc_value >= 21.2 and imc_value <= 24.8:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m13(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 18.5:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 18.6 and imc_value <= 21.9:
        imc_status = IMC.NORMAL
    if imc_value >= 22 and imc_value <= 25.9:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m14(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 19.2:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 19.3 and imc_value <= 22.7:
        imc_status = IMC.NORMAL
    if imc_value >= 22.8 and imc_value <= 26.9:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def imc_teen_m15_19(altura,peso):
    altura_m = altura / 100
    imc_value = peso / (altura_m**2)
    if imc_value <= 19.9:
        imc_status = IMC.PESO_BAIXO
    if imc_value >= 20 and imc_value <= 23.6:
        imc_status = IMC.NORMAL
    if imc_value >= 23.7 and imc_value <= 27.7:
        imc_status = IMC.SOBREPESO
    else:
        imc_status = IMC.OBESIDADE

    return imc_status, imc_value

def calculate_age(nascimento):
    nano, nmes, ndia = nascimento.split("-")
    ano = datetime.now()
    idade1 = ano.year - int(nano)
    if ano.month < int(nmes) or (ano.month == int(nmes) and ano.day < int(ndia)):
        resultado = idade1 - 1
        return (resultado)
    else:
        return (idade1)

def calculate_status(idade, genero):
    if (idade < 18):
        return Status.SLAUGHTER
    elif (genero == "M" and idade <= 59):
        return Status.JACK_POL7
    elif (genero == "M" and idade >= 60):
        return Status.TRAN_WEL3
    elif (genero == "F" and idade<= 59):
        return Status.PETROSKI

    return Status.TRAN_WEL2

def calculate_imc(genero, idade, altura, peso):
    # criar todas as chamadas de imc
    if (idade >= 60):
        imc_status, imc_value = imc_elderly(
            altura=altura,
            peso=peso
        )
    elif (idade >= 20):
        imc_status, imc_value = imc_adult(
            altura=altura,
            peso=peso
        )
    elif (genero =="F"):
        #6-19 feminino
        if (idade == 6):
            imc_status, imc_value = imc_teen_f6(
                altura=altura,
                peso=peso
            )
        elif (idade == 7):
            imc_status, imc_value = imc_teen_f7(
                altura=altura,
                peso=peso
            )
        elif (idade == 8):
            imc_status, imc_value = imc_teen_f8(
                altura=altura,
                peso=peso
            )
        elif (idade == 9):
            imc_status, imc_value = imc_teen_f9(
                altura=altura,
                peso=peso
            )
        elif (idade == 10):
            imc_status, imc_value = imc_teen_f10(
                altura=altura,
                peso=peso
            )
        elif (idade == 11):
            imc_status, imc_value = imc_teen_f11(
                altura=altura,
                peso=peso
            )
        elif (idade == 12):
            imc_status, imc_value = imc_teen_f12(
                altura=altura,
                peso=peso
            )
        elif (idade == 13):
            imc_status, imc_value = imc_teen_f13(
                altura=altura,
                peso=peso
            )
        elif (idade == 14):
            imc_status, imc_value = imc_teen_f14(
                altura=altura,
                peso=peso
            )
        else:
            imc_status, imc_value = imc_teen_f15_19(
                altura=altura,
                peso=peso
            )
    #6-19 anos masculino
    elif (genero == "M"):
        if (idade == 6):
            imc_status, imc_value = imc_teen_m6(
                altura=altura,
                peso=peso
            )
        elif (idade == 7):
            imc_status, imc_value = imc_teen_m7(
                altura=altura,
                peso=peso
            )
        elif (idade == 8):
            imc_status, imc_value = imc_teen_m8(
                altura=altura,
                peso=peso
            )
        elif (idade == 9):
            imc_status, imc_value = imc_teen_m9(
                altura=altura,
                peso=peso
            )
        elif (idade == 10):
            imc_status, imc_value = imc_teen_m10(
                altura=altura,
                peso=peso
            )
        elif (idade == 11):
            imc_status, imc_value = imc_teen_m11(
                altura=altura,
                peso=peso
            )
        elif (idade == 12):
            imc_status, imc_value = imc_teen_m12(
                altura=altura,
                peso=peso
            )
        elif (idade == 13):
            imc_status, imc_value = imc_teen_m13(
                altura=altura,
                peso=peso
            )
        elif (idade == 14):
            imc_status, imc_value = imc_teen_m14(
                altura=altura,
                peso=peso
            )
        else:
            imc_status, imc_value = imc_teen_m15_19(
                altura=altura,
                peso=peso
            )

    return imc_status, imc_value

def calculate_parq(questionario):
    return not any(filter(lambda q: q == 'S', questionario.values()))

def calculate_ipaq(ipaq):
    horas0, minutos0 = ipaq.get('1c').split(':')
    horas1, minutos1 = ipaq.get('1e').split(':')
    horas2, minutos2 = ipaq.get('1g').split(':')
    horas3, minutos3 = ipaq.get('2b').split(':')
    horas4, minutos4 = ipaq.get('2d').split(':')
    horas5, minutos5 = ipaq.get('2f').split(':')
    horas6, minutos6 = ipaq.get('3b').split(':')
    horas7, minutos7 = ipaq.get('3d').split(':')
    horas8, minutos8 = ipaq.get('3f').split(':')
    horas9, minutos9 = ipaq.get('4b').split(':')
    horas10, minutos10 = ipaq.get('4d').split(':')
    horas11, minutos11 = ipaq.get('4f').split(':')
    horas12, minutos12 = ipaq.get('5a').split(':')
    horas13, minutos13 = ipaq.get('5b').split(':')

    vigorosa_hora = sum([int(horas0), int(horas6), int(horas10)])
    vigorosa_minutos = sum([int(minutos0), int(minutos6), int(minutos10)]) + (vigorosa_hora *60)
    vigorosa_dia = sum([int(ipaq.get('1b')),
                        int(ipaq.get('3a')),
                        int(ipaq.get('4c'))])

    caminhada_hora = sum([int(horas2), int(horas5), int(horas9)])
    caminhada_minutos = sum([int(minutos2), int(minutos5), int(minutos9)]) + (caminhada_hora * 60)
    caminhada_dia = sum([int(ipaq.get('1f')),
                         int(ipaq.get('2e')),
                         int(ipaq.get('4a'))])

    moderada_hora = sum([int(horas1), int(horas7), int(horas8), int(horas11)])
    moderada_minutos = sum([int(minutos1), int(minutos7), int(minutos8), int(minutos11)]) + (moderada_hora * 60)
    moderada_dia = sum([int(ipaq.get('1d')),
                        int(ipaq.get('3c')),
                        int(ipaq.get('3e')),
                        int(ipaq.get('4e'))])

    qualquer_atividade_hora = int(horas4)
    qualquer_atividade_minutos = int(minutos4) + (qualquer_atividade_hora * 60)
    qualquer_atividade_dia = int(ipaq.get('2c'))

    soma_dias = sum([vigorosa_dia, moderada_dia, caminhada_dia, qualquer_atividade_dia])
    soma_minutos = sum([vigorosa_minutos, moderada_minutos, caminhada_minutos, qualquer_atividade_minutos])

    # Verificação

    muito_ativo_a = vigorosa_dia >= 5 and vigorosa_minutos >= 150
    muito_ativo_b = vigorosa_dia >= 3 and vigorosa_minutos >= 60
    muito_ativo_c = caminhada_dia >= 5 and caminhada_minutos >= 150
    if (muito_ativo_a or muito_ativo_b or muito_ativo_c):
        return IPAQ.MUITO_ATIVO

    ativo_a = vigorosa_dia >= 3 and vigorosa_minutos >= 60
    ativo_b = moderada_dia >= 5 and moderada_minutos >= 150
    ativo_c = caminhada_dia >= 5 and caminhada_minutos >= 150
    ativo_d = qualquer_atividade_dia >= 5 and qualquer_atividade_minutos >= 150
    if (ativo_a or ativo_b or ativo_c or ativo_d):
        return IPAQ.ATIVO

    if (soma_dias >= 5 or soma_minutos >= 150):
        return IPAQ.IRREGULARMENTE_ATIVO_A

    if (soma_minutos > 10 and (soma_dias < 5 or soma_minutos < 150)):
        return IPAQ.IRREGULARMENTE_ATIVO_B
    
    return IPAQ.SEDENTARIO

# RECEBER DADOS DO FORMS
def receber_dados(email):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file('unique-provider-451418-a7-f5c5e75273e3.json', scopes=scope)
    client = gspread.authorize(credentials)

    anamnese = client.open("Anamnese (respostas)").sheet1
    ipaq = client.open("IPAQ (QUESTIONARIO INTERNACIONAL DE ATIVIDADE FISICA) (respostas)").sheet1
    parq = client.open("PAR-Q(Questionário de Prontidão para Atividade Física) (respostas)").sheet1

    def search_by_email(sheet, email):
        records = sheet.get_all_records()
        for record in records:
            if record.get('Email') == email:
                return record
        return None

    anamnese_data = search_by_email(anamnese, email)
    ipaq_data = search_by_email(ipaq, email)
    parq_data = search_by_email(parq, email)

    return {
        'anamnese': anamnese_data,
        'ipaq': ipaq_data,
        'parq': parq_data
    }

# def vo2_max():
#     velocidade = input(int('Velocidade em km/h do ultimo esstágio completado'))
#     vo2_max_ = 31.025 + (3.238 * velocidade) - (3.248 * anos) + (0.1536 * anos * velocidade)
#     print(vo2_max_)
# def tanaka():
#     tanaka_ = 208 - (0.7 * anos)
#     print(tanaka_)
# def pam():
#     pam_ = (pad + (pas - pad)) / 3
#     print(pam_)
# def slaughter():
#     slaughter_ = (0.735 * (tri + pa)) + 1
#     print(slaughter_)
# def jack_pol7():
#     dobras = sub + tri + pei + abd + si + cx + max_
#     jack_pol7_ = 1.112 - (0.00043499 * dobras) + (0.00000055 * (dobras * dobras)) - (0.00028826 *anos)
#     percent_g7 = (457 / jack_pol7_) - 414.2
#     print(percent_g7)
# def tran_wel3():
#     tran_wel3_ = -47.371817 + (0.57914807 * cab) + (0.25189114 * cqua) + (0.21366088 * cil) - (0.35595404 *pc)
#     print(tran_wel3_)
# def tran_wel2():
#     tran_wel2_ = 1.168297 - (0.002824 * cab) + (0.0000122098 * (cab * cab)) - (0.000733128 * cqua) + \
#                  (0.000510477 * atot) - (0.000216161 * anos)
#     print(tran_wel2_)
# def petroski():
#     petroski_ =  1.03465850 – 0.00063129 (max_ + si + cx + pt)**2 – 0.000311 ( idade_milesimal() ) – 0.00048890 (pc) + 0.00051345 (atot)
#     print(petroski_)
