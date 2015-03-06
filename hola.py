#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import suma
import aleat

class hola(webapp.app):
    
    def parse(self, request, rest):
        
        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1> Hola. </h1></body></html>")

class adios(webapp.app):
   
    def parse(self, request, rest):
        
        return None

    de process(self, parsedRequest):

        return ("200 OK", "<html><body><h1> Adiós. </h1></body></html>")

if __name__ == "__main__":

    holaApp = hola()
    adiosApp = adios()
    aleatApp = aleat.aleat()
    sumaApp = suma.suma()

    testWebApp = webapp.webApp("localhost", 1234, {'/hola': holaApp, '/adios': adiosApp, '/aleat/': aleatApp, '/suma/': sumaApp})
