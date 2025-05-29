class NormalizeAmpToFloatNode:
    @staticmethod
    def INPUT_TYPES():
        return {"required": {"normalized_amp": "NORMALIZED_AMPLITUDE"}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "convert"

    CATEGORY = "Audio"

    def convert(self, normalized_amp):
        if normalized_amp is None:
            return (None,)

        # numpy arrayならリストに変換
        if hasattr(normalized_amp, "tolist"):
            audio_weights = normalized_amp.tolist()
        else:
            audio_weights = normalized_amp

        return (audio_weights,)
