"""
ComfyUI Audio Amplitude Converter Node

このノードは、Normalize Amplitudeノードの出力（NORMALIZED_AMPLITUDE型）を
Audio Peaks Detectionノードの入力（FLOAT型）に変換するためのカスタムノードです。

Author: ComfyUI Community
License: MIT
"""

import numpy as np
import torch
from typing import Union, List, Tuple, Any


class NormalizeAmpToFloatNode:
    """
    NORMALIZED_AMPLITUDE型からFLOAT型への変換ノード
    
    ComfyUIのオーディオ処理ワークフローにおいて、
    異なる型間の変換を行うためのブリッジノードです。
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        入力タイプの定義
        
        Returns:
            dict: 入力パラメータの定義
        """
        return {
            "required": {
                "normalized_amp": ("NORMALIZED_AMPLITUDE",),
            },
            "optional": {
                "scale_factor": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.1,
                    "display": "number"
                }),
                "clamp_values": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("audio_weights",)
    FUNCTION = "convert"
    CATEGORY = "Audio/Conversion"
    
    OUTPUT_NODE = False
    
    @classmethod
    def IS_CHANGED(cls, normalized_amp, scale_factor=1.0, clamp_values=True):
        """
        入力が変更されたかどうかを判定
        """
        return float("nan")  # 常に再計算

    def convert(self, normalized_amp: Any, scale_factor: float = 1.0, clamp_values: bool = True) -> Tuple[Union[List[float], None]]:
        """
        NORMALIZED_AMPLITUDE型からFLOAT型への変換を実行
        
        Args:
            normalized_amp: 正規化された振幅データ
            scale_factor: スケーリング係数（デフォルト: 1.0）
            clamp_values: 値を0-1の範囲にクランプするかどうか
            
        Returns:
            Tuple[Union[List[float], None]]: 変換されたFLOAT型のオーディオウェイト
        """
        try:
            # None チェック
            if normalized_amp is None:
                print("[NormalizeAmpToFloat] Warning: Input is None")
                return (None,)
            
            # 型に応じた変換処理
            audio_weights = self._convert_to_float_list(normalized_amp)
            
            if audio_weights is None:
                return (None,)
            
            # スケーリング適用
            if scale_factor != 1.0:
                audio_weights = [float(val * scale_factor) for val in audio_weights]
            
            # 値のクランプ（オプション）
            if clamp_values:
                audio_weights = [max(0.0, min(1.0, val)) for val in audio_weights]
            
            print(f"[NormalizeAmpToFloat] Successfully converted {len(audio_weights)} values")
            return (audio_weights,)
            
        except Exception as e:
            print(f"[NormalizeAmpToFloat] Error during conversion: {str(e)}")
            return (None,)
    
    def _convert_to_float_list(self, data: Any) -> Union[List[float], None]:
        """
        様々な型のデータをfloatのリストに変換
        
        Args:
            data: 変換対象のデータ
            
        Returns:
            Union[List[float], None]: 変換されたfloatリスト、または失敗時はNone
        """
        try:
            # NumPy array の場合
            if isinstance(data, np.ndarray):
                return data.flatten().astype(float).tolist()
            
            # PyTorch tensor の場合
            elif isinstance(data, torch.Tensor):
                return data.detach().cpu().numpy().flatten().astype(float).tolist()
            
            # リストまたはタプルの場合
            elif isinstance(data, (list, tuple)):
                return [float(val) for val in data]
            
            # 単一の数値の場合
            elif isinstance(data, (int, float)):
                return [float(data)]
            
            # 文字列の場合（数値として解釈を試行）
            elif isinstance(data, str):
                try:
                    return [float(data)]
                except ValueError:
                    print(f"[NormalizeAmpToFloat] Cannot convert string '{data}' to float")
                    return None
            
            # その他の型でtolist()メソッドを持つ場合
            elif hasattr(data, 'tolist'):
                converted = data.tolist()
                if isinstance(converted, list):
                    return [float(val) for val in converted]
                else:
                    return [float(converted)]
            
            # その他の型で__iter__を持つ場合
            elif hasattr(data, '__iter__'):
                return [float(val) for val in data]
            
            else:
                print(f"[NormalizeAmpToFloat] Unsupported data type: {type(data)}")
                return None
                
        except Exception as e:
            print(f"[NormalizeAmpToFloat] Error in type conversion: {str(e)}")
            return None


# ComfyUI用のノード登録
NODE_CLASS_MAPPINGS = {
    "NormalizeAmpToFloatNode": NormalizeAmpToFloatNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NormalizeAmpToFloatNode": "Normalize Amp to Float"
}

# バージョン情報
__version__ = "1.1.0"
