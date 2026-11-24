"""Tests for DocumentGraphRAG."""
import unittest
from cross_document_graph_rag_synthesizer.core import DocumentGraphRAG

class TestDocumentGraphRAG(unittest.TestCase):
    def test_multi_hop_traversal(self):
        rag = DocumentGraphRAG()
        rag.add_relation("A", "connects", "B", "doc1")
        rag.add_relation("B", "depends_on", "C", "doc2")

        paths = rag.multi_hop_query("A", max_hops=2)
        self.assertTrue(len(paths) >= 2)
        final_path = paths[-1]
        self.assertIn("C", final_path)
