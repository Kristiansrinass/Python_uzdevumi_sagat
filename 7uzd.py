"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
om"

saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
sarakts2=[]

for uzvards in sarakts1:
    doktors="Dr. "+uzvards
    sarakts2.append(doktors)
    print(sarakts2)
    """
#2 variants
saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
sarakts2=[]
def pievienot_dokt(uzvards):
    return "Dr. "+uzvards

sarakts2=list(map)
