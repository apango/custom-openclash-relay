#!/bin/bash
# ============================================================
# OpenClash 链式代理配置 - 初始化脚本
#
# 使用方法:
# 1. 修改下方 GITHUB_USER 和 REPO_NAME 为你的信息
# 2. 在 GitHub 创建空仓库（不初始化 README）
# 3. 运行此脚本
# ============================================================

# ========== 配置区（请修改）==========
GITHUB_USER="你的GitHub用户名"
REPO_NAME="custom-openclash-relay"
BRANCH="main"

# ============================================================

set -e

echo "=========================================="
echo "OpenClash 链式代理配置 - 初始化"
echo "=========================================="

# 检查 git 是否可用
if ! command -v git &> /dev/null; then
    echo "错误: 未找到 git，请先安装 Git"
    exit 1
fi

# 检查 gh 是否可用
if ! command -v gh &> /dev/null; then
    echo "提示: 未找到 gh CLI，将使用 HTTPS 方式推送"
    USE_HTTPS=true
else
    echo "检测到 gh CLI，将使用更安全的方式推送"
    USE_HTTPS=false
fi

# 切换到脚本目录
cd "$(dirname "$0")"

# 初始化 git
echo ""
echo "[1/5] 初始化 Git 仓库..."
git init -b $BRANCH 2>/dev/null || git init
git config user.email "actions@github.com"
git config user.name "GitHub Actions"

# 添加文件（排除敏感文件）
echo "[2/5] 添加文件..."
git add cfg/*.ini .github/workflows/*.yml README.md

# 提交
echo "[3/5] 提交更改..."
git commit -m "feat: initial custom openclash relay config

- 添加链式代理配置模板
- 添加 GitHub Actions 自动同步
- 敏感信息通过本地覆写配置注入"

# 添加远程仓库
echo "[4/5] 添加远程仓库..."
if [ "$USE_HTTPS" = true ]; then
    REMOTE_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo "远程仓库: $REMOTE_URL"
    git remote add origin $REMOTE_URL 2>/dev/null || git remote set-url origin $REMOTE_URL
else
    # 使用 gh 认证
    echo "请在弹出的浏览器窗口中授权 GitHub CLI"
    gh repo create "$GITHUB_USER/$REPO_NAME" --public --source=. --push --branch=$BRANCH
    echo ""
    echo "=========================================="
    echo "仓库已创建并推送!"
    echo "仓库地址: https://github.com/$GITHUB_USER/$REPO_NAME"
    echo "=========================================="
    exit 0
fi

# 推送
echo "[5/5] 推送到 GitHub..."
echo ""
echo "=========================================="
echo "请在 GitHub 创建空仓库后再执行推送"
echo "仓库地址: https://github.com/new"
echo "不要勾选任何初始化选项"
echo "=========================================="
echo ""
read -p "按回车键继续推送..."

git branch -M $BRANCH
git push -u origin $BRANCH

echo ""
echo "=========================================="
echo "推送完成!"
echo "仓库地址: https://github.com/$GITHUB_USER/$REPO_NAME"
echo "=========================================="
echo ""
echo "下一步:"
echo "1. 访问上述仓库地址"
echo "2. 点击 Settings > Pages > Source > main branch 保存"
echo "3. 复制 Raw URL 用于 OpenClash 配置"
echo "   https://raw.githubusercontent.com/$GITHUB_USER/$REPO_NAME/main/cfg/Custom_Clash_Relay.ini"
echo ""
