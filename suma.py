#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp

class suma(webapp.app):

    def parse(self, request, rest):
        
        try:
            numeros = rest.split('/')
            numero1 = int(numeros[0])
            numero2 = int(numeros[1])

        except ValueError:
            return None
        return (numero1,numero2)

    def process(self, parsedRequest):
        if not parsedRequest:

            return("400 Bad Request" ,
                   "<html><body><h1>Error!</h1>" +
                   "</body></html>")

        resultado = (str(parsedRequest[0]) + "+" + str(parsedRequest[1]) +
                    "=" + str(parsedRequest[0]+parsedRequest[1]))

        return("200 OK",
               "<html><body>" +
               "<h1>" + resultado +"</h1>" +
               "</body></html>")                 

