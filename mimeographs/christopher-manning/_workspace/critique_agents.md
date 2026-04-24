# Critique of AGENTS.md

**Score:** 6/10

The draft captures Manning's philosophical stance on LLMs and intelligence well, but it strips out his specific technical contributions in favor of generic industry concepts. It also suffers from missing source attributions across the entire Frameworks section and one Principle. Finally, the core theme of 'LLMs lack adaptability' is repeated redundantly across three different sections, wasting valuable space.

## Strengths

- Accurately captures Manning's specific framing of NLP as a 'domain science' rather than just generic machine learning.
- The 'How to engage' section provides highly actionable, behavioral triggers for the agent.
- Successfully translates his academic perspective into practical advice for evaluating and building agentic workflows.

## Issues

### High

- **[unattributed]** _Frameworks_
  - None of the frameworks include source attributions, despite clear mappings in the corpus. 'Interactive Linguistic Web Agent Loop' maps to src_011, 'Critical Reading for Research' to src_020, and 'RAG' to src_023.
  - _Suggestion:_ Append the appropriate (src_XXX) tags to the end of each framework's description or title.

### Medium

- **[coverage]** _Frameworks_
  - The artifact includes 'Retrieval-Augmented Generation (RAG)'—a generic industry framework—while completely omitting Manning's highly specific architectural frameworks like 'The Structural Probe Method', 'Layer-Grouped Universal Transformer', or 'Bagel'. This makes the skill feel like a generic AI assistant rather than Christopher Manning.
  - _Suggestion:_ Replace RAG with 'The Structural Probe Method' to give the agent a concrete, Manning-specific way to investigate latent linguistic structures in neural networks.
- **[duplication]** _Throughout_
  - The idea that LLMs are just memorizing facts and lack true adaptability is repeated three times: as a Principle ('Adaptability as True Intelligence'), a Mental Model ('LLMs as Talking Encyclopedias'), and an Anti-pattern ('Assuming Scaling Leads to AGI').
  - _Suggestion:_ Keep 'LLMs as Talking Encyclopedias' as the primary mental model, and use the freed-up space in Principles and Anti-patterns to introduce his views on 'Self-Supervised Word Prediction' or 'Deep Learning as a Vein of Ore'.
- **[unattributed]** _Core principles > Meaning via Use_
  - The 'Meaning via Use' principle is missing its source attribution, which is clearly supported by src_013 in the corpus.
  - _Suggestion:_ Add (src_013) to the end of the principle's description.

### Low

- **[coverage]** _Mental models we reach for_
  - The artifact captures Manning's skepticism of AGI but misses his profound optimism about the current trajectory of AI, specifically his mental models 'Deep Learning as a Vein of Ore' or 'The Worst Technology'.
  - _Suggestion:_ Add 'Deep Learning as a Vein of Ore' to balance his AGI skepticism with his pragmatic advice to keep pushing current architectures.
