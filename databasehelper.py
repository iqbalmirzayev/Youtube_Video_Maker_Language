import sqlite3

from word import Word


class DBHelper():
    def __init__(self, table_name):
        self.db=sqlite3.connect("DICTIONARY.db")
        self.cursor=self.db.cursor()
        self.table_name=table_name
        self.cursor.execute(f"""Create table if not exists {table_name} ( 
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                  word TEXT NOT NULL UNIQUE,
                  word_part TEXT NOT NULL,
                  meaning TEXT NOT NULL,
                  phrase TEXT,
                  synonym TEXT,
                  antonym TEXT )""")
        self.db.commit()


    def add_word(self, w_o: Word):
        try:
            self.cursor.execute(f"""INSERT INTO {self.table_name} (word, word_part, meaning, phrase,synonym, antonym) VALUES (?,?,?,?,?,?) """, [w_o.word, w_o.word_part, w_o.meaning, w_o.phrase, w_o.synonym,w_o.antonym])
            self.db.commit()
        except sqlite3.IntegrityError as e:
            pass
    
    def get_word(self, word:str)->Word:
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE word = ?",[word])
        data = self.cursor.fetchone()
        self.db.commit()
        
        if not data:
            return None
        return Word(*data)
    
    def get_all_words(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        data = self.cursor.fetchall()
        self.db.commit()
        if not data:
            return None
        return [Word(*data[i]) for i in range(len(data))]