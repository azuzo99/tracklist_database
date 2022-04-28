import sqlite3
import pandas as pd
from datetime import datetime

'''Create an engine and connect to sqlite3 base'''''

conn=sqlite3.connect('Tracks.db')
c=conn.cursor()
'''______________________________________________________________________________________________________________________________'''
c.execute('''CREATE TABLE IF NOT EXISTS unique_tracklist (id_wykonania text,id_utworu text,artysta text,tytul text)''')

'''Clear existing table in case of code check'''

#c.execute('DELETE FROM unique_tracklist');   

''' Loading  unique_tracks.txt data to table ( file is uploaded ) with specified path'''

def load_data_unique(path=r'C:\Users\Adam\python_projects\baza danych\unique_tracks.txt'):
    start_time=datetime.now()
    with open(path,'r',encoding='ISO-8859-1') as d:
        for line in d:
            id_wykonania,id_utworu,artysta,tytul= line.split('<SEP>')
            tytul=tytul.strip('\n')
            c.execute('INSERT INTO unique_tracklist (id_wykonania,id_utworu,artysta,tytul) VALUES (?,?,?,?)',(id_wykonania,id_utworu,artysta,tytul))
    end_time = datetime.now()
    print(f'Duration of unique data loading: {end_time-start_time}')

c.execute('''CREATE TABLE IF NOT EXISTS sample (id_uzytkownika text,id_utworu text,data text)''')

'''Clear existing table in case of code check'''

c.execute('DELETE FROM sample');   

''' Inserting triplets_sample_20p.txt data into table with specified path ( file is around 2 Gb so it is too big for uploading )'''
start_time=datetime.now()
def load_data_sample(path=r'C:\Users\Adam\python_projects\baza danych\triplets_sample_20p.txt'):
    start_time=datetime.now()
    with open(path,'r',encoding='ISO-8859-1') as d:
        for line in d:
            id_uzytkownika,id_utworu,data= line.split('<SEP>')
            data=data.strip('\n')
            c.execute('INSERT INTO sample (id_uzytkownika,id_utworu,data) VALUES (?,?,?)',(id_uzytkownika,id_utworu,data))
    end_time = datetime.now()
    print(f'Duration of sample data loading: {end_time-start_time}')


'''Create a function that will give us a top 5 played tracks'''
def top5():
    c.execute('SELECT tytul,artysta FROM unique_tracklist WHERE id_utworu in (SELECT id_utworu FROM sample GROUP BY id_utworu ORDER BY COUNT(id_utworu) DESC LIMIT 5)')
    print(pd.DataFrame(c.fetchall(),columns=['Tytuł','Wykonawca']))



'''Create a function that will give us a top played artits from database'''
def top_artist():
    c.execute('SELECT * FROM (SELECT id_utworu, COUNT(*) from sample GROUP BY id_utworu) AS tempo LEFT JOIN unique_tracklist ON tempo.id_utworu=unique_tracklist.id_utworu')
    data=pd.DataFrame(c.fetchall()).iloc[:,[4 ,1]]
    data.columns=['Artysta','Liczba']
    data=data.groupby('Artysta')['Liczba'].sum().nlargest(1)
    print(f'Największa liczba odtworzeń :{data}')

'''Execute'''
load_data_unique()
load_data_sample()
top5()
top_artist()


'''Close connection to database'''
conn.commit()
conn.close()