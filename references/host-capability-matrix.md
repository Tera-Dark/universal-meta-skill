# 宿主能力矩阵 (Host Capability Matrix)

本表格用于客观记录主流宿主（Agent 平台/模型环境）对 Agent Skill 的实际支持情况。
**原则：杜绝臆测；只有经过可复现的实际测试或可靠官方文档确认时，才标注为 `VERIFIED`。**

### 状态枚举值：

- `VERIFIED`: 已通过当前环境可复现测试或官方明确文档验证。
- `PARTIAL`: 仅部分支持或存在明确约束。
- `UNKNOWN`: 尚未进行端到端实测验证。
- `NOT_SUPPORTED`: 经测试或官方声明不支持。

## 实测与待测记录

| 宿主平台 (Host) | 能力项 (Capability) | 状态 (Status) | 证据来源 / 验证日期 | 备注说明 |
|---|---|:---:|---|---|
| **Google Antigravity** | 根目录 `SKILL.md` 识别与加载 | **VERIFIED** | 实测 (2026-09-17) | 自动通过 frontmatter 发现 name 与 description，作为技能载入 |
| **Google Antigravity** | YAML Frontmatter 解析 | **VERIFIED** | 实测 (2026-09-17) | 支持标准 name 与 description，并在运行时作为触发索引 |
| **Google Antigravity** | 子目录与 `references/` 读取 | **VERIFIED** | 实测 (2026-09-17) | 可通过 `view_file` 或工具动态读取子目录参考文档 |
| **Google Antigravity** | `scripts/` 脚本执行 | **VERIFIED** | 实测 (2026-09-17) | 可直接通过终端工具执行 Python / Node / Shell 脚本 |
| **Google Antigravity** | 渐进式披露 (Progressive Disclosure) | **VERIFIED** | 实测 (2026-09-17) | 支持在主规程引导下按需调阅深层资料，节省上下文窗口 |
| **Claude Code** | 根目录 `SKILL.md` 识别 | **VERIFIED** | 官方文档与社区规范 | 依据标准 Skill 规范发现技能 |
| **Claude Code** | 外部参考文件按需读取 | **PARTIAL** | 社区实测 | 默认加载根文件，关联文件通常需显式指示或按需读取 |
| **Claude Code** | 脚本执行与工具链 | **VERIFIED** | 官方文档 | 支持 Bash 命令执行自动化验证脚本 |
| **OpenCode / OpenClaw** | Skill 发现与触发 | **UNKNOWN** | 待实测 | 待在对应 CLI 环境下跑冒烟用例 |
| **OpenAI Codex CLI** | 独立 Skill 目录解析 | **UNKNOWN** | 待实测 | 待验证多层级文件读取与自动路由表现 |

## 维护准则

1. 严禁仅因同名或相似产品就推定具备某项能力。
2. 必须记录具体的测试版本号、执行方式或官方文档日期。
3. 严格区分“静态元数据解析支持”与“运行时实际行为支持”。
4. 若不同套餐、模式或权限配置下的行为存在差异，必须在备注中注明测试环境。
5. 宿主发生大版本升级后，应重新跑验证用例并更新本表格。
