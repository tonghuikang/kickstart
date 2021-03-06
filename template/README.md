# Competitive Programming Template

This contains the code template I use for competitive programming.

[TOC]



### Contest preparation script

```
cd template
git checkout -b $CONTEST_NAME
ss
sa code
code .
jn
```

These are the command-line shortcuts that I use

```
alias ss="source /usr/local/anaconda3/etc/profile.d/conda.sh"
alias sa="conda activate"
alias jn="jupyter notebook"

alias t="touch"
alias cx="./run_cpp.sh"
alias px="./run_py.sh"
alias pi="./run_pi.sh"
```



### How to use (general)

Copy the test case to `a0`. If there are additional test cases copy them as `a1`, `a2` etc. I hope to automate this process




### How to use (Python)

To run the code

````bash
python a.py < a0
````

The debug statements prints in a different color.
You can submit the code without commenting out the debugging statements, I do not think it should affect the run time.

To compile the code and run for all test cases

```bash
./run_py.sh a
```

I made the above command an alias, so in contests I run

```bash
px a
```



##### Recursion

If you need to recursively call functions more than 1000 times, please use the function decorator in `recursive_example_1.py` (may not always work)



##### Interactive questions
- You can read input as usual.
- When printing, please flush, i.e. `print(x, flush=True)`
- At the end of the program, please execute `sys.exit()`



Google provides an [interactive testing tool](https://codingcompetitions.withgoogle.com/codejam/faq#interactive-problems). Google maintains an `interactive_runner.py` for all interactive problems. In each interactive problem, they provide a specific `local_testing_tool.py` for you to test your code.

You will need to write your code in `sample_interactive_script.py`.

```bash
python interactive_runner.py python3 sample_local_testing_tool.py $TEST_CASE -- python3 sample_interactive_script.py
```

I made the above command an alias, so in contests I run

```bash
pxi 1
```





##### Python Algorithm Templates 
The following algorithmic templates should be available.

- [AtCoder library](https://atcoder.github.io/ac-library/master/document_en/) 
  - (There is a [Python](https://github.com/not522/ac-library-python) [version](https://github.com/Mitarushi/ACL-Python) but probably I want to extract copiable snippets instead of running the script to transfer the functions.
- Math
  - Ceiling division (ok)
  - Inverse modulo (ok)
  - Prime factorisation (ok)
  - Chinese Remainder Theorem (please check)
  - Floor Sum
  - Convolution
  - Binomial coefficient
- Trees
  - Trie (ok)
  - Fenwick Tree
  - Segment Tree
  - Lazy Segment Tree
  - [intervaltree](https://github.com/chaimleib/intervaltree) clone
  - [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) clone
- Arrays
  - Prefix Sum
  - Longest Common Subsequence (ok)
  - Longest Common Subarray (ok)
  - Longest Increasing Subsequence (ok)
  - Sliding Windows
  - Suffix Array
  - LCP array
  - Z algorithm
- Search
  - Binary Search
  - Ternary Search
  - [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
  - Gradient Descent
- Graphs
  - (Some code to process graphs)
  - Dijkstra Algorithm (ok)
  - Count Connected Components (ok)
  - Disjoint Set Union (ok)
  - Minimum Spanning Tree (ok)
  - Topological Sort and Cycle Detection (ok)
  - Clique Cover and Chromatic Number (ok)
  - Floyd–Warshall algorithm (tbc, for graphs with negative edges)
  - Dinic's algorithm for max-flow problem (tbc)
  - Algorithm (?) for min-cost flow problem (tbc)
  - 2-SAT (tbc)
- Recursion template
  - (Because the default recursion limit for Python is 1000)
- Other Algorithms
  - Convex Hull (tbc, Monotone Chain algorithm)
  - Coordinate Compression (tbc)




### How to use (C++)

Please refer to my [C++ conversion course](../docs/cpp_conversion_course.md)

To compile the code and run for all test cases

```
./run_cpp.sh x
```

I made the above command an alias, so in contests I run

```bash
cx a
```






## Todo

- Automatically download test cases 
  - From Codeforces given address like https://codeforces.com/contest/1519/problems

CI/CD to check correctness and runtime of algorithm templates

## Resources

Recently I found a [competitive programing library in Python](https://github.com/cheran-senthil/PyRival).
- I think I will continue developing this because it also saves all my participation attempts, and I want folders and files to navigate through.
- Some code will be copied from there, I will change them to fit my style.