import os
import sys
from databasehelper import DBHelper
from get_words import get_words
from network_processor_word import NetworkProcessor
from process_caller import ProcessCaller
from constants import table_name
    
if __name__ == "__main__":
    dbHelper = DBHelper(table_name)
    if len(sys.argv) != 2:
        print("Invalid argument")
        exit()
    if sys.argv[1] == "network":
        letter=os.listdir("corpus")
        for s in letter:
            
            words = get_words(s)   
            for word in words:
                NetworkProcessor.process_word(word, dbHelper)
    elif sys.argv[1] == "video":
        ProcessCaller(table_name).run()
    else:
        print("Invalid argument")
    
    
    
    