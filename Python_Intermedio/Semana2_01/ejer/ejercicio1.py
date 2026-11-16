class CuentaUsuario:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)

    def recargar(self, monto):
        self.saldo += monto
        print(f"El nuevo saldo es s/.{self.saldo}")

    def pagar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Pago realizado con exito")
        else:
            print("Saldo insuficiente")

cuenta = CuentaUsuario("Bryan", 100)
cuenta.recargar(30)
cuenta.pagar(80)



