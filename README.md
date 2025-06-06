# solemne-2-optimizacion

## 📌 Descripción

Este proyecto corresponde a la **Solemne 2** del curso de Optimización. Su objetivo es implementar y comparar distintos algoritmos de optimización para resolver el problema de asignacion de turnos a guardias, evaluando su desempeño y eficiencia.

---

## ⚙️ Requisitos

- **Python:** Versión 3.12

**Bibliotecas necesarias:**

- `numpy`
- `matplotlib`
- `scipy`

> **Nota:** Se recomienda utilizar un entorno virtual para gestionar las dependencias.

---

## 🛠️ Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/crxsx0/solemne-2-optimizacion.git
    cd solemne-2-optimizacion
    ```

2. **Crear y activar un entorno virtual:**

    ```bash
    python3.12 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

    > **Nota:** Si el archivo `requirements.txt` no está presente, puedes instalar las bibliotecas manualmente:
    >
    > ```bash
    > pip install numpy matplotlib scipy
    > ```

---

## 🧠 Lógica y Arquitectura del Proyecto

La solución sigue una arquitectura modular organizada en las siguientes capas:

```
src/
├── algorithm/             # Algoritmos de optimización (solución inicial y búsqueda local)
│   └── heuristic/
│       └── heuristica.py
├── config/                # Parámetros globales como TURNOS
├── data/
│   ├── inputs/            # Archivos JSON con datos de entrada
│   └── outputs/           # Resultados finales generados
├── infrastructure/        # Cargadores de datos desde JSON
├── models/                # Modelos Pydantic para validación y serialización
├── services/
│   ├── grafo/             # Clases y lógica de grafos
│   ├── guardias/          # GuardiaPlanta y GuardiaOcasional
│   ├── locaciones/
│   └── nodo/              # Clase base Nodo
└── main.py                # Script principal de ejecución
```

### 📂 Explicación de Componentes

- **main.py:** Orquesta el flujo: carga datos, construye grafo, genera solución inicial y aplica heurística. Guarda las asignaciones finales optimizadas en JSON.
- **models/outputs.py:** Modelo `Asignacion` que representa cada fila del resultado.
- **services/guardias/:** Clases con lógica de turnos, validación de disponibilidad y costos.
- **services/locaciones/:** Nodos donde se asignan guardias.
- **services/nodo/:** Clase base `Nodo` con ID y vecinos conectados.
- **services/grafo/:** Construcción y conexión lógica entre nodos.
- **infrastructure/loaders.py:** Funciones que leen y transforman datos desde archivos `.json` en objetos Python.
- **algorithm/initial_solution.py:** Algoritmo de construcción inicial que asigna guardias por cercanía y disponibilidad horaria, priorizando guardias de planta antes de usar ocasionales.
- **algorithm/heuristic/heuristica.py:** Implementación de una búsqueda local simple que intenta reemplazar asignaciones costosas por otras más baratas manteniendo factibilidad.

---

## 🧪 Cómo ejecutar

Desde el directorio raíz del proyecto:

```bash
python src/main.py
```

Este comando:

- Carga los datos desde `data/inputs/`.
- Construye la solución inicial.
- Aplica heurística local.
- Guarda las asignaciones resultantes en `data/outputs/asignaciones_finales.json`.

---

## 📊 Resultados Esperados

- JSON con todas las asignaciones válidas, incluyendo día, turno, ID de guardia y locación, tipo de guardia y costo.
- Optimización del costo total mensual utilizando preferencia por guardias de planta con jornada horaria disponible.
- Verificación de que se cumpla con la cobertura diaria de turnos en cada locación.

**Ejemplo de una asignación:**

```json
{
    "dia": "lunes",
    "turno": "mañana",
    "id_guardia": "gp14",
    "nombre_guardia": "Guardia Planta 14",
    "tipo_guardia": "planta",
    "id_locacion": "l1",
    "nombre_locacion": "Locación 1",
    "costo_turno": 1600.0
}
```

---

## 🧑‍💻 Autores

- Cristopher Arredondo Canchis
- Cristóbal Hachim (s7n5c4n)

