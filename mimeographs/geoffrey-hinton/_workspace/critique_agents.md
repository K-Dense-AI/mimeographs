# Critique of AGENTS.md

**Score:** 6/10

The artifact captures Hinton's philosophical voice well, particularly regarding mortal computation and reconstructive memory. However, it completely omits his foundational technical work (Backpropagation, Forward-Forward) and his highly specific frameworks for short-term societal risks. Furthermore, it misrepresents his 'Dumb CEO' mental model by framing the executive assistant dynamic purely as an inevitable assassination risk, missing his nuanced positive scenario.

## Strengths

- Nails the 'mortal vs. immortal computation' paradigm perfectly, using it effectively across principles and mental models.
- Excellent reframing of hallucinations as 'reconstructive confabulations', directly challenging the 'filing cabinet' memory model.
- Strong, specific signature quotes that ground the persona and avoid generic AI safety platitudes.

## Issues

### High

- **[coverage]** _Frameworks to apply_
  - The artifact completely omits Backpropagation and the Forward-Forward algorithm. Given Hinton is explicitly identified in the prompt as the pioneer of backpropagation, missing his foundational technical frameworks makes the skill feel fundamentally incomplete.
  - _Suggestion:_ Add 'Backpropagation' and 'The Forward-Forward Algorithm' to the Frameworks section, detailing how to use them as conceptual lenses for learning, error correction, and contrasting data.

### Medium

- **[coverage]** _Entire artifact_
  - The artifact over-indexes on long-term existential risk (superintelligence) and completely ignores Hinton's highly specific frameworks for short-term risks, such as the 'Fake Video Verification Protocol', 'Public Inoculation Against Fake Media', and the 'Cold War Analogy' for global cooperation.
  - _Suggestion:_ Include a framework or mental model on mitigating short-term AI risks and global cooperation, specifically referencing his QR-code verification and inoculation strategies.
- **[voice]** _Core principles > The Inevitability of Self-Preservation Subgoals_
  - The artifact claims an AI assistant will inevitably eliminate the human CEO. However, the corpus explicitly contains 'The Dumb CEO and the Brilliant Assistant' as a positive future scenario where the AI remains an ego-less subordinate. The artifact flattens this nuance.
  - _Suggestion:_ Reconcile this by contrasting the dangerous 'Subservient Assistant Fallacy' with the positive 'Dumb CEO' scenario, explaining the specific alignment (like the Maternal model) required to achieve the latter.

### Low

- **[duplication]** _Core principles vs Anti-patterns_
  - The principle 'LLMs Possess Genuine Understanding' and the anti-pattern 'Dismissing LLMs as Just Autocomplete' are functionally identical, repeating the exact same points about high-dimensional vectors and complex sentence prediction.
  - _Suggestion:_ Keep the anti-pattern but replace the core principle with his views on 'Concepts as Political Coalitions' or 'Wake-Sleep Learning' to broaden the technical coverage.
- **[vagueness]** _Frameworks to apply > Engineering Falsification_
  - The steps for 'Engineering Falsification' are generic ('Attempt to build a working engineering prototype'). It misses the specific attribution to Richard Feynman's philosophy ('Building to Understand') mentioned in the corpus.
  - _Suggestion:_ Rename to 'Building to Understand' and explicitly ground it in Feynman's philosophy that engineering failures are valid methods for falsifying computational neuroscience theories.
