# Usage

Suppose we have the preference list and other socio-demographic variables:

| name | pref1 | pref2 | pref3 | sex | age | grade |
|------|-------|-------|-------|-----|-----|-------|
| 张三   | 王五    | 王柳    | 李四    | 1   | 14  | 78    |
| 王五   | 张三    | 王柳    | 李四    | 0   | 15  | 79    |
| 王柳   | 张三    | 王五    | 李四    | 1   | 16  | 97    |
| 李四   | 张三    | 王五    | 王柳    | 1   | 17  | 68    |
| 范总   | 王柳    | 张三    | 王五    | 0   | 12  | 66    |
| 杨总   | 李四    | 张三    | 王五    | 0   | 32  | 77    |

In the form above, the preference is not complete. So the first step is to fill in the list randomly using the unused names. After the matching process, the program find the peer's socio-demographic, and store them in `peer_${socio-var}`, like:
| name | age | grade | pref1 | pref2 | pref3 | pref4 | pref5 | sex | peer_age | peer_grade | peer_name | peer_sex |
|------|-----|-------|-------|-------|-------|-------|-------|-----|----------|------------|-----------|----------|
| 张三   | 14  | 78    | 王五    | 王柳    | 李四    | 杨总    | 范总    | 1   | 15       | 79         | 王五        | 0        |
| 王五   | 15  | 79    | 张三    | 王柳    | 李四    | 范总    | 杨总    | 0   | 14       | 78         | 张三        | 1        |
| 王柳   | 16  | 97    | 张三    | 王五    | 李四    | 杨总    | 范总    | 1   | 17       | 68         | 李四        | 1        |
| 李四   | 17  | 68    | 张三    | 王五    | 王柳    | 范总    | 杨总    | 1   | 16       | 97         | 王柳        | 1        |
| 范总   | 12  | 66    | 王柳    | 张三    | 王五    | 李四    | 杨总    | 0   | 32       | 77         | 杨总        | 0        |
| 杨总   | 32  | 77    | 李四    | 张三    | 王五    | 王柳    | 范总    | 0   | 12       | 66         | 范总        | 0        |

For the raw data: we store the survey data in `class` folder, and the output can be seen at root folder with names like "三年二班_匹配.csv". 

Run `use.py` to get the matching results. 

The repo is built on open-sourced repo here 
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
