from ejemplo.models import Auto

Auto(marca="Ford", modelo="EcoSport", ano=2013, kilometros=60000).save()
Auto(marca="Volkswagen", modelo="Suran", ano=2014, kilometros=90000).save()
Auto(marca="Ford", modelo="Fiesta", ano=2016, kilometros=75000).save()
Auto(marca="Ford", modelo="Focus", ano=2010, kilometros=120000).save()
print("Se cargo con éxito los autos de pruebas")
