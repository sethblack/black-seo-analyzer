# Black SEO Analyzer (黑帽SEO分析器)

一款专业的命令行工具，用于全面的SEO分析，专为需要在搜索结果和AI答案中被找到的网站而设计。

在没有许可证的情况下运行时，您可以抓取的页面数量有限，但其他功能不受限制。要购买许可证并解锁无限的分析能力，请访问[Black SEO Analyzer产品页面](https://www.sethserver.com/seo/black-seo-analyzer.html)。

![Black SEO Analyzer](https://www.sethserver.com/static/images/black-seo-analyzer.png)

## 概述

Black SEO Analyzer是一款功能强大的命令行工具，可让您的网站在传统搜索结果和AI生成的响应中保持可见。良好的技术性SEO不仅仅关乎Google排名，还关乎确保AI系统在人们询问您时能够找到并理解您的内容。

当您的网站结构和元数据得到正确优化后，您将同时出现在搜索结果和AI对话中。Black SEO Analyzer能够消除噪音，准确告诉您是什么阻碍了您的网站发展——没有企业流行语，只有可操作的数据，这样当有人向AI询问您所销售的产品时，您就不会被抛在后面。

## 真正所有权，而非订阅

与那些在您停止付费后就停止工作的基于订阅的工具不同，Black SEO Analyzer提供真正的软件所有权。您的购买包括一项具有法律约束力的源代码访问保证，如果我们停止该产品，将永久保护您的投资。

**Black SEO Analyzer许可证：一次性购买**
- 终身软件所有权
- 所有未来更新
- 命令行效率
- 源代码托管保证
- 无限的URL和站点
- 包括所有高级功能

## 安装

请阅读[INSTALL.md](INSTALL.md)文件以获取安装说明。

## Windows用法

```
一款全面的SEO分析工具

用法：black-seo-analyzer.exe [选项]

选项：
      --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>
          要分析的站点地图的URL
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
          可选标志，指示站点是否为单页应用程序（SPA）
      --is-sitemap
          可选标志，指示初始页面是否为sitemap.xml
      --disable-external-links
          可选标志，禁用外部链接检查
      --locale <LOCALE>
          可选的国际化区域设置 [默认: en]
      --use-anthropic-analyzer
          可选标志，启用Anthropic Claude API进行SEO分析
      --anthropic-api-key <ANTHROPIC_API_KEY>
          可选的Anthropic API密钥（也可以通过ANTHROPIC_API_KEY环境变量设置）
      --anthropic-model <ANTHROPIC_MODEL>
          可选的用于分析的Anthropic模型 [默认: claude-3-haiku-20240307]
      --anthropic-prompt-file <ANTHROPIC_PROMPT_FILE>
          可选的包含自定义Anthropic提示的文件的路径
      --use-deepseek-analyzer
          可选标志，启用DeepSeek API进行SEO分析
      --deepseek-api-key <DEEPSEEK_API_KEY>
          可选的DeepSeek API密钥（也可以通过DEEPSEEK_API_KEY环境变量设置）
      --deepseek-model <DEEPSEEK_MODEL>
          可选的用于分析的DeepSeek模型 [默认: deepseek-chat]
      --deepseek-prompt-file <DEEPSEEK_PROMPT_FILE>
          可选的包含自定义DeepSeek提示的文件的路径
      --use-openai-analyzer
          可选标志，启用OpenAI API进行SEO分析
      --openai-api-key <OPENAI_API_KEY>
          可选的OpenAI API密钥（也可以通过OPENAI_API_KEY环境变量设置）
      --openai-model <OPENAI_MODEL>
          可选的用于分析的OpenAI模型 [默认: gpt-4o]
      --openai-prompt-file <OPENAI_PROMPT_FILE>
          可选的包含自定义OpenAI提示的文件的路径
      --use-gemini-analyzer
          可选标志，启用Google Gemini API进行SEO分析
      --gemini-api-key <GEMINI_API_KEY>
          可选的Google Gemini API密钥（也可以通过GEMINI_API_KEY环境变量设置）
      --gemini-model <GEMINI_MODEL>
          可选的用于分析的Google Gemini模型 [默认: gemini-1.5-flash-latest]
      --gemini-prompt-file <GEMINI_PROMPT_FILE>
          可选的包含自定义Google Gemini提示的文件的路径
      --user-agent <USER_AGENT>
          可选的HTTP请求的用户代理字符串 [默认: "black-seo-analyzer v25.6.61905"]
      --max-pages <MAX_PAGES>
          可选的最大抓取页面数
      --html-templates-dir <HTML_TEMPLATES_DIR>
          可选的自定义HTML模板目录路径
      --headless
          在无头模式下运行，不启动GUI [实验性] 默认为true
  -h, --help
          打印帮助
  -V, --version
          打印版本
```

### Windows示例用法

#### 单个站点的基本JSON输出
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type json --output-file example-report.json
```

#### 带有站点地图的网站
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap --output-type json --output-file sitemap-report.json
```

#### 单页应用
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://spa-example.com --spa --output-type json --output-file spa-report.json
```

#### HTML文件夹输出
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type html-folder --output-file ./seo-reports
```

## Linux/MacOS用法

```
一款全面的SEO分析工具

用法：black-seo-analyzer [选项]

选项：
      --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>
          要分析的站点地图的URL
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
          可选标志，指示站点是否为单页应用程序（SPA）
      --is-sitemap
          可选标志，指示初始页面是否为sitemap.xml
      --disable-external-links
          可选标志，禁用外部链接检查
      --locale <LOCALE>
          可选的国际化区域设置 [默认: en]
      --use-anthropic-analyzer
          可选标志，启用Anthropic Claude API进行SEO分析
      --anthropic-api-key <ANTHROPIC_API_KEY>
          可选的Anthropic API密钥（也可以通过ANTHROPIC_API_KEY环境变量设置）
      --anthropic-model <ANTHROPIC_MODEL>
          可选的用于分析的Anthropic模型 [默认: claude-3-haiku-20240307]
      --anthropic-prompt-file <ANTHROPIC_PROMPT_FILE>
          可选的包含自定义Anthropic提示的文件的路径
      --use-deepseek-analyzer
          可选标志，启用DeepSeek API进行SEO分析
      --deepseek-api-key <DEEPSEEK_API_KEY>
          可选的DeepSeek API密钥（也可以通过DEEPSEEK_API_KEY环境变量设置）
      --deepseek-model <DEEPSEEK_MODEL>
          可选的用于分析的DeepSeek模型 [默认: deepseek-chat]
      --deepseek-prompt-file <DEEPSEEK_PROMPT_FILE>
          可选的包含自定义DeepSeek提示的文件的路径
      --use-openai-analyzer
          可选标志，启用OpenAI API进行SEO分析
      --openai-api-key <OPENAI_API_KEY>
          可选的OpenAI API密钥（也可以通过OPENAI_API_KEY环境变量设置）
      --openai-model <OPENAI_MODEL>
          可选的用于分析的OpenAI模型 [默认: gpt-4o]
      --openai-prompt-file <OPENAI_PROMPT_FILE>
          可选的包含自定义OpenAI提示的文件的路径
      --use-gemini-analyzer
          可选标志，启用Google Gemini API进行SEO分析
      --gemini-api-key <GEMINI_API_KEY>
          可选的Google Gemini API密钥（也可以通过GEMINI_API_KEY环境变量设置）
      --gemini-model <GEMINI_MODEL>
          可选的用于分析的Google Gemini模型 [默认: gemini-1.5-flash-latest]
      --gemini-prompt-file <GEMINI_PROMPT_FILE>
          可选的包含自定义Google Gemini提示的文件的路径
      --user-agent <USER_AGENT>
          可选的HTTP请求的用户代理字符串 [默认: "black-seo-analyzer v2025.1.100001"]
      --max-pages <MAX_PAGES>
          可选的最大抓取页面数
      --html-templates-dir <HTML_TEMPLATES_DIR>
          可选的自定义HTML模板目录路径
      --headless
          在无头模式下运行，不启动GUI [实验性] 默认为true
  -h, --help
          打印帮助
  -V, --version
          打印版本
```

### Linux/MacOS示例用法

注意：

* 如果二进制文件不可执行，您可能需要先运行`chmod +x ./black-seo-analyzer`。
* 以下示例假定二进制文件位于当前目录中。如果它在不同的目录中，您需要提供二进制文件的完整路径，或者如果它在您的PATH中，您可以直接运行`black-seo-analyzer`。

#### 单个站点的基本JSON输出
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com --output-type json --output-file example-report.json
```

#### 带有站点地图的网站
```bash
./black-seo-analyzer.exe --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap --output-type json --output-file sitemap-report.json
```

#### 单页应用
```bash
./black-seo-analyzer.exe --url-to-begin-crawl https://spa-example.com --spa --output-type json --output-file spa-report.json
```

#### HTML文件夹输出
```bash
./black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type html-folder --output-file ./seo-reports
```

## 实际应用

### 自动化SEO监控

```bash
# 每周站点审计，并通过电子邮件通知关键问题
0 0 * * 1 /usr/local/bin/black-seo-analyzer.exe --url-to-begin-crawl example.com --output-type json \
| /usr/local/bin/seo-alert-filter \
| mail -s "每周SEO报告" team@example.com
```

### CI/CD管道集成

```yaml
# 在您的GitHub Actions工作流程中
seo_validation:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: 运行SEO分析
      run: |
        black-seo-analyzer.exe --url-to-begin-crawl https://staging.example.com \
        --output-type json --output-file seo-report.json
    - name: 验证关键SEO元素
      run: |
        cat seo-report.json | jq '.pages[] | select(.errors | length > 0)' > critical-errors.json
        if [ -s critical-errors.json ]; then
          echo "SEO验证失败 - 请参阅critical-errors.json"
          exit 1
        fi
```

### 批量站点分析

```bash
# 分析多个站点并合并报告
for site in site1.com site2.com site3.com; do
  black-seo-analyzer.exe --url-to-begin-crawl $site --output-type json --output-file "${site}.json"
done

# 合并结果以进行比较
jq -s '[.[] | {site: .site, score: .score, errorCount: .errorCount}]' *.json > summary.json
```

### 内容优化工作流程

```bash
# 提取所有H1标签和元描述以供内容审查
black-seo-analyzer.exe --url-to-begin-crawl example.com --output-type csv-flat \
| grep -E "(h1|meta_description)" \
| sort -t',' -k2 \
> content-review.csv
```

## 全面功能列表

### 核心功能
- 命令行界面
- 从指定URL开始抓取网站
- 使用站点地图抓取网站
- 支持静态网站（HTTP请求）和单页应用程序（SPA）（通过无头浏览器）
- 可配置的并发请求限制
- 可配置的最大页面限制
- 详细的日志系统
- 可配置的日志文件位置

### 抓取能力
- 基于HTTP请求的抓取器
- 基于无头浏览器的抓取器
- 自动检测和提取链接、脚本、样式表、图像
- 站点地图解析和处理
- 用于抓取和分析的异步处理
- 内容哈希生成（SHA1）用于重复内容检测
- 可配置的抓取延迟
- 遵守robots.txt
- 用户代理自定义
- 域名提取实用程序

### SEO分析模块
- **内容分析**
    - 字数统计
    - 关键词密度分析
    - 可读性分析（Flesch-Kincaid分数，音节计数）
    - 重复内容检测
    - 标题结构分析（H1, H2等）
    - 从附加标签（`<strong>`, `<em>`等）中提取内容
- **元数据分析**
    - 标题标签提取和验证
    - 元描述提取和验证
    - 元关键词提取
    - 视口元标签验证
    - 机器人元标签验证
    - 规范URL验证
    - OpenGraph数据提取和分析（og:title, og:description, og:image等）
    - Twitter Card数据提取和分析（twitter:card, twitter:title等）
- **URL结构分析**
    - 协议验证（首选HTTPS）
    - 路径分析（长度、字符使用、关键词存在）
    - 查询参数分析（识别、潜在问题）
    - 片段标识符分析
    - URL长度验证
    - 检测常见URL模式（例如，文件扩展名）
- **链接分析**
    - 识别内部和外部链接
    - 锚文本分析（长度、描述性）
    - 链接状态的异步检查（断开的链接）
    - 重定向的异步检查
    - 链接的大文件大小的异步检查
    - 链接属性分析（nofollow, target）
    - URL的规范化和分类（内部/外部）
- **图像分析**
    - Alt标签存在和内容分析
    - 图像尺寸分析
    - 文件大小考虑
- **移动友好性评估**
    - 视口元标签分析
    - 触摸目标大小和间距分析
    - 响应式图像分析（`srcset`, `sizes`属性）
    - 字体大小分析（移动设备上的可读性）
    - 媒体查询分析（断点覆盖）
- **性能分析**
    - 资源加载分析（脚本、样式表、图像、字体）
    - 脚本加载分析（`async`, `defer`）
    - 样式表加载分析
    - 图像加载分析（`loading="lazy"`）
    - 字体加载分析（`font-display`）
    - 关键渲染路径分析
    - 资源提示分析（`preload`, `prefetch`, `preconnect`）
    - 缓存头分析（Cache-Control, Expires）
    - 缓存清除技术检测
    - 压缩分析（Content-Encoding）
    - 关键资源识别
    - 首屏内容检测启发法
    - TTFB和总加载时间记录
    - 从浏览器/头中提取性能指标
- **安全分析**
    - HTTPS使用检查
    - 混合内容检测
    - 内容安全策略（CSP）头分析
    - 表单安全分析（敏感字段上的自动完成）
    - 外部资源完整性分析（SRI检查）
    - SSL证书到期检查
- **结构化数据/Schema标记验证**
    - JSON-LD提取和验证
    - 微数据提取和验证
    - RDFa提取和验证
    - 根据已知类型验证schema属性
    - 检测已弃用的schema属性
- **Web Vitals指标分析**
    - 与最大内容绘制（LCP）相关的分析
    - 与首次输入延迟（FID）/下一次绘制交互（INP）前体相关的分析
    - 与累积布局偏移（CLS）相关的分析
    - 与首次内容绘制（FCP）相关的分析
    - 与可交互时间（TTI）相关的分析
    - 与总阻塞时间（TBT）相关的分析
    - 识别阻塞资源、长任务、主线程工作
    - 分析图像尺寸、动态内容、字体加载影响
    - 计算总体优化分数
    - 根据指标生成具体建议
- **CSS分析**
    - 识别外部和内联样式
    - 分析样式表内容（潜在问题、复杂性）
    - 媒体查询分析（与响应性相关）
    - 基本的CSS相关可访问性检查
    - 基本的CSS相关性能检查
    - 检测潜在的重复CSS规则
- **JavaScript分析**
    - 识别外部和内联脚本
    - 分析脚本属性（`async`, `defer`）
    - 分析脚本加载模式
    - 基本安全检查
    - 分析内联脚本内容复杂性
    - 分析事件处理程序
    - 识别第三方脚本
    - 基本检查已弃用的JS API
- **国际化分析**
    - 语言声明分析（`lang`属性）
    - `hreflang`实现分析
    - 字符编码分析（首选UTF-8）
    - 文本方向分析（`dir`属性）
    - 对特定区域设置格式问题的基本检查
    - 对翻译完整性启发法的基本检查
    - 对时区处理启发法的基本检查
- **AI/LLM分析**
    - 与Anthropic API集成（需要API密钥）
    - 能够根据预定义提示将页面内容（或部分）发送到LLM进行分析
    - AI驱动的内容推荐
    - 自动元描述生成
    - 标题标签优化建议
    - 标题结构建议
    - 内容扩展建议
    - 执行摘要生成

### 输出格式
- JSON输出格式
- JSONL（JSON Lines）输出格式
- XML输出格式
- CSV输出格式
- HTML报告格式
- 每个页面的单独JSON文件
- 带有索引和单个页面报告的HTML文件夹输出

### 报告功能
- 由单个分析器生成的详细警告和建议
- 收集页面级元数据
- 收集页面内容详细信息（标题等）
- 收集页面资源（链接、脚本、样式、图像）
- 收集Web Vitals分析结果
- 性能指标报告（TTFB、加载时间）
- 基于模板的HTML报告生成

### 国际化
- UI文本和报告标签的多语言支持
- 内置翻译（英语、西班牙语、中文）
- 可扩展的翻译系统
- 用于特定建议的区域设置

### 许可系统
- 功能有限的试用模式
- 功能齐全的许可模式
- 许可证验证系统
- 影响功能的不同许可证层级

### 技术细节
- 使用Rust构建
- 异步架构
- HTML解析和DOM操作
- 无头Chrome集成
- HTTP客户端
- 序列化/反序列化
- 自定义URL序列化包装器
- 用于从URL创建安全文件名的实用程序
- 命令行参数解析
- 用于HTML报告生成的模板引擎

## 常见问题

**Black SEO Analyzer与其他SEO工具有何不同？**
与具有基于浏览器的界面和订阅模式的传统SEO工具不同，Black SEO Analyzer是一款命令行工具，可直接集成到您的开发工作流程中。这种方法实现了其他工具无法实现的自动化功能，而且您通过一次性购买真正拥有该软件。

**源代码保证如何运作？**
您的购买包括一项具有法律约束力的承诺，即如果我们停止产品、停止运营或连续12个月以上未能提供更新，您将有权访问完整的源代码。这确保您可以无限期地继续使用该软件，无论我们公司的未来如何。

**Black SEO Analyzer能否抓取大量使用JavaScript的网站？**
是的，我们集成的无头浏览器技术提供完整的JavaScript渲染功能。这确保了对使用React、Angular、Vue.js和其他JavaScript框架构建的现代Web应用程序的准确分析。

**更新如何处理？**
更新通过我们的GitHub存储库提供，可以随时下载。您将免费获得所有未来的更新。终身所有权。
