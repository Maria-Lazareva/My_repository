import sys

if len(sys.argv) < 4:
    print(f"Enter the correct data: ")
else:
    ar1 = float(sys.argv[1])
    ar2 = float(sys.argv[2])
    ar3 = float(sys.argv[3])
    res = ar1 * ar2 + ar3
    print(res)
