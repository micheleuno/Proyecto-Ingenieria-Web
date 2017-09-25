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
        
    def get_datos_H9(rutE, carreraE, anioE, semestreE, estadoE)
        insc = InscripcionAsignatura.object.filter(estudiante__rut=rutE)
        if carreraE:
            insc.object.filter(carrera=carreraE)
        if anioE:
            insc.object.filter(InstanciaAsignatura__anio=anioE)
        if semestreE:
            insc.object.filter(InstanciaAsignatura__semestre=semestreE)
        if estadoE:
            insc.object.filter(estadoInscripcion=estadoE)
        return insc