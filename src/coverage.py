import re;
import sys;

coverage_str = open('coverage.txt', 'r').readlines()[0]
pattern =  r"^total\:\W+\w+\W+(?P<val>\d+\.\d)"
m = re.search(pattern, coverage_str)
cov = float(m.groups()[0])
print(cov)

if (cov < 30):
    sys.exit("Code Coverage is too low: " + str(cov) + "%, expected 30%")

print("Code Coverage check is passed with " + str(cov) + "%, expected 30%")

