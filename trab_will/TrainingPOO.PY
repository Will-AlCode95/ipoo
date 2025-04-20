
class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    
    def acelerar(self, aumento):
        self.velocidade = self.velocidade + aumento

    def frear(self, diminuir):
        self.velocidade = self.velocidade - diminuir

meu_carro = Carro("Fiat", "Uno", 0) # Passando a velocidade inicial (0 neste caso)
print(f"Velocidade inicial: {meu_carro.velocidade}")

meu_carro.acelerar(10)
print(f"Velocidade após acelerar: {meu_carro.velocidade}")

meu_carro.acelerar(50)
print(f"Velocidade após acelerar: {meu_carro.velocidade}")

meu_carro.frear(20)
print(f"Velocidade após diminuir: {meu_carro.velocidade}")