import os 
from databasehelper import DBHelper
from process_function import Processor        
        
class ProcessCaller:
    def __init__(self, table_name):
        self.db = DBHelper(table_name)
        self.dictionary = self.db.get_all_words()

    def run(self):
        for d in self.dictionary: 
            
            folder_name = "folders/{}".format(d.id)
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            if len(d.word) >13:
                    words = d.word.split() 
                    words_l = list(map(lambda x: len(x), words))
                    print(words_l)
                    words_div_min = []
                    for i, l in enumerate(words_l):
                        words_div_min.append(abs((sum(words_l[:i+1])/sum(words_l))-0.5))
                    i = words_div_min.index(min(words_div_min))
                    word1 = " ".join(words[:i+1])
                    word2 = " ".join(words[i+1:])
                    d.word = word1 + "\n" + word2

            Processor.word_to_image(d.word,d.id)
            Processor.word_part_to_image(d.word_part,d.id)
            Processor.meaning_image(word="Meaning",id=d.id)
            grup_sayisi=1
            print(d.meaning.split(":"))
            if d.meaning:
                meanings=d.meaning.split('\n')
                meanings = [x for x in meanings if ":" in x]
                for i in range(0, len(meanings), grup_sayisi):
                    grup =meanings[i:i+grup_sayisi]
                    grup_s = "\n".join(grup)
                    # print(grup_s)
                    Processor.meaning_to_image(d.id, grup_s)
                    print("\n\n\n")
            else:
                print(f"{d.word} menasi yoxdu")
            
            if d.phrase:
                phrases=d.phrase.split("\n")
                for i in phrases:
                    Processor.phrase_to_image(d.id,i)
                # print("yeni soz"*10)  
            else:
                print("soz yoxd")
            Processor.concatenate_all_videos(d.id)
            
            
            

