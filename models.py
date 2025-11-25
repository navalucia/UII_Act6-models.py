from django.db import models

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    num_seguro_social = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    licencia_medica = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    motivo = models.TextField()
    estado_cita = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cita {self.id_cita}"


class HistorialMedico(models.Model):
    id_historial = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    medicamentos = models.TextField()
    notas = models.TextField()
    medico_tratante = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return f"Historial {self.id_historial}"


class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    numero_habitacion = models.CharField(max_length=10)
    tipo_habitacion = models.CharField(max_length=50)
    estado_habitacion = models.CharField(max_length=50)
    costo_diario = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Habitación {self.numero_habitacion}"


class Internacion(models.Model):
    id_internacion = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)
    diagnostico_ingreso = models.TextField()
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField()

    def __str__(self):
        return f"Internación {self.id_internacion}"


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    internacion = models.ForeignKey(Internacion, on_delete=models.SET_NULL, null=True, blank=True)
    cita = models.ForeignKey(Cita, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Factura {self.id_factura}"

