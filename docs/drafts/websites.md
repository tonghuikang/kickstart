# Coding platforms

[TOC]

Calendar containing all competitions information https://competitiveprogramming.info/calendar



Probably should make a table with the following features.

- Full feedback
- Peer hacking
- Shows wrong test case
- Interactive problems
- Input parsing required
- Python libraries - numpy, scipy, numba
- PyPy
- Online Judging
- Official solutions
- Frequency



Probably a rating map table as well.





### Codeforces

Basically the platform for competitive programming.



### AtCoder

Neat and minimal interface. Discussion threads are held at Codeforces.



### Leetcode
Pretty intuitive. Very regular contests. Problems are sufficiently novel every time. I have obtained the T-shirt.

This is the platform to share interview questions.

For interactive problems, just fill up their functions.



### Hackerrank

They have mostly discontinued contests.



### TopCoder

The defining feature of TopCoder is the focus on hacking other's solutions.




### CodeChef

Codeforces but with slow UI and troublesome UX.



### Google Coding platforms

This refers to the [Kickstart](https://codingcompetitions.withgoogle.com/kickstart) and [Codejam](https://codingcompetitions.withgoogle.com/codejam) environments. This may be applicable to other platforms.


Interactive problems might be easier to compensate on its difficulty of implementation. Many interactive problems have a lower bound on the number of moves that can be made, and you can experiment with that to formulate a strategy.

The size limits hints the allowed computation time. Sometimes it may fool you, as the optimal computation time is much lower compared.



Libraries allowed in Google coding environment, other than native libraries - Numpy and scipy is [allowed](https://codingcompetitions.withgoogle.com/kickstart/faq)

```
python 3.5.3 (package: python3.5)
numpy 1.16.2 (pip install numpy)
scipy 1.2.1 (pip install scipy)
python3.5 Solution.py
```

#### Interactive problems

You need to obtain `interactive_runner.py` which applies to all CodeJam problem post-2020, and `local_testing_tool.py` from the specific problem. Refer to [template.md](template/template.md) for the code to run.

Run this on your computer to ensure that it is working.

```bash
for TEST_CASE in 0 1 2
do
  python interactive_runner.py python3 sample_local_testing_tool.py $TEST_CASE -- python3 sample_interactive_script.py
done
```




### Facebook Hackercup

You compute your solution on your computer and upload the result.

There are three sets of data

- Public set - in the question statement and the expected solution is shown
- Validation set - you need to solve this to unlock the private set and the expected solution is not shown
- Private set - you need to submit your solution within 6 minutes from downloading this set
  - Please test your algorithm on the largest possible input before trying this. You may need to resolve stack overflow issues.

It is possible to run your code on parallel machines. You might want to set that up.



## Interactive problems - general

Google and Codeforces may ask you to parse beyond the first input.

You need to flush after printing `print(i, flush=True)`.  

When done, please execute `sys.exit()`











