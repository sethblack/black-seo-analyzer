# Black SEO Analyzer

Una herramienta profesional de línea de comandos para un análisis SEO completo, diseñada para sitios web que necesitan ser encontrados tanto en los resultados de búsqueda como en las respuestas de IA.

![Black SEO Analyzer](https://www.sethserver.com/static/images/black-seo-analyzer.png)

Para comprar una licencia, visite la [página del producto Black SEO Analyzer](https://www.sethserver.com/seo/black-seo-analyzer.html).

## Descripción General

Black SEO Analyzer es una potente herramienta de línea de comandos que mantiene su sitio web visible tanto en los resultados de búsqueda tradicionales como en las respuestas generadas por IA. Un buen SEO técnico no se trata solo de las clasificaciones de Google, se trata de asegurarse de que los sistemas de IA puedan encontrar y comprender su contenido cuando la gente pregunte por usted.

Cuando la estructura y los metadatos de su sitio están optimizados correctamente, aparecerá tanto en los resultados de búsqueda como en las conversaciones de IA. Black SEO Analyzer elimina el ruido y le dice exactamente qué está frenando su sitio, sin palabras de moda corporativas, solo datos procesables para que no se quede atrás cuando alguien le pregunte a una IA exactamente sobre lo que vende.

## Lista Completa de Funciones

### Funcionalidad Principal
- Interfaz de línea de comandos
- Rastrear sitios web comenzando desde una URL especificada
- Rastrear sitios web usando un sitemap
- Soporte para sitios web estáticos (solicitudes HTTP) y Aplicaciones de Página Única (SPAs) a través de navegador sin cabeza
- Límite de solicitudes concurrentes configurable
- Límite máximo de páginas configurable
- Sistema de registro detallado
- Ubicación del archivo de registro configurable

### Capacidades de Rastreo
- Rastreador basado en solicitudes HTTP
- Rastreador basado en navegador sin cabeza
- Detección y extracción automática de enlaces, scripts, hojas de estilo, imágenes
- Análisis y procesamiento de sitemaps
- Procesamiento asíncrono para rastreo y análisis
- Generación de hash de contenido (SHA1) para detección de contenido duplicado
- Retraso de rastreo configurable
- Respetar robots.txt
- Personalización del agente de usuario
- Utilidad de extracción de dominio

### Módulos de Análisis SEO
- **Análisis de Contenido**
    - Recuento de palabras
    - Análisis de densidad de palabras clave
    - Análisis de legibilidad (puntuación Flesch-Kincaid, conteo de sílabas)
    - Detección de contenido duplicado
    - Análisis de estructura de encabezados (H1, H2, etc.)
    - Extracción de contenido de etiquetas adicionales (`<strong>`, `<em>`, etc.)
- **Análisis de Metadatos**
    - Extracción y validación de la etiqueta de título
    - Extracción y validación de la meta descripción
    - Extracción de meta palabras clave
    - Validación de la meta etiqueta viewport
    - Validación de la meta etiqueta robots
    - Validación de la URL canónica
    - Extracción y análisis de datos OpenGraph (og:title, og:description, og:image, etc.)
    - Extracción y análisis de datos de Twitter Card (twitter:card, twitter:title, etc.)
- **Análisis de Estructura de URL**
    - Validación del esquema (se prefiere HTTPS)
    - Análisis de la ruta (longitud, uso de caracteres, presencia de palabras clave)
    - Análisis de parámetros de consulta (identificación, problemas potenciales)
    - Análisis de identificadores de fragmento
    - Validación de la longitud de la URL
    - Detección de patrones de URL comunes (p. ej., extensiones de archivo)
- **Análisis de Enlaces**
    - Identificación de enlaces internos y externos
    - Análisis del texto ancla (longitud, descriptividad)
    - Comprobaciones asíncronas del estado del enlace (enlaces rotos)
    - Comprobaciones asíncronas de redirecciones
    - Comprobaciones asíncronas de tamaños de archivo grandes enlazados
    - Análisis de atributos de enlace (nofollow, target)
    - Normalización y clasificación de URLs (internas/externas)
- **Análisis de Imágenes**
    - Presencia de etiqueta alt y análisis de contenido
    - Análisis de dimensiones de imagen
    - Consideraciones sobre el tamaño del archivo
- **Evaluación de Amigabilidad Móvil**
    - Análisis de la meta etiqueta viewport
    - Análisis del tamaño y espaciado de los objetivos táctiles
    - Análisis de imágenes responsivas (atributos `srcset`, `sizes`)
    - Análisis del tamaño de fuente (legibilidad en móviles)
    - Análisis de media queries (cobertura de puntos de interrupción)
- **Análisis de Rendimiento**
    - Análisis de la carga de recursos (scripts, hojas de estilo, imágenes, fuentes)
    - Análisis de carga de scripts (`async`, `defer`)
    - Análisis de carga de hojas de estilo
    - Análisis de carga de imágenes (`loading="lazy"`)
    - Análisis de carga de fuentes (`font-display`)
    - Análisis de la ruta crítica de renderizado
    - Análisis de sugerencias de recursos (`preload`, `prefetch`, `preconnect`)
    - Análisis de encabezados de caché (Cache-Control, Expires)
    - Detección de técnicas de cache busting
    - Análisis de compresión (Content-Encoding)
    - Identificación de recursos críticos
    - Heurísticas de detección de contenido above-the-fold
    - Registro de TTFB y Tiempo Total de Carga
    - Extracción de métricas de rendimiento del navegador/encabezados
- **Análisis de Seguridad**
    - Comprobación de uso de HTTPS
    - Detección de contenido mixto
    - Análisis del encabezado Content Security Policy (CSP)
    - Análisis de seguridad de formularios (autocompletar en campos sensibles)
    - Análisis de integridad de recursos externos (comprobaciones SRI)
    - Comprobación de caducidad del certificado SSL
- **Validación de Datos Estructurados/Marcado Schema**
    - Extracción y validación de JSON-LD
    - Extracción y validación de Microdatos
    - Extracción y validación de RDFa
    - Validación de propiedades de schema contra tipos conocidos
    - Detección de propiedades de schema obsoletas
- **Análisis de Métricas Web Vitals**
    - Análisis relacionado con Largest Contentful Paint (LCP)
    - Análisis relacionado con precursores de First Input Delay (FID) / Interaction to Next Paint (INP)
    - Análisis relacionado con Cumulative Layout Shift (CLS)
    - Análisis relacionado con First Contentful Paint (FCP)
    - Análisis relacionado con Time to Interactive (TTI)
    - Análisis relacionado con Total Blocking Time (TBT)
    - Identificación de recursos bloqueantes, tareas largas, trabajo del hilo principal
    - Análisis del impacto de las dimensiones de imagen, contenido dinámico, carga de fuentes
    - Cálculo de una puntuación de optimización general
    - Generación de recomendaciones específicas basadas en métricas
- **Análisis de CSS**
    - Identificación de estilos externos e inline
    - Análisis del contenido de las hojas de estilo (problemas potenciales, complejidad)
    - Análisis de media queries (relacionado con la responsividad)
    - Comprobaciones básicas de accesibilidad relacionadas con CSS
    - Comprobaciones básicas de rendimiento relacionadas con CSS
    - Detección de reglas CSS potencialmente duplicadas
- **Análisis de JavaScript**
    - Identificación de scripts externos e inline
    - Análisis de atributos de script (`async`, `defer`)
    - Análisis de patrones de carga de scripts
    - Comprobaciones básicas de seguridad
    - Análisis de la complejidad del contenido de scripts inline
    - Análisis de manejadores de eventos
    - Identificación de scripts de terceros
    - Comprobaciones básicas de APIs JS obsoletas
- **Análisis de Internacionalización**
    - Análisis de declaración de idioma (atributo `lang`)
    - Análisis de implementación `hreflang`
    - Análisis de codificación de caracteres (se prefiere UTF-8)
    - Análisis de dirección del texto (atributo `dir`)
    - Comprobaciones básicas de problemas de formato específicos de la configuración regional
    - Comprobaciones básicas de heurísticas de completitud de traducción
    - Comprobaciones básicas de heurísticas de manejo de zona horaria
- **Análisis de IA/LLM**
    - Integración con la API de Anthropic (requiere clave API)
    - Capacidad para enviar contenido de página (o partes) a LLM para análisis basado en prompts predefinidos
    - Recomendaciones de Contenido Impulsadas por IA
    - Generación Automatizada de Meta Descripciones
    - Sugerencias de Optimización de Etiquetas de Título
    - Recomendaciones de Estructura de Encabezados
    - Sugerencias de Expansión de Contenido
    - Generación de Resumen Ejecutivo

### Formatos de Salida
- Formato de salida JSON
- Formato de salida JSONL (JSON Lines)
- Formato de salida XML
- Formato de salida CSV
- Formato de salida HTML
- Archivos JSON individuales por página
- Salida de carpeta HTML con índice e informes de página individuales

### Funciones de Informes
- Advertencias y recomendaciones detalladas generadas por analizadores individuales
- Recopilación de metadatos a nivel de página
- Recopilación de detalles de contenido de página (encabezados, etc.)
- Recopilación de recursos de página (enlaces, scripts, estilos, imágenes)
- Recopilación de resultados de análisis de Web Vitals
- Informes de métricas de rendimiento (TTFB, Tiempo de Carga)
- Generación de informes HTML basados en plantillas

### Internacionalización
- Soporte multilingüe para texto de interfaz de usuario y etiquetas de informe
- Traducciones incorporadas (inglés, español, chino)
- Sistema de traducción extensible
- Configuración regional utilizada para recomendaciones específicas

### Sistema de Licencias
- Modo de prueba con funcionalidad limitada
- Modo con licencia con funcionalidad completa
- Sistema de validación de licencias
- Diferentes niveles de licencia que afectan la funcionalidad

### Detalles Técnicos
- Construido con Rust
- Arquitectura asíncrona
- Análisis HTML y manipulación del DOM
- Integración con Chrome sin cabeza
- Cliente HTTP
- Serialización/Deserialización
- Envoltorio de serialización de URL personalizado
- Utilidad para crear nombres de archivo seguros a partir de URLs
- Análisis de argumentos de línea de comandos
- Motor de plantillas

## Propiedad Real, No Suscripción

A diferencia de las herramientas basadas en suscripción que dejan de funcionar cuando dejas de pagar, Black SEO Analyzer ofrece una propiedad genuina del software. Su compra incluye una garantía de acceso al código fuente legalmente vinculante si alguna vez descontinuamos el producto, protegiendo su inversión permanentemente.

**Licencia de Black SEO Analyzer: Compra Única**
- Propiedad del software de por vida
- Todas las actualizaciones futuras
- Eficiencia de línea de comandos
- Garantía de depósito de código fuente
- URLs y sitios ilimitados
- Todas las funciones avanzadas incluidas

## Instalación

1. Descargue el ejecutable apropiado para su sistema operativo desde la [página de lanzamientos](https://github.com/sethblack/black-seo-analyzer/releases).
2. Haga que el archivo sea ejecutable (Linux/macOS): `chmod +x .\black-seo-analyzer`
3. Muévalo a un directorio en su PATH para un fácil acceso (opcional)

## Uso en Windows

```
Uso: black-seo-analyzer.exe [OPCIONES] --url-to-begin-crawl <URL_PARA_COMENZAR_RASTREO>

Opciones:
      --url-to-begin-crawl <URL_PARA_COMENZAR_RASTREO>
          URL del sitemap a analizar
      --log-file <ARCHIVO_LOG>
          Ruta al archivo de registro
      --output-type <TIPO_SALIDA>
          Tipo de formato de salida [predeterminado: html-folder] [valores posibles: json, jsonl, xml, csv, csv-flat, html-folder, json-files]
      --concurrent-requests <SOLICITUDES_CONCURRENTES>
          Número opcional de solicitudes concurrentes a realizar [predeterminado: 20]
      --rate-limit <LIMITE_TASA>
          Límite de tasa opcional en milisegundos [predeterminado: 50]
      --output-file <ARCHIVO_SALIDA>

      --spa

      --is-sitemap

      --disable-external-links
          Indicador opcional para deshabilitar la comprobación de enlaces externos
      --locale <CONFIGURACION_REGIONAL>
          Configuración regional opcional para internacionalización [predeterminado: en]
      --use-anthropic-analyzer
          Indicador opcional para habilitar la API de Anthropic Claude para análisis SEO
      --anthropic-api-key <CLAVE_API_ANTHROPIC>
          Clave API opcional de Anthropic (también se puede establecer mediante la variable de entorno ANTHROPIC_API_KEY)
      --anthropic-model <MODELO_ANTHROPIC>
          Modelo opcional de Anthropic a usar para el análisis [predeterminado: claude-3-haiku-20240307]
      --user-agent <AGENTE_USUARIO>
          Cadena opcional de User-Agent para solicitudes HTTP [predeterminado: "black-seo-analyzer v2025.1.10000"]
      --max-pages <MAX_PAGINAS>
          Número máximo opcional de páginas a rastrear
  -h, --help
          Imprimir ayuda
  -V, --version
          Imprimir versión
```

### Ejemplo de Uso en Windows

#### Salida JSON básica para un sitio
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type json --output-file example-report.json
```

#### Sitio web con un sitemap
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap --output-type json --output-file sitemap-report.json
```

#### Aplicación de página única
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://spa-example.com --spa --output-type json --output-file spa-report.json
```

#### Salida de carpeta HTML
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type html-folder --output-file ./seo-reports
```

## Uso en Linux/MacOS

```
Uso: black-seo-analyzer [OPCIONES] --url-to-begin-crawl <URL_PARA_COMENZAR_RASTREO>

Opciones:
      --url-to-begin-crawl <URL_PARA_COMENZAR_RASTREO>
          URL del sitemap a analizar
      --log-file <ARCHIVO_LOG>
          Ruta al archivo de registro
      --output-type <TIPO_SALIDA>
          Tipo de formato de salida [predeterminado: html-folder] [valores posibles: json, jsonl, xml, csv, csv-flat, html-folder, json-files]
      --concurrent-requests <SOLICITUDES_CONCURRENTES>
          Número opcional de solicitudes concurrentes a realizar [predeterminado: 20]
      --rate-limit <LIMITE_TASA>
          Límite de tasa opcional en milisegundos [predeterminado: 50]
      --output-file <ARCHIVO_SALIDA>

      --spa

      --is-sitemap

      --disable-external-links
          Indicador opcional para deshabilitar la comprobación de enlaces externos
      --locale <CONFIGURACION_REGIONAL>
          Configuración regional opcional para internacionalización [predeterminado: en]
      --use-anthropic-analyzer
          Indicador opcional para habilitar la API de Anthropic Claude para análisis SEO
      --anthropic-api-key <CLAVE_API_ANTHROPIC>
          Clave API opcional de Anthropic (también se puede establecer mediante la variable de entorno ANTHROPIC_API_KEY)
      --anthropic-model <MODELO_ANTHROPIC>
          Modelo opcional de Anthropic a usar para el análisis [predeterminado: claude-3-haiku-20240307]
      --user-agent <AGENTE_USUARIO>
          Cadena opcional de User-Agent para solicitudes HTTP [predeterminado: "black-seo-analyzer v2025.1.10000"]
      --max-pages <MAX_PAGINAS>
          Número máximo opcional de páginas a rastrear
  -h, --help
          Imprimir ayuda
  -V, --version
          Imprimir versión
```

### Ejemplo de Uso en Linux/MacOS

Notas:

* Si el binario no es ejecutable, es posible que primero deba ejecutar `chmod +x ./black-seo-analyzer`.
* Los ejemplos a continuación asumen que el binario está en el directorio actual. Si está en un directorio diferente, deberá proporcionar la ruta completa al binario o, si está en su PATH, simplemente puede ejecutar `black-seo-analyzer`.

#### Salida JSON básica para un sitio
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com --output-type json --output-file example-report.json
```

#### Sitio web con un sitemap
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap --output-type json --output-file sitemap-report.json
```

#### Aplicación de página única
```bash
./black-seo-analyzer --url-to-begin-crawl https://spa-example.com --spa --output-type json --output-file spa-report.json
```

#### Salida de carpeta HTML
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder --output-file ./seo-reports
```

## Aplicaciones del Mundo Real

### Monitoreo SEO Automatizado

```bash
# Auditoría semanal del sitio con notificación por correo electrónico para problemas críticos
0 0 * * 1 /usr/local/bin/black-seo-analyzer --url-to-begin-crawl example.com --output-type json \
| /usr/local/bin/seo-alert-filter \
| mail -s "Informe SEO Semanal" team@example.com
```

### Integración en Pipeline CI/CD

```yaml
# En su flujo de trabajo de GitHub Actions
seo_validation:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: Ejecutar Análisis SEO
      run: |
        black-seo-analyzer --url-to-begin-crawl https://staging.example.com \
        --output-type json --output-file seo-report.json
    - name: Validar Elementos SEO Críticos
      run: |
        cat seo-report.json | jq '.pages[] | select(.errors | length > 0)' > critical-errors.json
        if [ -s critical-errors.json ]; then
          echo "La validación SEO falló - ver critical-errors.json"
          exit 1
        fi
```

### Análisis Masivo de Sitios

```bash
# Analizar múltiples sitios y combinar informes
for site in site1.com site2.com site3.com; do
  black-seo-analyzer --url-to-begin-crawl $site --output-type json --output-file "${site}.json"
done

# Combinar resultados para comparación
jq -s '[.[] | {site: .site, score: .score, errorCount: .errorCount}]' *.json > summary.json
```

### Flujo de Trabajo de Optimización de Contenido

```bash
# Extraer todas las etiquetas H1 y meta descripciones para revisión de contenido
black-seo-analyzer --url-to-begin-crawl example.com --output-type csv-flat \
| grep -E "(h1|meta_description)" \
| sort -t',' -k2 \
> content-review.csv
```

## Preguntas Frecuentes

**¿Qué diferencia a Black SEO Analyzer de otras herramientas SEO?**  
A diferencia de las herramientas SEO tradicionales con interfaces basadas en navegador y modelos de suscripción, Black SEO Analyzer es una herramienta de línea de comandos que se integra directamente en su flujo de trabajo de desarrollo. Este enfoque permite capacidades de automatización que no son posibles con otras herramientas, además de que usted realmente posee el software con una compra única.

**¿Cómo funciona la garantía del código fuente?**  
Su compra incluye un compromiso legalmente vinculante que le da acceso al código fuente completo si alguna vez descontinuamos el producto, cesamos operaciones o no proporcionamos actualizaciones durante más de 12 meses consecutivos. Esto garantiza que pueda continuar usando el software indefinidamente, independientemente del futuro de nuestra empresa.

**¿Puede Black SEO Analyzer rastrear sitios con mucho JavaScript?**  
Sí, nuestra tecnología integrada de navegador sin cabeza proporciona capacidades completas de renderizado de JavaScript. Esto garantiza un análisis preciso de las aplicaciones web modernas construidas con React, Angular, Vue.js y otros frameworks de JavaScript.

**¿Cómo se manejan las actualizaciones?**  
Las actualizaciones se proporcionan a través de nuestro repositorio de GitHub y se pueden descargar en cualquier momento. Recibirá todas las actualizaciones futuras sin costo adicional. Propiedad de por vida.
