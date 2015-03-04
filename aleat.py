#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

class aleat:
    
    def parse(self, request, rest):
        
        return None

    def process(self, parsedRequest):
        numAleatorio = str(random.randrange(10000))
        nuevaPagina = "http://localhost:1234/aleat/" + numAleatorio

        return ("200 OK",
        "<html><body><h1>URL'S ALEATORIAS</h1>" +
        "<p>Hola.<A HREF= "+ nuevaPagina +">Dame otra</A></p>" +
        "</body></html>")
