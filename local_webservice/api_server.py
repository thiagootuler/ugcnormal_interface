#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, json, Response
import requests
import subprocess
import io
import re
import os, errno

app = Flask(__name__)
file_path = "./temp/file.txt"
directory = os.path.dirname(file_path)

class normalizer(object):
    def __init__(self):
        None
    
    def file_save(self, text):
        #if subprocess.call('ls ./temp/'.split()):
        #    suprobcess.call('rm ./temp/file.txt'.split())
        File = io.open("./temp/file.txt", mode="w", encoding="utf-8")
        File.write(text.decode('utf-8'))
        File.close()
    
    def tokenizer(self, text):
        print("Aplicando o tokenizador...")
        #'echo' + request.json['text'] + ' | ./tokenizer/webtok'
        echo = subprocess.Popen(['echo', text], stdout=subprocess.PIPE)
        tokenize = subprocess.Popen(['./tokenizer/webtok'], stdin=echo.stdout, stdout=subprocess.PIPE)
        output = tokenize.communicate()[0]
        return output

    def speller(self, text):
        tokens = self.tokenizer(text)
        print("Aplicando o speller...")
        self.file_save(tokens)
        #subprocess.call('perl ./spell.pl -stat ./speller/lexicos/regra+cb_freq.txt -f ./input/in.txt > ./output/out.txt'.split())
        #process = subprocess.Popen('perl ./spell.pl -stat ./speller/lexicos/regra+cb_freq.txt -f ./temp/file.txt'.split(), shell=False, stdout=subprocess.PIPE)
        actual_direcory = subprocess.Popen('pwd', shell=False, stdout=subprocess.PIPE)
        previous_path = actual_direcory.communicate()[0]
        command = 'perl ./spell.pl -stat ./lexicos/regra+cb_freq.txt -f ' + previous_path[:-1] + '/temp/file.txt'
        process = subprocess.Popen(command.split(), shell=False, stdout=subprocess.PIPE, cwd='./speller/')
        output = process.communicate()[0]
        return output
    
    def acronym_searcher(self, text):
        checked_text = self.speller(text)
        print("Normalizando siglas...")
        self.file_save(checked_text)
        process = subprocess.Popen('perl ./siglas_map.pl ./resources/lexico_siglas.txt ./temp/file.txt'.split(), shell=False, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output
        
    def untextese(self, text):
        text_with_acronyms = self.acronym_searcher(text)
        print("Normalizando internetes...")
        self.file_save(text_with_acronyms)
        process = subprocess.Popen('perl internetes_map.pl ./resources/lexico_internetes.txt ./resources/lexico_internetes_sigl_abrv.txt ./temp/file.txt'.split(), shell=False, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output

    def proper_noun_normalizer(self, text):
        without_textese = self.untextese(text)
        print("Normalizando nomes proprios...")
        self.file_save(without_textese )
        process = subprocess.Popen('perl np_map.pl ./resources/lexico_nome_proprio.txt ./temp/file.txt'.split(), shell=False, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output     
    
@app.route('/')
def test():
    return 'It works!'

@app.route('/token', methods=['POST'])
def token():
    output = normalizer().tokenizer(request.json['text'])
    data = {"result" : output.split()}
    json_response = json.dumps(data, ensure_ascii = False)
    response = Response(json_response, content_type="application/json; charset=utf-8")
    return response

@app.route('/spell', methods=['POST'])
def spell():
    output = normalizer().speller(request.json['text'])
    data = {"result" : output}
    json_response = json.dumps(data, ensure_ascii = False)
    response = Response(json_response, content_type="application/json; charset=utf-8")
    return response
    
@app.route('/acronym', methods=['POST'])
def acronym():
    output = normalizer().acronym_searcher(request.json['text'])
    data = {"result" : output}
    json_response = json.dumps(data, ensure_ascii = False)
    response = Response(json_response, content_type="application/json; charset=utf-8")
    return response
    
@app.route('/textese', methods=['POST'])
def textese():
    output = normalizer().untextese(request.json['text'])
    data = {"result" : output}
    json_response = json.dumps(data, ensure_ascii = False)
    response = Response(json_response, content_type="application/json; charset=utf-8")
    return response

@app.route('/proper_noun', methods=['POST'])
def proper_noun():
    output = normalizer().proper_noun_normalizer(request.json['text'])
    data = {"result" : output}
    json_response = json.dumps(data, ensure_ascii = False)
    response = Response(json_response, content_type="application/json; charset=utf-8")
    return response

if __name__ == '__main__':
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    app.run()
