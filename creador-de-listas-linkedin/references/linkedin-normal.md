# LinkedIn normal, modo light

Comprobación documental: 2026-09-13. Usar únicamente controles que el usuario tenga disponibles.

LinkedIn permite buscar personas desde la barra, seleccionar People y refinar desde All filters. Su ayuda menciona ubicación, conexiones, empresa actual, industria y palabras clave, entre otros controles. También describe búsqueda por lenguaje natural y Boolean como alternativas. Si se usa lenguaje natural, no mezclar comillas ni sintaxis Boolean en la misma consulta. No asumir que toda cuenta tiene la misma experiencia. [Búsqueda de personas](https://www.linkedin.com/help/linkedin/answer/a525054).

Entrega 1 consulta corta, la pestaña Personas, los filtros disponibles y lo que deberá revisarse perfil por perfil. Si no aparece un filtro, no prometer equivalencia. Tamaño exacto del equipo, actividad reciente, rol actual y exclusiones se verifican manualmente cuando no exista el control necesario. No atribuir listas guardadas ni funciones avanzadas a una cuenta gratuita sin comprobarlo.

Si la búsqueda parte de empresas, localizar las empresas y buscar personas indicando la empresa actual; verificar que trabajan allí ahora. Conservar en un registro local los perfiles revisados y sus enlaces. Separar los resultados guardados en ese registro de cualquier lista dentro de LinkedIn.

Pedir el recuento observado y revisar calidad antes de ampliar. No prometer 100–300 perfiles ni proponer saltarse límites de la cuenta. Cuando falte acceso o alcance, entregar el estado parcial y continuar con otro segmento permitido o más adelante.

## Prueba real con navegador (2026-10-07)

Búsqueda de Personas en México, sector Staffing and Recruiting (ID 104, menú en español: "Dotación y selección de personal") y palabra clave "fundador". Resultado reportado en la prueba original: 10 páginas visibles; de los primeros 10 perfiles, 2 A, 3 B y 5 Fuera con el criterio anterior de rol/giro. Esos conteos no equivalen a ENCAJA según la revisión completa actual ni a un límite universal de LinkedIn. La evidencia de navegación no está incluida en este repositorio; repetir la muestra en la cuenta del usuario.

- Ubicación y sector viajan en la URL: `geoUrn=["103323778"]` (México) e `industry=["104"]`. Con eso la URL sirve como búsqueda guardada.
- El parámetro de cargo (`titleFreeText`) se descartó al cargar desde URL: no confiar en él; aplicar el filtro de cargo desde el menú y verificarlo en pantalla, o usar 1 palabra clave.
- Una cadena OR larga en palabras clave mostró 0 resultados. No quedó confirmado si fue la sintaxis o la carga de la página. Por defecto, 1 término de puesto por búsqueda.
- El sector filtra por la industria del perfil de la persona, no de su empresa: se cuelan perfiles de otros giros. Revisar titular.
- En el resultado solo se ven puesto y giro; la señal (publica, contrata) exige abrir el perfil.
- El link del perfil está en el enlace del nombre. Al copiar texto de la página no viaja.
