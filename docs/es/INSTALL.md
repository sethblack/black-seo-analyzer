# Instalación de Black SEO Analyzer

Este documento proporciona instrucciones para instalar la herramienta Black SEO Analyzer en diferentes sistemas operativos.

## Tabla de Contenidos

- [Prerrequisitos](#prerrequisitos)
- [Instalación Básica](#instalacion-basica)
  - [Windows](#windows-basico)
  - [macOS](#macos-basico)
  - [Linux](#linux-basico)
- [Instalación Avanzada](#instalacion-avanzada)
  - [Windows](#windows-avanzado)
- [Verificación de la Instalación](#verificacion-instalacion)
- [Solución de Problemas](#solucion-problemas)

## Prerrequisitos

Antes de instalar Black SEO Analyzer, asegúrese de tener lo siguiente:

- Conexión a Internet para descargar la herramienta
- Familiaridad básica con las interfaces de línea de comandos (para la instalación básica)
- Privilegios de administrador/sudo (pueden ser necesarios para algunos métodos de instalación)

## Instalación Básica

### Windows (Básico) {#windows-basico}

1. Descargue el último ejecutable de Windows (`black-seo-analyzer.exe`) desde la [página de lanzamientos](https://github.com/sethblack/black-seo-analyzer/releases).

2. Mueva el archivo `black-seo-analyzer.exe` descargado a una ubicación de su elección (p. ej., `C:\Program Files\black-seo-analyzer`).

3. Abra el Símbolo del sistema y navegue al directorio donde colocó el ejecutable:

```cmd
cd C:\Program Files\black-seo-analyzer
```

4. Abra el Símbolo del sistema y verifique la instalación:

```cmd
black-seo-analyzer --version
```

5. Cree un archivo `license.txt` en el mismo directorio con su clave de licencia:

```cmd
echo "SU_CLAVE_DE_LICENCIA" > license.txt
```

#### Ejemplo de Inicio Rápido

Analizar un sitio web y generar un informe HTML:

```cmd
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

### macOS (Básico) {#macos-basico}

1. Descargue el último binario de macOS (`black-seo-analyzer`) desde la [página de lanzamientos](https://github.com/sethblack/black-seo-analyzer/releases).

2. Mueva el binario descargado a una ubicación en su PATH (p. ej., `/usr/local/bin/`):

```bash
sudo mv /ruta/al/descargado/black-seo-analyzer /usr/local/bin/
```
   *(Reemplace `/ruta/al/descargado/black-seo-analyzer` con la ruta real al archivo descargado)*

3. Hágalo ejecutable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

4. Verifique la instalación:

```bash
black-seo-analyzer --version
```

5. Cree un archivo `license.txt` en el mismo directorio que el binario (`/usr/local/bin/` en este ejemplo) o en su directorio de trabajo con su clave de licencia:

```bash
echo "SU_CLAVE_DE_LICENCIA" > license.txt
```

#### Ejemplo de Inicio Rápido

Analizar un sitio web y generar un informe HTML:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

### Linux (Básico) {#linux-basico}

#### Ubuntu/Debian

1. Descargue el último binario de Linux (`black-seo-analyzer`) para su arquitectura desde la [página de lanzamientos](https://github.com/sethblack/black-seo-analyzer/releases).

2. Mueva el binario descargado a una ubicación en su PATH (p. ej., `/usr/local/bin/`):

```bash
sudo mv /ruta/al/descargado/black-seo-analyzer /usr/local/bin/
```
   *(Reemplace `/ruta/al/descargado/black-seo-analyzer` con la ruta real al archivo descargado)*

3. Hágalo ejecutable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

4. Verifique la instalación:

```bash
black-seo-analyzer --version
```

#### Fedora/RHEL/CentOS

1. Descargue el último binario de Linux (`black-seo-analyzer`) para su arquitectura desde la [página de lanzamientos](https://github.com/sethblack/black-seo-analyzer/releases).

2. Mueva el binario descargado a una ubicación en su PATH (p. ej., `/usr/local/bin/`):

```bash
sudo mv /ruta/al/descargado/black-seo-analyzer /usr/local/bin/
```
   *(Reemplace `/ruta/al/descargado/black-seo-analyzer` con la ruta real al archivo descargado)*

3. Hágalo ejecutable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

4. Verifique la instalación:

```bash
black-seo-analyzer --version
```

#### Ejemplo de Inicio Rápido

Analizar un sitio web y generar un informe HTML:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

## Instalación Avanzada

### Windows (Avanzado) {#windows-avanzado}


#### Instalación Manual

1. Descargue el último ejecutable de Windows (`black-seo-analyzer.exe`) desde la [página de lanzamientos](https://github.com/sethblack/black-seo-analyzer/releases).

2. Coloque el archivo `black-seo-analyzer.exe` descargado en una ubicación de su elección (p. ej., `C:\Program Files\black-seo-analyzer`).

3. Agregue el directorio que contiene el ejecutable a la variable de entorno PATH de su sistema:
   - Haga clic derecho en "Este equipo" o "Mi PC" y seleccione "Propiedades"
   - Haga clic en "Configuración avanzada del sistema"
   - Haga clic en "Variables de entorno"
   - En "Variables del sistema", busque y seleccione "Path", luego haga clic en "Editar"
   - Haga clic en "Nuevo" y agregue la ruta al directorio que contiene el ejecutable (p. ej., `C:\Program Files\black-seo-analyzer`)
   - Haga clic en "Aceptar" en todos los cuadros de diálogo para guardar los cambios

4. Abra un *nuevo* Símbolo del sistema (los existentes no verán el PATH actualizado) y verifique la instalación:

```cmd
black-seo-analyzer --version
```


## Verificación de la Instalación {#verificacion-instalacion}

Después de la instalación, verifique que Black SEO Analyzer funcione correctamente:

```bash
black-seo-analyzer --version
```

Debería ver una salida similar a:

```
black-seo-analyzer 2025.1.6
```

## Solución de Problemas {#solucion-problemas}

### Problemas Comunes

#### Error "Comando no encontrado"

- Asegúrese de que el directorio de instalación esté en su PATH
- Intente reiniciar su terminal o símbolo del sistema

#### Dependencias faltantes

Si encuentra errores sobre dependencias faltantes:

- Windows: Instale el [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Linux: Instale las bibliotecas requeridas:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install libssl-dev pkg-config

  # Fedora/RHEL/CentOS
  sudo dnf install openssl-devel pkgconfig
  ```
- macOS: Instale las bibliotecas requeridas:
  ```bash
  brew install openssl@3
  ```

#### Permiso denegado

Si obtiene errores de "permiso denegado" al ejecutar la herramienta:

- Windows: Ejecute el Símbolo del sistema como Administrador
- macOS/Linux: Use sudo o asegúrese de que el binario tenga permisos de ejecución:
  ```bash
  sudo chmod +x /ruta/a/black-seo-analyzer
  ```

### Obtener Ayuda

Si encuentra problemas no cubiertos en esta guía:

1. Consulte los [Issues de GitHub](https://github.com/sethblack/black-seo-analyzer/issues) para problemas y soluciones similares
2. Abra un nuevo issue con detalles sobre su problema
3. Contacte al soporte en support@example.com

## Opciones de Línea de Comandos

Black SEO Analyzer admite varias opciones de línea de comandos:

```
USO:
    black-seo-analyzer [OPCIONES] --url-to-begin-crawl <URL>

OPCIONES:
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

## Ejemplos

### Análisis Básico de Sitio Web

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com
```

### Análisis de una Aplicación de Página Única (SPA)

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --spa
```

### Análisis de un Sitemap

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap
```

### Generación de Diferentes Formatos de Salida

```bash
# Salida JSON
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type json --output-file report.json

# Salida CSV
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type csv --output-file report.csv

# Salida XML
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type xml --output-file report.xml
```

### Ajuste de la Configuración de Rastreo

```bash
# Aumentar las solicitudes concurrentes para un rastreo más rápido
black-seo-analyzer --url-to-begin-crawl https://example.com --concurrent-requests 30

# Aumentar el límite de tasa para un rastreo más lento (más suave para el servidor)
black-seo-analyzer --url-to-begin-crawl https://example.com --rate-limit 100
```

### Uso de un Idioma Diferente

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --locale es
