import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('TREMBLAY', 'Antoine', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('GAGNON', 'Nicolas', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '0'))
cur.execute("INSERT INTO livres (nom, prenom, emprunter) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '0'))

cur.execute("INSERT INTO emprunt (clientsID, livresID) VALUES (?, ?)",('1', '1'))


connection.commit()
connection.close()
