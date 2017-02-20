#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas
from palabras_comunes import palabras_comunes

palabras_negativas = open("negative_words_es.txt","r")
palabras_positivas = open("positive_words_es.txt","r")

pn = [p.rstrip("\r\n") for p in palabras_negativas.readlines()]
pp = [p.rstrip("\r\n") for p in palabras_positivas.readlines()]


def quitarStopWords(tuit):
    palabras = tuit.lower().split(" ")
    nuevaLista = [palabra for palabra in palabras if (len(palabra) != 0) and palabra not in palabras_comunes and palabra[0] not in "@#0123456789"]
    return nuevaLista


def evaluarTuit(tuitListaPalabras):
    puntuacion = 0
    for palabra in tuitListaPalabras :
        if palabra in pn :
            puntuacion -= 1
        if palabra in pp :
            puntuacion += 1
        
    return puntuacion


datasets = ["csv_2017_01_22__2017_01_29.csv",
            "csv_2017_01_30__2017_02_05.csv",
            "csv_2017_02_06__2017_02_12.csv",
            "csv_2017_02_13__2017_02_19.csv"]


for dataset in datasets:
    
    datos = pandas.read_csv(dataset, usecols=[4])
    datosSinStopWords = datos.applymap(quitarStopWords)
    datosEvaluados = datosSinStopWords.applymap(evaluarTuit)
    datosEvaluados.to_csv("evaluado_"+dataset)
