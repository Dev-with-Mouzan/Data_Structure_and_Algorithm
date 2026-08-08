<div align="center">

<img width="88" height="88" alt="DSA" src="assets/icons/logo.svg" />

# Data Structures &amp; Algorithms

### A curated collection of fundamental data structures and algorithms implemented in Python

| Python 3.8+ | 15 Topics | PRs Welcome |
| :---------: | :-------: | :---------: |
| <img width="96" height="20" alt="Python 3.8+" src="assets/icons/badge-python.svg" /> | <img width="104" height="20" alt="15 Topics" src="assets/icons/badge-topics.svg" /> | <img width="110" height="20" alt="PRs Welcome" src="assets/icons/badge-prs.svg" /> |

</div>

---

This repository contains clean, commented implementations of core **data structures** and **algorithms** in Python. Every topic is organized into its own numbered folder, making it easy to browse, learn, and practice.

## 📑 Table of Contents

- [Data Structures](#-data-structures)
- [Sorting Algorithms](#-sorting-algorithms)
- [Algorithm Design Techniques](#-algorithm-design-techniques)
- [Repository Map](#-repository-map)
- [Getting Started](#-getting-started)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧱 Data Structures

| Icon | Topic | Description |
| :--: | :---- | :---------- |
| <img width="34" height="34" alt="Array" src="assets/icons/array.svg" /> | **[01-Array](./01-Array)** | Fundamentals of array operations and manipulations |
| <img width="34" height="34" alt="Singly Linked List" src="assets/icons/singly-linked-list.svg" /> | **[02-Singly-Linked-List](./02-Singly-Linked-List)** | Implementation and operations on singly linked lists |
| <img width="34" height="34" alt="Doubly Linked List" src="assets/icons/doubly-linked-list.svg" /> | **[03-Doubly-Linked-List](./03-Doubly-Linked-List)** | Implementation and operations on doubly linked lists |
| <img width="34" height="34" alt="Stack" src="assets/icons/stack.svg" /> | **[04-Stack](./04-Stack)** | LIFO data structure implementations |
| <img width="34" height="34" alt="Queue" src="assets/icons/queue.svg" /> | **[05-Queue](./05-Queue)** | FIFO data structure implementations |
| <img width="34" height="34" alt="Tree" src="assets/icons/tree.svg" /> | **[06-Tree](./06-Tree)** | Hierarchical structures (Binary Trees, BSTs) |
| <img width="34" height="34" alt="Graph" src="assets/icons/graph.svg" /> | **[07-Graph](./07-Graph)** | Graph representations and traversal algorithms |

---

## ⚡ Sorting Algorithms

| Icon | Topic | Description |
| :--: | :---- | :---------- |
| <img width="34" height="34" alt="Bubble Sort" src="assets/icons/bubble-sort.svg" /> | **[08-Bubble-Sort](./08-Bubble-Sort)** | Repeatedly swaps adjacent elements in order |
| <img width="34" height="34" alt="Selection Sort" src="assets/icons/selection-sort.svg" /> | **[09-Selection-Sort](./09-Selection-Sort)** | Selects the minimum and swaps it into place |
| <img width="34" height="34" alt="Insertion Sort" src="assets/icons/insertion-sort.svg" /> | **[10-Insertion-Sort](./10-Insertion-Sort)** | Inserts each element into its correct position |
| <img width="34" height="34" alt="Merge Sort" src="assets/icons/merge-sort.svg" /> | **[11-Merge-Sort](./11-Merge-Sort)** | Divide-and-conquer by splitting and merging |
| <img width="34" height="34" alt="Quick Sort" src="assets/icons/quick-sort.svg" /> | **[12-Quick-Sort](./12-Quick-Sort)** | Partition-based sorting around a pivot |

---

## 🧠 Algorithm Design Techniques

| Icon | Topic | Description |
| :--: | :---- | :---------- |
| <img width="34" height="34" alt="Recursion" src="assets/icons/recursion.svg" /> | **[13-Recursion](./13-Recursion)** | Problem-solving using recursive approaches |
| <img width="34" height="34" alt="Dynamic Programming" src="assets/icons/dynamic-programming.svg" /> | **[14-Dynamic-Programming](./14-Dynamic-Programming)** | Optimization via memoization and tabulation |
| <img width="34" height="34" alt="Greedy Approach" src="assets/icons/greedy-approach.svg" /> | **[15-Greedy-Approach](./15-Greedy-Approach)** | Algorithms making locally optimal choices |

---

## 🗂 Repository Map

```
.
├── 01-Array/                      # Array operations & NumPy basics
├── 02-Singly-Linked-List/         # Singly linked list creation & insertion
├── 03-Doubly-Linked-List/         # Doubly linked list creation & insertion
├── 04-Stack/                      # Stack implementation (LIFO)
├── 05-Queue/                      # Queue & circular queue (FIFO)
├── 06-Tree/                       # Binary tree, BST & deletion
├── 07-Graph/                      # Matrix & adjacency list, BFS, DFS
├── 08-Bubble-Sort/                # Bubble sort
├── 09-Selection-Sort/             # Selection sort
├── 10-Insertion-Sort/             # Insertion sort
├── 11-Merge-Sort/                 # Merge sort
├── 12-Quick-Sort/                 # Quick sort
├── 13-Recursion/                  # Fibonacci & factorial (recursive)
├── 14-Dynamic-Programming/        # 0/1 Knapsack (DP)
├── 15-Greedy-Approach/            # Fractional Knapsack (greedy)
├── assets/icons/                  # SVG icons used in this README
├── requirements.txt               # Python dependencies (numpy)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Dev-with-Mouzan/Data_Structure_and_Algorithm.git
cd Data_Structure_and_Algorithm
```

### 2. Enter a topic folder

Each topic lives in its own numbered directory. Navigate into the one you want to explore:

```bash
cd 01-Array          # Windows & Linux/macOS
cd "01-Array"        # safer quoting, works everywhere
```

### 3. Install dependencies

Only [NumPy](https://numpy.org/) is required (for the array examples); everything else uses the Python standard library:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the examples

```bash
python "01-Array/Array_python.py"
python "01-Array/Numpy_array.py"
python "02-Singly-Linked-List/Singly_Linklist.py"
python "07-Graph/BFS.py"
```

Each folder contains source code related to its specific topic, ready to read, run, and experiment with.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to submit a pull request if you have improvements, optimizations, or new algorithms to add.



