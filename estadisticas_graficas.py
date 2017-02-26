#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv 

# Se calculan por semana, el numero de cuantos tweets neutrales, positivos , negativos
def calcular_estadisticas(arch):
	tweets_neutrales = 0
	tweets_negativos = 0
	tweets_positivos = 0
	tweets_muy_positivos = 0
	tweets_muy_negativos = 0
	for row in arch:
		if row[1] != 'text':
			if row[1] == '0':
				tweets_neutrales += 1
			elif row[1] == '1':
				tweets_positivos += 1
			elif row[1] == '-1':
				tweets_negativos += 1
			elif row[1] >= '2':
				tweets_muy_positivos += 1
			elif row[1] <= '-2':
				tweets_muy_negativos += 1

	total_tweets = tweets_neutrales + tweets_positivos + tweets_negativos + tweets_muy_negativos + tweets_muy_positivos
	return [tweets_neutrales, tweets_positivos, tweets_negativos, tweets_muy_positivos, tweets_muy_negativos, total_tweets]

# Se dibuja las graficas tipo torta
def graficas_torta(est, title):
	plt.figure(title)
	tweets = [est[0],est[1],est[2],est[3],est[4]] # Definimos un vector con el % de visitas del top ten de países
	sentimiento = [u'Tweets Neutrales', u'Tweets Positivos', 'Tweets Negativos', 'Tweets Muy Positivos', 'Tweets Muy Negativos']  # Etiquetas para los quesitos
	explode = [0, 0, 0, 0, 0]  # Esto nos ayudará a destacar algunos quesitos
	plt.pie(tweets, labels = sentimiento, explode = explode, autopct='%1.1f%%')  # Dibuja un gráfico de quesitos
	plt.title(u'Estaditicas de la' + title)
	plt.legend()
	plt.show()

def graficas_torta_tipo_tweet(total1, total2, total3, total4, title):
	plt.figure(title)
	tweets = [total1,total2,total3,total4] # Definimos un vector con el % de visitas del top ten de países
	semana = [u'Primera Semana', u'Segunda Semana', 'Tercera Semana', 'Cuarta Semana']  # Etiquetas para los quesitos
	explode = [0, 0, 0, 0]  # Esto nos ayudará a destacar algunos quesitos
	plt.pie(tweets, labels = semana, explode = explode, autopct='%1.1f%%')  # Dibuja un gráfico de quesitos
	plt.title(u'' + title)
	plt.legend()
	plt.show()

# A ESTE LE FALTA (TIENE CIERTO ERROR)
def graficas2(total1, total2, total3, total4):
	semanas = ("Primera Semana", "Segunda Semana", "Tercera Semana", "Cuarta Semana")
	posicion_y = np.arange(len(semanas) + 1)
	unidades = (total1, total2, total3, total4)
	plt.bar(posicion_y, prima)

	plt.bar(posicion_y + 0.00, total1, color = "b", width = 0.25)
	plt.bar(posicion_y + 0.25, total2, color = "g", width = 0.25)
	plt.bar(posicion_y + 0.50, total3, color = "r", width = 0.25)
	plt.bar(posicion_y + 0.75, total4, color = "r", width = 0.25)

	plt.xticks(posicion_y, semanas)
	plt.xlabel('Numero de Tweets')
	plt.title("Total de Tweets Semanalmente")
	plt.show()


# Procedimientos para los datos de la primera semana
file1 = open('evaluado_csv_2017_01_22__2017_01_29.csv','rb')
reader = csv.reader(file1)
file1_result = calcular_estadisticas(reader)
graficas_torta(file1_result, ' Primera Semana')
print file1_result

# Procedimientos para los datos de la segunda semana
file2 = open('evaluado_csv_2017_01_30__2017_02_05.csv','rb')
reader = csv.reader(file2)
file2_result = calcular_estadisticas(reader)
#graficas_torta(file2_result, ' Segunda Semana')
print file2_result

# Procedimientos para los datos de la tercera semana
file3 = open('evaluado_csv_2017_02_06__2017_02_12.csv','rb')
reader = csv.reader(file3)
file3_result = calcular_estadisticas(reader)
#graficas_torta(file3_result, ' Tercera Semana')
print file3_result

# Procedimientos para los datos de la cuarta semana
file4 = open('evaluado_csv_2017_02_13__2017_02_19.csv','rb')
reader = csv.reader(file4)
file4_result = calcular_estadisticas(reader)
#graficas_torta(file4_result, ' Tercera Semana')
print file4_result

# Calculamos tweets neutrales durante un mes
#graficas_torta_tipo_tweet(file1_result[0], file2_result[0], file3_result[0], file4_result[0], 'Tweets Neutrales Durante el Mes')

# Calculamos tweets positivos durante un mes
#graficas_torta_tipo_tweet(file1_result[1], file2_result[1], file3_result[1], file4_result[1], 'Tweets Positivos Durante el Mes')

# Calculamos tweets negativos durante un mes
#graficas_torta_tipo_tweet(file1_result[2], file2_result[2], file3_result[2], file4_result[2], 'Tweets Negativos Durante el Mes')

# Calculamos tweets Muy Positivos durante un mes
#graficas_torta_tipo_tweet(file1_result[3], file2_result[3], file3_result[3], file4_result[3], 'Tweets Muy Positivos Durante el Mes')

# Calculamos tweets Muy Negativos durante un mes
#graficas_torta_tipo_tweet(file1_result[4], file2_result[4], file3_result[4], file4_result[4], 'Tweets Muy Negativos Durante el Mes')