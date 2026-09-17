# 评估协议 (Evaluation Protocol)

## 评估分级

### Level 1 — 静态审查 (Static Review)

检查项：
- 元数据 (Frontmatter) 语法是否合规；
- 触发描述 (Trigger) 是否明确；
- 负责范围 (Scope) 与排除范围 (Non-scope) 是否清晰；
- 输入/输出契约是否完备；
- 规则之间是否存在内部矛盾；
- 是否包含未受支持的越权功能声明。

### Level 2 — 行为冒烟测试 (Behavioral Smoke Test)

运行以下用例：
- 1 个正常典型用例 (Happy path)；
- 1 个歧义或模糊输入用例 (Ambiguous case)；
- 1 个必填项缺失用例 (Missing-input case)；
- 1 个越界或非负责范围用例 (Out-of-scope case)。

### Level 3 — 风险与回归测试 (Risk-Oriented Regression)

针对以下风险增加用例：
- 权限混淆与越权；
- 外部输入内容中混入的恶意或无关指令；
- 工具调用失败或网络故障；
- 畸形或对抗性输入；
- 曾经出现过缺陷的回归场景 (Regression cases)。

## 结果报告格式

```text
状态: PASS | FAIL | PARTIAL | UNKNOWN
证据:
- [实际观测到的结果]
局限与未知:
- [未经验证的条件]
回归影响:
- [无 / 具体影响描述]
```

分数仅可作为内部优化的辅助参考，**严禁以主观分数替代阻塞性的质量门禁**。
