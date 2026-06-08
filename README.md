# Mini-Neuro Molecular Ontology

A semantic web knowledge graph designed to translate standard Class XII Molecular Biology and Biotechnology frameworks into machine-readable logic structures (OWL/RDF). 

##  Project Overview
This repository contains a foundational biological ontology developed to bridge the gap between textbook molecular biology and computational neuroscience. By converting the static information found in standard undergraduate-entry biology curricula into dynamic, queryable data structures, this project provides a concrete blueprint for how Artificial Intelligence systems can interpret genetic and cellular mechanisms.

##  Curriculum Mapping (Class XII Syllabus)
The logical architecture of this ontology directly mirrors the core competencies found in pre-university sciences:
*   **Chapter 4: Molecular Basis of Inheritance:** Translation of structural properties (Purines, Pyrimidines), base-pairing laws, and procedural rules governing the Central Dogma (Transcription & Translation).
*   **Chapter 12: Biotechnology & Applications:** Structural modeling of cloning vectors (Plasmids, Viral Vectors) and their transitive relationship with host organisms.
*   **Neuroscience Minor Foundations:** Linking molecular entities to specific neuroreceptors and pathways (Dopamine and GABA).

##  Technical Stack
*   **Ontology Language:** Web Ontology Language (OWL) / Resource Description Framework (RDF)
*   **Serialization:** Turtle Syntax (`.ttl`)
*   **Development Environment:** Protégé Desktop (Stanford University)
*   **Programmatic Interface:** Python 3 + `owlready2`

## 📁 Repository Architecture
```text
📁 mini-neuro-molecular-ontology/
├── 📄 README.md             # Project abstract, syllabus mapping, and technical specs
├── 📁 ontologies/
│   └── 📄 mini_neuro.ttl    # Complete biological ontology in Turtle format
├── 📁 scripts/
│   └── 📄 query_ontology.py # Python script using Owlready2 to search the graph
└── 📁 documentation/
    └── 📄 graph_viz.png     # Visual map of your ontology generated from Protégé
```

##  Execution & Querying
To programmatically query this ontology using the Python script provided:

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd mini-neuro-molecular-ontology
   ```
2. Install the required Python semantic web engine:
   ```bash
   pip install owlready2
   ```
3. Run the automated query engine:
   ```bash
   python scripts/query_ontology.py
   ```
