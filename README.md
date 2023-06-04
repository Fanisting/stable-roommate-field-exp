# Intro

This repo aims to transform the survey data (matching preference + socio vars) into the matching outcome using Irving algorithm. The repo is designed for an ongoing field experiment. The repo achieves:
1. output the matching outcome and whether it is stable
2. find each one's socio-demographic vars for their peers

# Usage

Suppose we have the preference list and other socio-demographic variables:

| name | pref1 | pref2 | pref3 | self_piece | win_tour | peer_piece |
|------|-------|-------|-------|------------|----------|------------|
| 张三   | 王五    | 王柳    | 李四    | 1          | 1        | 1          |
| 王五   | 张三    | 王柳    | 李四    | 0          | 0        | 0          |
| 王柳   | 张三    | 王五    | 李四    | 1          | 1        | 0          |
| 李四   | 张三    | 王五    | 王柳    | 1          | 1        | 1          |
| 范总   | 王柳    | 张三    | 王五    | 0          | 0        | 0          |
| 杨总   | 李四    | 张三    | 王五    | 1          | 1        | 1          |


In the form above, the preference is not complete. So the first step is to fill in the list randomly using the unused names. After the matching process, the program find the peer's socio-demographic, and store them in `peer_${socio-var}`, like:
| name | peer_piece | pref1 | pref2 | pref3 | pref4 | pref5 | self_piece | win_tour | peer_name | peer_peer_piece | peer_self_piece | peer_win_tour |
|------|------------|-------|-------|-------|-------|-------|------------|----------|-----------|-----------------|-----------------|---------------|
| 张三   | 1          | 王五    | 王柳    | 李四    | 范总    | 杨总    | 1          | 1        | 王五        | 0               | 0               | 0             |
| 王五   | 0          | 张三    | 王柳    | 李四    | 杨总    | 范总    | 0          | 0        | 张三        | 1               | 1               | 1             |
| 王柳   | 0          | 张三    | 王五    | 李四    | 范总    | 杨总    | 1          | 1        | 李四        | 1               | 1               | 1             |
| 李四   | 1          | 张三    | 王五    | 王柳    | 杨总    | 范总    | 1          | 1        | 王柳        | 0               | 1               | 1             |
| 范总   | 0          | 王柳    | 张三    | 王五    | 李四    | 杨总    | 0          | 0        | 杨总        | 1               | 1               | 1             |
| 杨总   | 1          | 李四    | 张三    | 王五    | 王柳    | 范总    | 1          | 1        | 范总        | 0               | 0               | 0             |

For the raw data: we store the survey data in `class` folder, and the output can be seen at root folder with names like "三年二班_匹配.csv". 

Run `use.py` to get the matching results. 

### If the group number is not even

This situation is a little bit tricky. Here the matching algorithm will determine which one to be the single one. And the `peer` variables in the single person's line will be none. 

The repo is built on open-sourced repo [here](https://github.com/charlierproctor/matching_algorithm). The following is its README file. 

# Stable Roommates Matching Algorithm

This is an implementation of the stable roommates algorithm, inspired by none other than [https://en.wikipedia.org/wiki/Stable_roommates_problem](https://en.wikipedia.org/wiki/Stable_roommates_problem).

The algorithm has been developed and tested using Python 2.7.

## Usage

For immediate results:

```bash
python match.py
python test.py
```

To run the algorithm on a given preference matrix, run `matchmaker.execute(matrix)`. For example,

```python
# random preference array generator in tests.py
prefs = matrices.random_matrix(20)

# execute the match!!
matchmaker.execute(prefs)
```

Examples such as this are contained in the `match.py` executable. Feel free to run it and play with the results.

`test.py` runs a series of tests, displaying the results in a nicer format.

## Layout

The core of the matching occurs in the `matchmaker.py` file. `match.py` is meant to be the executable, from which you can test the other methods. `person.py` contains the definition of a `Person` class, which allows for proposal to/from another, etc.

The rest of the files are for testing / exploration purposes:

- `matrices.py` contains a variety of common preference matrix options (such as random, wikipedia, and rosetta code).
- `result.py` contains the `Result` class, which attempts to format results nicely
- `stats.py` tracks the statistics of a particular matching run.
- `test.py` runs the algorithm on a series of matrices of varying sizes, displaying the results as appropriate.
