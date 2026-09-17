# 通用 Agent 母技能 (Universal Meta-Skill)

[English](README_EN.md) | **简体中文**

面向 Agent 的宿主感知母技能（Meta-Skill），用于**创建、重构、审计、演进、修复、迁移和打包**高质量智能体技能（Agent Skills）。

拒绝华而不实的提示词模板堆砌，将 Skill 视为具备显式契约、边界清晰、可观测验证的工程化执行规程。

---

## 核心设计目标

- **去伪工程化**：不搞无意义的 XML 标签堆砌和虚荣打分，聚焦可落地的可执行逻辑。
- **显式契约与边界**：强制明确 Scope（负责范围）与 Non-scope（严禁越权范围）。
- **CAEE 规则四元组**：重要规则遵循 **条件 (Condition) - 动作 (Action) - 证据 (Evidence) - 异常 (Exception)**。
- **渐进式披露 (Progressive Disclosure)**：核心保持精简，非必要不膨胀上下文；长篇资料与模版下沉到 `references/`。
- **诚实验收**：绝不把脑补推导当作测试通过，未实际验证的状态诚实标注为 `UNKNOWN` 或 `NOT EXECUTED`。
- **双轨模式**：提供 6 步轻量极速通路（Fast Path）与全量深度工程路径，大小任务兼顾。

---

## 目录结构与双语架构

```text
universal-meta-skill/
├── .gitignore
├── CHANGELOG.md               # 变更日志
├── README.md                  # 【默认】中文说明文档
├── README_EN.md               # 英文说明文档
├── SKILL.md                   # 【默认主入口】中文版核心规范
├── SKILL_EN.md                # 英文版核心规范
├── scripts/                   # 自动化校验脚本 (零外部依赖)
│   └── validate_skill.py      # Skill 静态合规性与引用完整性校验
├── tests/                     # 测试夹具与用例
│   ├── fixtures/
│   │   ├── ambiguous-request.md
│   │   ├── missing-input.md
│   │   └── out-of-scope.md
│   └── README.md
└── references/                # 中文参考资料与模版
    ├── minimal-skill-template.md        # 极简技能模板 (50行黄金骨架)
    ├── evaluation-protocol.md           # 三级评估协议 (静态/冒烟/回归)
    ├── host-capability-matrix.md        # 宿主能力矩阵 (含实测记录)
    ├── metadata-profiles.md             # 元数据配置规范 (核心与扩展)
    └── en/                              # 英文原版参考资料镜像
        ├── minimal-skill-template.md
        ├── evaluation-protocol.md
        ├── host-capability-matrix.md
        └── metadata-profiles.md
```

---

## 快速使用

### 1. 本地作为 Agent 技能载入
将本仓库目录放入目标宿主所规定的 Skill 搜索路径（例如 Antigravity、Claude Code、OpenCode 等），并根据该宿主的官方文档确认发现、加载和执行行为。不同宿主可能需要额外配置或权限设置。

### 2. 自动化静态合规性校验
仓库内置了基于 Python 标准库的零依赖验证脚本，可随时检查 Skill 的 Frontmatter 格式与文件引用有效性：

```bash
python scripts/validate_skill.py
```

### 3. 远程直接读取 (Raw URL)
各大 Agent 或自动化工具可直接请求 Raw 链接获取最新指令：
- **母技能中文核心**：`https://raw.githubusercontent.com/Tera-Dark/universal-meta-skill/main/SKILL.md`
- **母技能英文核心**：`https://raw.githubusercontent.com/Tera-Dark/universal-meta-skill/main/SKILL_EN.md`
- **极简中文模板**：`https://raw.githubusercontent.com/Tera-Dark/universal-meta-skill/main/references/minimal-skill-template.md`
