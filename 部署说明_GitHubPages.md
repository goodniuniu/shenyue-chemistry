# 部署到 GitHub Pages 的说明

网站成品已生成在 `docs/` 目录（含 `.nojekyll`，无需额外配置）。按以下步骤发布：

## 第一步：在 GitHub 创建仓库

1. 打开 https://github.com/new ，新建一个仓库，建议命名为 `shenyue-chemistry`
2. 设为 Public（GitHub Pages 免费版要求公开仓库；如用 Private 需 GitHub Pro）

## 第二步：推送项目到 GitHub

在项目文件夹中执行（已装 Git 的情况下）：

```bash
cd "E:\MyOutput\AI_Project\申悦学习-AI指导化学学习"
git remote add origin https://github.com/<你的用户名>/shenyue-chemistry.git
git push -u origin main
```

> 项目已初始化 git 并完成提交，直接加远程推送即可。
> `node_modules/`（目录联接）与 `docs/` 之外的产物已被 `.gitignore` 排除，不会误传。
> 如沿用物理项目的网络方案：SSH 走 443 端口 + 本地代理 7897，首次大推送慢属正常。

## 第三步：开启 Pages

1. 仓库页面 → **Settings** → **Pages**
2. Source 选 **Deploy from a branch**，分支选 `main`，目录选 `/ (root)`
3. 保存后 1–3 分钟生效，访问 `https://<你的用户名>.github.io/shenyue-chemistry/`

> 注意：站点发布在子路径 `/shenyue-chemistry/` 下，当前页面内链接均为相对路径，子路径部署可直接生效（物理项目同结构已验证）。

## 更新网站

改 Markdown 源文件 → `python build_site.py` → `git add -A && git commit -m "更新XX" && git push`，Pages 自动更新。

不熟命令行可安装 GitHub Desktop 图形界面操作。
