"""CLI for Cross-Document Graph RAG."""
import argparse
from .core import DocumentGraphRAG

def main():
    parser = argparse.ArgumentParser(description="Cross-Document Graph RAG Synthesizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run multi-hop graph RAG demo")
    args = parser.parse_args()

    graph = DocumentGraphRAG()
    graph.add_relation("AuthService", "stores_in", "PostgreSQL", "doc1.md")
    graph.add_relation("PostgreSQL", "backed_up_to", "S3_Vault", "doc2.md")

    paths = graph.multi_hop_query("AuthService", max_hops=2)
    print("Multi-Hop Relations Discovered:")
    for p in paths:
        print(" ", " ".join(p))

if __name__ == "__main__":
    main()
