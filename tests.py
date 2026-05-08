from magazzino import Magazzino
#from spedizione import Spedizione

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
