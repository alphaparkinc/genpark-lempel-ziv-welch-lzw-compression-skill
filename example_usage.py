"""Example usage for LZW Compression Skill."""
from client import LZWCompressor

def main():
    print("Executing LZW Compression...")
    text = "TOBEORNOTTOBEORTOBEORNOT"
    comp = LZWCompressor.compress(text)
    print("Compressed codes:", comp)
    print(f"Original chars: {len(text)}, Compressed codes: {len(comp)}")

    decomp = LZWCompressor.decompress(comp)
    print("Decompressed string:", decomp)
    assert decomp == text, "Decompressed string does not match original"
    print("LZW Compression verified successfully!")

if __name__ == "__main__":
    main()
