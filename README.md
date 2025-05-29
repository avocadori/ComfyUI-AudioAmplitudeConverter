# ComfyUI-AudioAmplitudeConverter# ComfyUI-NormalizeAmpToFloat

ComfyUI用カスタムノードで、Normalize Amplitudeノードの出力（NORMALIZED_AMPLITUDE型）を  
Audio Peaks Detectionノードの入力（FLOAT型）に変換するための変換ノードです。

---

## 概要

ComfyUIのオーディオ処理ワークフローにおいて、  
`Normalize Amplitude` ノードの出力は `NORMALIZED_AMPLITUDE` 型であり、  
`Audio Peaks Detection` ノードの入力は `FLOAT` 型のため、  
直接接続できない問題を解決します。

---

## インストール

1. 本リポジトリをクローンまたはダウンロードします。  
2. `NormalizeAmpToFloatNode.py` を ComfyUIの `custom_nodes` フォルダに配置します。  
3. ComfyUIを再起動します。

---

## 使い方

- Normalize Amplitude ノードの出力 `normalized_amp` を本ノードの入力 `normalized_amp` に接続してください。  
- 本ノードの出力 `audio_weights` を Audio Peaks Detection ノードの入力 `audio_weights` に接続してください。

---

## ライセンス

MIT License

---

## 作者

[あなたの名前またはハンドルネーム]

---

## コントリビューション

プルリクエストやIssueは大歓迎です。
