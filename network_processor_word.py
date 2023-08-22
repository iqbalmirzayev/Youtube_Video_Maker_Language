from constants import url_template,url_template_2,headers
import requests
from bs4 import BeautifulSoup

from databasehelper import DBHelper
from word import Word

class  NetworkProcessor():
    @staticmethod
    def process_word(word, db:DBHelper):
        
        w = db.get_word(word)
        if w:
            return
        if " " in word:
            formatted_word="%20".join(word.split())
        else:
            formatted_word=word
        url = url_template.format(formatted_word)
        url_2=url_template_2.format(formatted_word)
        resp = requests.request(method="GET",url=url, headers=headers)
        resp_2 = requests.request(method="GET",url=url_2, headers=headers)
        soup=BeautifulSoup(resp.text,'lxml')
        soup_2=BeautifulSoup(resp_2.text,'lxml')
        
        
        
        if '/' not in word:
                id_id=id
                
                word_word=("{}".format(soup.find("h1").text)) #word
                word_wordpart=("{}".format(soup.find("h2").text))# nitq hissesi
                
                
                i=0
                word_meaning=""
                word_phrase=""
                word_antonym=""
                word_synonym=""
                for sp in soup.find_all("span",attrs={"class":"dtText"}):
                    
                    if sp==[] :
                        pass
                    else:
                        
                        
                        # if : have then write 
                        if ":" in sp.text:
                            i=i+1
                            word_meaning=word_meaning+("{}.{}\n".format(i,sp.text))
                        # else:
                        #     pass
                        
                i=0
            
                for sp2 in soup.find_all("span",attrs={"class":"mw_t_sp"}):
                    if sp2==[] :
                        pass
                    else:
                        
                        i=i+1
                        word_phrase=word_phrase+("{}. {}\n".format(i,sp2.text))
                        
                if_synonym=soup_2.find_all("div",attrs={"class":"mw-grid-table-list"})
                if if_synonym==[]:
                    pass
                else:
                    split_synonym=if_synonym[0].text
                    split_synonym=split_synonym.split()
                    for i in split_synonym:
                        word_synonym=word_synonym+("\n{}".format(i))
                    
                if_antonym=soup_2.find_all("div",attrs={"class":"mw-grid-table-list"})
                if if_antonym==[]:
                    pass
                else:
                    split_antonym=if_antonym[0].text
                    split_antonym=split_antonym.split()
                    for i in split_antonym:
                        word_antonym=word_antonym+("\n{}".format(i))
                        
                print(word_word)
                db.add_word(Word(id_id,word_word,word_wordpart,word_meaning,word_phrase,word_synonym,word_antonym))