<div align="center">
  <h1>Práctica 0: Nodos y Tópicos</h1>
  <p><b>Laboratorio de Robótica Remota - Proyecto PAPIME PE110923</b></p>

  [![ROS2 Humble](https://img.shields.io/badge/ROS2-Humble-blue?style=for-the-badge&logo=ros)](https://docs.ros.org/en/humble/index.html)
  [![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![UNAM](https://img.shields.io/badge/UNAM-FI-FFD700?style=for-the-badge&logo=academia)](https://www.ingenieria.unam.mx/)
</div>

---

## Descripción General

Este repositorio forma parte del proyecto **PAPIME PE110923**: *"Desarrollo de un Laboratorio de Robótica Remoto para realizar prácticas de programación de algoritmos de planeación y de navegación en bancos de prueba físicos"*.

La **Práctica 0** tiene como objetivo establecer los fundamentos de la comunicación entre procesos en ROS 2 mediante la implementación de una arquitectura de Nodos Publicadores y Suscriptores.

---

## Objetivos y Metas

### Principal
Dominar la gestión de información e interacción en entornos de robótica mediante el manejo de espacios de trabajo de **ROS 2** en Python.

### Específicos
- [x] Configuración y compilación de un *workspace* de ROS 2.
- [x] Implementación de **Nodos Publicadores** empleando temporizadores.
- [x] Implementación de **Nodos Suscriptores** con funciones de *callback*.
- [x] Uso de herramientas de documentación avanzada (Jupyter Lab).

---

## Estructura del Proyecto

El espacio de trabajo está organizado de la siguiente manera:

```text
practica_0/
├── imagenes_p1/           # Recursos visuales del proyecto
├── p0_py/                 # Paquete principal de lógica
│   ├── p0_py/
│   │   ├── primer_nodo.py   # Nodo Publicador (Talker)
│   │   └── subscriber_node.py # Nodo Suscriptor (Listener)
│   └── package.xml
└── practica_0/            # Paquete de organización y reporte
    └── Práctica_0_Nodos_y_Tópicos.ipynb
```

---

## Guía de Inicio Rápido

### Preferencias del Sistema
- **OS**: Ubuntu 22.04 LTS (o similar con soporte ROS 2)
- **ROS 2 Distro**: Humble / Iron / Jazy

### Instalación y Compilación

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPO>
   cd practica_0
   ```

2. **Compilar el espacio de trabajo:**
   ```bash
   colcon build
   source install/setup.zsh  # O setup.bash
   ```

### Ejecución
Abre dos terminales y ejecuta:

**Terminal 1 (Publisher):**
```bash
ros2 run p0_py primer_nodo
```

**Terminal 2 (Subscriber):**
```bash
ros2 run p0_py subscriber_node
```

---

## Evaluación y Resultados

### Rúbrica de Evaluación

| Criterio | Peso | Descripción |
| :--- | :---: | :--- |
| **Previo** | 25% | Investigación teórica y referencias. |
| **Desarrollo** | 25% | Implementación técnica y lógica. |
| **Resultado** | 25% | Interpretación de datos obtenidos. |
| **Conclusiones** | 25% | Relación con los objetivos y resultados. |

> [!NOTE]  
> Para una descripción detallada de los criterios, consulte la sección de rúbrica en el cuaderno de Jupyter.

---

## Autores
*   **M.I. Erik Peña Medina** - *Academia de Robótica*
*   **Dr. Víctor Javier Gonzáles Villela** - *Academia de Robótica*

