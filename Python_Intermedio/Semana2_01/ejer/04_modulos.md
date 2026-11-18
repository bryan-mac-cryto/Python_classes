# Arquitectura y Definición de Módulos – Proyecto 08
**Simulador de Riego y Balance Hídrico del Suelo** | **Curso:** SW303 – LP1  
**Responsable:** Bryan Yllanes

---

## 1. Flujo de Interacción Modular

El sistema aplica programación **modular estructurada en C estándar** (`C99/C11`), dividiendo la arquitectura en 6 pares de archivos (`.h` para interfaces/estructuras y `.c` para implementación):

```text
[ datos_climaticos ] ──(P_t, ET_t)──┐
                                    ├──> [ balance_hidrico ] <──(I_t)── [ control_riego ]
[ parametros_suelo ] ──(CC,PMP,RAW)─┴─────────────────────────────────────────┘
                                                 │
                                                 ▼ (Historial EstadoDia)
                                    ┌────────────────────────┐
                                    ▼                        ▼
                             [ indicadores ]           [ reportes ]
                         (I_total, N_deficit)      (Salida CSV / Gráfica)
```

---

## 2. Especificación de Módulos

### 2.1 `datos_climaticos` (`.h` / `.c`)
* **Función:** Lee y valida ($P_t \ge 0$, $ET_t \ge 0$) los registros diarios desde el CSV (RF-01, RNF-06).
* **Estructura y Prototipos:**
```c
typedef struct {
    int dia;
    double precipitacion;       // P_t (mm)
    double evapotranspiracion;  // ET_t (mm)
} RegistroClima;

int cargar_datos_climaticos(const char *ruta_csv, RegistroClima **registros, int *total_dias);
void liberar_datos_climaticos(RegistroClima *registros);
```

### 2.2 `parametros_suelo` (`.h` / `.c`)
* **Función:** Configura y valida las propiedades físicas del suelo ($CC > PMP$, $0 \le H_1 \le CC$) (RF-02, RNF-06).
* **Estructura y Prototipos:**
```c
typedef struct {
    double capacidad_campo;    // CC (mm)
    double punto_marchitez;    // PMP (mm)
    double agua_aprovechable;  // RAW (mm)
    double humedad_inicial;    // H_1 (mm)
} ParametrosSuelo;

ParametrosSuelo inicializar_suelo(double cc, double pmp, double raw, double h_inicial);
int validar_parametros_suelo(const ParametrosSuelo *suelo);
```

### 2.3 `control_riego` (`.h` / `.c`)
* **Función:** Calcula el riego diario $I_t$ según estrategia fija (por intervalo) o por umbral ($A_t = CC - H_t \ge RAW$) (RF-06).
* **Estructuras y Prototipos:**
```c
typedef enum { ESTRATEGIA_FIJA, ESTRATEGIA_UMBRAL } TipoEstrategia;

typedef struct {
    TipoEstrategia estrategia;
    int intervalo_dias;
    double dosis_fija;    // I_fijo (mm)
    double dosis_umbral;  // I_umbral (mm)
} ConfiguracionRiego;

int validar_configuracion_riego(const ConfiguracionRiego *config);
double calcular_riego_diario(const ConfiguracionRiego *config, const ParametrosSuelo *suelo, double humedad_actual, int dia);
```

### 2.4 `balance_hidrico` (`.h` / `.c`)
* **Función:** Motor diario de conservación de masa ($H_t^* = H_t + P_t + I_t - ET_t$) y drenaje ($D_t = \max(0, H_t^* - CC)$) (RF-03, RF-04).
* **Estructura y Prototipos:**
```c
typedef struct {
    int dia;
    double humedad_inicial, precipitacion, riego, evapotranspiracion, drenaje, humedad_final;
    int alerta_estres;
} EstadoDia;

EstadoDia simular_dia(int dia, double h_actual, RegistroClima clima, const ParametrosSuelo *suelo, const ConfiguracionRiego *riego);
EstadoDia* ejecutar_simulacion_completa(const RegistroClima *clima, int total_dias, const ParametrosSuelo *suelo, const ConfiguracionRiego *riego);
```

### 2.5 `indicadores` (`.h` / `.c`)
* **Función:** Evalúa alertas críticas y calcula el consumo total ($I_{total}$) y días con déficit ($H_{t+1} < PMP$) (RF-05, RF-07).
* **Estructura y Prototipos:**
```c
typedef struct {
    double consumo_total_riego;  // I_total (mm)
    double drenaje_total;        // Suma D_t (mm)
    int dias_deficit_hidrico;    // N_deficit
    int dias_alerta_umbral;
} ResumenIndicadores;

int verificar_alerta_humedad(double humedad_final, const ParametrosSuelo *suelo);
ResumenIndicadores calcular_indicadores(const EstadoDia *historial, int total_dias, const ParametrosSuelo *suelo);
```

### 2.6 `reportes` (`.h` / `.c`)
* **Función:** Exporta la tabla diaria a CSV, compara estrategias en consola y grafica la evolución (ASCII/Raylib) (RF-08, RNF-04).
* **Prototipos:**
```c
int exportar_resultados_csv(const char *ruta_salida, const EstadoDia *historial, int total_dias, const ResumenIndicadores *indicadores);
void mostrar_comparacion_consola(const ResumenIndicadores *res_fijo, const ResumenIndicadores *res_umbral);
void graficar_evolucion_ascii(const EstadoDia *historial, int total_dias, const ParametrosSuelo *suelo);
```

---

## 3. Trazabilidad Rápida

| Módulo | Cabecera | RF / RNF | Rol Principal |
| :--- | :--- | :--- | :--- |
| `datos_climaticos` | `datos_climaticos.h` | RF-01, RNF-03, RNF-06 | Lectura y validación de CSV climático |
| `parametros_suelo` | `parametros_suelo.h` | RF-02, RNF-06 | Parámetros físicos del suelo ($CC, PMP, RAW$) |
| `control_riego` | `control_riego.h` | RF-06 | Reglas de riego fijo vs. por umbral |
| `balance_hidrico` | `balance_hidrico.h` | RF-03, RF-04 | Cálculo diario de humedad y drenaje |
| `indicadores` | `indicadores.h` | RF-05, RF-07 | Alertas y métricas acumuladas |
| `reportes` | `reportes.h` | RF-08, RNF-03, RNF-04 | Salida CSV y gráficos ASCII / Raylib |