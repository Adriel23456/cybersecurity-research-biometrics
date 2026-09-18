# Matriz de revisión de referencias

**Tema 9:** Reconocimiento facial, biometría y vigilancia
**Curso:** CE-1115 Seguridad de la Información, II Semestre 2026
**Grupo 4:** Meibel Ceciliano, Carlos Contreras, Ludwin Ramos, Henry Nuñez, Adriel Chaves
**Última actualización:** [POR COMPLETAR: fecha]

---

## 1. Reglas de este documento

- Cada celda se redacta con palabras del grupo. **No se copian abstracts.**
- Las cifras se transcriben de la fuente original, con la sección o tabla de donde salen.
- `[?]` marca un dato pendiente de verificar contra la fuente. No pasa al informe hasta resolverse.
- Esta matriz es la fuente de verdad: la Tabla I del informe y el PDF del atributo IN se actualizan a partir de aquí.

### Categorías de fuente (enunciado)

| Categoría | Requisito | Cantidad actual |
|---|---|---|
| Académica | Mínimo 2 de las 5; revisión por pares, survey, SLR o preprint arXiv | 5 |
| Técnica con autoría | Organismo o equipo firmante y fecha | 3 |
| Actualidad | Solo para Impacto; no cuenta entre las cinco | 5 |

---

## 2. Matriz de revisión (obligatoria)

| ID | Referencia | Año | Cat. | Eje | Problema | Método | Datos / entorno | Hallazgo principal | Limitación |
|---|---|---|---|---|---|---|---|---|---|
| R01 | Buolamwini y Gebru | 2018 | Acad. | Sesgo | Disparidad de exactitud por sexo y tono de piel en sistemas faciales comerciales | Auditoría externa de tres servicios comerciales, con análisis interseccional y escala de Fitzpatrick | 1 270 rostros de parlamentarios de seis países, equilibrados por sexo y tono de piel | Error máximo de 34.7 % en mujeres de piel oscura frente a 0.8 % en hombres de piel clara | Evalúa clasificación de sexo, no identificación; etiquetado binario; retratos en condiciones controladas |
| R02 | Raji y Buolamwini | 2019 | Acad. | Sesgo | Efecto de publicar resultados de auditoría sobre los proveedores | Reauditoría de proveedores señalados públicamente y de proveedores no señalados | Mismo conjunto de referencia; cinco servicios comerciales | Los proveedores señalados redujeron sus brechas; los no señalados mostraron brechas mayores [?] | Misma tarea de clasificación de sexo; ventana temporal corta; no establece causalidad estricta |
| R03 | Sharif et al. | 2016 | Acad. | Ataques | Evasión y suplantación física de sistemas de reconocimiento facial | Optimización de perturbaciones adversarias impresas en marcos de anteojos | Modelos de redes profundas en caja blanca y un servicio comercial en caja negra [?] | Los anteojos físicos permiten evadir la identificación o suplantar a otra persona [?] | Captura controlada; no evalúa sistemas con detección de ataques de presentación [?] |
| R04 | Shan et al. | 2020 | Acad. | Ataques | Entrenamiento no autorizado de modelos con fotos públicas | Perturbaciones imperceptibles aplicadas por el usuario antes de publicar | Servicios comerciales de reconocimiento y modelos propios | Protección superior al 95 % frente a los modelos evaluados, según los autores [?] | Supone un atacante que no se adapta; trabajos posteriores reportan modelos que anulan la protección |
| R05 | Drozdowski et al. | 2020 | Acad. | Sesgo | Sesgo demográfico en biometría en general | Revisión de literatura sobre rostro, huella, iris y otras modalidades | Estudios publicados hasta 2020 | El sesgo está documentado, pero métricas y protocolos son heterogéneos; propone una agenda | Sin experimentos propios; anterior a la generación actual de modelos |
| R06 | Grother et al. (NISTIR 8280) | 2019 | Técn. | Sesgo | Efectos demográficos en algoritmos de reconocimiento facial | Evaluación independiente de 189 algoritmos de 99 desarrolladores, en verificación e identificación | 18.27 M de imágenes de 8.49 M de personas, de registros gubernamentales de EE. UU. | Falsos positivos entre 10 y más de 100 veces mayores según el grupo; varía mucho entre algoritmos | Imágenes de calidad administrativa, no de cámaras en espacio público; no evalúa sistemas desplegados |
| R07 | Garvie et al. | 2016 | Técn. | Vigilancia | Uso policial del reconocimiento facial sin regulación | Solicitudes de acceso a información pública y análisis de políticas | Agencias policiales de EE. UU. | Unos 117 M de adultos figuran en redes de reconocimiento facial policial | Solo EE. UU.; anterior a los servicios de extracción masiva de fotos de redes sociales |
| R08 | Fussey y Murray | 2019 | Técn. | Vigilancia | Legalidad y exactitud del reconocimiento facial en vivo | Observación independiente de pruebas operativas y análisis de derechos humanos | Pruebas de la Policía Metropolitana de Londres | De 42 coincidencias generadas, solo 8 se verificaron como correctas [?] | Pocos despliegues observados; acceso limitado a datos técnicos del proveedor |

---

## 3. Fichas por referencia

Una ficha por ID. Sirve para las preguntas individuales: cada integrante debe poder defender las referencias de su eje.

### R01 — Buolamwini y Gebru (2018)

- **Cita completa:** J. Buolamwini y T. Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," *Proc. 1st Conf. on Fairness, Accountability and Transparency*, PMLR 81, pp. 77–91, 2018.
- **Enlace:** https://proceedings.mlr.press/v81/buolamwini18a.html
- **Encontrada en:** [POR COMPLETAR: base de datos y palabra clave]
- **Responsable de lectura:** [POR COMPLETAR]
- **Ubicación de las cifras:** [POR COMPLETAR: sección o tabla]
- **Por qué entra:** es el trabajo fundacional sobre sesgo interseccional; ancla el Eje 1.
- **Cómo se relaciona:** contrasta con R06 (distinta tarea y escala) y motiva R02.

### R02 — Raji y Buolamwini (2019)

- **Cita completa:** I. D. Raji y J. Buolamwini, "Actionable Auditing," *Proc. AAAI/ACM Conf. on AI, Ethics, and Society*, pp. 429–435, 2019.
- **DOI:** 10.1145/3306618.3314244
- **Encontrada en:** [POR COMPLETAR]
- **Responsable de lectura:** [POR COMPLETAR]
- **Ubicación de las cifras:** [POR COMPLETAR]
- **Por qué entra:** muestra un efecto medible de la auditoría pública sobre la industria.
- **Cómo se relaciona:** continuación directa de R01.

### R03 — Sharif et al. (2016)

- **Cita completa:** M. Sharif, S. Bhagavatula, L. Bauer y M. K. Reiter, "Accessorize to a Crime," *Proc. ACM CCS*, pp. 1528–1540, 2016.
- **DOI:** 10.1145/2976749.2978392
- **Encontrada en:** [POR COMPLETAR]
- **Responsable de lectura:** [POR COMPLETAR]
- **Ubicación de las cifras:** [POR COMPLETAR]
- **Por qué entra:** ataque físico contra la integridad; conecta con amenazas y controles.
- **Cómo se relaciona:** opuesto a R04 (el mismo espacio de representación, usado para atacar o para proteger).

### R04 — Shan et al. (2020)

- **Cita completa:** S. Shan, E. Wenger, J. Zhang, H. Li, H. Zheng y B. Y. Zhao, "Fawkes: Protecting Privacy against Unauthorized Deep Learning Models," *29th USENIX Security Symposium*, pp. 1589–1604, 2020.
- **Enlace:** https://www.usenix.org/conference/usenixsecurity20/presentation/shan
- **Encontrada en:** [POR COMPLETAR]
- **Responsable de lectura:** [POR COMPLETAR]
- **Ubicación de las cifras:** [POR COMPLETAR]
- **Por qué entra:** control de confidencialidad del lado del usuario.
- **Cómo se relaciona:** su limitación (atacante adaptativo) alimenta la Discusión. [POR COMPLETAR: citar el trabajo posterior que la anula]

### R05 — Drozdowski et al. (2020)

- **Cita completa:** P. Drozdowski, C. Rathgeb, A. Dantcheva, N. Damer y C. Busch, "Demographic Bias in Biometrics: A Survey on an Emerging Challenge," *IEEE Trans. Technology and Society*, vol. 1, no. 2, pp. 89–103, 2020.
- **DOI:** 10.1109/TTS.2020.2992344
- **Encontrada en:** [POR COMPLETAR]
- **Responsable de lectura:** [POR COMPLETAR]
- **Por qué entra:** survey que ordena el Eje 1 y ubica los demás trabajos.
- **Cómo se relaciona:** marco general para R01, R02 y R06.

### R06 — Grother, Ngan y Hanaoka (2019)

- **Cita completa:** P. Grother, M. Ngan y K. Hanaoka, "Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects," NISTIR 8280, NIST, 2019.
- **DOI:** 10.6028/NIST.IR.8280
- **Encontrada en:** [POR COMPLETAR]
- **Responsable de lectura:** [POR COMPLETAR]
- **Ubicación de las cifras:** [POR COMPLETAR]
- **Por qué entra:** la mayor evaluación independiente; fuente de las métricas que usa la demo.
- **Cómo se relaciona:** contrasta con R01 en escala y tarea; con R08 en laboratorio frente a despliegue.

### R07 — Garvie, Bedoya y Frankle (2016)

- **Cita completa:** C. Garvie, A. M. Bedoya y J. Frankle, "The Perpetual Line-Up: Unregulated Police Face Recognition in America," Georgetown Law Center on Privacy & Technology, 2016.
- **Enlace:** https://www.perpetuallineup.org
- **Encontrada en:** [POR COMPLETAR]
- **Responsable de lectura:** [POR COMPLETAR]
- **Por qué entra:** dimensiona la vigilancia policial y el vacío regulatorio.
- **Cómo se relaciona:** base del contraste con la Ley 8968.

### R08 — Fussey y Murray (2019)

- **Cita completa:** P. Fussey y D. Murray, "Independent Report on the London Metropolitan Police Service's Trial of Live Facial Recognition Technology," Human Rights Centre, University of Essex, 2019.
- **Enlace:** [POR COMPLETAR]
- **Encontrada en:** [POR COMPLETAR]
- **Responsable de lectura:** [POR COMPLETAR]
- **Ubicación de las cifras:** [POR COMPLETAR]
- **Por qué entra:** único trabajo de la matriz que mide un despliegue real en espacio público.
- **Cómo se relaciona:** contrasta con R06.

---

## 4. Fuentes de actualidad (sección de Impacto)

No cuentan entre las cinco. Se cita siempre el documento original, no la nota de prensa.

| ID | Fuente | Fecha | Tipo | Efecto medible | Documento original | Verificado |
|---|---|---|---|---|---|---|
| A01 | Reglamento (UE) 2024/1689, Ley de IA | 2024 | Norma | Restringe la identificación biométrica remota en tiempo real en espacios públicos (Art. 5) | [POR COMPLETAR: enlace EUR-Lex] | [ ] |
| A02 | Ley 8968, Costa Rica | 2011 | Norma | Marco local de datos personales; [POR COMPLETAR: tratamiento de biométricos] | [POR COMPLETAR: enlace SCIJ] | [ ] |
| A03 | FTC v. Rite Aid | Dic. 2023 [?] | Sanción | Prohibición de usar reconocimiento facial durante 5 años [?] | [POR COMPLETAR: comunicado de la FTC] | [ ] |
| A04 | Sanciones a Clearview AI (Italia, Países Bajos, Reino Unido) | 2022–2024 [?] | Sanción | Multas de autoridades de protección de datos [?] | [POR COMPLETAR: resoluciones originales] | [ ] |
| A05 | Williams v. City of Detroit | 2024 [?] | Acuerdo judicial | Cambios en la política policial tras una detención errónea [?] | [POR COMPLETAR: acuerdo o comunicado] | [ ] |

---

## 5. Registro de descartes

Evidencia del proceso de selección (atributo IN, indicador de búsqueda).

| Fuente evaluada | Encontrada en | Motivo de exclusión |
|---|---|---|
| [POR COMPLETAR] | [POR COMPLETAR] | Nota periodística sin fuente primaria |
| [POR COMPLETAR] | [POR COMPLETAR] | Blog sin autoría identificable |
| [POR COMPLETAR] | [POR COMPLETAR] | Fuera del alcance: [motivo] |

---

## 6. Control de estado

| ID | Leída completa | Cifras verificadas | En Tabla I del informe | En diapositivas | Responsable |
|---|---|---|---|---|---|
| R01 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |
| R02 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |
| R03 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |
| R04 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |
| R05 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |
| R06 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |
| R07 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |
| R08 | [ ] | [ ] | [x] | [x] | [POR COMPLETAR] |