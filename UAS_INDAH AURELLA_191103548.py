#!/usr/bin/env python
# coding: utf-8

# In[2]:


def conv_reamur(celcius):
    convert_reamur = 4 * celcius / 5
    return convert_reamur

def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit

def main():
    temperature = int(input('Masukan Skala Celcius: '))

    print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_reamur(temperature)} Reamur')
    print(f'Hasil Konversi Suhu {temperature} C adalah {conv_farenheit(temperature)} Farenheit')

 
if __name__ =='__main__':
    main()


# In[5]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

if db.is_connected():
    print("Berhasil terhubung ke database")


# In[7]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE db_film")
print("Datebase berhasil dibuat!")


# In[9]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = """CREATE TABLE tblfilm (
    kode_id INT AUTO_INCREMENT PRIMARY KEY,
    judulfilm VARCHAR(255),
    jenis_film varchar(255)
    
)
"""
cursor.execute(sql)
print("tabel film berhasil dibuat!")


# In[12]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "INSERT INTO tblFilm (JudulFilm, Jenis_Film) VALUES (%s, %s)"
val = ("X-men: Dark Phoenix", "Action")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))


# In[14]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "INSERT INTO tblFilm (JudulFilm, Jenis_Film) VALUES (%s, %s)"
values = [
    ("Aladdin", "Fantasy"),
    ("Godilla II : King of the Monster","Fantasy"),
    ("John Wick: Chapter 3 - Parabellum","Action")
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))


# In[15]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "SELECT * FROM tblFilm"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)


# In[17]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "SELECT * FROM tblFilm"
cursor.execute(sql)

result = cursor.fetchone()

print(result)


# In[18]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "UPDATE tblFilm SET JudulFilm=%s, Jenis_Film=%s WHERE kode_id=%s"
val = ("X-Men: Dark Phoenix", "Fantasy Action", 1)
cursor.execute(sql, val)

db.commit()

print("{}data diubah".format(cursor.rowcount))


# In[19]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "DELETE FROM tblFilm WHERE kode_id=%s"
val = (1, )
cursor.execute(sql, val)

db.commit()

print("{}data dihapus".format(cursor.rowcount))


# In[ ]:




