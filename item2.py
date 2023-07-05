import requests

while True:
    url = "https://www.mapquestapi.com/directions/v2/route?key=UYVlLC4Sc37nmBbFkjoDdHdiFTYCfcDn&from="
    print("/////////////////////////////////////////////////////////////////////////////////////////////")
    print("////////////////////////////////////////Bienvenido///////////////////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////////////////")
    desde = input("Ingrese la ciudad de partida o ingrese la letra (s) para salir : ")
    if desde == "s":
        break
    hasta = input("Ingrese la ciudad de destino: ")

    consulta = url + desde + str("&to=") + hasta

    print("La URL es" , consulta)

    vis = requests.get(consulta).json()

    print("//////////////////////////////// Consulta exitosa ///////////////////////////////////////////")
    print("La ruta consultada es desde : ", desde)
    print("Hasta : ", hasta)
    print("La distancia que hay entre las ciudades en kilometros es: " , round(vis["route"]["distance"] * 1.60934, 1), "KM")
    print("La duracion del viaje es: " , vis["route"]["formattedTime"], "(--> Horas:Minutos:Segundos)")
    print("Combustible requerido para el viaje:", round(vis["route"]["distance"] * 0.12, 1), "litros Aprox.") #suponiendo que se gasta 0.12 litros por km
    print("/////////////////////////////////////////////////////////////////////////////////////////////")
    print("Debe seguir las siguientes intrucciones para llegar a su destino:")
    print("/////////////////////////////////////////////////////////////////////////////////////////////")
    for rutacompl in vis["route"]["legs"][0]["maneuvers"]:
        print(rutacompl["narrative"])
