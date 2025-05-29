# ComfyUI Audio Amplitude Converter

ComfyUI用の高機能オーディオ振幅変換カスタムノードです。`Normalize Amplitude`ノードの出力（`NORMALIZED_AMPLITUDE`型）を`Audio Peaks Detection`ノードの入力（`FLOAT`型）に変換するためのブリッジノードとして機能します。

## 🚀 新機能（v1.1.0）

- **堅牢なエラーハンドリング**: 様々な入力形式に対応し、エラー時の適切な処理
- **型安全性の向上**: NumPy配列、PyTorchテンソル、リスト、単一値など多様な入力型をサポート
- **スケーリング機能**: 出力値にスケーリング係数を適用可能
- **値のクランプ機能**: 出力値を0-1の範囲に制限するオプション
- **詳細なログ出力**: デバッグとトラブルシューティングのための情報出力
- **包括的なテストスイート**: 動作確認用のテストスクリプトを同梱

## 📋 概要

ComfyUIのオーディオ処理ワークフローにおいて、異なるノード間での型の不一致を解決します：

- **入力**: `NORMALIZED_AMPLITUDE` 型（Normalize Amplitudeノードの出力）
- **出力**: `FLOAT` 型（Audio Peaks Detectionノードの入力）

## 🛠️ インストール

### 方法1: 手動インストール
1. 本リポジトリをクローンまたはダウンロード
```bash
git clone https://github.com/avocadori/ComfyUI-AudioAmplitudeConverter.git
```

2. ComfyUIの`custom_nodes`フォルダに配置
```
ComfyUI/
└── custom_nodes/
    └── ComfyUI-AudioAmplitudeConverter/
        ├── __init__.py
        ├── NormalizeAmpToFloatNode.py
        ├── test_node.py
        └── README.md
```

3. ComfyUIを再起動

### 方法2: ComfyUI Manager（推奨）
ComfyUI Managerを使用している場合は、カスタムノードリストから直接インストールできます。

## 🎯 使用方法

### 基本的な使用方法
1. **Normalize Amplitude**ノードの`normalized_amp`出力を本ノードの`normalized_amp`入力に接続
2. 本ノードの`audio_weights`出力を**Audio Peaks Detection**ノードの`audio_weights`入力に接続

### 高度な設定

#### スケーリング係数（scale_factor）
- **範囲**: 0.0 - 10.0
- **デフォルト**: 1.0
- **用途**: 出力値の増幅・減衰

```
例: scale_factor = 2.0 の場合
入力: [0.1, 0.5, 0.8] → 出力: [0.2, 1.0, 1.6]
```

#### 値のクランプ（clamp_values）
- **タイプ**: Boolean
- **デフォルト**: True
- **用途**: 出力値を0-1の範囲に制限

```
例: clamp_values = True の場合
入力: [-0.2, 0.5, 1.5] → 出力: [0.0, 0.5, 1.0]
```

## 🧪 テスト

ノードの動作確認には、同梱のテストスクリプトを使用できます：

```bash
cd ComfyUI-AudioAmplitudeConverter
python test_node.py
```

テストでは以下の項目を確認します：
- 基本的な型変換機能
- オプションパラメータの動作
- エッジケースの処理
- エラーハンドリング

## 📊 サポートする入力形式

| 入力型 | 説明 | 例 |
|--------|------|-----|
| NumPy配列 | `numpy.ndarray` | `np.array([0.1, 0.5, 0.8])` |
| PyTorchテンソル | `torch.Tensor` | `torch.tensor([0.1, 0.5, 0.8])` |
| リスト | `list` | `[0.1, 0.5, 0.8]` |
| タプル | `tuple` | `(0.1, 0.5, 0.8)` |
| 単一値 | `int`, `float` | `0.5` |
| 文字列（数値） | `str` | `"0.5"` |

## 🔧 トラブルシューティング

### よくある問題

**Q: ノードが表示されない**
- ComfyUIを完全に再起動してください
- `custom_nodes`フォルダの配置を確認してください
- コンソールでエラーメッセージを確認してください

**Q: 変換エラーが発生する**
- 入力データの形式を確認してください
- テストスクリプトで動作確認を行ってください
- ログ出力でエラーの詳細を確認してください

**Q: 出力値が期待と異なる**
- `scale_factor`の設定を確認してください
- `clamp_values`の設定を確認してください

## 📝 ログ出力

ノードは以下の情報をコンソールに出力します：

```
[NormalizeAmpToFloat] Successfully converted 100 values
[NormalizeAmpToFloat] Warning: Input is None
[NormalizeAmpToFloat] Error during conversion: ...
```

## 🔄 バージョン履歴

### v1.1.0 (2024-05-29)
- 堅牢なエラーハンドリングの追加
- 多様な入力型のサポート
- スケーリング機能の追加
- 値のクランプ機能の追加
- 包括的なテストスイートの追加
- 詳細なドキュメントの作成

### v1.0.0 (初期版)
- 基本的な型変換機能

## 📄 ライセンス

MIT License

## 👥 コントリビューション

プルリクエストやIssueは大歓迎です！

### 開発に参加する場合
1. リポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 🙏 謝辞

- ComfyUIコミュニティの皆様
- オーディオ処理ワークフローの改善にご協力いただいた皆様

## 📞 サポート

問題や質問がある場合は、GitHubのIssueページでお気軽にお尋ねください。

---

**ComfyUI Audio Amplitude Converter** - より良いオーディオワークフローのために 🎵
