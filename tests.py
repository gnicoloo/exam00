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
