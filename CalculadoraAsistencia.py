import numpy as np

# Listas para reuniones de mitad de semana y fines de semana
reuniones_mitad_semana = [3, 5, 4, 4, 4, 4]
reuniones_fin_semana = [3, 4, 5, 3, 4, 5]
asistencia_mitad_semana = [374, 636, 497, 506, 491, 430]
asistencia_fin_semana = [391, 484, 636, 408, 480, 556]

def llenar_datos(tipo_reunion, reuniones, asistencia):
    pass  # No longer needed as data is directly included

def calcular_promedio_asistencia(mes_index, reuniones, asistencia):
    total_reuniones = reuniones[mes_index]
    total_asistencia = asistencia[mes_index]
    
    # Evitar división por cero
    if total_reuniones == 0:
        return 0.0

    return total_asistencia / total_reuniones

def calcular_promedio_mensual(asistencia, reuniones):
    total_asistencia = sum(asistencia)
    total_reuniones = sum(reuniones)
    
    # Evitar división por cero
    if total_reuniones == 0:
        return 0.0

    return total_asistencia / total_reuniones

def main():
    meses = ["Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    print("\nResultados:")
    for i in range(len(meses)):
        asistencia_total_mitad_semana = asistencia_mitad_semana[i]
        asistencia_total_fin_semana = asistencia_fin_semana[i]
        asistencia_total = asistencia_total_mitad_semana + asistencia_total_fin_semana
        promedio_asistencia_mitad_semana = calcular_promedio_asistencia(i, reuniones_mitad_semana, asistencia_mitad_semana)
        promedio_asistencia_fin_semana = calcular_promedio_asistencia(i, reuniones_fin_semana, asistencia_fin_semana)

        print(f"Mes: {meses[i]}")
        print(f"Número de Reuniones Mitad de Semana: {reuniones_mitad_semana[i]}")
        print(f"Asistencia Total Mitad de Semana: {asistencia_total_mitad_semana}")
        print(f"Promedio Asistencia Mitad de Semana: {promedio_asistencia_mitad_semana}")
        print("-" * 40)  # Línea divisoria
        print(f"Número de Reuniones Fin de Semana: {reuniones_fin_semana[i]}")
        print(f"Asistencia Total Fin de Semana: {asistencia_total_fin_semana}")
        print(f"Promedio Asistencia Fin de Semana: {promedio_asistencia_fin_semana}")
        print(f"Asistencia Total: {asistencia_total}")
        print()

    promedio_mensual_mitad_semana = calcular_promedio_mensual(asistencia_mitad_semana, reuniones_mitad_semana)
    promedio_mensual_fin_semana = calcular_promedio_mensual(asistencia_fin_semana, reuniones_fin_semana)

    print(f"Promedio Mensual de Asistencia Mitad de Semana: {promedio_mensual_mitad_semana}")
    print(f"Promedio Mensual de Asistencia Fin de Semana: {promedio_mensual_fin_semana}")

    input("Presiona Enter para cerrar...")

if __name__ == "__main__":
    main()