import matplotlib.pyplot as plt # pip install matplotlib (COMANDO PARA INSTALAR)

# Questão 2
def dados_com_intervalos():
  rol = [61, 65, 43, 53, 55, 51, 58, 55, 59, 56,
        52, 53, 62, 49, 68, 51, 50, 67, 62, 64,
        53, 46, 48, 50, 61, 44, 64, 53, 54, 55,
        48, 54, 57, 41, 54, 71, 57, 53, 46, 48,
        55, 46, 57, 54, 48, 63, 49, 55, 52, 51]
  rol.sort()

#Determinando os intervalos de classe
  H = 5
  min_valor = min(rol)
  max_valor = max(rol)
  intervalos_classe = []

  for i in range(7):
    inicio = min_valor + i * H
    fim = inicio + H
    intervalos_classe.append((inicio, fim))

#Determinando a frequencai
  fi = [0] * len(intervalos_classe)
  for valor in rol:
    for i, intervalo in enumerate(intervalos_classe):
      if intervalo[0] <= valor < intervalo[1]:
        fi[i] += 1
        break


    # Chamando as funções
    pontos_medios = ponto_medio(intervalos_classe)
    fi_somatorio = somatorio_fi(fi)
    media = calculo_media(pontos_medios, fi, fi_somatorio)
    moda = calculo_moda(intervalos_classe, fi)
    mediana = calculo_mediana(intervalos_classe, fi, fi_somatorio)
    desvioPadrao = calculo_desvio_padrao(intervalos_classe, fi, fi_somatorio, media)
    quartil, decil3, decil7, percentil15, percentil90 = calcular_quartil_decil_percentil(fi_somatorio)

    return media, moda, mediana, desvioPadrao, pontos_medios, fi, intervalos_classe, quartil, decil3, decil7, percentil15, percentil90

def ponto_medio(intervalos_classe):
    pontos_medios = []

    for intervalo in intervalos_classe:
        xi = (intervalo[0] + intervalo[1]) / 2
        pontos_medios.append(xi)

    return pontos_medios

def somatorio_fi(fi):
    fi_somatorio = sum(fi)
    return fi_somatorio

def calculo_media(pontos_medios, fi, fi_somatorio):
    produto_xi_fi = 0

    for i in range(len(pontos_medios)):
        produto_xi_fi += pontos_medios[i] * fi[i]
    media = produto_xi_fi / fi_somatorio

    return media

def calculo_moda(intervalos_classe, fi):
    maior_fi = max(fi)
    posicao_maior_fi = fi.index(maior_fi)

    classe_maior_fi = intervalos_classe[posicao_maior_fi]
    moda = (classe_maior_fi[0] + classe_maior_fi[1]) / 2

    return moda

def calculo_mediana(intervalo_classes, fi, fi_somatorio):
    frequencia_acu = 0
    posicao_central = fi_somatorio / 2
    mediana = 0

    for i in range(len(intervalo_classes)):
        frequencia_acu += fi[i]
        if frequencia_acu >= posicao_central:
            classe_inferior = intervalo_classes[i][0]
            classe_superior = intervalo_classes[i][1]
            fi_da_classe = fi[i]
            f_acumulada_anterior = sum(fi[:i])
            mediana = classe_inferior + ((posicao_central - f_acumulada_anterior) / fi_da_classe) * (classe_superior - classe_inferior)
            break

    return mediana

def calculo_desvio_padrao(intervalos_classe, fi, fi_somatorio, media):
    soma_dos_quadrados = 0

    for i in range(len(intervalos_classe)):
        xi = (intervalos_classe[i][0] + intervalos_classe[i][1]) / 2
        diferenca = xi - media
        quadrado = diferenca ** 2
        produto = quadrado * fi[i]
        soma_dos_quadrados += produto

    variancia = soma_dos_quadrados / fi_somatorio

    desvio_padrao = variancia ** 0.5

    return desvio_padrao

def calcular_quartil_decil_percentil(fi_somatorio):
    q1 = 1 * (fi_somatorio) / 4
    d3 = 3 * (fi_somatorio + 1) / 10
    d7 = 7 * (fi_somatorio + 1) / 10
    p15 = 15 * (fi_somatorio + 1) / 100
    p90 = 90 * (fi_somatorio + 1) / 100

    return q1, d3, d7, p15, p90

# Resultados

media, moda, mediana, desvioPadrao, pontos_medios, fi, intervalos_classe, quartil, decil3, decil7, percentil15, percentil90 = dados_com_intervalos()

print(" Questão 2 \n")
print(f"A média é: {media}\n")
print(f"A moda é: {moda}\n")
print(f"A mediana é: {mediana}\n")
print(f"O desvio padrão é: {desvioPadrao}\n")
print(f"O quartil é (Q1):{quartil}\n O decil 3 é (D3):{decil3}\n O decil 7 é (D7):{decil7}\n O percentil15 é (P15):{percentil15}\n O percentil90 é (P90):{percentil90} \n")
print("Gráfico")

# Configurações do gráfico
plt.bar(pontos_medios, fi, width=50, color='skyblue', edgecolor='black')
plt.title('Gráfico')
plt.xlabel('Pontos Médios')
plt.ylabel('Frequência')
plt.show()