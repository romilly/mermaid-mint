## 🧜‍♂️ Mermaid Flowchart Cheat Sheet

Mermaid is a JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions to create and modify diagrams dynamically. It's particularly useful for generating flowcharts, sequence diagrams, and more, directly from your code or documentation.

---
- ### 📐 Basic Flowchart Syntax
  
  To define a flowchart in Mermaid, start with the `flowchart` keyword followed by a direction (`LR`, `TB`, `RL`, `BT`):
  
  ```
  flowchart LR
  A[Start] --> B[Process]
  B --> C{Decision}
  C -->|Yes| D[Action 1]
  C -->|No| E[Action 2]
  D --> F[End]
  E --> F
  ```
  
  This code generates a simple flowchart with a decision node and two possible actions.
  
  ---
- ### 🔄 Flowchart Directions
- `LR`: Left to Right
- `TB`: Top to Bottom
- `RL`: Right to Left
- `BT`: Bottom to Top
  
  Example:
  
  ```
  flowchart TB
  A --> B --> C
  ```
  
  This sets the flowchart direction from top to bottom.
  
  ---
- ### 🔗 Node Types and Links
  
  Mermaid supports various node types:
- `[ ]`: Rectangle (default)
- `(( ))`: Circle
- `[[ ]]`: Round rectangle
- `{{ }} `: Subroutine
- `> >`: Asymmetric rectangle
- `> >`: Asymmetric rectangle
  
  Links between nodes can be defined using:
- `-->`: Solid arrow
- `-.->`: Dashed arrow
- `==>`: Thick arrow
- `~~~>`: Invisible link
  
  Example:
  
  ```
  flowchart LR
  A --> B
  B -.-> C
  C ==> D
  D ~~~> E
  ```
  
  ---
- ### 🧩 Subgraphs and Grouping
  
  Subgraphs allow you to group nodes together, which is useful for representing modules or components within a system.
  
  ```
  flowchart LR
  subgraph A [Group A]
    A1[Node A1]
    A2[Node A2]
  end
  subgraph B [Group B]
    B1[Node B1]
    B2[Node B2]
  end
  A1 --> B1
  A2 --> B2
  ```
  
  This creates two groups, A and B, each containing two nodes.
  
  ---
- ### 🧠 Advanced Features
- **Links with labels**:
  
  ```
  flowchart LR
  A -->|Label| B
  ```
- **Multiple links**:
  
  ```
  flowchart LR
  A & B --> C
  ```
- **Link styles**:
  
  ```
  flowchart LR
  A --> B
  B ==> C
  C -.-> D
  D ~~~> E
  ```
- **Markdown formatting in labels**:
  
  ```
  flowchart LR
  A["`code`"] --> B["**bold**"]
  ```
- **Unicode characters**:
  
  ```
  flowchart LR
  A["🚀"] --> B["🌟"]
  ```
  
  ---
- ### ⚠️ Important Notes
- Avoid using the word `end` in lowercase within flowcharts, as it can cause rendering issues. Use `End` or wrap it in quotes.
- When using the letters `o` or `x` as the first character in a node ID, add a space before them or capitalize the letter to prevent rendering issues.
  
  ---
- ### 🖼️ Example Diagram
  
  ```
  flowchart LR
  A[Start] --> B[Process]
  B --> C{Decision}
  C -->|Yes| D[Action 1]
  C -->|No| E[Action 2]
  D --> F[End]
  E --> F
  ```
  
  This code generates a simple flowchart with a decision node and two possible actions.
  
  ---
  
  For more detailed information and advanced features, refer to the official Mermaid documentation: [Mermaid Flowchart Syntax](https://mermaid.js.org/syntax/flowchart.html).
  
  Feel free to ask if you need further assistance with Mermaid diagrams or integrating them into your projects!