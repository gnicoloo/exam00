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
