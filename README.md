# Custom OpenClash 链式代理配置

基于 [Aethersailor/Custom_OpenClash_Rules](https://github.com/Aethersailor/Custom_OpenClash_Rules) 的 OpenClash 自定义配置模板，支持**链式代理出口**功能。

## 功能特点

- 所有海外流量可优先选择**链式出口**转发
- 流量路径：OpenWrt 设备 → 机场节点（链式上游）→ 私宅 IP（链式出口）→ 目标网站
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
├── relay.yaml                    # 本地真实覆写配置（不上传）
├── overlay-example.yaml          # 覆写配置示例（不上传）
└── README.md
```

## 使用方法

### 1. 在线订阅模板

OpenClash 的订阅模板 URL 使用：
```
https://raw.githubusercontent.com/apango/custom-openclash-relay/main/cfg/Custom_Clash_Relay.ini
```

### 2. 配置 OpenClash

在 OpenClash「订阅管理」中添加：

| 配置项 | 值 |
|--------|-----|
| 订阅模板 URL | 上面的 Raw URL |
| 覆写配置 | 使用本地 `relay.yaml` 内容 |

### 3. 覆写配置（本地）

在线模板只提供代理组和规则，不包含私宅代理凭证。将本地 `relay.yaml` 的内容粘贴到 OpenClash「覆写配置」中，结构如下：

```yaml
proxies:
  - name: 链式美国私宅
    type: socks5
    server: YOUR_SERVER_IP
    port: YOUR_PORT
    username: YOUR_USERNAME
    password: YOUR_PASSWORD
    udp: true
    dialer-proxy: 🔗 链式上游

proxy-groups:
  - name: 🔗 链式出口
    type: select
    proxies:
      - 链式美国私宅

```

`🔗 链式上游` 由在线模板生成，可以使用 `♻️ 自动选择` 自动挑选机场前置节点。`♻️ 自动选择` 只排除名称包含“链式”的节点；家宽、住宅、私宅字样的机场节点仍会参与自动测速。

`🚀 手动选择` 是总入口，可选 `🔗 链式出口`、`♻️ 自动选择`、各地区自动优选组，也可以直接手动选择订阅里的具体机场节点。各地区组如 `🇭🇰 香港节点`、`🇺🇸 美国节点` 会在对应地区节点范围内自动测速优选。

## 自动同步

此仓库配置了 GitHub Actions，每天自动检查上游更新并同步。

## 流量走向

```
OpenWrt 设备
    │
    ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  OpenClash  │ ──▶ │  机场节点     │ ──▶ │  私宅 IP     │ ──▶ 目标网站
│  规则分流     │     │ (链式上游)   │     │ (链式出口)   │
└─────────────┘     └─────────────┘     └─────────────┘
```

## 安全说明

- 私宅代理凭证**仅保存在本地** OpenClash 配置中
- GitHub 仓库中**不包含任何敏感信息**
- 覆写配置不对外曝光
- 不要提交 `relay.yaml`、`overlay-*.yaml` 或任何包含真实账号密码的文件
