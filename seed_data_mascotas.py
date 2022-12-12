from ejemplo.models import Mascota

Mascota(nombre="Tyron", tipo= "Perro", raza="Dogo de burdeos", edad=4).save()
Mascota(nombre="arya", tipo="Perra", raza="Callejera", edad=3).save()
Mascota(nombre="cazzu", tipo="Gata", raza="Tricolor", edad=5).save()
Mascota(nombre="Brownie", tipo="Perro", raza="Ovejero Aleman", edad=7).save()
print("Se cargon con éxito las mascotas de prueba")