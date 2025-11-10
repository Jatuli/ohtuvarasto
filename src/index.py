from varasto import Varasto

def main():
    mehu, olut = tee_varastot()
    getterit(olut)
    setterit(mehu)
    varasto_virheet()
    lisays_virheet(mehu, olut)
    otto_virheet(mehu, olut)

def tee_varastot():
    mehu = Varasto(100.0)
    olut = Varasto(100.0, 20.2)
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu}")
    print(f"Olutvarasto: {olut}")
    return mehu, olut

def getterit(olut):
    print("Olut getterit:")
    print(f"saldo = {olut.saldo}")
    print(f"tilavuus = {olut.tilavuus}")
    print(f"paljonko_mahtuu = {olut.paljonko_mahtuu()}")

def setterit(mehu):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehu.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehu}")
    print("Otetaan 3.14")
    mehu.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehu}")

def varasto_virheet():
    print("Virhetilanteita:")
    huono1 = Varasto(-100.0)
    print(f"Varasto(-100.0): {huono1}")
    huono2 = Varasto(100.0, -50.7)
    print(f"Varasto(100.0, -50.7): {huono2}")

def lisays_virheet(mehu, olut):
    olut.lisaa_varastoon(1000.0)
    print(f"Lisätään 1000 olutvarastoon, Olutvarasto: {olut}")
    mehu.lisaa_varastoon(-666.0)
    print(f"Lisätään -666 mehuvarastoon, Mehuvarasto: {mehu}")

def otto_virheet(mehu, olut):
    saatiin = olut.ota_varastosta(1000.0)
    print(f"Otetaan 1000 olutvarastosta, saatiin {saatiin}, Olutvarasto:{olut}")
    saatiin = mehu.ota_varastosta(-32.9)
    print(f"Otetaan -32.9 mehuvarastosta,saatiin {saatiin}, Mehuvarasto:{mehu}")

if __name__ == "__main__":
    main()
