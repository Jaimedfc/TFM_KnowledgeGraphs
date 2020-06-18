
import pandas as pd
from neo4j import GraphDatabase

#Definir driver con uri y credenciales
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test"), encrypted=False)
triples = []
#Recuperar todo el grafo
with driver.session() as session:
    result = session.run("MATCH (a)-[rel]->(b) RETURN a.val,b.val,rel")
    for record in result:
        rel = record["rel"]
        a = record["a.val"]
        b = record["b.val"]
        triple = (a, rel.type, b)
        triples.append(triple)
#Crear dataset y guardarlo
dataset = pd.DataFrame(triples, columns=["subject", "predicate", "object"])
dataset.to_pickle("../Data/NeoTriples.pkl")
