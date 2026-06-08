import os
from owlready2 import *

def main():
    # Construct paths dynamically to maintain cross-platform compatibility
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ontology_path = os.path.join(script_dir, "..", "ontologies", "mini_neuro.ttl")
    
    print("--------------------------------------------------")
    print("🧬 UNIFIED BIO-ONTOLOGY FRAMEWORK | QUERY ENGINE  ")
    print("--------------------------------------------------")
    print(f"[STATUS] Loading ontology from: {os.path.normpath(ontology_path)}")
    
    try:
        # Load the local Turtle ontology into Owlready2
        onto = get_ontology(ontology_path).load()
        
        # Sync the reasoning engine to verify inferred Symmetric properties
        print("[STATUS] Synchronizing HermiT Reasoner...")
        with onto:
            sync_reasoner_hermit()
            
        print("[STATUS] Ontology loaded successfully.\n")
        
        # --- QUERY 1: Demonstrate the Symmetric Property ---
        print("🔍 [QUERY 1] Checking Base-Pairing Laws (Symmetric Properties):")
        adenine = onto.Adenine
        thymine = onto.Thymine
        
        # Read asserted configuration
        a_pairs = adenine.pairs_with
        print(f"  Asserted: Adenine pairs with -> {[x.name for x in a_pairs]}")
        
        # Read reasoned configuration (Thymine pairs with Adenine automatically)
        t_pairs = thymine.pairs_with
        print(f"  Reasoned/Inferred: Thymine pairs with -> {[x.name for x in t_pairs]}")
        
        # --- QUERY 2: Find Class Substructures ---
        print("\n🔍 [QUERY 2] Scanning Molecular Neuroscience Assertions:")
        neuroreceptors = list(onto.Neuroreceptor.instances())
        for receptor in neuroreceptors:
            transmitters = receptor.utilizes_neurotransmitter
            tx_names = [tx.name for tx in transmitters]
            print(f"  Neuroreceptor Entity: '{receptor.name}' utilizes Neurotransmitter: {tx_names}")
            
        # --- QUERY 3: Central Dogma Flow ---
        print("\n🔍 [QUERY 3] Extracting Central Dogma Transcription Data:")
        dna_templates = list(onto.DNA.instances())
        for template in dna_templates:
            targets = template.is_template_for
            target_names = [r.name for r in targets]
            print(f"  DNA Template: '{template.name}' is_template_for -> {target_names}")
            
    except Exception as e:
        print(f"\n[ERROR] Failed to load or execute queries on the ontology. Details: {e}")
        print("[TIP] Ensure that your working directory is correct and Protégé output matches the syntax.")

    print("\n--------------------------------------------------")

if __name__ == "__main__":
    main()
