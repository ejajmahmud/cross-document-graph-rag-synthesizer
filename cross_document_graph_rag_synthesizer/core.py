"""Core Document Graph RAG Synthesizer implementation."""
from typing import Dict, List, Set, Tuple, Optional

class EntityNode:
    def __init__(self, name: str, entity_type: str):
        self.name = name
        self.entity_type = entity_type

class RelationEdge:
    def __init__(self, source: str, relation: str, target: str, doc_id: str):
        self.source = source
        self.relation = relation
        self.target = target
        self.doc_id = doc_id

class DocumentGraphRAG:
    def __init__(self):
        self.nodes: Dict[str, EntityNode] = {}
        self.edges: List[RelationEdge] = []
        self.adj: Dict[str, List[Tuple[str, str, str]]] = {}  # src -> (relation, target, doc_id)

    def add_relation(self, source: str, relation: str, target: str, doc_id: str):
        if source not in self.nodes:
            self.nodes[source] = EntityNode(source, "concept")
        if target not in self.nodes:
            self.nodes[target] = EntityNode(target, "concept")

        edge = RelationEdge(source, relation, target, doc_id)
        self.edges.append(edge)

        if source not in self.adj:
            self.adj[source] = []
        self.adj[source].append((relation, target, doc_id))

    def multi_hop_query(self, start_entity: str, max_hops: int = 2) -> List[List[str]]:
        paths = []

        def dfs(curr: str, depth: int, current_path: List[str]):
            if depth > max_hops:
                return
            for rel, nxt, doc in self.adj.get(curr, []):
                new_path = current_path + [f"-[{rel}]->", nxt]
                paths.append(new_path)
                dfs(nxt, depth + 1, new_path)

        dfs(start_entity, 1, [start_entity])
        return paths
