# Custom OpenClash 链式代理配置

基于 [Aethersailor/Custom_OpenClash_Rules](https://github.com/Aethersailor/Custom_OpenClash_Rules) 的 OpenClash 自定义配置模板，支持**链式代理出口**功能。

## 功能特点

- 所有海外流量可优先选择**链式出口**转发
- 流量路径：OpenWrt 设备 → 🔗 链式出口（全链路代理组）→ 目标网站，网站看到私宅 IP
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
| 覆写配置 | 由路由器脚本 `openclash_custom_overwrite.sh` 自动注入 |

### 3. 覆写配置（本地，脚本自动注入）

在线模板只提供代理组和规则，不包含私宅代理凭证，`🔗 链式出口` 在模板里只是 `DIRECT` 占位组。真正的私宅出口与全链路代理组由路由器上的本地覆写脚本 `openclash_custom_overwrite.sh` 自动注入，无需手动粘贴 YAML。

私宅服务器参数写在脚本的 `RELAY_LIST` 里，脚本会为每个私宅生成一个「全链路代理组」（如 `🔗 链路·美国私宅`），组内含「该私宅 × 全部机场首跳」的副本，以 `url-test` 端到端测两跳通路自动选最优，也可手动指定首跳。`🔗 链式出口` 则被改写为 `select` 组，用于在各私宅的全链路代理组之间切换。

`🚀 手动选择` 是总入口，可选 `🔗 链式出口`、`♻️ 自动选择`、各地区自动优选组，也可以直接手动选择订阅里的具体机场节点。各地区组如 `🇭🇰 香港节点`、`🇺🇸 美国节点` 会在对应地区节点范围内自动测速优选。

## 自动同步

此仓库配置了 GitHub Actions，每天自动检查上游更新并同步。

## 流量走向

```
OpenWrt 设备
    │
    ▼
┌─────────────┐     ┌──────────────────┐
│  OpenClash  │ ──▶ │  🔗 链式出口        │ ──▶ 目标网站
│  规则分流     │     │ (全链路代理组:      │     (私宅 IP)
│             │     │  机场首跳 → 私宅)   │
└─────────────┘     └──────────────────┘
```

全链路代理组由 `openclash_custom_overwrite.sh` 注入，组内每个副本就是一条「机场首跳 → 私宅出口」的完整两跳通路，`url-test` 端到端选最优。

## 安全说明

- 私宅代理凭证**仅保存在本地** OpenClash 配置中
- GitHub 仓库中**不包含任何敏感信息**
- 覆写配置不对外曝光
- 不要提交 `relay.yaml`、`overlay-*.yaml` 或任何包含真实账号密码的文件
