# Demo — Reconocimiento facial: umbral y ataque de presentación

Demo práctica del Tema 9 (Reconocimiento facial, biometría y vigilancia).
Reproduce, a escala pequeña, el mecanismo que la literatura evalúa a gran
escala: la decisión por umbral sobre la distancia entre dos rostros, y su
vulnerabilidad ante un ataque de presentación.

## Qué es y qué enseña

Un sistema de reconocimiento facial convierte cada rostro en un vector de
números y mide la distancia entre dos rostros. Si esa distancia es menor
que un valor de corte (el umbral), decide que son la misma persona.

La demo muestra dos ideas centrales del tema:

1. **El umbral es el punto donde el error técnico se vuelve una decisión
   sobre una persona.** La misma distancia puede dar "coincide" o "no
   coincide" según dónde se ponga el corte. Un umbral demasiado alto acepta
   a personas distintas (falso positivo); uno demasiado bajo rechaza a la
   persona correcta (falso rechazo). Son las tasas FMR y FNMR que mide el
   NIST, y el ajuste de umbral que la policía decidía en el estudio de campo
   de Londres.

2. **El sistema no distingue una persona viva de una foto.** Al mostrarle
   una fotografía en la pantalla de un celular, el sistema la acepta como si
   fuera la persona real. Es un ataque de presentación, una de las amenazas
   a la integridad descritas en la literatura de ataques adversarios.

## Herramienta usada

- **Librería:** DeepFace (Python).
- **Modelo:** ArcFace, elegido a propósito porque es el mismo modelo
  estudiado en varias de las fuentes de la investigación.
- **Cámara y video:** OpenCV.
- **Entorno:** local, en Linux. Procesamiento sin servicios externos.

## Estructura de la demo

- `capture_faces.py` — captura fotos de rostros desde la cámara.
- `act1_threshold.py` — Acto 1: compara rostros y muestra la decisión a
  varios umbrales (fotos fijas).
- `act2_liveness.py` — Acto 2: cámara en vivo; permite mover el umbral en
  tiempo real y demostrar el ataque del celular.
- `distance_test.py` — prueba mínima de comparación entre dos fotos.
- `camera_test.py` — prueba mínima de que la cámara funciona.
- `faces/` — fotos usadas en la demo. No se sube al repositorio.

## Cómo correrla

Crear el entorno e instalar dependencias:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install deepface tf-keras "opencv-contrib-python==4.10.0.84"

Luego:

    python act1_threshold.py     # Acto 1: tabla de umbrales
    python act2_liveness.py      # Acto 2: cámara en vivo + ataque del celular

Controles del Acto 2 en vivo: `W` sube el umbral, `S` lo baja, `D` lo
devuelve al valor por defecto, `Q` cierra.

## Conexión con la literatura (para el informe y la presentación)

- **NIST (Grother et al.):** define FMR y FNMR y mide cómo varían según el
  umbral y el grupo demográfico. La demo reproduce ese mecanismo.
- **Fussey et al.:** en los pilotos policiales de Londres, el umbral y la
  discreción humana decidían el resultado. La demo muestra ese ajuste en vivo.
- **Vakhshiteh et al.:** describe ataques al reconocimiento facial. El
  ataque del celular es una versión simple de un ataque de presentación.

## Nota de ética y privacidad

Solo se usan fotos de integrantes del grupo, con su consentimiento. El
procesamiento es local, las imágenes no se suben al repositorio y se
eliminan al terminar. La demo ilustra el mecanismo con pocas personas, por
lo que no permite medir sesgo demográfico, que requiere miles de imágenes.