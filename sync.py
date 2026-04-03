#!/usr/bin/env python3
"""同步上游 Custom_Clash.ini 并生成自定义配置"""
import os
from datetime import datetime

timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

# 读取上游规则
with open('rules_from_upstream.txt', 'r') as f:
    rules = f.read()

with open('groups_from_upstream.txt', 'r') as f:
    groups = f.read()

# 生成新的 INI
content = f'''; ============================================================
; Custom_Clash_Relay.ini - 链式代理出口版本
; 流量路径: 用户 → 链式代理节点 → 美国私宅(dialer-proxy) → 机场节点 → 目标网站
; 上游: https://github.com/Aethersailor/Custom_OpenClash_Rules
; 自动同步于: {timestamp}
;
; 使用说明:
; 1. 在 OpenClash 订阅配置中使用此 ini 作为订阅模板
; 2. 在本地配置中添加代理定义（使用 dialer-proxy）
; ============================================================

[custom]

; ========== 规则配置（与上游保持一致）==========
{rules}

; ========== 代理组配置 ==========

; 【核心】节点选择 - 包含链式代理选项
custom_proxy_group=🚀 节点选择`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连

; 链式代理组 - 选择出口节点
custom_proxy_group=🔗 链式代理`select`[]🏠 香港链式`[]🏠 美国链式`[]🏠 日本链式`[]🏠 新加坡链式`[]🏠 台湾链式`[]🏠 韩国链式

; 各地区链式代理组
custom_proxy_group=🏠 香港链式`select`[]🇭🇰 香港节点
custom_proxy_group=🏠 美国链式`select`[]🇺🇸 美国节点
custom_proxy_group=🏠 日本链式`select`[]🇯🇵 日本节点
custom_proxy_group=🏠 新加坡链式`select`[]🇸🇬 新加坡节点
custom_proxy_group=🏠 台湾链式`select`[]🇼🇸 台湾节点
custom_proxy_group=🏠 韩国链式`select`[]🇰🇷 韩国节点

; 自动选择
custom_proxy_group=♻️ 自动选择`url-test`.*`https://cp.cloudflare.com/generate_204`300,,50

; 各功能分组
custom_proxy_group=💬 即时通讯`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连
custom_proxy_group=🌐 社交媒体`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连
custom_proxy_group=🚀 GitHub`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连
custom_proxy_group=🤖 ChatGPT`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🤖 AI服务`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎶 TikTok`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=📹 YouTube`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎥 Netflix`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎥 DisneyPlus`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎥 HBO`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎥 PrimeVideo`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎥 AppleTV+`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇸🇬 新加坡节点`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连`.*
custom_proxy_group=🎥 Emby`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连`.*
custom_proxy_group=🎻 Spotify`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连`.*
custom_proxy_group=📺 Bahamut`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连`.*
custom_proxy_group=🌎 国外媒体`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🛒 国外电商`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`[]🎯 全球直连`.*
custom_proxy_group=📢 谷歌FCM`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点
custom_proxy_group=🇬 谷歌服务`select`[]🔗 链式代理`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🍎 苹果服务`select`[]🔗 链式代理`[]🎯 全球直连`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=Ⓜ️ 微软服务`select`[]🔗 链式代理`[]🎯 全球直连`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎮 游戏平台`select`[]🔗 链式代理`[]🎯 全球直连`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🎮 Steam`select`[]🔗 链式代理`[]🎯 全球直连`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🚀 测速工具`select`[]🔗 链式代理`[]🎯 全球直连`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🐟 漏网之鱼`select`[]🔗 链式代理`[]🎯 全球直连`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*
custom_proxy_group=🔀 非标端口`select`[]🐟 漏网之鱼`[]🎯 全球直连

{groups}

; 下方参数请勿修改
enable_rule_generator=true
overwrite_original_rules=true
'''

with open('cfg/Custom_Clash_Relay.ini', 'w') as f:
    f.write(content)

print("INI 文件已生成")
