from magazzino import Magazzino
from spedizione import Spedizione

print("========== PASSO 1 ==========")

m = Magazzino("Mario Rossi", "MAG-001", 100)

print("Creato magazzino:", m.responsabile, m.codice, m.scorta)

assert m.responsabile == "Mario Rossi"
assert m.codice == "MAG-001"
assert m.scorta == 100

m_default = Magazzino("Anna Bianchi", "MAG-002")

print("Creato magazzino default:", m_default)

assert m_default.scorta == 0

print("PASSO 1 OK\n")


# --------------------------------------------------

print("========== PASSO 2 ==========")

print("Stringa magazzino:", str(m))

assert str(m) == "Mario Rossi (MAG-001): 100 unità"

print(m)

print("PASSO 2 OK\n")



print("========== PASSO 3 ==========")

print("Scorta iniziale:", m.scorta)

risultato = m.carica(50)

print("Carica 50 ->", risultato)
print("Nuova scorta:", m.scorta)

assert risultato is True
assert m.scorta == 150

risultato = m.carica(0)

print("Carica 0 ->", risultato)
print("Scorta:", m.scorta)

assert risultato is False
assert m.scorta == 150

risultato = m.carica(-10)

print("Carica -10 ->", risultato)
print("Scorta:", m.scorta)

assert risultato is False
assert m.scorta == 150

print("PASSO 3 OK\n")



print("========== PASSO 4 ==========")

print("Scorta iniziale:", m.scorta)

risultato = m.scarica(30)

print("Scarica 30 ->", risultato)
print("Scorta:", m.scorta)

assert risultato is True
assert m.scorta == 120

risultato = m.scarica(0)

print("Scarica 0 ->", risultato)
print("Scorta:", m.scorta)

assert risultato is False
assert m.scorta == 120

risultato = m.scarica(-5)

print("Scarica -5 ->", risultato)
print("Scorta:", m.scorta)

assert risultato is False
assert m.scorta == 120

risultato = m.scarica(10000)

print("Scarica 10000 ->", risultato)
print("Scorta:", m.scorta)

assert risultato is False
assert m.scorta == 120

print("PASSO 4 OK\n")

# --------------------------------------------------
# --------------------------------------------------

print("========== PASSO 5 ==========")

mittente = Magazzino("Luca Verdi", "MAG-LV", 1000)
destinatario = Magazzino("Sara Neri", "MAG-SN", 200)

s = Spedizione(mittente, destinatario, 100, "Riassortimento")

print("Spedizione creata:")
print("Mittente:", s.mittente)
print("Destinatario:", s.destinatario)
print("Quantità:", s.quantita)
print("Descrizione:", s.descrizione)
print("Eseguita:", s.eseguita)

assert s.mittente is mittente
assert s.destinatario is destinatario
assert s.quantita == 100
assert s.descrizione == "Riassortimento"
assert s.eseguita is False

print("PASSO 5 OK\n")

# --------------------------------------------------

print("========== PASSO 6 ==========")

descrizione = str(s)

print("Descrizione spedizione:")
print(descrizione)

assert "in attesa" in descrizione
assert "Luca Verdi" in descrizione
assert "Sara Neri" in descrizione
assert "100" in descrizione

print("PASSO 6 OK\n")

# --------------------------------------------------

print("========== PASSO 7 ==========")

print("SCENARIO 1 - Esecuzione regolare")

print("Scorta mittente prima:", mittente.scorta)
print("Scorta destinatario prima:", destinatario.scorta)

risultato = s.esegui()

print("Esegui ->", risultato)

print("Scorta mittente dopo:", mittente.scorta)
print("Scorta destinatario dopo:", destinatario.scorta)

assert risultato is True
assert s.eseguita is True
assert mittente.scorta == 900
assert destinatario.scorta == 300

print(str(s))

print("\nSCENARIO 2 - Doppia esecuzione")

risultato = s.esegui()

print("Esegui di nuovo ->", risultato)

assert risultato is False
assert mittente.scorta == 900
assert destinatario.scorta == 300

print("\nSCENARIO 3 - Scorta insufficiente")

m2 = Magazzino("Tizio", "MAG-003", 50)
d2 = Magazzino("Caio", "MAG-004", 0)

s2 = Spedizione(m2, d2, 100)

print("Scorta mittente:", m2.scorta)

risultato = s2.esegui()

print("Esegui ->", risultato)

print("Scorta mittente dopo:", m2.scorta)
print("Scorta destinatario dopo:", d2.scorta)

assert risultato is False
assert m2.scorta == 50
assert d2.scorta == 0

print("\nSCENARIO 4 - Stesso magazzino")

m3 = Magazzino("Pluto", "MAG-005", 100)

s3 = Spedizione(m3, m3, 50)

risultato = s3.esegui()

print("Esegui ->", risultato)
print("Scorta:", m3.scorta)

assert risultato is False
assert m3.scorta == 100

print("\nSCENARIO 5 - Quantità non positiva")

m4 = Magazzino("Topolino", "MAG-006", 100)
d4 = Magazzino("Paperino", "MAG-007", 100)

s4 = Spedizione(m4, d4, 0)

risultato = s4.esegui()

print("Esegui quantità 0 ->", risultato)

assert risultato is False

s5 = Spedizione(m4, d4, -10)

risultato = s5.esegui()

print("Esegui quantità -10 ->", risultato)

assert risultato is False

print("\nPASSO 7 OK\n")

print("===================================")
print("TUTTI I TEST SONO STATI SUPERATI")
print("===================================")
