# Custom OpenClash 链式代理配置

基于 [Aethersailor/Custom_OpenClash_Rules](https://github.com/Aethersailor/Custom_OpenClash_Rules) 的 OpenClash 自定义配置模板，支持**链式代理出口**功能。

## 功能特点

- 所有海外流量通过**链式代理**转发
- 流量路径：设备 → 机场节点 → 私宅IP（最终出口）
- 自动同步上游规则更新
- 私宅代理凭证仅本地存储，不上传

## 目录结构

```
.
├── cfg/
│   └── Custom_Clash_Relay.ini    # 订阅模板（上传到 GitHub）
├── .github/
│   └── workflows/
│       └── sync.yml              # 自动同步上游
├── overlay-example.yaml          # 覆写配置示例（本地使用）
└── README.md
```

## 使用方法

### 1. 创建 GitHub 仓库

将此仓库内容上传到你的 GitHub 仓库。

### 2. 获取 Raw URL

仓库上传后，访问：
```
https://raw.githubusercontent.com/你的用户名/你的仓库名/main/cfg/Custom_Clash_Relay.ini
```

### 3. 配置 OpenClash

在 OpenClash「订阅管理」中添加：

| 配置项 | 值 |
|--------|-----|
| 订阅模板 URL | 上一步的 Raw URL |
| 覆写配置 | 见下方「覆写配置」 |

### 4. 覆写配置（本地）

在 OpenClash 的「覆写配置」中填入你的私宅代理信息：

```yaml
proxies:
  - name: 🏠 私宅代理
    type: ss
    server: 你的私宅IP
    port: 你的端口
    cipher: aes-256-gcm
    password: 你的密码
    udp: true

proxy-groups:
  - name: 🏠 私宅代理
    type: select
    proxies:
      - 🏠 私宅代理
```

## 自动同步

此仓库配置了 GitHub Actions，每天自动检查上游更新并同步。

## 流量走向

```
你的设备
    │
    ▼
┌─────────────┐     ┌─────────────┐
│  机场节点     │ ──▶ │  私宅IP      │
│ (入口/跳板)   │     │ (最终出口IP) │
└─────────────┘     └─────────────┘
```

## 安全说明

- 私宅代理凭证**仅保存在本地** OpenClash 配置中
- GitHub 仓库中**不包含任何敏感信息**
- 覆写配置不对外曝光
