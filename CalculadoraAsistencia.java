import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CalculadoraAsistencia {

    // Listas para reuniones de mitad de semana y fines de semana
    static List<Integer> reunionesMitadDeSemana = new ArrayList<>();
    static List<Integer> reunionesFinDeSemana = new ArrayList<>();
    static List<Integer> asistenciaMitadDeSemana = new ArrayList<>();
    static List<Integer> asistenciaFinDeSemana = new ArrayList<>();

    public static void main(String[] args) {
        // Llenar las listas pidiendo datos al usuario
        llenarDatos("Mitad de Semana", reunionesMitadDeSemana, asistenciaMitadDeSemana);
        llenarDatos("Fin de Semana", reunionesFinDeSemana, asistenciaFinDeSemana);

        String[] meses = {"Junio", "Julio", "Agosto", "Septiembre"};

        System.out.println("\nResultados:");
        for (int i = 0; i < meses.length; i++) {
            int asistenciaTotal = asistenciaMitadDeSemana.get(i) + asistenciaFinDeSemana.get(i);
            double promedioAsistenciaSemanal = calcularPromedioAsistenciaSemanal(i);

            System.out.println("Mes: " + meses[i]);
            System.out.println("Asistencia Total: " + asistenciaTotal);
            System.out.println("Promedio Asistencia Semanal: " + promedioAsistenciaSemanal);
            System.out.println();
        }
    }

    public static void llenarDatos(String tipoReunion, List<Integer> reuniones, List<Integer> asistencia) {
        Scanner scanner = new Scanner(System.in);
        String[] meses = {"Junio", "Julio", "Agosto", "Septiembre"};

        for (String mes : meses) {
            System.out.print("Ingresa el número de reuniones de " + tipoReunion + " para " + mes + ": ");
            reuniones.add(scanner.nextInt());

            System.out.print("Ingresa la asistencia para " + tipoReunion + " en " + mes + ": ");
            asistencia.add(scanner.nextInt());
        }
    }

    public static double calcularPromedioAsistenciaSemanal(int mesIndex) {
        int totalReuniones = reunionesMitadDeSemana.get(mesIndex) + reunionesFinDeSemana.get(mesIndex);
        int totalAsistencia = asistenciaMitadDeSemana.get(mesIndex) + asistenciaFinDeSemana.get(mesIndex);
        
        // Evitar división por cero
        if (totalReuniones == 0) {
            return 0.0;
        }

        return (double) totalAsistencia / totalReuniones;
    }
}
