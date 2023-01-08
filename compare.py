import ast
import argparse


def levenshtein_distance(s1, s2):
    n = len(s1)
    m = len(s2)
    if n > m:
        n, m = m, n
        s1, s2 = s2, s1

    cur = range(n + 1)
    for i in range(1, m + 1):
        prev = cur
        cur = [i] + [0] * n
        for j in range(1, n + 1):
            add = prev[j] + 1
            delete = cur[j - 1] + 1
            change = prev[j - 1]
            if s1[j - 1] != s2[i - 1]:
                change += 1
            cur[j] = min(add, delete, change)
    return cur[n]


def solve(code1, code2):
    tree1 = ast.parse(code_txt1)
    tree_txt1 = ast.dump(tree1)
    tree2 = ast.parse(code_txt2)
    tree_txt2 = ast.dump(tree2)
    return levenshtein_distance(tree_txt1, tree_txt2) / max(len(code1), len(code2))


parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str)
parser.add_argument("output_file", type=str)
args = parser.parse_args()
input_file = open(args.input_file, 'r')
output_file = open(args.output_file, 'w')

while True:
    files = input_file.readline()
    if not files:
        break
    code_file1, code_file2 = files.split()
    code_txt1 = open(code_file1).read()
    code_txt2 = open(code_file2).read()

    output_file.write(str(solve(code_txt1, code_txt2)) + '\n')
