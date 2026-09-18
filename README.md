# Reconocimiento facial, biometría y vigilancia

Revisión de literatura sobre el debate técnico-legal del reconocimiento facial en espacios públicos: sesgos algorítmicos documentados, ataques contra la integridad de estos sistemas y el marco costarricense (Ley 8968) frente a casos internacionales.

**Curso:** CE-1115 Seguridad de la Información · Instituto Tecnológico de Costa Rica
**Profesor:** MSc. Andrés Vargas Rivera
**Semestre:** II Semestre, 2026
**Tema asignado:** Tema 9 — Reconocimiento facial, biometría y vigilancia
**Fecha de entrega:** [POR COMPLETAR]

---

## Integrantes — Grupo 4

| Integrante | Carné | Responsabilidad principal |
|---|---|---|
| Meibel Ceciliano | [POR COMPLETAR] | [POR COMPLETAR] |
| Carlos Contreras | [POR COMPLETAR] | [POR COMPLETAR] |
| Ludwin Ramos | [POR COMPLETAR] | [POR COMPLETAR] |
| Henry Nuñez | [POR COMPLETAR] | [POR COMPLETAR] |
| Adriel S. Chaves Salazar | 2021031465 | [POR COMPLETAR] |

---

## Entregables

| Entregable | Ubicación | Formato | Estado |
|---|---|---|---|
| Informe tipo survey paper (máx. 5 páginas, dos columnas) | `paper/` | LaTeX → PDF | 🟡 En progreso |
| Matriz de revisión | `01Matriz-Referencias.md` | Markdown | 🟡 En progreso |
| PDF del atributo IN (IN1–IN5) | `atributo-in/` | LaTeX → PDF | 🟡 En progreso |
| Diapositivas de la presentación | `slides/` | Beamer → PDF | 🟡 En progreso |
| Demo o ejemplo práctico | `demo/` | Por definir | 🔴 Pendiente |

---

## Estructura del repositorio

```text
.
├── README.md
├── .gitignore
├── 01Matriz-Referencias.md       # Fuente de verdad de las referencias
├── paper/
│   ├── InformePrincipal.tex
│   ├── preamble.tex
│   ├── sec/                      # 01introduccion … 06conclusiones, 99referencias.bib
│   └── tab/matriz_revision.tex   # Tabla I
├── atributo-in/
│   ├── Atributo_IN_grupo4.tex
│   ├── preamble.tex
│   ├── img/TUlogo.png
│   └── sec/                      # 00cover, 01cuerpo, 02definicion, 03bloques
├── slides/
│   ├── Presentacion_grupo4.tex
│   ├── preamble.tex
│   ├── img/TUlogo.png
│   └── sec/                      # 00portada … 05conclusiones, 90respaldo, 99referencias.bib
└── demo/                         # Por definir
```

---

## Compilación

Requisitos: MiKTeX o TeX Live con `latexmk`.

```bash
cd paper       && latexmk -pdf InformePrincipal.tex
cd atributo-in && latexmk -pdf Atributo_IN_grupo4.tex
cd slides      && latexmk -pdf Presentacion_grupo4.tex
```

Si la compilación falla tras un cambio en referencias, limpiar primero:

```bash
latexmk -C <archivo>.tex
```

---

## Estructura del informe

| # | Sección | Contenido |
|---|---|---|
| — | Resumen | 150–200 palabras: tema, hallazgos, relevancia |
| I | Introducción | Qué es el tema, por qué importa, qué problema de seguridad plantea |
| II | Metodología de búsqueda | Bases de datos, palabras clave, criterios de inclusión y exclusión |
| III | Desarrollo / estado del arte | Síntesis cruzada y matriz de revisión (Tabla I) |
| IV | Discusión | Contradicciones, vacíos, riesgos; tríada CID, Clase 4 y Clase 5 |
| V | Impacto actual | Casos reales con nombre propio y fecha |
| VI | Conclusiones | Hacia dónde va el tema y qué vigilar |
| — | Referencias | IEEE, consistente de principio a fin |

### Ejes de investigación

| Eje | Pregunta | Referencias |
|---|---|---|
| Sesgo demográfico | ¿Cuánto varía el error entre grupos? | R01, R02, R05, R06 |
| Ataques y contramedidas | ¿Se puede engañar o evadir el sistema? | R03, R04 |
| Vigilancia en espacio público | ¿Qué pasa al desplegarlo? | R07, R08 |
| Marco legal | ¿Cómo se compara la Ley 8968 con casos internacionales? | A01–A05 |

---

## Metodología de búsqueda

| Herramienta | Enlace |
|---|---|
| Biblioteca TEC | https://biblioteca.tec.ac.cr |
| IEEE Xplore (acceso TEC) | https://ieeexplore.tec.elogim.com/ |
| Scopus | https://www.scopus.com |
| Semantic Scholar | https://www.semanticscholar.org |
| Connected Papers | https://www.connectedpapers.com |
| Consensus | https://consensus.app |

**Criterios de fuentes (enunciado):**

- Mínimo 2 de 5 fuentes académicas con revisión por pares (se aceptan preprints de arXiv cs.CR).
- Fuentes técnicas con autoría y fecha identificables (NIST, ENISA, CERT, fabricantes, universidades).
- Fuentes de actualidad solo para la sección de Impacto; no cuentan entre las cinco.
- No cuentan: blogs sin autor, foros, videos sin fuente, Wikipedia ni notas periodísticas sin fuente primaria.

---

## Presentación (mínimo 15 minutos)

| Parte | Tiempo | Expone |
|---|---|---|
| 1. Contexto | ~2 min | [POR COMPLETAR] |
| 2. Búsqueda y selección | ~2 min | [POR COMPLETAR] |
| 3. Síntesis cruzada | ~5–6 min | [POR COMPLETAR] |
| 4. Demo | ~5–6 min | [POR COMPLETAR] |
| 5. Conclusiones | ~1–2 min | [POR COMPLETAR] |

Las preguntas individuales van aparte, en dos bloques: general e IN. Las del bloque IN deben cuadrar con lo escrito en el PDF del atributo IN.

---

## Demo

**Objetivo:** mostrar con una librería de reconocimiento facial de código abierto el mecanismo de decisión por umbral y su margen de error, enlazado a las métricas de la literatura.

| Aspecto | Decisión |
|---|---|
| Librería | [POR COMPLETAR] |
| Entorno | [POR COMPLETAR] |
| Datos | Solo fotos de integrantes con consentimiento |
| Privacidad | Procesamiento local; datos eliminados al terminar |
| Formato | En vivo con video de respaldo: [POR COMPLETAR: enlace] |

> Las imágenes de rostros **no se suben al repositorio**.

---

## Convenciones de redacción

Los tres documentos LaTeX comparten marcadores que se apagan antes de entregar:

| Marcador | Uso |
|---|---|
| `\pc{...}` | Contenido por completar |
| `\razon{...}` | Justificación interna de una decisión |
| `\decidir{...}` | Requiere decisión del equipo |
| `\pct` | Dato de tabla pendiente de verificar |

Para apagarlos, descomentar el bloque **Apagado de marcadores** al final de cada `preamble.tex` y recompilar. Todo lo que desaparezca del PDF nunca se escribió.

La matriz `01Matriz-Referencias.md` es la fuente de verdad: las cifras se verifican ahí primero y luego se copian al informe, al atributo IN y a las diapositivas.

---

## Pendientes

- [ ] Carnés de los integrantes
- [ ] Texto oficial literal de la definición del atributo IN y de IN1–IN5
- [ ] Verificar cifras marcadas con `[?]` contra las fuentes originales
- [ ] Verificar el tratamiento de datos biométricos en la Ley 8968
- [ ] Completar las fuentes de actualidad A01–A05 con documentos originales
- [ ] Redactar las secciones I–VI del informe
- [ ] Definir e implementar la demo
- [ ] Asignar expositores y ensayar los tiempos
- [ ] Alinear las respuestas IN1–IN5 con las diapositivas de respaldo
- [ ] Apagar marcadores y revisar el límite de 5 páginas

---

## Uso académico

Trabajo académico del curso CE-1115, Instituto Tecnológico de Costa Rica, II Semestre 2026.