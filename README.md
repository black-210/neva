

# NEVA

### Lattice Mathematics • Lattice Reduction • Cryptographic Research

Neva is a lightweight mathematical toolkit for experimenting with **lattices, linear algebra, and lattice reduction** using Python and NumPy.

The project is designed around a simple idea:

> **Advanced mathematics should not require an enormous codebase.**

Neva provides an interactive environment where users can enter lattice bases, inspect their mathematical properties, and experiment with reduction techniques such as **LLL**.

---

## ✦ What is Neva?

Lattices are mathematical structures that appear throughout modern cryptography, optimization, computational number theory, and post-quantum cryptography.

Neva provides a small experimental environment for studying these structures directly.

Instead of hiding the mathematics behind a large framework, Neva exposes the underlying operations:

- Matrix analysis
- Vector norms
- Dot products
- Determinants
- Angles
- Projections
- Gram-Schmidt analysis
- Eigenvalues
- Eigenvectors
- Singular Value Decomposition
- Lattice basis analysis
- LLL reduction experiments
- Reduced-basis comparison

The goal is not to create another enormous dependency-heavy framework.

The goal is **simplicity with mathematical depth**.

---

## ⚡ Philosophy

Neva follows three principles:

### Simple Code

The implementation intentionally stays small and understandable.

### Powerful Mathematics

A small amount of code can still perform meaningful mathematical analysis.

### Freedom to Experiment

Users can enter their own lattice dimensions and basis vectors and immediately inspect the resulting mathematical structure.

---

## 🧮 Example

Start Neva:

```bash
python neva.py

Enter a lattice:

Dimension: 2

Row 1: 105 821
Row 2: 12 95
```
Neva analyzes the lattice and produces information such as:

Determinant
Vector norms
Dot products
Angles
Projections
Gram-Schmidt
Eigenvalues
Eigenvectors
Singular Values
LLL Reduction
Reduced Basis
Reduced Norms

The resulting reduced basis can then be compared with the original basis.


---

🔬 Lattice Reduction

Neva currently contains an experimental implementation of LLL lattice reduction.

LLL is an important algorithm in computational number theory and lattice-based cryptographic research.

Conceptually:

Original Basis
      │
      ▼
Lattice Analysis
      │
      ▼
Gram-Schmidt Information
      │
      ▼
LLL Reduction
      │
      ▼
Reduced Basis

The purpose is to make the mathematics visible and easy to experiment with.


---

🧠 Mathematical Components

Neva currently works with several fundamental linear-algebra operations.

Vector Norms

Measure the magnitude of lattice vectors.

Dot Products

Analyze relationships between vectors.

Determinants

Provide information about the volume of the fundamental parallelepiped of a lattice.

Projections

Measure the component of one vector along another.

Angles

Analyze geometric relationships between basis vectors.

Gram-Schmidt

Provides orthogonalized representations useful for understanding lattice geometry and reduction algorithms.

Eigenvalues & Eigenvectors

Provide additional matrix-level analysis.

Singular Values

Expose the numerical structure and conditioning of the lattice matrix.


---

🛠 Requirements

Neva currently requires:

Python 3

NumPy


Install NumPy:
```
pip install numpy
```
Run:
```
python neva.py
```

---

📦 Dependencies

Neva intentionally keeps dependencies minimal.

Current core dependency:

NumPy

The project avoids unnecessary libraries so the mathematical implementation remains easy to inspect and modify.


---

🚧 Project Status

Experimental / Research

Neva is actively evolving.

Current work focuses on building a compact foundation for lattice experimentation and reduction algorithms.

Future development may include:

Improved LLL implementation

BKZ experimentation

SVP research tools

CVP research tools

Lattice visualization

Basis quality metrics

Reduction benchmarking

Cryptographic parameter analysis

Post-quantum cryptography research utilities



---

🔐 Post-Quantum Cryptography

Lattice mathematics plays an important role in modern post-quantum cryptography.

Neva is intended as a research and educational mathematics toolkit for exploring the underlying structures and algorithms.

Neva is not currently a production cryptographic library and should not be treated as one.

The project does not claim to break modern cryptographic systems or recover real-world private keys.


---

🎯 Why Neva?

Many mathematical and cryptographic tools become difficult to understand because their implementations grow into huge frameworks.

Neva takes another approach:

Small Code
   +
Clear Mathematics
   +
Interactive Input
   =
Easy Experimentation

The project is built to make it possible to look at a lattice, manipulate it, reduce it, and understand what happened without navigating through thousands of lines of framework code.


---

🧪 Example Research Workflow

1. Create a lattice
        ↓
2. Inspect the basis
        ↓
3. Calculate mathematical properties
        ↓
4. Analyze vector relationships
        ↓
5. Perform Gram-Schmidt analysis
        ↓
6. Run LLL reduction
        ↓
7. Compare original and reduced bases


---

📈 Roadmap

v0.x

[x] Interactive lattice input

[x] Matrix analysis

[x] Vector norms

[x] Dot products

[x] Determinants

[x] Angles

[x] Projections

[x] Gram-Schmidt analysis

[x] Eigenvalue analysis

[x] Eigenvector analysis

[x] Singular values

[x] LLL experimentation


Future

[ ] Improved LLL

[ ] BKZ

[ ] SVP experimentation

[ ] CVP experimentation

[ ] Lattice visualization

[ ] Benchmarking

[ ] Cryptographic research modules

[ ] PQC parameter analysis

[ ] Expanded mathematical toolkit



---

📜 License

Neva is released under the MIT License.

You are free to use, modify, study, and distribute the software according to the terms of the license.


---

⚠️ Disclaimer

Neva is an experimental mathematical and research project.

Results should be independently verified before being used in security-critical research or cryptographic implementations.

The current LLL implementation is intended for experimentation and learning, not as a replacement for mature, formally tested cryptographic libraries.


---

⭐ Contributing

Contributions, experiments, mathematical improvements, bug fixes, and research ideas are welcome.

If you improve an algorithm, please include an explanation of the mathematical change whenever possible.

The goal is not simply to make Neva larger.

The goal is to make it better.


---

NEVA

Small implementation.
Large mathematics.
Unlimited experimentation.
