# ArkInfraSchemer

明日方舟基建规划助手（V1 开发中）。

## 文档
- 实现方案（中文）：`docs/IMPLEMENTATION_PLAN_ZH.md`

## 当前已实现（M1 起步）
- 手动输入干员 ID 的“干员列表解析”接口（模拟 OCR 输出）。
- 基于规则库的排班引擎（制造站/贸易站/发电站），支持 252/243 布局。
- Top-K 候选方案输出与简单可解释加成说明。

## 快速使用

```bash
python -m backend.app.cli --layout 252 --top-k 2 --ops texas lappland exusiai saria ptilopsis courier
```

## 运行测试

```bash
pytest backend/tests -q
```
