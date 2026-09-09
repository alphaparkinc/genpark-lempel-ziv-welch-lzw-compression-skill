# genpark-lempel-ziv-welch-lzw-compression-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-lempel-ziv-welch-lzw-compression-skill?style=social)](https://github.com/alphaparkinc/genpark-lempel-ziv-welch-lzw-compression-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Lempel-Ziv-Welch (LZW) Adaptive Lossless Dictionary Compression & Decompression Engine

Part of the **GenPark Autonomous Information Theory & Optimal Entropy Coding Swarm**.

## Architecture Overview

```mermaid
graph TD
    A[Uncompressed Character Stream] --> B[Initialize ASCII 0-255 Dictionary]
    B --> C[Find Longest Prefix String W in Dictionary]
    C --> D[Read Next Character C]
    D --> E{W + C in Dictionary?}
    E -->|Yes| F[W = W + C]
    E -->|No| G[Emit Dictionary Code for W]
    G --> H[Add W + C to Dictionary New Index]
    H --> I[W = C]
    F --> J{More Characters?}
    I --> J
    J -->|Yes| C
    J -->|No| K[Emit Final Code for W]
    K --> L[Compressed Integer Code Sequence]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies. Runs anywhere.
- **Production-Grade Design**: Type annotations, exhaustive edge cases, robust numerical stability.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-lempel-ziv-welch-lzw-compression-skill.git
cd genpark-lempel-ziv-welch-lzw-compression-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
