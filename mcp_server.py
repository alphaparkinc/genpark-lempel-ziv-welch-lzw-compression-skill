"""MCP Server for LZW Compression Skill."""
import json
import sys
from client import LZWCompressor

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [
                            {
                                "name": "lzw_compress",
                                "description": "Compress text using LZW algorithm",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {"text": {"type": "string"}},
                                    "required": ["text"]
                                }
                            },
                            {
                                "name": "lzw_decompress",
                                "description": "Decompress LZW integer code sequence",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "codes": {"type": "array", "items": {"type": "integer"}}
                                    },
                                    "required": ["codes"]
                                }
                            }
                        ]
                    }
                }
            elif method == "tools/call":
                name = params.get("name")
                args = params.get("arguments", {})
                if name == "lzw_compress":
                    codes = LZWCompressor.compress(args["text"])
                    out = {"codes": codes, "count": len(codes)}
                else:
                    text = LZWCompressor.decompress(args["codes"])
                    out = {"text": text}
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
