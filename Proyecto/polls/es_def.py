class funciones_etudiante():
    def get_datos_H8(rutE):
        try:
            es = Estudiante.object.get(rut=rutE)
        except Estudiante.DoesNotExist:
            print 'Inexistente'
            es = ''
        return es
        
    def set_datos_H8(rutE, direccionE, correoE)
        es = get_datos_H8(rutE)
        es.direccion = direccionE
        es.correo = correoE
        es.save()
        
    def get_datos_H9(rutE, carreraE, añoE, semestreE, estadoE)
        es = get_datos_H8(rutE)
        ia = InstanciaAsignatura.object.filter(estudiante=es)
        if carreraE:
            ia.filter(carrera=carreraE)
        if añoE:
            ia.filter(año=añoE)
        if semestreE:
            ia.filter(semestre=semestreE)
        if estadoE:
            ia.filter(estado=estadoE)
        return ia