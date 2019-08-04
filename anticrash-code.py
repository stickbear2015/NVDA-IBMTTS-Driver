anticrash_res = {
 re.compile(r'\b(|\d+|\W+)?(|un|anti|re)c(ae|\xe6)sur', re.I): r'\1\2seizur',
 re.compile(r"\b(|\d+|\W+)h'(r|v)[e]", re.I): r"\1h ' \2 e",
 re.compile(r"\b(\w+[bdflmnrvzqh])hes([bcdfgjklmnprtw]\w+)\b", re.I): r"\1 hes\2",
 re.compile(r"(\d):(\d\d[snrt][tdh])", re.I): r"\1 \2",
 re.compile(r"([hH])'([bBdDfFjJkKpPsStTvVxX]+)'([rR][aAeEiIoOuU]?)", re.I): r"\1 \2 \3",
 re.compile(r"(re|un|non|anti)cosp", re.I): r"\1kosp",
 re.compile(r"(anti|non|re|un)caesure", re.I): r"\1ceasure",
 re.compile(r"(EUR[A-Z]+)(\d+)", re.I): r"\1 \2",
 re.compile(r"\b(|\d+|\W+)?tz[s]che", re.I): r"\1tz sche"
}
