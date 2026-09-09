"""
Autonomous Agent LZW Lossless Compression Skill
Pure Python Standard Library implementation.
"""
from typing import List, Dict, Any

class LZWCompressor:
    """
    Adaptive LZW (Lempel-Ziv-Welch) Dictionary Compression Engine.
    """
    @staticmethod
    def compress(uncompressed: str) -> List[int]:
        if not uncompressed:
            return []
        dict_size = 256
        dictionary = {chr(i): i for i in range(dict_size)}
        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = c
        if w:
            result.append(dictionary[w])
        return result

    @staticmethod
    def decompress(compressed: List[int]) -> str:
        if not compressed:
            return ""
        dict_size = 256
        dictionary = {i: chr(i) for i in range(dict_size)}
        w = chr(compressed[0])
        result = [w]
        for k in compressed[1:]:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0]
            else:
                raise ValueError(f"Bad compressed code: {k}")
            result.append(entry)
            dictionary[dict_size] = w + entry[0]
            dict_size += 1
            w = entry
        return "".join(result)
