import numpy as np


def dump(path, L):
    print("Dump to ", path)
    with open(path, "w") as f:
        f.write("\n".join([str(x) for x in L]))


def parse_dump_bw(path):
    out_list, in_list = [], []

    def Kbps(s):
        if s[-1] == "M":
            return float(s[:-1]) * 1024.0
        elif s[-1] == "K":
            return float(s[:-1])
        else:
            return float(s) / 1024.0

    with open(path, "r") as f:
        for line in f.readlines():
            if "8443" in line:
                line = line.strip().split()
                b_out, b_in = line[2], line[-2]
                b_out = b_out[:b_out.find("bps")]
                b_in = b_in[:b_in.find("bps")]

                b_out, b_in = Kbps(b_out), Kbps(b_in)

                out_list.append(b_out)
                in_list.append(b_in)

    dump(path.split("/")[-1].split(".")[-2]+"_out.txt", out_list)
    dump(path.split("/")[-1].split(".")[-2]+"_in.txt", in_list)
    print("Out Mean={}Kbps".format(np.mean(out_list)))
    print("In Mean={}Kbps".format(np.mean(in_list)))


# parse_dump_bw("./statbbr5.txt")
# parse_dump_bw("./statbbrblack.txt")
# parse_dump_bw("./statcubic5.txt")
# parse_dump_bw("./statcubicblack.txt")
# parse_dump_bw("./statfusion5.txt")
parse_dump_bw("./statloki.txt")
parse_dump_bw("./statgcc.txt")
parse_dump_bw("./statloki2.txt")
parse_dump_bw("./statgcc2.txt")

parse_dump_bw("./statloki3.txt")
parse_dump_bw("./statgcc3.txt")

