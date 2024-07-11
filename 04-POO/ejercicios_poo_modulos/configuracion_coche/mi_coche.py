from coche_electrico.coche_electrico import Coche_electrico


miCocheElectrico = Coche_electrico('Toyota', 'Auris', 2024)

kilometrosActuales = int(input('Cuantos Km tiene tu coche? '))

print(miCocheElectrico)
print(miCocheElectrico.modelo_bateria)

print(miCocheElectrico.actualizacion_kilometros(kilometrosActuales))