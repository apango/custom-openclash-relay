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
; 流量路径: 设备 → 机场节点 → 私宅IP(最终出口)
; 上游: https://github.com/Aethersailor/Custom_OpenClash_Rules
; 自动同步于: {timestamp}
;
; 使用说明:
; 1. 在 OpenClash 订阅配置中使用此 ini 作为订阅模板
; 2. 在覆写配置中填入本地私宅代理配置
; ============================================================

[custom]

; ========== 规则配置（与上游保持一致）==========
{rules}

; ========== 代理组配置（所有流量走链式代理）==========

; 【核心】链式代理 - 可选出口：各私宅出口、直连
; 在 OpenClash 中手动选择出口
custom_proxy_group=🔗 链式代理`select`[]🇺🇸 美国私宅1`[]🎯 全球直连

; 美国私宅1代理（通过本地覆写注入）
custom_proxy_group=🇺🇸 美国私宅1`relay`[]🏠 美国私宅1`[]✈️ 机场节点

; 机场节点选择（第一跳）
custom_proxy_group=✈️ 机场节点`select`[]♻️ 自动选择`[]🇭🇰 香港节点`[]🇺🇸 美国节点`[]🇯🇵 日本节点`[]🇸🇬 新加坡节点`[]🇼🇸 台湾节点`[]🇰🇷 韩国节点`.*

; 美国私宅1实际代理（通过本地覆写注入）
custom_proxy_group=🏠 美国私宅1`select`[]✈️ 机场节点

; 各功能分组
custom_proxy_group=🚀 节点选择`select`[]🔗 链式代理`[]🎯 全球直连
custom_proxy_group=♻️ 自动选择`url-test`.*`https://cp.cloudflare.com/generate_204`300,,50
custom_proxy_group=💬 即时通讯`select`[]🔗 链式代理`[]🎯 全球直连
custom_proxy_group=🌐 社交媒体`select`[]🔗 链式代理`[]🎯 全球直连
custom_proxy_group=🚀 GitHub`select`[]🔗 链式代理`[]🎯 全球直连
custom_proxy_group=🤖 ChatGPT`select`[]🔗 链式代理`.*
custom_proxy_group=🤖 AI服务`select`[]🔗 链式代理`.*
custom_proxy_group=🎶 TikTok`select`[]🔗 链式代理`.*
custom_proxy_group=📹 YouTube`select`[]🔗 链式代理`.*
custom_proxy_group=🎥 Netflix`select`[]🔗 链式代理`.*
custom_proxy_group=🎥 DisneyPlus`select`[]🔗 链式代理`.*
custom_proxy_group=🎥 HBO`select`[]🔗 链式代理`.*
custom_proxy_group=🎥 PrimeVideo`select`[]🔗 链式代理`.*
custom_proxy_group=🎥 AppleTV+`select`[]🔗 链式代理`[]🎯 全球直连`.*
custom_proxy_group=🎥 Emby`select`[]🔗 链式代理`[]🎯 全球直连`.*
custom_proxy_group=🎻 Spotify`select`[]🔗 链式代理`[]🎯 全球直连`.*
custom_proxy_group=📺 Bahamut`select`[]🔗 链式代理`[]🎯 全球直连`.*
custom_proxy_group=🌎 国外媒体`select`[]🔗 链式代理`.*
custom_proxy_group=🛒 国外电商`select`[]🔗 链式代理`[]🎯 全球直连`.*
custom_proxy_group=📢 谷歌FCM`select`[]🔗 链式代理
custom_proxy_group=🇬 谷歌服务`select`[]🔗 链式代理`.*
custom_proxy_group=🍎 苹果服务`select`[]🎯 全球直连`[]🔗 链式代理`.*
custom_proxy_group=Ⓜ️ 微软服务`select`[]🎯 全球直连`[]🔗 链式代理`.*
custom_proxy_group=🎮 游戏平台`select`[]🎯 全球直连`[]🔗 链式代理`.*
custom_proxy_group=🎮 Steam`select`[]🎯 全球直连`[]🔗 链式代理`.*
custom_proxy_group=🚀 测速工具`select`[]🎯 全球直连`[]🔗 链式代理`.*
custom_proxy_group=🐟 漏网之鱼`select`[]🔗 链式代理`[]🎯 全球直连`.*
custom_proxy_group=🔀 非标端口`select`[]🐟 漏网之鱼`[]🎯 全球直连

{groups}

; 下方参数请勿修改
enable_rule_generator=true
overwrite_original_rules=true
'''

with open('cfg/Custom_Clash_Relay.ini', 'w') as f:
    f.write(content)

print("INI 文件已生成")
