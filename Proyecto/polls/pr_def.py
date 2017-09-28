class funciones_profesor():
    def get_datos_H6(nombreP, carreraE, anioE, semestreE):
        try:
            ia = InstanciaAsignatura.object.filter(profesor=nombreP)
        except InstanciaAsignatura.DoesNotExist:
            print 'Inexistente'
            return ''
        if carreraE:
            ia.object.filter(Asignatura__MallaCurricular__Carrera__nombre=carreraE)
        if anioE:
            ia.object.filter(anio=anioE)
        if semestreE:
            ia.object.filter(semestre=semestreE)
        return ia
    
    def get_estudiantes_H7(nombreP, apellidoPE, apellidoME, nombreE, estadoE):
        try:
            ia = InscripcionAsignatura.object.filter(InstanciaAsignatura__profesor=nombreP)
        except InscripcionAsignatura.DoesNotExist:
            print 'Inexistente'
            return ''            
        if carreraE:
            ia.object.filter(InstanciaAsignatura__Asignatura__MallaCurricular__Carrera__nombre=carreraE)
        if anioE:
            ia.object.filter(InstanciaAsignatura__anio=anioE)
        if semestreE:
            ia.object.filter(InstanciaAsignatura__semestre=semestreE)
        if estadoE:
            ia.object.filter(EstadoInscripcion__estado=estadoE)  
        estudiantes = ia.values_list('estudiante')
        return estudiantes
