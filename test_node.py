"""
NormalizeAmpToFloatNode のテストスクリプト

このスクリプトは、ノードの基本的な動作をテストするためのものです。
ComfyUIの環境外でも動作確認ができます。
"""

import numpy as np
import sys
import os

# 現在のディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from NormalizeAmpToFloatNode import NormalizeAmpToFloatNode
    print("✓ NormalizeAmpToFloatNode のインポートに成功しました")
except ImportError as e:
    print(f"✗ インポートエラー: {e}")
    sys.exit(1)


def test_basic_functionality():
    """基本的な機能のテスト"""
    print("\n=== 基本機能テスト ===")
    
    node = NormalizeAmpToFloatNode()
    
    # テストケース1: NumPy配列
    test_data_np = np.array([0.1, 0.5, 0.8, 1.0])
    result = node.convert(test_data_np)
    print(f"NumPy配列テスト: {test_data_np} -> {result[0]}")
    
    # テストケース2: リスト
    test_data_list = [0.2, 0.4, 0.6, 0.9]
    result = node.convert(test_data_list)
    print(f"リストテスト: {test_data_list} -> {result[0]}")
    
    # テストケース3: 単一値
    test_data_single = 0.75
    result = node.convert(test_data_single)
    print(f"単一値テスト: {test_data_single} -> {result[0]}")
    
    # テストケース4: None
    result = node.convert(None)
    print(f"Noneテスト: None -> {result[0]}")


def test_optional_parameters():
    """オプションパラメータのテスト"""
    print("\n=== オプションパラメータテスト ===")
    
    node = NormalizeAmpToFloatNode()
    test_data = [0.5, 1.5, -0.2, 0.8]  # 範囲外の値を含む
    
    # スケーリングテスト
    result = node.convert(test_data, scale_factor=2.0, clamp_values=False)
    print(f"スケーリング(2.0倍, クランプなし): {test_data} -> {result[0]}")
    
    # クランプテスト
    result = node.convert(test_data, scale_factor=2.0, clamp_values=True)
    print(f"スケーリング(2.0倍, クランプあり): {test_data} -> {result[0]}")


def test_edge_cases():
    """エッジケースのテスト"""
    print("\n=== エッジケーステスト ===")
    
    node = NormalizeAmpToFloatNode()
    
    # 空のリスト
    result = node.convert([])
    print(f"空のリスト: [] -> {result[0]}")
    
    # 非常に大きな値
    large_values = [1000.0, -500.0, 999999.9]
    result = node.convert(large_values, clamp_values=True)
    print(f"大きな値(クランプあり): {large_values} -> {result[0]}")
    
    # 文字列（数値）
    result = node.convert("0.5")
    print(f"数値文字列: '0.5' -> {result[0]}")
    
    # 文字列（非数値）
    result = node.convert("invalid")
    print(f"無効な文字列: 'invalid' -> {result[0]}")


def test_input_types():
    """入力タイプ定義のテスト"""
    print("\n=== 入力タイプ定義テスト ===")
    
    input_types = NormalizeAmpToFloatNode.INPUT_TYPES()
    print("入力タイプ定義:")
    for category, params in input_types.items():
        print(f"  {category}:")
        for param_name, param_def in params.items():
            print(f"    {param_name}: {param_def}")


def main():
    """メインテスト関数"""
    print("ComfyUI Audio Amplitude Converter - ノードテスト")
    print("=" * 50)
    
    try:
        test_input_types()
        test_basic_functionality()
        test_optional_parameters()
        test_edge_cases()
        
        print("\n" + "=" * 50)
        print("✓ すべてのテストが完了しました")
        
    except Exception as e:
        print(f"\n✗ テスト中にエラーが発生しました: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
