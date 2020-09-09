res = {"A": {"C": 3, "H": 5, "N": 1, "O": 1, "S": 0},
       "R": {"C": 6, "H": 12, "N": 4, "O": 1, "S": 0},
       "N": {"C": 4, "H": 6, "N": 2, "O": 2, "S": 0},
       "D": {"C": 4, "H": 5, "N": 1, "O": 3, "S": 0},
       "C": {"C": 3, "H": 5, "N": 1, "O": 1, "S": 1},
       "Q": {"C": 5, "H": 8, "N": 2, "O": 2, "S": 0},
       "E": {"C": 5, "H": 7, "N": 1, "O": 3, "S": 0},
       "G": {"C": 2, "H": 3, "N": 1, "O": 1, "S": 0},
       "H": {"C": 6, "H": 7, "N": 3, "O": 1, "S": 0},
       "I": {"C": 6, "H": 11, "N": 1, "O": 1, "S": 0},
       "L": {"C": 6, "H": 11, "N": 1, "O": 1, "S": 0},
       "K": {"C": 6, "H": 12, "N": 2, "O": 1, "S": 0},
       "M": {"C": 5, "H": 9, "N": 1, "O": 1, "S": 1},
       "F": {"C": 9, "H": 9, "N": 1, "O": 1, "S": 0},
       "P": {"C": 5, "H": 7, "N": 1, "O": 1, "S": 0},
       "S": {"C": 3, "H": 5, "N": 1, "O": 2, "S": 0},
       "T": {"C": 4, "H": 7, "N": 1, "O": 2, "S": 0},
       "W": {"C": 11, "H": 10, "N": 2, "O": 1, "S": 0},
       "Y": {"C": 9, "H": 9, "N": 1, "O": 2, "S": 0},
       "V": {"C": 5, "H": 9, "N": 1, "O": 1, "S": 0}}

c_no = 0
h_no = 0
n_no = 0
o_no = 0
s_no = 0

protein = "GSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHPGSAKDFLIYMCWENQTRVHP"

for i in protein:
    c_no += res[i]["C"]
    h_no += res[i]["H"]
    n_no += res[i]["N"]
    o_no += res[i]["O"]
    s_no += res[i]["S"]

print("The formula is C" + str(c_no) + "H" + str(h_no) + "N"
      + str(n_no) + "O" + str(o_no) + "S" + str(s_no))

iso ={"C": {"C12": [12, 0.9893], "C13": [13.00335483778, 0.0107]},
      "H": {"H1": [1.00782503207, 0.999885], "H2": [2.01410177785, 0.000115]},
      "N": {"N14": [14.00307400478, 0.99632], "N15": [15.00010889823, 0.00368]},
      "O": {"O16": [15.99491461956, 0.99757], "O17": [16.999131703, 0.00038], "O18": [17.999161001, 0.00205]},
      "S": {"S32": [31.972070999, 0.9493], "S33": [32.971458759, 0.0076], "S34": [33.967866902, 0.0429], "S36": [35.96708076, 0.0002]}}

c_ave = iso["C"]["C12"][0] * iso["C"]["C12"][1] + iso["C"]["C13"][0] * iso["C"]["C13"][1]
h_ave = iso["H"]["H1"][0] * iso["H"]["H1"][1] + iso["H"]["H2"][0] * iso["H"]["H2"][1]
n_ave = iso["N"]["N14"][0] * iso["N"]["N14"][1] + iso["N"]["N15"][0] * iso["N"]["N15"][1]
o_ave = iso["O"]["O16"][0] * iso["O"]["O16"][1] + iso["O"]["O17"][0] * iso["O"]["O17"][1] + iso["O"]["O18"][0] * iso["O"]["O18"][1]
s_ave = iso["S"]["S32"][0] * iso["S"]["S32"][1] + iso["S"]["S33"][0] * iso["S"]["S33"][1] + iso["S"]["S34"][0] * iso["S"]["S34"][1] + iso["S"]["S36"][0] * iso["S"]["S36"][1]

ave_mass = c_no * c_ave + h_no * h_ave + n_no * n_ave + o_no * o_ave + s_no * s_ave

print("The average mass is %f" %ave_mass)


mono_iso = c_no * iso["C"]["C12"][0] +h_no * iso["H"]["H1"][0] + n_no * iso["N"]["N14"][0] + o_no * iso["O"]["O16"][0] + s_no * iso["S"]["S32"][0]
print("The smallest monoisotopic mass is %f" %mono_iso)


