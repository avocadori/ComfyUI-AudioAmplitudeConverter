"""
ComfyUI Audio Amplitude Converter

ComfyUI用のオーディオ振幅変換カスタムノードパッケージ
"""

from .NormalizeAmpToFloatNode import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
__version__ = "1.1.0"
