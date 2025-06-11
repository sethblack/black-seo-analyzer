# 安装 Black SEO Analyzer

本文档提供在不同操作系统上安装 Black SEO Analyzer 工具的说明。

如果您更喜欢观看视频而不是阅读，请查看我的 YouTube 视频：

[Windows 安装](https://youtu.be/WKq0-EHhuUw)

## 目录

- [先决条件](#先决条件)
- [基本安装](#基本安装)
  - [Windows](#windows-basic)
  - [macOS](#macos-basic)
  - [Linux](#linux-basic)
- [高级安装](#高级安装)
  - [Windows](#windows-advanced)
- [验证安装](#验证安装)
- [故障排除](#故障排除)

## 先决条件

在安装 Black SEO Analyzer 之前，请确保您具备以下条件：

- 用于下载工具的互联网连接
- 对命令行界面的基本熟悉（用于基本安装）
- 管理员/sudo 权限（某些安装方法可能需要）

## 基本安装

### Windows (基本) {#windows-basic}

#### Windows MSI 安装程序

1. 从[发布页面](https://github.com/sethblack/black-seo-analyzer/releases)下载最新的 Windows MSI 安装程序 (`setup.msi`)。
2. 运行 `setup.msi` 安装程序。这会将应用程序安装到 `C:\Program Files (x86)\Black SEO Analyzer\` 并将其添加到系统的 PATH 中。
3. 打开一个新的命令提示符并验证安装：

```cmd
black-seo-analyzer --version
```

4. 在您的用户主目录（例如 `C:\Users\YourUser\license.txt`）中创建一个 `license.txt` 文件，其中包含您的许可证密钥。

#### Windows 便携版 (exe)

1. 从[发布页面](https://github.com/sethblack/black-seo-analyzer/releases)下载最新的 Windows 可执行文件 (`black-seo-analyzer.exe`)。

2. 将下载的 `black-seo-analyzer.exe` 移动到您选择的位置（例如 `C:\Users\YourUser\Documents\black-seo-analyzer`）。

3. 打开命令提示符并导航到您移动可执行文件的目录：

```cmd
cd C:\Users\YourUser\Documents\black-seo-analyzer
```

4. 验证安装：

```cmd
black-seo-analyzer --version
```

5. 在同一目录中创建一个 `license.txt` 文件，其中包含您的许可证密钥：

```cmd
echo "YOUR_LICENSE_KEY" > license.txt
```

#### 快速入门示例

分析一个网站并生成 HTML 报告：

```cmd
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

### macOS (基本) {#macos-basic}

1. 从[发布页面](https://github.com/sethblack/black-seo-analyzer/releases)下载最新的 macOS 二进制文件。

2. 使二进制文件可执行：

```bash
chmod +x <binary_name>
```

3. 将二进制文件移动到您的 PATH 中的一个位置：

```bash
sudo mv <binary_name> /usr/local/bin/black-seo-analyzer
```

4. 验证安装：

```bash
black-seo-analyzer --version
```

6. 在同一目录中创建一个 `license.txt` 文件，其中包含您的许可证密钥：

```bash
echo "YOUR_LICENSE_KEY" > license.txt
```

#### 快速入门示例

分析一个网站并生成 HTML 报告：

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

### Linux (基本) {#linux-basic}

1. 从[发布页面](https://github.com/sethblack/black-seo-analyzer/releases)为您的体系结构下载最新的 Linux 二进制文件。

   - **x86_64**: 用于标准的 64 位 Intel/AMD 处理器。
   - **arm**: 用于基于 ARM 的处理器，如 Raspberry Pi 和一些云服务器中的处理器。
   - **musl**: 用于使用 musl C 标准库的容器化环境（例如 Docker）的版本。

2. 使二进制文件可执行：

```bash
chmod +x <binary_name>
```

3. 将二进制文件移动到您的 PATH 中的一个位置：

```bash
sudo mv <binary_name> /usr/local/bin/black-seo-analyzer
```

4. 验证安装：

```bash
black-seo-analyzer --version
```

#### 快速入门示例

分析一个网站并生成 HTML 报告：

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

## 高级安装

### Windows (高级) {#windows-advanced}


#### 手动安装

1. 从[发布页面](https://github.com/sethblack/black-seo-analyzer/releases)下载最新的 Windows 可执行文件 (`black-seo-analyzer.exe`)。

2. 将下载的 `black-seo-analyzer.exe` 移动到系统 PATH 中包含的目录，或将包含可执行文件的目录添加到您的 PATH 中。

3. 要将二进制文件位置添加到您的 PATH：
   - 右键单击“此电脑”或“我的电脑”，然后选择“属性”
   - 单击“高级系统设置”
   - 单击“环境变量”
   - 在“系统变量”下，找到并选择“Path”，然后单击“编辑”
   - 单击“新建”并添加包含二进制文件的目录的路径（例如 `C:\Program Files\black-seo-analyzer`）
   - 在所有对话框上单击“确定”以保存更改

4. 打开一个新的命令提示符并验证安装：

```cmd
black-seo-analyzer --version
```


## 验证安装

安装后，验证 Black SEO Analyzer 是否正常工作：

```bash
black-seo-analyzer --version
```

您应该会看到类似以下的输出：

```
black-seo-analyzer 2025.1.6
```

## 故障排除

### 常见问题

#### “找不到命令”错误

- 确保安装目录在您的 PATH 中
- 尝试重新启动您的终端或命令提示符

#### 缺少依赖项

如果您遇到有关缺少依赖项的错误：

- Windows: 安装 [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Linux: 安装所需的库：
  ```bash
  # Ubuntu/Debian
  sudo apt-get install libssl-dev pkg-config
  
  # Fedora/RHEL/CentOS
  sudo dnf install openssl-devel pkgconfig
  ```
- macOS: 安装所需的库：
  ```bash
  brew install openssl@3
  ```

#### 权限被拒绝

如果您在运行工具时遇到“权限被拒绝”的错误：

- Windows: 以管理员身份运行命令提示符
- macOS/Linux: 使用 sudo 或确保二进制文件具有执行权限：
  ```bash
  sudo chmod +x /path/to/black-seo-analyzer
  ```

### 获取帮助

如果您遇到本指南未涵盖的问题：

1. 查看 [GitHub Issues](https://github.com/sethblack/black-seo-analyzer/issues) 以查找类似的问题和解决方案
2. 打开一个新问题，详细说明您的问题
3. 通过 support@example.com 联系支持

## 命令行选项

Black SEO Analyzer 支持各种命令行选项：

```
用法: black-seo-analyzer.exe [选项] --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>

选项:
      --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>
          要分析的站点地图的 URL
      --log-file <LOG_FILE>
          日志文件的路径
      --output-type <OUTPUT_TYPE>
          输出格式类型 [默认: html-folder] [可选值: json, jsonl, xml, csv, csv-flat, html-folder, json-files]
      --concurrent-requests <CONCURRENT_REQUESTS>
          可选的并发请求数 [默认: 20]
      --rate-limit <RATE_LIMIT>
          可选的速率限制（毫秒） [默认: 50]
      --output-file <OUTPUT_FILE>
          可选参数，用于指定输出文件
      --spa
          可选标志，指示站点是否为单页应用程序 (SPA)
      --is-sitemap
          可选标志，指示初始页面是否为 sitemap.xml
      --disable-external-links
          可选标志，禁用外部链接检查
      --locale <LOCALE>
          可选的国际化区域设置 [默认: en]
      --use-anthropic-analyzer
          可选标志，启用 Anthropic Claude API 进行 SEO 分析
      --anthropic-api-key <ANTHROPIC_API_KEY>
          可选的 Anthropic API 密钥（也可以通过 ANTHROPIC_API_KEY 环境变量设置）
      --anthropic-model <ANTHROPIC_MODEL>
          可选的用于分析的 Anthropic 模型 [默认: claude-3-haiku-20240307]
      --anthropic-prompt-file <ANTHROPIC_PROMPT_FILE>
          可选的包含自定义 Anthropic 提示的文件的路径
      --use-deepseek-analyzer
          可选标志，启用 DeepSeek API 进行 SEO 分析
      --deepseek-api-key <DEEPSEEK_API_KEY>
          可选的 DeepSeek API 密钥（也可以通过 DEEPSEEK_API_KEY 环境变量设置）
      --deepseek-model <DEEPSEEK_MODEL>
          可选的用于分析的 DeepSeek 模型 [默认: deepseek-chat]
      --deepseek-prompt-file <DEEPSEEK_PROMPT_FILE>
          可选的包含自定义 DeepSeek 提示的文件的路径
      --use-openai-analyzer
          可选标志，启用 OpenAI API 进行 SEO 分析
      --openai-api-key <OPENAI_API_KEY>
          可选的 OpenAI API 密钥（也可以通过 OPENAI_API_KEY 环境变量设置）
      --openai-model <OPENAI_MODEL>
          可选的用于分析的 OpenAI 模型 [默认: gpt-4o]
      --openai-prompt-file <OPENAI_PROMPT_FILE>
          可选的包含自定义 OpenAI 提示的文件的路径
      --use-gemini-analyzer
          可选标志，启用 Google Gemini API 进行 SEO 分析
      --gemini-api-key <GEMINI_API_KEY>
          可选的 Google Gemini API 密钥（也可以通过 GEMINI_API_KEY 环境变量设置）
      --gemini-model <GEMINI_MODEL>
          可选的用于分析的 Google Gemini 模型 [默认: gemini-1.5-flash-latest]
      --gemini-prompt-file <GEMINI_PROMPT_FILE>
          可选的包含自定义 Google Gemini 提示的文件的路径
      --user-agent <USER_AGENT>
          可选的 HTTP 请求的用户代理字符串 [默认: "black-seo-analyzer v25.6.61905"]
      --max-pages <MAX_PAGES>
          可选的最大抓取页面数
      --html-templates-dir <HTML_TEMPLATES_DIR>
          可选的自定义 HTML 模板目录路径
      --headless
          在无头模式下运行，不启动 GUI [实验性] 默认为 true
  -h, --help
          打印帮助
  -V, --version
          打印版本
```

## 示例

### 基本网站分析

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com
```

### 分析单页应用程序 (SPA)

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --spa
```

### 分析站点地图

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap
```

### 生成不同的输出格式

```bash
# JSON 输出
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type json --output-file report.json

# CSV 输出
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type csv --output-file report.csv

# XML 输出
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type xml --output-file report.xml
```

### 调整抓取设置

```bash
# 增加并发请求以加快抓取速度
black-seo-analyzer --url-to-begin-crawl https://example.com --concurrent-requests 30

# 增加速率限制以减慢抓取速度（对服务器更友好）
black-seo-analyzer --url-to-begin-crawl https://example.com --rate-limit 100
```

### 使用不同的语言

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --locale es
```

### 使用自定义 HTML 模板

您可以提供自己的 HTML 模板来自定义输出外观：

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --templates-dir ./my-templates
```

模板目录应包含与默认模板同名的 HTML 模板文件：
- base.html
- index_file.html
- page_file.html
- page.html
- preamble.html
- postamble.html

在自定义目录中找不到的任何模板都将回退到默认模板。
