# Installing Black SEO Analyzer

This document provides instructions for installing Black SEO Analyzer on different operating systems.

If you'd rather watch than read, check out my YouTube videos:

[Windows Installation](https://youtu.be/WKq0-EHhuUw)

## Table of Contents

- [Basic Installation](#basic-installation)
  - [Windows](#windows-basic)
  - [macOS](#macos-basic)
  - [Linux](#linux-basic)
- [Advanced Installation](#advanced-installation)
  - [Windows](#windows-advanced)
- [Verifying Installation](#verifying-installation)
- [Troubleshooting](#troubleshooting)

## Basic Installation

### Windows (Basic) {#windows-basic}

#### Windows MSI Installer

1. Download the latest Windows MSI installer (`setup.msi`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Run the `setup.msi` installer. This will install the application to `C:\Program Files (x86)\Black SEO Analyzer\` and add it to your system's PATH.

3. **Note:** If you encounter an error about missing MSVC redistributable DLLs, download and install the [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe).

4. Use the start menu to search for "Black SEO Analyzer" and launch the application.


### macOS (Basic) {#macos-basic}

1. Download the latest macOS DMG (`Black SEO Analyzer.dmg`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases) or from the [official website](https://www.blackseoanalyzer.com/).

2. Open the downloaded DMG file and drag the `Black SEO Analyzer` application to your Applications folder.

3. Open your Applications folder and double-click on `Black SEO Analyzer` to launch the application.

### Linux (Basic) {#linux-basic}

1. Download the latest Linux binary for your architecture from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

   - **x86_64**: For standard 64-bit Intel/AMD processors.
   - **arm**: For ARM-based processors, like those found in Raspberry Pi and some cloud servers.
   - **musl**: A version for containerized environments (e.g., Docker) that uses the musl C standard library.

2. Make the binary executable:

```bash
chmod +x <binary_name>
```

3. Move the binary to a location in your PATH:

```bash
sudo mv <binary_name> /usr/local/bin/black-seo-analyzer
```

4. Verify the installation:

```bash
black-seo-analyzer --version
```

#### Quick Start Example

Analyze a website and generate an HTML report:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

## Advanced Installation

### Windows (Advanced) {#windows-advanced}

#### Manual Installation

1. Download the latest Windows executable file (`black-seo-analyzer.exe`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Move the downloaded `black-seo-analyzer.exe` to a directory that is included in your system's PATH, or add the directory containing the executable to your PATH.

3. To add the binary location to your PATH:
   - Right-click on "This PC" or "My Computer" and select "Properties"
   - Click on "Advanced system settings"
   - Click on "Environment Variables"
   - Under "System variables", find and select "Path", then click "Edit"
   - Click "New" and add the path to the directory containing the binary (e.g., `C:\Program Files\black-seo-analyzer`)
   - Click "OK" on all dialogs to save the changes

4. Open a new Command Prompt and verify the installation:

```cmd
black-seo-analyzer --version
```


## Verifying Installation

After installation, verify that Black SEO Analyzer is working correctly:

```bash
black-seo-analyzer --version
```

You should see output similar to:

```
black-seo-analyzer 25.1.6
```

## Troubleshooting

### Common Issues

#### "Command not found" error

- Ensure the installation directory is in your PATH
- Try restarting your terminal or command prompt

#### Missing dependencies

If you encounter errors about missing dependencies:

- Windows: Install the [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Linux: Install required libraries:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install libssl-dev pkg-config
  
  # Fedora/RHEL/CentOS
  sudo dnf install openssl-devel pkgconfig
  ```
- macOS: Install required libraries:
  ```bash
  brew install openssl@3
  ```

#### Permission denied

If you get "permission denied" errors when running the tool:

- Windows: Run Command Prompt as Administrator
- macOS/Linux: Use sudo or ensure the binary has execute permissions:
  ```bash
  sudo chmod +x /path/to/black-seo-analyzer
  ```

### Getting Help

If you encounter issues not covered in this guide:

1. Check the [GitHub Issues](https://github.com/sethblack/black-seo-analyzer/issues) for similar problems and solutions
2. Open a new issue with details about your problem
3. Contact me at seth@blackseoanalyzer.com
