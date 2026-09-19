# Matriz de revisión de referencias

**Tema 9:** Reconocimiento facial, biometría y vigilancia
**Curso:** CE-1115 Seguridad de la Información, II Semestre 2026
**Grupo 4:** Meibel Ceciliano, Carlos Contreras, Ludwin Ramos, Henry Nuñez, Adriel Chaves
**Última actualización:** 19/09/2026

---

## Índice

1. Conjunto de referencias
2. Matriz de revisión (5 principales)
3. Matriz extendida (7 opcionales)
4. Fichas de los trabajos principales
5. Fichas de los trabajos opcionales
6. Lectura cruzada
7. Conexión con el curso
8. Costa Rica: marco legal, despliegues e interpretación
9. Casos internacionales y documentos originales
10. Glosario
11. Referencias

---

## 1. Conjunto de referencias

| ID | Referencia corta | Año | Categoría | Eje | Clave BibTeX |
|---|---|---|---|---|---|
| P1 | Grother, Ngan y Hanaoka | 2019 | Técnica (NIST) | Sesgo | `grother_nistir8280_2019` |
| P2 | Fussey, Davies e Innes | 2021 | Académica | Despliegue | `fussey_assisted_2020` |
| P3 | Almeida, Shmarko y Lomas | 2022 | Académica | Legal | `almeida_ethics_2022` |
| P4 | Kotwal y Marcel | 2026 | Académica (revisión) | Sesgo | `kotwal_fairness_2026` |
| P5 | Vakhshiteh, Nickabadi y Ramachandra | 2021 | Académica (revisión) | Ataques | `vakhshiteh_adversarial_2021` |
| O1 | Albiero, Zhang, King y Bowyer | 2022 | Académica | Sesgo (causas) | `albiero_gendered_2022` |
| O2 | Linghu et al. | 2024 | Académica | Sesgo (control) | `linghu_scorenorm_2024` |
| O3 | Shan et al. (Fawkes) | 2020 | Académica | Privacidad | `shan_fawkes_2020` |
| O4 | Buolamwini y Gebru (Gender Shades) | 2018 | Académica | Sesgo (fundacional) | `buolamwini_gendershades_2018` |
| O5 | Scherhag et al. | 2019 | Académica (revisión) | Ataques (morphing) | `scherhag_morphing_2019` |
| O6 | Franqueira, Hartmann y Abbas da Silva | 2021 | Académica | Latinoamérica: reconocimiento facial | `franqueira_reconhecimento_2021` |
| O7 | Chavarría-Mora | 2025 | Académica | Latinoamérica: ley de datos | `chavarria_patterns_2025` |

**Composición:** 4 académicas y 1 técnica entre las principales; 7 académicas opcionales.

**Cobertura por eje:**

- **Sesgo demográfico:** P1, P4, O1, O2, O4.
- **Ataques y controles:** P5, O3, O5.
- **Despliegue en espacio público:** P2, O6.
- **Legal y regulatorio:** P3, O6, O7.

---

## 2. Matriz de revisión (5 principales)

| ID | Referencia | Año | Problema | Método | Datos / entorno | Hallazgo principal | Limitación |
|---|---|---|---|---|---|---|---|
| P1 | Grother et al. | 2019 | Diferencias de exactitud entre grupos demográficos en verificación (1:1) e identificación (1:N) | Evaluación independiente a umbral fijo, reportando por separado falsos positivos y falsos negativos | 18.27 M de imágenes de 8.49 M de personas (fichas policiales, visas, inmigración y cruces fronterizos de EE. UU.); 189 algoritmos de 99 desarrolladores | Falsos positivos varían entre 10 y más de 100 veces entre grupos; mayores en mujeres, niños y adultos mayores; falsos negativos varían usualmente menos de 3 veces y dependen de la calidad de imagen | No explica causas; sin imágenes de internet ni de videovigilancia; algoritmos prototipo no reentrenados |
| P2 | Fussey et al. | 2021 | Operación real del reconocimiento facial en vivo por la policía y rol de la discreción humana | Etnografía (observación y entrevistas) y análisis de alertas y bitácoras | Pilotos de South Wales Police (35 h observadas) y Policía Metropolitana de Londres (más de 50 h), 2016–2019 | En Londres, de 43 alertas se juzgaron creíbles 27 y solo 9 fueron correctas; el umbral, las listas de vigilancia y la discreción deciden el resultado | Dos fuerzas del Reino Unido; muestras pequeñas; muchas alertas sin verificar; no mide sesgo demográfico |
| P3 | Almeida et al. | 2022 | Rendición de cuentas del uso policial del reconocimiento facial | Análisis comparativo de marcos regulatorios y jurisprudencia | EE. UU., UE y Reino Unido; casos judiciales y sanciones de autoridades de datos | El reglamento europeo exige evaluaciones de impacto y trata la biometría como categoría especial; EE. UU. sin ley federal; propone diez preguntas para regular | Discursivo, sin evaluación empírica; no cubre América Latina; anterior al Reglamento Europeo de IA aprobado |
| P4 | Kotwal y Marcel | 2026 | Disparidades persistentes en modelos modernos | Revisión de causas, conjuntos de datos, métricas y mitigaciones (pre, intra y posprocesamiento) | Literatura hasta 2025; NIST; ISO/IEC 19795-10 | Las disparidades aparecen en todo el rango de umbrales; combinan datos, tono de piel, calidad de imagen y factores no demográficos; balancear datos no basta | Centrada en raza y sexo; sin experimentos propios; poca evidencia en baja resolución |
| P5 | Vakhshiteh et al. | 2021 | Vulnerabilidad del reconocimiento facial profundo a ejemplos adversarios | Revisión con taxonomía de ataques (4 orientaciones) y defensas (3 estrategias) | FaceNet, ArcFace, SphereFace y servicios comerciales; LFW, CASIA-WebFace | Anteojos impresos, gorras con LED infrarrojos, luz proyectada o parches engañan sistemas reales; las defensas no generalizan | Solo ataques adversarios; condiciones controladas en los estudios; sin comparación cuantitativa común |

> Las cifras de Londres (43, 27 y 9) son la suma de las seis filas de la Tabla 2 de P2; el artículo las presenta por operación, no totalizadas.

---

## 3. Matriz extendida (7 opcionales)

| ID | Referencia | Año | Problema | Método | Datos / entorno | Hallazgo principal | Limitación |
|---|---|---|---|---|---|---|---|
| O1 | Albiero et al. | 2022 | Por qué el reconocimiento facial falla más en mujeres | Segmentación del rostro, igualación de área visible y de maquillaje, y agrupamiento de identidades | MORPH (fichas policiales) y Asian-Celeb depurado; ArcFace, un modelo entrenado balanceado por sexo y un comercial | Al igualar el área visible del rostro, los falsos rechazos en mujeres quedan iguales o mejores que en hombres; los falsos positivos siguen siendo mayores | Solo diferencia por sexo; categorías binarias; conjunto web con factores no aislables |
| O2 | Linghu et al. | 2024 | Un único umbral produce errores distintos por grupo | Nueve técnicas de normalización de puntajes aplicadas después del modelo, sin reentrenar | VGGFace2 y RFW; cinco redes preentrenadas; métrica WERM a FMR de 10⁻³ | Varias técnicas mejoran la equidad sin reducir la verificación; balancear pares por submuestreo empeora la equidad | Requiere conocer el grupo demográfico al enrolar; un solo punto de operación reportado |
| O3 | Shan et al. | 2020 | Entrenamiento no autorizado de modelos con fotos públicas | Perturbaciones imperceptibles ("capas") aplicadas por el usuario antes de publicar | PubFig, FaceScrub, WebFace, VGGFace2; Azure Face, Amazon Rekognition y Face++ | Más de 95 % de protección; 100 % contra los tres servicios con capas robustas; más de 80 % aun con fotos limpias filtradas | Pierde eficacia si el atacante tiene muchas fotos limpias o un modelo muy robusto; sin garantía a futuro |
| O4 | Buolamwini y Gebru | 2018 | Disparidad interseccional en clasificadores comerciales | Auditoría externa con escala de Fitzpatrick y análisis interseccional | 1 270 parlamentarios de seis países (PPB); Microsoft, IBM y Face++ | Error de hasta 34.7 % en mujeres de piel oscura frente a un máximo de 0.8 % en hombres de piel clara | Clasificación de sexo, no identificación; etiquetas binarias; retratos controlados |
| O5 | Scherhag et al. | 2019 | Imágenes fusionadas ("morphs") que verifican a dos personas | Revisión con categorización, métricas y estado del arte de detección | Literatura sobre generación y detección; escenario de pasaporte electrónico | Un morph puede verificar a ambos contribuyentes; sin entrenamiento, observadores humanos aceptan el 68 % | Solo morphing; no hay bases públicas grandes para comparar detectores |
| O6 | Franqueira et al. | 2021 | Estado regulatorio del reconocimiento facial en seguridad pública en América Latina | Estudio exploratorio de casos y normas nacionales | 11 países con ley de datos, incluida Costa Rica | El uso se apoya en excepciones generales de las leyes de datos, sin reglas sobre auditoría ni tasas de error tolerables | Descriptivo; sin mediciones técnicas; información hasta 2020 |
| O7 | Chavarría-Mora | 2025 | Compromiso de las leyes de datos personales en América Latina y el Caribe | Análisis temático inductivo del texto de las leyes y puntaje ordinal de compromiso | 25 jurisdicciones, 17 con ley; Costa Rica incluida | Costa Rica obtiene el puntaje máximo (9), junto con Argentina y Uruguay; no hay patrón subregional | Mide la ley escrita, no su aplicación; puntaje ordinal no comparable en intervalos |

---

## 4. Fichas de los trabajos principales

### P1 — Grother, Ngan y Hanaoka (2019), NISTIR 8280

**Cita:** P. Grother, M. Ngan y K. Hanaoka, *Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects*, NISTIR 8280, National Institute of Standards and Technology, dic. 2019. DOI: 10.6028/NIST.IR.8280.

**Tipo:** técnica con autoría identificable (organismo federal, equipo firmante y fecha). 82 páginas, más de 1 200 páginas de anexos.

**Qué es:** la evaluación independiente más grande publicada sobre diferencias demográficas en algoritmos de reconocimiento facial, y la primera en medirlas también en identificación 1:N.

**Método:**
- Algoritmos enviados voluntariamente al FRVT por empresas y algunas universidades, evaluados tal como fueron enviados, sin reentrenar.
- Los errores se reportan **a umbral fijo**, como operan los sistemas reales. Los autores critican que la mayoría de estudios académicos reporten falsos negativos a una tasa fija de falsos positivos, porque eso oculta cuánto se disparan los falsos positivos.
- Falsos positivos (FMR, FPIR) y falsos negativos (FNMR, FNIR) se reportan por separado, porque cada error perjudica a actores distintos.

**Datos:** cuatro conjuntos de operaciones gubernamentales reales de EE. UU.:
- fichas policiales nacionales, con etiqueta de raza;
- fotos de solicitudes de beneficios migratorios;
- fotos de visas;
- fotos de cruces fronterizos, de menor calidad.

Total: **18.27 millones de imágenes de 8.49 millones de personas**, procesadas por **189 algoritmos de 99 desarrolladores**. Fuera de las fichas policiales, la raza se aproxima con el país de nacimiento: 24 países de 7 regiones.

**Hallazgos (Executive Summary y Technical Summary):**
- Hay diferencias demográficas en la mayoría de algoritmos evaluados.
- **Falsos positivos:** varían entre 10 y más de 100 veces entre grupos. Son más altos en personas de África Occidental, África Oriental y Asia Oriental, y más bajos en Europa del Este. Varios algoritmos desarrollados en China invierten el patrón y tienen menos falsos positivos en rostros de Asia Oriental.
- Los falsos positivos son **entre 2 y 5 veces mayores en mujeres** que en hombres, de forma consistente.
- Los falsos positivos son mayores en **adultos mayores y niños**.
- En fichas policiales, los falsos positivos más altos están en indígenas americanos, con tasas elevadas en afroamericanos y asiáticos.
- **Falsos negativos:** varían usualmente menos de 3 veces y dependen mucho del algoritmo (de menos de 0.5 % a más de 10 %) y de la calidad de imagen. En fotos fronterizas son mayores en personas nacidas en África y el Caribe.
- Los algoritmos más precisos tienen diferenciales menores. Algunos algoritmos de identificación (por ejemplo, Idemia y NEC-3) muestran diferenciales de falsos positivos no detectables.
- Recomendación: el dueño del sistema debe **conocer su algoritmo** y medirlo con sus propios datos operativos.

**Limitaciones declaradas ("What we did not do"):**
- No entrenaron algoritmos.
- No analizaron causas ni relacionaron errores con el tono de piel.
- No estudiaron el efecto de la cámara.
- No usaron imágenes de internet ni de videovigilancia.

**Aclaración de los autores:** Gender Shades (O4) evaluó clasificación de sexo, no reconocimiento facial, y ambos resultados no deben mezclarse.

**Conexión con el curso:**
- *Tríada CID:* un falso positivo en identificación afecta la **integridad** de la identidad atribuida; en verificación, es un problema de seguridad del dueño del sistema, porque permite el acceso de un impostor.
- *Clase 16:* fuente canónica de FMR, FNMR, FPIR, FNIR y del concepto de umbral.
- *Clase 5:* "conocer el algoritmo" encaja como control y métrica en la cadena principio → política → procedimiento → control → métrica.

---

### P2 — Fussey, Davies e Innes (2021), The British Journal of Criminology

**Cita:** P. Fussey, B. Davies y M. Innes, "'Assisted' facial recognition and the reinvention of suspicion and discretion in digital policing," *The British Journal of Criminology*, vol. 61, n.º 2, pp. 325–344, mar. 2021. DOI: 10.1093/bjc/azaa068.

**Tipo:** académica, revisión por pares, acceso abierto (CC BY). Publicada en línea en 2020.

**Qué es:** estudio empírico sobre los dos primeros pilotos policiales de largo plazo de reconocimiento facial en vivo en el mundo: South Wales Police (SWP) y la Policía Metropolitana de Londres (MPS).

**Método:**
- Dos evaluaciones independientes que se integraron después.
- Etnografía: investigadores dentro de las furgonetas de vigilancia observando cómo los operadores interpretaban las alertas, más entrevistas.
- Análisis de salidas del sistema y bitácoras en Gales; registro manual de resultados en Londres.
- Análisis temático cualitativo.

**Datos y entorno:**
- SWP: 12 eventos entre junio de 2017 y marzo de 2018; observación en 7 despliegues, **35 horas**.
- MPS: 10 despliegues entre agosto de 2016 y febrero de 2019; observación en 6 operaciones, **más de 50 horas**.
- Listas de vigilancia de 400 a 1 200 personas en Gales y hasta 2 226 en Londres.
- Algoritmo de NEC en ambos pilotos.

**Hallazgos:**
- **Londres (Tabla 2):** 43 alertas en seis operaciones; los operadores juzgaron creíbles 27, pero solo 9 resultaron correctas tras verificar la identidad.
- **Gales (Tabla 1):** en la final de la Champions League 2017 hubo 2 632 alertas y solo 78 (3 %) fueron juzgadas creíbles. El desempeño mejoró después, en parte por una actualización del algoritmo.
- Los operadores tendían a **ceder la decisión al algoritmo**.
- **Umbral:** SWP subió el umbral de similitud de 0.55 (recomendado por el proveedor) a 0.59; la MPS usó 0.55 siempre. Subir el umbral reduce falsos positivos y aumenta falsos negativos.
- Aunque se instruyó ignorar el puntaje, los puntajes altos influían en la decisión de intervenir.
- Tres grupos de factores determinan el resultado:
  - **organizacionales:** dónde y cuándo desplegar, a veces por conveniencia técnica y no por criminalidad;
  - **del sistema:** composición y calidad de las listas de vigilancia, umbral, resolución y encuadre;
  - **del operador:** juicio y deferencia a la máquina.
- Las listas de vigilancia fueron discrecionales. En una planificación se propuso incluir a "todos los buscados de Londres", más de 23 700 personas.
- Con poca luz el sistema rendía peor, así que operaciones pensadas para la vida nocturna se hicieron de día.
- Conclusión conceptual: debe hablarse de reconocimiento facial **asistido** y no **automatizado**.
- El artículo cita que en agosto de 2020 el Tribunal de Apelación consideró insuficiente la base legal y excesiva la discreción policial (caso Bridges; ver sección 9).

**Limitaciones:** solo dos fuerzas del Reino Unido; número de alertas pequeño; muchas alertas no verificadas; los autores dejan de lado el debate normativo; no mide sesgo demográfico.

**Conexión con el curso:**
- *Clase 4:* **fail-safe**. Ante una coincidencia incierta, lo seguro es no intervenir; los operadores tendían a lo contrario.
- *Clase 4:* **privilegio mínimo** y proporcionalidad en las listas de vigilancia.
- *Clase 5:* falta de política sobre quién entra a la lista y con qué umbral se opera.
- *Tríada CID:* **confidencialidad** de todas las personas escaneadas; **integridad** de la identificación.

---

### P3 — Almeida, Shmarko y Lomas (2022), AI and Ethics

**Cita:** D. Almeida, K. Shmarko y E. Lomas, "The ethics of facial recognition technologies, surveillance, and accountability in an age of artificial intelligence: a comparative analysis of US, EU, and UK regulatory frameworks," *AI and Ethics*, vol. 2, pp. 377–387, 2022. DOI: 10.1007/s43681-021-00077-w. Publicado en línea el 29 de julio de 2021.

**Tipo:** académica, revisión por pares, acceso abierto (CC BY).

**Método:** análisis discursivo comparativo de legislación, guías regulatorias y jurisprudencia.

**Hallazgos:**
- El uso en **espacio público** es ética y legalmente distinto del desbloqueo de un dispositivo.
- **UE y Reino Unido:**
  - El RGPD trata la biometría como **categoría especial** (art. 9): no se usa para identificar sin consentimiento explícito u otra excepción.
  - La aplicación de la ley es una excepción delegada a los Estados miembros (art. 23).
  - Aun así, la **evaluación de impacto de protección de datos** (EIPD) es obligatoria para usos de alto riesgo como este, junto con la privacidad desde el diseño y por defecto (art. 25) y el delegado de protección de datos.
- **Casos citados:**
  - *Bridges vs. South Wales Police:* EIPD deficiente y discreción demasiado amplia; el despliegue indiscriminado violó la privacidad por defecto.
  - *Kings Cross (Londres):* una empresa privada usó reconocimiento facial en cámaras de un nodo de transporte sin informar, compartiendo imágenes con la policía entre 2016 y 2018.
  - *Suecia:* multas de la autoridad de datos a una escuela y a la policía (detalle en la sección 9).
  - En 2019, 12 fuerzas policiales nacionales de la UE ya usaban reconocimiento facial y 7 más lo planeaban.
- **EE. UU.:**
  - No hay ley federal de datos ni autoridad de protección de datos; la rendición de cuentas depende de demandas individuales.
  - Solo Illinois permite demandar por mal uso de datos biométricos.
  - Unos 117 millones de adultos figuran en redes policiales de reconocimiento facial.
  - Caso Willie Allen Lynch (Florida, 2016): condenado tras una coincidencia facial, sin acceso a la foto ni a los candidatos, con detectives que no sabían cómo funcionaba el puntaje.
  - Clearview AI abastecía a más de 600 departamentos policiales y extraía fotos contra los términos de servicio de Facebook.
  - En junio de 2020, IBM, Amazon y Microsoft se retiraron o pausaron la venta a la policía.
  - San Francisco y Berkeley prohibieron su uso.
- **Recomendaciones:** EIPD y evaluaciones de impacto en derechos humanos obligatorias y públicas, reguladores con poder de sanción, auditorías regulares y **diez preguntas éticas** (quién controla, para qué fines, qué consentimiento, cómo se construyen las bases de rostros, qué límites de desempeño, cómo auditar, cómo reclamar).

**Limitaciones:** discursivo, sin datos propios; no cubre América Latina; anterior a la aprobación del Reglamento Europeo de IA.

**Conexión con el curso:**
- *Clase 3:* RGPD, privacidad desde el diseño, límites del consentimiento (escuela sueca).
- *Clase 5:* la EIPD como política verificable; el regulador como control externo.
- *Clase 6:* extracción de fotos contra términos de servicio (Clearview).
- *Clase 4:* dilema ético entre seguridad pública y privacidad.

---

### P4 — Kotwal y Marcel (2026), IEEE T-BIOM

**Cita:** K. Kotwal y S. Marcel, "Review of Demographic Fairness in Face Recognition," *IEEE Transactions on Biometrics, Behavior, and Identity Science*, vol. 8, n.º 1, pp. 20–45, 2026. DOI: 10.1109/TBIOM.2025.3601217. Publicado en línea en 2025 (arXiv:2502.02309).

**Tipo:** académica, revisión en revista IEEE. Autores del Idiap Research Institute (Suiza).

**Hallazgos:**
- Las disparidades **no se limitan a un tipo de error ni a un umbral**: aparecen en todo el espacio de puntajes.
- **Causas (sección III):** conjuntos de entrenamiento desbalanceados, variabilidad del tono de piel, factores del modelo, calidad de imagen, factores interseccionales, y factores no demográficos (peinado, maquillaje, oclusión) de origen cultural o social.
- **Mitigación (sección VI):** preprocesamiento (datos), intraprocesamiento (función de pérdida y arquitectura) y posprocesamiento (puntajes, como O2).
- El tema ya está en marcos formales: el NIST FRVT incluye análisis demográfico desde 2019, y la norma **ISO/IEC 19795-10** cuantifica diferenciales demográficos.
- **Direcciones futuras relevantes para vigilancia:**
  - **Baja resolución:** casi toda la investigación usa imágenes de alta resolución, mientras la vigilancia usa cámaras lejanas y de baja calidad.
  - **Compresión:** la compresión JPEG degrada más el desempeño en tonos de piel oscuros.
  - **Modelos ligeros:** la destilación, la poda y la cuantización pueden amplificar el sesgo.
  - **Datos sintéticos:** pueden empeorar el sesgo.
  - **Verificación remota de identidad (KYC):** de cinco sistemas comerciales analizados en otro estudio, solo dos fueron equitativos.
  - **Interseccionalidad:** la mayoría de mitigaciones atacan un solo atributo.
- Casos citados en la introducción: detención errónea en Detroit, legisladores confundidos con criminales por un servicio comercial y sesgo en sistemas de abordaje en aeropuertos.

**Limitaciones:** centrada en raza y sexo; sin experimentos propios; no aborda el marco legal.

**Conexión con el curso:**
- *Clase 16:* métricas de equidad y umbral.
- *Clase 5:* mitigación como control; ISO/IEC 19795-10 como estándar auditable.
- *Tríada CID:* también afecta la **disponibilidad**, porque un grupo con más falsos rechazos pierde acceso a servicios.

---

### P5 — Vakhshiteh, Nickabadi y Ramachandra (2021), IEEE Access

**Cita:** F. Vakhshiteh, A. Nickabadi y R. Ramachandra, "Adversarial Attacks Against Face Recognition: A Comprehensive Study," *IEEE Access*, vol. 9, pp. 92735–92756, 2021. DOI: 10.1109/ACCESS.2021.3092646.

**Tipo:** académica, revisión. Autores de la Universidad Amirkabir (Irán) y del Norwegian Biometrics Laboratory, NTNU (Noruega).

**Contexto de la amenaza:** los ataques son **físicos** (modificar la apariencia antes de la captura, como la suplantación) o **digitales** (modificar la imagen capturada, como los ataques adversarios y el morphing).

**Taxonomía de ataques (sección 4.2):**
1. **Contra el modelo:** ruido o líneas de rejilla bastan para bajar la exactitud. Ataques evolutivos contra ArcFace, CosFace y SphereFace. DFANet generó pares adversarios contra las API de Amazon, Microsoft, Baidu y Face++.
2. **Físicos:** anteojos impresos para evadir o suplantar, gorra con LED infrarrojos invisibles al ojo, luz proyectada sobre el rostro, el sombrero AdvHat contra ArcFace, y parches en anteojos o frente.
3. **Desidentificación:** envenenamiento de un sistema basado en OpenFace; perturbaciones que protegen la privacidad preservando la calidad.
4. **Geométricos:** manipulación de puntos faciales unas 200 veces más rápida que los ataques geométricos tradicionales; redes generativas que crean rostros adversarios naturales.

**Defensas (sección 5):**
- **Objetivos:** preservar la arquitectura, la exactitud y la velocidad.
- **Estrategias:** (1) alterar la entrada, (2) modificar la red y (3) añadir redes externas de detección.

**Retos (sección 6):**
1. Los ataques son específicos y no generalizan; falta un banco de pruebas común.
2. Los modelos profundos aumentaron la superficie de ataque.
3. Los modelos no ven como los humanos.
4. Faltan perturbaciones universales.

Además, los estudios usan condiciones de imagen más controladas que las reales.

**Limitaciones:** limitada a ataques adversarios; sin comparación cuantitativa unificada; literatura hasta 2020 aproximadamente.

**Conexión con el curso:**
- *Clases 1–2:* **ataques activos** contra la **integridad**. La evasión equivale a burlar un control de acceso; la suplantación viola la autenticación.
- *Clase 7:* los ataques adversarios son herramienta de un *red team*; las defensas, del *blue team*.
- *Clase 4:* **defensa en profundidad**. Ninguna defensa sola generaliza, así que se combinan capas.
- *Clase 16:* ataques de presentación e ISO/IEC 30107-3.

---

## 5. Fichas de los trabajos opcionales

### O1 — Albiero, Zhang, King y Bowyer (2022), IEEE T-IFS

**Cita:** V. Albiero, K. Zhang, M. C. King y K. W. Bowyer, "Gendered Differences in Face Recognition Accuracy Explained by Hairstyles, Makeup, and Facial Morphology," *IEEE Trans. Inf. Forensics Security*, vol. 17, pp. 127–137, 2022. DOI: 10.1109/TIFS.2021.3135750.

**Idea central:** P1 documentó menor exactitud en mujeres sin analizar causas; este trabajo las busca.

**Datos:**
- **MORPH** depurado (fichas policiales con iluminación controlada): 35 276 imágenes de 8 835 hombres caucásicos, 10 941 de 2 798 mujeres caucásicas, 56 245 de 8 839 hombres afroamericanos y 24 857 de 5 929 mujeres afroamericanas.
- **Asian-Celeb** depurado: 73 376 imágenes de 12 673 hombres y 43 356 de 6 083 mujeres.

**Modelos:** ArcFace, un modelo entrenado balanceado por sexo y uno comercial no revelado.

**Método:** segmentación con BiSeNet para medir qué parte de la imagen es rostro, conjuntos con igual información facial entre sexos, balanceo por maquillaje y agrupamiento jerárquico de identidades.

**Hallazgos:**
- Las mujeres tienen menos "píxeles de rostro" por el peinado (que tapa orejas y laterales) y por un rostro más pequeño en promedio.
- Al igualar la información facial, los **falsos rechazos en mujeres quedan iguales o mejores** que en hombres, salvo en Asian-Celeb.
- El maquillaje explica parte de la brecha restante.
- Los **falsos positivos** siguen siendo mayores en mujeres: rostros de mujeres distintas resultan más parecidos entre sí.
- Los autores atribuyen la brecha a convenciones sociales (peinado, maquillaje) y a la morfología, y recomiendan reportar la composición de los datos de prueba.

**Limitaciones:** solo diferencia por sexo; etiquetas binarias; conjunto web con factores no aislables.

---

### O2 — Linghu et al. (2024), IEEE IJCB

**Cita:** Y. Linghu, T. de Freitas Pereira, C. Ecabert, S. Marcel y M. Günther, "Score Normalization for Demographic Fairness in Face Recognition," *Proc. IEEE IJCB*, 2024, pp. 1–11. DOI: 10.1109/IJCB62174.2024.10744514.

**Idea central:** en producción se usa un único umbral, pero las distribuciones de puntajes difieren por grupo, así que el mismo umbral produce errores distintos. La corrección se hace después del modelo, sin reentrenar.

**Método:** nueve técnicas de normalización:
- Z-norm y T-norm clásicas (M1 y M2) y sus extensiones por grupo demográfico (M1.1, M1.2, M2.1, M2.2);
- M3, cohorte de impostores del mismo grupo;
- M4, escalado de Platt;
- M5, CDF bimodal, propuesta nueva.

**Datos:** VGGFace2 (protocolos por sexo y etnia, originales y balanceados) y RFW (protocolo original y uno aleatorio nuevo), con cinco redes preentrenadas (ArcFace, AdaFace, MagFace y DALIFace).

**Métrica:** WERM, que compara la peor tasa de error con la media geométrica de los grupos, a un umbral de FMR de 10⁻³.

**Hallazgos:**
- La mayoría de técnicas mejora la equidad sin reducir la verificación.
- Los métodos basados en impostores (M1.1, M2.1, M3) son los más estables.
- **Balancear pares por submuestreo empeora la equidad.**
- FMR y FNMR deben pesar por igual en la evaluación.
- El código es público.

**Limitaciones:** requiere conocer el grupo demográfico al enrolar; un solo punto de operación reportado.

---

### O3 — Shan et al. (2020), USENIX Security (Fawkes)

**Cita:** S. Shan, E. Wenger, J. Zhang, H. Li, H. Zheng y B. Y. Zhao, "Fawkes: Protecting Privacy against Unauthorized Deep Learning Models," *Proc. 29th USENIX Security Symposium*, 2020, pp. 1589–1604.

**Idea central:** cualquiera puede extraer fotos de internet y entrenar un modelo que identifique personas sin su conocimiento; el caso motivador es Clearview AI, con más de 3 mil millones de fotos. Fawkes permite al usuario "encubrir" sus fotos antes de publicarlas.

**Método:** perturbaciones imperceptibles (DSSIM ≤ 0.007) que desplazan la representación del rostro hacia la de otra persona objetivo. Un modelo entrenado con esas fotos aprende rasgos equivocados.

**Hallazgos:**
- Más de **95 %** de protección, sin importar cómo entrene el rastreador.
- Más de **80 %** aun si la mitad de las fotos filtradas están limpias, usando una cuenta *sybil*.
- Contra servicios comerciales, con 82 fotos de un coautor: capa normal con 100 % en Azure, 34 % en Rekognition y 0 % en Face++; **capa robusta con 100 % en los tres** (Tabla 4).
- La protección cae por debajo de 39 % si más del 15 % de las fotos del usuario están limpias (Fig. 10).
- Contra un rastreador con un modelo muy robusto baja a 64 %, y vuelve a 100 % con una perturbación mayor (DSSIM > 0.01).

**Limitaciones declaradas:** el usuario no controla las fotos que publican otros; la protección no está garantizada a futuro; también puede ser usada por criminales.

**Contrapunto:** PuFace (2024, arXiv) reporta que reduce el éxito de estas capas de 69.84 % a 7.61 %.

---

### O4 — Buolamwini y Gebru (2018), FAT* (Gender Shades)

**Cita:** J. Buolamwini y T. Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," *Proc. 1st Conf. on Fairness, Accountability and Transparency*, PMLR 81, 2018, pp. 77–91.

**Datos:** Pilot Parliaments Benchmark (PPB) con 1 270 personas de los parlamentos de Ruanda, Senegal, Sudáfrica, Islandia, Finlandia y Suecia, etiquetadas con la escala de Fitzpatrick por una dermatóloga. Los conjuntos previos eran mayoritariamente de piel clara: 79.6 % en IJB-A y 86.2 % en Adience.

**Sistemas:** clasificadores de sexo de Microsoft, IBM y Face++ (abril y mayo de 2017).

**Hallazgos (Tablas 4 y 5):**
- Los tres clasifican peor a las mujeres (entre 8.1 y 20.6 puntos más de error) y a las personas de piel oscura (entre 11.8 y 19.2 puntos más).
- **Mujeres de piel oscura: error de 20.8 % (Microsoft) a 34.7 % (IBM).**
- Hombres de piel clara: error máximo de 0.8 %.
- Las mujeres de piel oscura son el 21.3 % del conjunto y concentran entre el 61 % y el 72.4 % de los errores.
- Las API no permitían ajustar el umbral.

**Limitaciones:** clasificación de sexo, no reconocimiento facial; etiquetas binarias; retratos oficiales.

---

### O5 — Scherhag et al. (2019), IEEE Access

**Cita:** U. Scherhag, C. Rathgeb, J. Merkle, R. Breithaupt y C. Busch, "Face Recognition Systems Under Morphing Attacks: A Survey," *IEEE Access*, vol. 7, pp. 23012–23026, 2019. DOI: 10.1109/ACCESS.2019.2899367.

**Idea central:** un morph fusiona dos rostros. Si un cómplice obtiene un pasaporte con esa foto, él y el criminal pasan las puertas de control fronterizo automático. Se rompe el vínculo único entre la muestra y la persona.

**Contenido:**
- Pasos del morphing: correspondencia de puntos, deformación y mezcla.
- Posprocesamiento para ocultar artefactos; la impresión y el escaneo del pasaporte los reducen aún más.
- Herramientas accesibles como FaceMorpher, FantaMorph y GIMP.
- Métricas: MMPMR y RMMR para vulnerabilidad; APCER y BPCER (ISO/IEC 30107-3) para detección.
- Detección sin referencia (una imagen) y diferencial (con captura en vivo).

**Hallazgos:**
- Con un sistema comercial, el morph se verifica contra ambos contribuyentes con umbral 0.5 y FMR de 0.1 % (Fig. 2).
- Observadores humanos aceptaban el 68 % de los morphs sin entrenamiento y el 21 % tras una breve capacitación.
- Los detectores funcionan en sus propias bases, pero no se ha demostrado que generalicen.

**Limitaciones:** sin bases públicas grandes ni detectores abiertos; solo morphing.

---

### O6 — Franqueira, Hartmann y Abbas da Silva (2021), Revista Digital de Direito Administrativo

**Cita:** B. D. Franqueira, I. A. Hartmann y L. Abbas da Silva, "O que os olhos não veem, as câmeras monitoram: reconhecimento facial para segurança pública e regulação na América Latina," *Revista Digital de Direito Administrativo*, vol. 8, n.º 1, pp. 171–204, 2021. DOI: 10.11606/issn.2319-0558.v8i1p171-204. Revista de la Facultad de Derecho de Ribeirão Preto (USP).

**Método:** estudio exploratorio de casos y normas en los 11 países latinoamericanos con ley de datos: Argentina, Brasil, Chile, Colombia, Costa Rica, México, Nicaragua, Panamá, Perú, República Dominicana y Uruguay.

**Hallazgos por país:**
- **Argentina:**
  - La Resolución 398/2019 implantó en Buenos Aires el Sistema de Reconocimiento Facial de Prófugos (SRFP) en 300 de más de 7 000 cámaras, con unas 174 detenciones en menos de tres meses.
  - Se apoyó en la excepción de la Ley 25.326 para no pedir consentimiento.
  - En agosto de 2019, un hombre pasó 6 días detenido por una identificación errónea; las autoridades lo atribuyeron a un documento mal cargado en la base CONARC.
  - El gobierno declaró más de 90 % de aciertos y negó el acceso al código invocando secreto comercial.
  - En octubre de 2019, la Asociación por los Derechos Civiles demandó su inconstitucionalidad.
- **Brasil:**
  - Metro de São Paulo: más de 300 000 boletos bloqueados en dos años.
  - La justicia ordenó apagar las cámaras publicitarias de ViaQuatro.
  - Río de Janeiro pasó de 34 a 140 cámaras en 2019, con al menos dos falsos positivos ese mes.
  - La LGPD considera sensible la biometría, pero exceptúa la seguridad pública.
- **Costa Rica:** ver la sección 8.

**Conclusión de los autores:** en toda la región el reconocimiento facial se regula solo por excepciones generales de las leyes de datos, sin decisión legislativa expresa ni reglas sobre transparencia, tasas de error tolerables o auditorías independientes.

**Limitaciones:** descriptivo; sin mediciones técnicas; información hasta 2020.

---

### O7 — Chavarría-Mora (2025), Social Media + Society

**Cita:** E. Chavarría-Mora, "(Lack of) Patterns in Commitment: Data Protection in the Latin America and Caribbean Personal Data Protection Laws," *Social Media + Society*, vol. 11, n.º 2, pp. 1–13, 2025. DOI: 10.1177/20563051251337206.

**Autor:** Universidad de Pittsburgh y Universidad de Costa Rica.

**Método:** análisis temático inductivo del texto vigente (a 2022) de las leyes de 25 jurisdicciones de América Latina y el Caribe, con una matriz cualitativa y un puntaje ordinal de compromiso de 0 a 9.

**Hallazgos:**
- 17 de 25 países tienen ley de datos. No la tienen Bolivia, El Salvador (vetada por el presidente), Guatemala, Guyana, Haití, Honduras, Surinam ni Venezuela.
- En la región, la biometría suele figurar como dato sensible y los derechos ARCO son comunes.
- **Costa Rica, Ley 8968 (2011): puntaje 9, el máximo**, junto con Argentina y Uruguay. Ley centrada en datos personales, agencia independiente con recursos, registro de bases y consentimiento explícito.
- No hay patrón subregional; la adopción responde en parte al "efecto Bruselas".
- Caso costarricense citado: la Unidad Presidencial de Análisis de Datos (UPAD, 2020).

**Precisión sobre la lectura de la ley:** el artículo cita un "art. 1.c" de la Ley 8968 que excluiría las bases de datos judiciales y de seguridad. El texto vigente del art. 1 solo establece el objetivo de la ley. La seguridad pública **no está excluida**: el art. 8 permite **limitar** los derechos para esos fines (ver sección 8).

**Limitaciones:** mide la ley escrita, no su aplicación; el puntaje es ordinal.

---

## 6. Lectura cruzada

### Convergencias

1. **El umbral es el punto crítico.** P1 exige reportar a umbral fijo; P2 documenta umbrales de 0.55 y 0.59 decididos por la policía; O2 corrige el sesgo de un umbral único; O4 critica que las API ocultaran su umbral.
2. **El error depende del algoritmo y del contexto, no solo de la persona.** Los algoritmos más precisos tienen menos diferenciales (P1); la calidad de imagen y los factores no demográficos pesan (P4, O1).
3. **La regulación llega tarde y por excepción.** Así ocurre en EE. UU. y Europa (P3) y en América Latina (O6, O7).

### Contradicciones y matices

| Tensión | Trabajo A | Trabajo B | Lectura |
|---|---|---|---|
| Laboratorio vs. campo | P1: algoritmos de punta casi sin diferenciales en 1:N | P2: 9 de 43 alertas correctas en Londres | La exactitud del algoritmo no es la del sistema desplegado |
| ¿El algoritmo es sesgado? | O4 y P1: diferencias grandes por sexo y raza | O1: parte de la brecha por sexo desaparece al igualar el rostro visible | Explicar la causa no elimina el daño a la persona afectada |
| Ley fuerte vs. aplicación | O7: Costa Rica con puntaje máximo | O6 y sección 8: videovigilancia por decreto; biometría no nombrada en la ley | Protección alta en el papel, con vacíos en seguridad pública |
| Protección del usuario | O3: 100 % contra servicios comerciales | PuFace (2024): elimina buena parte de la protección | Ningún control es definitivo |
| Balancear datos | Intuición común: balancear corrige el sesgo | P4 y O2: no basta y puede empeorarlo | El control debe medirse, no suponerse |

### Vacíos de investigación

- Casi no hay estudios de sesgo con imágenes de baja resolución de videovigilancia (P4, P1).
- No hay mediciones independientes de desempeño en campo en América Latina; solo cifras oficiales no auditadas (O6).
- Costa Rica no tiene estudios empíricos de despliegue; solo mapeos legales (O6, O7).
- No hay un banco de pruebas común para defensas adversarias ni para detección de morphing (P5, O5).

---

## 7. Conexión con el curso

| Clase | Concepto | Dónde aparece |
|---|---|---|
| 1–2 | **Confidencialidad:** exposición de rostros; extracción masiva | O3, P3 |
| 1–2 | **Integridad:** identidad alterada por falso positivo, ataque adversario o morph | P1, P5, O5 |
| 1–2 | **Disponibilidad:** falso rechazo que niega acceso a un servicio | P1, P4 |
| 1–2 | Ataque **activo** (suplantación, adversario) vs. vigilancia **pasiva** (observar sin alterar) | P5, P2 |
| 3 | Privacidad como control; autodeterminación informativa | P3, O7, Ley 8968 art. 4 |
| 3 | Ley 8968, PRODHAB, derechos ARCO | O6, O7, sección 8 |
| 3 | Privacidad desde el diseño y por defecto | P3 (Bridges) |
| 3 | Extracción masiva y reidentificación | O3, P3 |
| 4 | **Fail-safe:** ante una coincidencia incierta, no intervenir | P2 |
| 4 | **Privilegio mínimo:** alcance de las listas de vigilancia | P2, Bridges |
| 4 | **Defensa en profundidad** | P5, O3 |
| 4 | Dilema ético entre seguridad pública y privacidad | P3, O6 |
| 5 | Cadena principio → política → procedimiento → control → métrica | P1, P3, O2 |
| 5 | EIPD como política verificable; ISO/IEC 19795-10 | P3, P4 |
| 6 | Secreto comercial usado para negar el código (Buenos Aires) | O6 |
| 6 | Extracción contra términos de servicio (Clearview) | P3 |
| 7 | Ataques adversarios como prueba de *red team*; ISO/IEC 30107-3 | P5, O5 |
| 16 | FMR, FNMR, FPIR, FNIR, umbral, irrevocabilidad del rasgo | P1, O2, O5 |

---

## 8. Costa Rica: marco legal, despliegues e interpretación

### 8.1 Ley 8968 (2011): lo que dice el texto vigente

Fuente: texto completo de la Ley N.º 8968, *Protección de la Persona frente al Tratamiento de sus Datos Personales*, del 7 de julio de 2011 (SCIJ; copia publicada por el MICITT, generada el 7/1/2026).

| Artículo | Contenido relevante para el tema |
|---|---|
| 1 | Objetivo: garantizar a cualquier persona el derecho a la autodeterminación informativa. **No contiene exclusiones.** |
| 2 | Aplica a bases automatizadas o manuales, públicas o privadas. Solo excluye las bases con fines exclusivamente internos, personales o domésticos que no se comercialicen. |
| 3.b | Dato personal: cualquier dato relativo a una persona física identificada o identificable. |
| 3.e | Datos sensibles: fuero íntimo, "como por ejemplo" origen racial, opiniones políticas, convicciones religiosas o espirituales, condición socioeconómica, información biomédica o genética, vida y orientación sexual, **"entre otros"**. **No menciona datos biométricos.** |
| 4 | Autodeterminación informativa como derecho fundamental, con el objeto de evitar acciones discriminatorias. |
| 5 | Consentimiento informado, **expreso y por escrito**. No se requiere con orden judicial o de comisión legislativa, con datos de acceso irrestricto, o por disposición constitucional o legal. Prohíbe el acopio sin consentimiento. |
| 6 | Calidad y adecuación al fin; conservación máxima de 10 años para datos que puedan afectar al titular. |
| 7.1.d | Derecho del titular a conocer "el sistema, programa, método o proceso" usado en el tratamiento de sus datos. |
| 8 | **Excepciones:** los principios y derechos pueden limitarse "de manera justa, razonable y acorde con el principio de transparencia administrativa" para la seguridad del Estado, la seguridad y el ejercicio de la autoridad pública, y la prevención, persecución, investigación, detención y represión de infracciones penales, entre otros fines. |
| 9.1 | Prohíbe tratar datos sensibles (misma lista, con "entre otros"), salvo excepciones: interés vital, organizaciones con fines específicos, datos hechos públicos por el titular o necesarios en un proceso judicial, y salud. |
| 9.3 | La **fotografía** no se considera dato de acceso irrestricto. |
| 10 | Deber de medidas técnicas y organizativas de seguridad contra alteración, destrucción, pérdida o acceso no autorizado. |
| 15–16 | PRODHAB: órgano de desconcentración máxima adscrito al Ministerio de Justicia y Paz, con independencia de criterio. Lleva el registro de bases, puede acceder a ellas, resolver denuncias, ordenar supresión y sancionar. |
| 21 | Registro obligatorio de las bases administradas con fines de distribución, difusión o comercialización. |
| 28–31 | Multas en salarios base según la gravedad. Tratar datos sensibles por parte de privados es falta gravísima (31.a). |
| 32 | Bases públicas: la PRODHAB dicta una resolución con medidas para que cese o se corrija la falta, notificada al superior jerárquico. |

**Reglamento:** Decreto Ejecutivo N.º 37554-JP (2012). Exige protocolos mínimos de actuación y medidas de seguridad (arts. 27, 32, 34 y 35) y actualizar la inscripción ante la PRODHAB cuando cambia el tratamiento (art. 54).

### 8.2 Videovigilancia y seguridad pública

- La vigilancia de vías se rige por los decretos **34104-G-MSP (2007)** y **35532-MSP (2009)**, desactualizados y desconectados de la Ley 8968 y su reglamento (O6, citando a Chacón, 2019).
- En la práctica, los municipios operan las cámaras sin base legal propia, y la señalización es mínima (O6).
- Según O6, las competencias de la PRODHAB sobre videovigilancia son limitadas y la doctrina citada sostiene que estas medidas deberían regularse por ley (reserva legal), no por decreto.

### 8.3 Resolución N.º 029-2026-RF de la PRODHAB (mayo de 2026)

Fuentes: M. del P. López, "Datos biométricos y autodeterminación informativa en la Resolución N.º 029–2026–RF de la Prodhab de Costa Rica," IAPP, 7 jul. 2026; V. Martínez, "Costa Rica usa cada vez más reconocimiento facial, pero la ley todavía tiene vacíos," Teletica, 15 sep. 2026.

- Resolvió, **más de cinco años después**, una denuncia de diciembre de 2020 contra el Tribunal Supremo de Elecciones (TSE).
- Dos conductas examinadas: la consulta pública irrestricta de datos del Registro Civil en la web del TSE, y la comercialización de verificación biométrica mediante el **Sistema de Verificación de Identidad (VID)**, operado desde 2015 para bancos y comercios.
- Criterios que consolida:
  1. **Los datos biométricos son datos sensibles bajo la Ley 8968**, aunque la ley no los nombre.
  2. El **principio de finalidad** impide reutilizar comercialmente datos recolectados para fines electorales.
  3. La publicidad registral requiere habilitación legal específica.
- Se apoyó en el criterio **PGR-C-251-2021** de la Procuraduría: el art. 24 del Código Electoral no habilita vender datos biométricos.
- El TSE no acreditó protocolos para el VID ni actualizó su inscripción ante la PRODHAB.
- La autora del análisis señala como punto débil que en cada verificación el titular participa voluntariamente; la infracción más sólida es la falta de información previa sobre la existencia del sistema (art. 5).
- **El TSE anunció que apelaría** y rechazó que exista comercialización.

### 8.4 Caso UPAD (2020–2022)

Fuentes: La Nación, 8 jul. 2021 y 18 ago. 2022; Semanario Universidad, 18 ago. 2022; Access Now, 13 ene. 2023.

- El Decreto N.º 41996-MP-MIDEPLAN, publicado el **17 de febrero de 2020**, creó la Unidad Presidencial de Análisis de Datos. Su art. 7 le daba acceso a "información de carácter confidencial" de las instituciones públicas.
- Fue derogado el **21 de febrero de 2020** (Decreto 42216).
- La Fiscalía allanó Casa Presidencial el **28 de febrero de 2020**.
- La Defensoría de los Habitantes constató que el uso del SINIRUBE permitió a la UPAD acceder a datos sensibles.
- En **agosto de 2022**, la Sala Constitucional declaró por mayoría que el art. 7, párrafo segundo, infringió el derecho a la autodeterminación informativa y el principio de reserva legal.

### 8.5 Despliegues de reconocimiento facial en el país

| Año | Despliegue | Fuente |
|---|---|---|
| 2019 | Naranjo: videovigilancia con reconocimiento facial, 35 cámaras | O6 |
| 2019 | TSE anuncia reconocimiento facial asociado a las huellas del VID | O6 |
| 2020 | Alajuela: 195 cámaras con reconocimiento facial; la municipalidad indicó que solo se habilitaría para personas con denuncia de desaparición o requeridas por autoridades | El Mundo CR y Eco Municipal, nov. 2020 |
| 2025 | Romería: más de 290 cámaras con reconocimiento facial y lectura de placas | Teletica, sep. 2026 |
| 2025–2026 | Puertas biométricas en el Aeropuerto Juan Santamaría (reconocimiento facial y pasaporte biométrico) | Teletica, sep. 2026 |
| 2026 | Centro de mando del Ministerio de Seguridad Pública con cámaras de reconocimiento facial, interconexión con cámaras municipales; el ministro indicó coordinación con la PRODHAB; financiamiento del BID (US$1.5 M) y donación de EE. UU. (US$9.5 M) | El Observador, jul. 2025 |

### 8.6 Reforma legal en trámite

- **Expediente N.º 23.097**, *Ley de Protección de Datos Personales*, presentado el 9 de mayo de 2022 y dictaminado por la Comisión de Ciencia y Tecnología el 23 de enero de 2023.
- Define expresamente los datos biométricos y prohíbe tratarlos como datos sensibles, salvo excepciones.
- La Procuraduría emitió observaciones en 2023, entre ellas sobre la independencia de la agencia.
- A julio de 2026 seguía en trámite.

### 8.7 Interpretación general del caso costarricense

1. **Protección alta en el papel, con la biometría fuera del texto.** O7 le da a la Ley 8968 el puntaje máximo de la región, pero la ley no nombra la biometría. Que el rostro sea dato sensible depende hoy de una interpretación administrativa (Resolución 029-2026-RF), apelada por el TSE. La protección del dato más usado por el reconocimiento facial descansa en un criterio que puede cambiar, no en una norma expresa.
2. **La seguridad pública no está excluida, pero tampoco regulada.** El art. 8 permite limitar los derechos con fines policiales, con el único límite de hacerlo "de manera justa, razonable y acorde con la transparencia administrativa". No hay reglas sobre listas de vigilancia, umbrales, tasas de error tolerables, auditorías ni revisión humana. Es el mismo patrón de **excepción general** que O6 documentó en la región y que P3 criticó en EE. UU.
3. **La tecnología avanza antes que la regulación.** Los despliegues crecen (municipios, Romería, aeropuerto, centro de mando), mientras la videovigilancia se rige por decretos de 2007 y 2009 y la reforma legal lleva más de cuatro años en trámite. Es la situación que P2 observó en Londres antes del caso Bridges y que O6 describió en Buenos Aires antes del fallo judicial.
4. **Los controles existen, pero llegan tarde.** La Sala Constitucional resolvió el caso UPAD en dos años y medio; la PRODHAB resolvió el caso VID en más de cinco. En términos del curso, el control es **correctivo** y no **preventivo**: no existe un equivalente a la evaluación de impacto obligatoria antes de desplegar.
5. **Hay una base para exigir transparencia algorítmica.** El art. 7.1.d reconoce el derecho a conocer el sistema o método de tratamiento. Contrasta con Buenos Aires, donde el gobierno negó el acceso al código invocando secreto comercial (O6).
6. **Frente a Europa, falta la capa de habilitación.** Desde el 2 de febrero de 2025, el Reglamento Europeo de IA solo permite la identificación biométrica remota en tiempo real con fines policiales si una ley nacional la autoriza, con evaluación de impacto en derechos fundamentales y registro. Costa Rica no tiene esa capa: el uso se ampara en la excepción general del art. 8.
7. **Lectura en términos de la tríada CID:**
   - *Confidencialidad:* bases de rostros y del Registro Civil accesibles a terceros (VID) o a unidades sin base legal (UPAD).
   - *Integridad:* sin reglas sobre tasas de error, un falso positivo en vía pública no tiene un umbral ni un procedimiento de revisión definidos.
   - *Disponibilidad:* la verificación biométrica comercial condiciona el acceso a servicios financieros al funcionamiento de un solo sistema.

---

## 9. Casos internacionales y documentos originales

| ID | Caso | Fecha | Documento original | Hechos verificados |
|---|---|---|---|---|
| A01 | *R (Bridges) v Chief Constable of South Wales Police* | 11 ago. 2020 | [2020] EWCA Civ 1058, Tribunal de Apelación de Inglaterra y Gales (judiciary.uk; caselaw.nationalarchives.gov.uk) | El uso de reconocimiento facial en vivo por la policía galesa no era "conforme a la ley" (art. 8 del CEDH): demasiada discreción sobre quién entra a la lista de vigilancia y dónde se despliega. La EIPD fue deficiente y no se cumplió el deber público de igualdad. Primer desafío judicial exitoso contra esta tecnología. |
| A02 | Autoridad sueca de datos vs. Consejo de Educación Secundaria de Skellefteå | 20 ago. 2019 | Decisión de la IMY (antes Datainspektionen), DI-2019-2221 | Multa de 200 000 SEK (~20 000 €), primera multa del RGPD en Suecia. Reconocimiento facial para controlar la asistencia de 22 estudiantes durante tres semanas; el consentimiento se consideró inválido por la relación de dependencia; evaluación de impacto inadecuada. |
| A03 | Autoridad sueca de datos vs. Autoridad Policial Sueca (uso de Clearview AI) | 10 feb. 2021 | Decisión de la IMY, DI-2020-2719 | Multa de 2 500 000 SEK (~250 000 €) por la Ley de Datos Criminales. Uso sin autorización entre el otoño de 2019 y marzo de 2020, sin evaluación de impacto. Se ordenó capacitar al personal, informar a los afectados y procurar el borrado de datos enviados a Clearview. |
| A04 | Retiro o pausa de IBM, Amazon y Microsoft | 8, 10 y 11 jun. 2020 | Carta de Arvind Krishna (IBM) al Congreso de EE. UU., 8 jun. 2020; comunicado de Amazon, 10 jun. 2020; declaración de Microsoft, 11 jun. 2020 (citada en P3) | IBM dejó de ofrecer reconocimiento facial de propósito general; Amazon anunció una moratoria de un año para uso policial de Rekognition; Microsoft condicionó la venta a la policía a una ley federal. |
| A05 | Sistema de Reconocimiento Facial de Prófugos (Buenos Aires) | 2019–2023 | Amparo de la ADC (oct. 2019) y amparo colectivo de ODIA (2020); medida cautelar del juez Gallardo (abr. 2022); sentencia de la jueza Liberatori (7 sep. 2022); Cámara CAyT, Sala I (28 abr. 2023) | La cautelar de abril de 2022 suspendió el sistema. La sentencia de septiembre de 2022 lo declaró inconstitucional: se implementó sin controles, fue usado para buscar a más de 15 000 personas que no estaban en la lista de prófugos, y hubo consultas biométricas sobre casi 10 millones de personas. Se anuló lo actuado sin orden judicial y se condicionó cualquier reactivación a los órganos de control legislativos. La Cámara confirmó la inconstitucionalidad en abril de 2023. |
| A06 | Idec vs. ViaQuatro (Metro de São Paulo) | 2018–2023 | Acción civil pública del Idec (ago. 2018); sentencia de la 37.ª Vara Cível (may. 2021); decisión del TJSP (may. 2023) | Cámaras publicitarias que detectaban emoción, género y edad de pasajeros sin consentimiento. Suspensión cautelar en 2018; condena de R$100 000 en primera instancia (2021), elevada a R$500 000 en segunda instancia (2023), con prohibición de reactivar el sistema. |
| A07 | Reglamento (UE) 2024/1689, Ley de IA, art. 5(1)(h) | En vigor 1 ago. 2024; prohibiciones aplicables desde 2 feb. 2025 | Diario Oficial de la UE (EUR-Lex) | Prohíbe por defecto la identificación biométrica remota en tiempo real en espacios públicos con fines policiales. Solo hay tres excepciones, que requieren ley nacional habilitante, autorización judicial o administrativa independiente, evaluación de impacto en derechos fundamentales (art. 27) y registro (art. 49). |
| A08 | FTC vs. Rite Aid | 19 dic. 2023 | Comunicado y orden de la Comisión Federal de Comercio de EE. UU. | Prohibición de usar reconocimiento facial con fines de vigilancia durante cinco años. Entre 2012 y 2020 la cadena escaneó clientes en cientos de tiendas sin pruebas de exactitud; los falsos positivos afectaron sobre todo a mujeres y personas de color. Obligación de borrar imágenes y modelos derivados. |
| A09 | Sanciones a Clearview AI en Europa | 2022–2025 | Garante italiano (10 feb. 2022); CNIL Francia (20 oct. 2022 y 10 may. 2023); autoridad griega (2022); ICO Reino Unido (may. 2022); AP Países Bajos (3 sep. 2024) | 20 M€ en Italia, 20 M€ más 5.2 M€ adicionales en Francia, 20 M€ en Grecia, 30.5 M€ en Países Bajos, y £7.5 M en el Reino Unido. La multa británica fue anulada por el First-tier Tribunal en 2023 por jurisdicción; en octubre de 2025 el Upper Tribunal restituyó la jurisdicción del ICO y devolvió el caso para nueva audiencia. La recaudación sigue en disputa porque la empresa no tiene establecimiento en la UE. |
| A10 | UPAD (Costa Rica) | 2020–2022 | Decreto 41996-MP-MIDEPLAN; Decreto 42216; sentencia de la Sala Constitucional (ago. 2022) | Ver sección 8.4. |

---

## 10. Glosario

| Término | Significado |
|---|---|
| Verificación (1:1) | ¿Esta persona es quien dice ser? Una comparación contra una referencia |
| Identificación (1:N) | ¿Quién es esta persona? Búsqueda contra una galería o lista de vigilancia |
| Puntaje de similitud | Número que expresa cuán parecidos son dos rostros; se compara con el umbral |
| Umbral | Valor a partir del cual el sistema declara coincidencia |
| FMR | Tasa de falsas coincidencias (1:1) |
| FNMR | Tasa de falsos rechazos (1:1) |
| FPIR / FNIR | Equivalentes de FMR y FNMR en identificación 1:N |
| Diferencial demográfico | Diferencia en distribuciones de puntajes o tasas de error entre grupos (P1; ISO/IEC 19795-10) |
| WERM | Métrica de equidad: peor tasa de error frente a la media geométrica de los grupos (O2) |
| Ataque de presentación | Engañar al sensor con un artefacto físico (foto, máscara); ISO/IEC 30107-3 |
| Ataque adversario | Perturbación diseñada para que el modelo se equivoque (P5) |
| Morph | Imagen que fusiona dos rostros y verifica a ambos (O5) |
| MMPMR | Tasa de morphs aceptados para todos sus contribuyentes (O5) |
| APCER / BPCER | Errores de un detector de ataques: ataques aceptados y genuinos rechazados |
| DSSIM | Medida de distorsión perceptual de una imagen (O3) |
| EIPD (DPIA) | Evaluación de impacto de protección de datos (RGPD, art. 35) |
| Lista de vigilancia | Galería de personas buscadas contra la que se compara (P2) |
| Identificación biométrica remota en tiempo real | Identificación a distancia, sin participación de la persona, con captura y comparación inmediatas (Reglamento UE 2024/1689) |
| Dato sensible (Ley 8968) | Información del fuero íntimo cuyo tratamiento puede generar discriminación (art. 3.e); la PRODHAB incluye la biometría desde 2026 |

---

## 11. Referencias

### Trabajos revisados

[1] P. Grother, M. Ngan y K. Hanaoka, "Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects," National Institute of Standards and Technology, Gaithersburg, MD, EE. UU., NISTIR 8280, dic. 2019, doi: 10.6028/NIST.IR.8280.

[2] P. Fussey, B. Davies y M. Innes, "'Assisted' facial recognition and the reinvention of suspicion and discretion in digital policing," *The British Journal of Criminology*, vol. 61, n.º 2, pp. 325–344, mar. 2021, doi: 10.1093/bjc/azaa068.

[3] D. Almeida, K. Shmarko y E. Lomas, "The ethics of facial recognition technologies, surveillance, and accountability in an age of artificial intelligence: a comparative analysis of US, EU, and UK regulatory frameworks," *AI and Ethics*, vol. 2, pp. 377–387, 2022, doi: 10.1007/s43681-021-00077-w.

[4] K. Kotwal y S. Marcel, "Review of Demographic Fairness in Face Recognition," *IEEE Trans. Biom. Behav. Identity Sci.*, vol. 8, n.º 1, pp. 20–45, 2026, doi: 10.1109/TBIOM.2025.3601217.

[5] F. Vakhshiteh, A. Nickabadi y R. Ramachandra, "Adversarial Attacks Against Face Recognition: A Comprehensive Study," *IEEE Access*, vol. 9, pp. 92735–92756, 2021, doi: 10.1109/ACCESS.2021.3092646.

[6] V. Albiero, K. Zhang, M. C. King y K. W. Bowyer, "Gendered Differences in Face Recognition Accuracy Explained by Hairstyles, Makeup, and Facial Morphology," *IEEE Trans. Inf. Forensics Security*, vol. 17, pp. 127–137, 2022, doi: 10.1109/TIFS.2021.3135750.

[7] Y. Linghu, T. de Freitas Pereira, C. Ecabert, S. Marcel y M. Günther, "Score Normalization for Demographic Fairness in Face Recognition," en *Proc. IEEE Int. Joint Conf. Biometrics (IJCB)*, 2024, pp. 1–11, doi: 10.1109/IJCB62174.2024.10744514.

[8] S. Shan, E. Wenger, J. Zhang, H. Li, H. Zheng y B. Y. Zhao, "Fawkes: Protecting Privacy against Unauthorized Deep Learning Models," en *Proc. 29th USENIX Security Symp.*, 2020, pp. 1589–1604.

[9] J. Buolamwini y T. Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," en *Proc. 1st Conf. Fairness, Accountability and Transparency*, PMLR, vol. 81, 2018, pp. 77–91.

[10] U. Scherhag, C. Rathgeb, J. Merkle, R. Breithaupt y C. Busch, "Face Recognition Systems Under Morphing Attacks: A Survey," *IEEE Access*, vol. 7, pp. 23012–23026, 2019, doi: 10.1109/ACCESS.2019.2899367.

[11] B. D. Franqueira, I. A. Hartmann y L. Abbas da Silva, "O que os olhos não veem, as câmeras monitoram: reconhecimento facial para segurança pública e regulação na América Latina," *Revista Digital de Direito Administrativo*, vol. 8, n.º 1, pp. 171–204, 2021, doi: 10.11606/issn.2319-0558.v8i1p171-204.

[12] E. Chavarría-Mora, "(Lack of) Patterns in Commitment: Data Protection in the Latin America and Caribbean Personal Data Protection Laws," *Social Media + Society*, vol. 11, n.º 2, pp. 1–13, 2025, doi: 10.1177/20563051251337206.

### Normas y documentos oficiales

[13] Asamblea Legislativa de Costa Rica, *Ley N.º 8968, Protección de la Persona frente al Tratamiento de sus Datos Personales*, 7 jul. 2011. Texto completo en SCIJ: https://pgrweb.go.cr/scij/ (copia MICITT: https://micitt.go.cr/sites/default/files/marco_juridico_legal/).

[14] Poder Ejecutivo de Costa Rica, *Decreto Ejecutivo N.º 37554-JP, Reglamento a la Ley de Protección de la Persona frente al Tratamiento de sus Datos Personales*, 2012.

[15] Parlamento Europeo y Consejo, *Reglamento (UE) 2024/1689 (Ley de Inteligencia Artificial)*, DO L, 12 jul. 2024. https://eur-lex.europa.eu/eli/reg/2024/1689/oj

[16] Court of Appeal (England and Wales), *R (Bridges) v Chief Constable of South Wales Police* [2020] EWCA Civ 1058, 11 ago. 2020. https://www.judiciary.uk/judgments/r-bridges-v-cc-south-wales/

[17] Datainspektionen (IMY), *Supervision pursuant to the GDPR – facial recognition used to monitor the attendance of students*, DI-2019-2221, 20 ago. 2019. https://www.imy.se/globalassets/dokument/beslut/facial-recognition-used-to-monitor-the-attendance-of-students.pdf

[18] IMY, "Police unlawfully used facial recognition app," DI-2020-2719, feb. 2021. https://www.imy.se/en/about-us/arkiv/nyhetsarkiv/police-unlawfully-used-facial-recognition-app/

[19] Federal Trade Commission, "Rite Aid Banned from Using AI Facial Recognition After FTC Says Retailer Deployed Technology without Reasonable Safeguards," 19 dic. 2023. https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without

[20] Autoriteit Persoonsgegevens, "Decision fine Clearview AI," 3 sep. 2024. https://www.autoriteitpersoonsgegevens.nl/en/documents/decision-fine-clearview-ai

[21] Garante per la protezione dei dati personali, *Ordinanza ingiunzione nei confronti di Clearview AI*, 10 feb. 2022 (resumen del EDPB: https://www.edpb.europa.eu/news/national-news/2022/facial-recognition-italian-sa-fines-clearview-ai-eur-20-million_en).

### Análisis y reportes sobre casos

[22] M. del P. López, "Datos biométricos y autodeterminación informativa en la Resolución N.º 029–2026–RF de la Prodhab de Costa Rica," IAPP, 7 jul. 2026. https://iapp.org/news/a/datos-biom-tricos-y-autodeterminaci-n-informativa-en-la-resoluci-n-n-029-2026-rf-de-la-prodhab

[23] V. Martínez, "Costa Rica usa cada vez más reconocimiento facial, pero la ley todavía tiene vacíos," Teletica, 15 sep. 2026. https://www.teletica.com/nacional/costa-rica-usa-cada-vez-mas-reconocimiento-facial-pero-la-ley-todavia-tiene-vacios_417006

[24] Access Now, "El estado actual de la protección de los datos biométricos en Costa Rica," 13 ene. 2023. https://www.accessnow.org/el-estado-actual-de-la-proteccion-de-los-datos-biometricos-en-costa-rica/

[25] Semanario Universidad, "Sala IV declara inconstitucional creación de la UPAD durante la administración Alvarado Quesada," 18 ago. 2022. https://semanariouniversidad.com/pais/sala-constitucional-declara-inconstitucional-creacion-de-la-upad-durante-la-administracion-alvarado-quesada/

[26] CELS, "Declaran inconstitucional el uso del sistema de reconocimiento facial en CABA," 10 sep. 2022. https://www.cels.org.ar/web/2022/09/una-jueza-declaro-inconstitucional-el-uso-del-sistema-de-reconocimiento-facial-en-caba/

[27] Idec, "Idec vence ação contra uso de reconhecimento facial e ViaQuatro é condenada a pagar indenização de R$ 500 mil," 12 may. 2023. https://idec.org.br/noticia/idec-vence-acao-contra-uso-de-reconhecimento-facial-e-viaquatro-e-condenada-pagar

[28] Privacy International, "Challenge against Clearview AI in Europe." https://privacyinternational.org/legal-action/challenge-against-clearview-ai-europe

[29] El Observador, "Policías y patrullas de Fuerza Pública con cámaras: nuevo centro de mando operará en 2026," 21 jul. 2025. https://observador.cr/policias-y-patrullas-de-fuerza-publica-con-camaras-nuevo-centro-de-mando-operara-en-2026-anuncia-ministro-de-seguridad/

[30] IPANDETEC, "El nuevo proyecto de Ley de Protección de Datos Personales en Costa Rica," 15 jul. 2025. https://ipandetec.org/costa-rica/el-nuevo-proyecto-de-ley-de-proteccion-de-datos-personales-en-costa-rica/