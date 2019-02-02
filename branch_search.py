import tree
from bs4 import BeautifulSoup as sp
import pyttsx3
import requests
from multiprocessing import Queue
import sys
import time

class SearchEngine:

    def __init__(self):
        self.name = "Test-Subject"
        self.engine = pyttsx3.init()
        self.original_data = " "

    def query_return(self):                #gt query from tree

        query_out = tree.Tree.recognizer()
        self.original_data = query_out
        return query_out

    def search_init(self):           #init the requests


        keyword = self.query_return()
        modified_word = keyword.replace(" ", "+")
        get_data = requests.get("https://duckduckgo.com/html/?q={}".format(modified_word))
        return get_data

    def search_process(self):             #get the actual result process


        data = self.search_init()
        x="\nSearching results.....\n"
        for i in x:
            print(i, end = " ")
            time.sleep(.200)
            sys.stdout.flush()

        #print("Searching for results....")
        soup = sp(data.content, "lxml")
        data_scrap = soup.find("a", {"class": "result__a"}).get_text()
        return data_scrap

    def search_result(self):  #the result


        result = self.search_process()
        print(self.original_data)

        time.sleep(3)
        print("Your query: {original}\nResult: {result}".format(original=self.original_data, result=result))
        self.engine.say("{}".format(result))
        self.engine.runAndWait()

q = SearchEngine()
q.search_result()
