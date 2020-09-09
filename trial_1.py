import re
import math

iso ={"C": {"C12": [12, 0.9893], "C13": [13.00335483778, 0.0107]},
      "H": {"H1": [1.00782503207, 0.999885], "H2": [2.01410177785, 0.000115]},
      "N": {"N14": [14.00307400478, 0.99632], "N15": [15.00010889823, 0.00368]},
      "O": {"O16": [15.99491461956, 0.99757], "O17": [16.999131703, 0.00038], "O18": [17.999161001, 0.00205]},
      "S": {"S32": [31.972070999, 0.9493], "S33": [32.971458759, 0.0076], "S34": [33.967866902, 0.0429], "S36": [35.96708076, 0.0002]},
      "P": {"P31": [30.973762, 1]},
      "B": {"B10": [10.012937, 0.0199], "B11": [11.009305, 0.801]},
      "F": {"F19": [18.998403, 1]},
      "Cl": {"Cl35": [34.968853, 0.7578], "Cl37": [36.965903, 0.2422]},
      "As": {"As75": [74.921596, 1]},
      "Br": {"Br79": [78.918338, 0.5069], "Br81": [80.916291, 0.4931]},
      "I": {"I127": [126.904468, 1]},
      "Li": {"Li6": [6.015122, 0.0759], "Li7": [7.016004, 0.9241]},
      "Na": {"Na23": [22.98977, 1]},
      "Mg": {"Mg24": [23.985042, 0.7899], "Mg25": [24.985837, 0.10], "Mg26": [25.982593, 0.1101]},
      "Si": {"Si28": [27.976927, 0.922297], "Si29": [28.976495, 0.046832], "Si30": [29.973770, 0.030872]},
      "K": {"K39": [38.963707, 0.932581], "K40": [39.963999, 0.000117], "K41": [40.961826, 0.067302]},
      "Ca": {"Ca40": [39.962591, 0.96941], "Ca42": [41.958618, 0.00647], "Ca43": [42.958767, 0.00135], "Ca44": [43.955481, 0.02086], "Ca48": [47.952534, 0.00187]},
      "Sc": {"Sc45": [44.955910, 1]}}

def fact(m, n):
	if m == n:
		return 1
	else:
		accum = 1
		for i in range(m, n, -1):
			accum *= i
		return accum
		
def carbon():
	carbon_com = {}
	for i in range(1,76):
		carbon_com_sub ={}
		for j in range(i+1):
			if j > 10:
				break
			else:
				mono_iso_c = (i - j) * iso["C"]["C12"][0] + j * iso["C"]["C13"][0]
				weight_c_log = (i - j) * math.log(iso["C"]["C12"][1]) + j* math.log(iso["C"]["C13"][1]) + math.log(fact(i, i-j)) - math.log(math.factorial(j))
				carbon_com_sub[mono_iso_c] = weight_c_log
		carbon_com[i]=carbon_com_sub
			#print(str(mono_iso_c) + "\t" + str(weight_c_log))
	return carbon_com
	
def hydrogen():
	hydrogen_com = {}
	for n in range(1, 151):
		hydrogen_com_sub ={}
		for i in range(n+1):
			if i > 10:
				break
			else:
				mono_iso_h = (n -i) * iso["H"]["H1"][0] + i * iso["H"]["H2"][0]
				weight_h_log = (n - i) * math.log(iso["H"]["H1"][1]) + i * math.log(iso["H"]["H2"][1]) + math.log(fact(n, n-i)) - math.log(math.factorial(i))
			hydrogen_com_sub[mono_iso_h] = weight_h_log
		hydrogen_com[n] = hydrogen_com_sub
			#print(str(mono_iso_h) + "\t" + str(weight_h_log))
	return hydrogen_com
	
def nitrogen():
	nitrogen_com = {}
	for n in range(1, 31):
		nitrogen_com_sub ={}
		for i in range(n+1):
			if i > 10:
				break
			else:
				mono_iso_n = (n - i) * iso["N"]["N14"][0] + i * iso["N"]["N15"][0]
				weight_n_log = (n - i) * math.log(iso["N"]["N14"][1]) + i * math.log(iso["N"]["N15"][1]) + math.log(fact(n, n-i)) - math.log(math.factorial(i))
			nitrogen_com_sub[mono_iso_n] = weight_n_log
		nitrogen_com[n] = nitrogen_com_sub
	return nitrogen_com
	
def oxygen():
	oxygen_com = {}
	for n in range(1,31):
		oxygen_com_sub ={}
		for i in range(n+1):
			for j in range(n-i+1):
				if i + j > 10:
					break
				else:
					mono_iso_o = (n -i -j) * iso["O"]["O16"][0] + i * iso["O"]["O18"][0] + j * iso["O"]["O17"][0]
					weight_o_log = (n - i -j) * math.log(iso["O"]["O16"][1]) + i * math.log(iso["O"]["O18"][1]) + j * math.log(iso["O"]["O17"][1]) + math.log(fact(n, n-i-j)) - math.log(math.factorial(i)) - math.log(math.factorial(j))
					oxygen_com_sub[mono_iso_o] = weight_o_log
		oxygen_com[n] = oxygen_com_sub
	return oxygen_com
	
def sulfur():
	sulfur_com = {}
	for n in range(1, 11):
		sulfur_com_sub = {}
		for i in range(n+1):
			for j in range(n-i+1):
				for k in range(n-i-j+1):
					if i+j+k > 10:
						break
					else:
						mono_iso_s = (n - i -j -k) * iso["S"]["S32"][0] + i * iso["S"]["S34"][0] + j * iso["S"]["S33"][0] + k * iso["S"]["S36"][0]
						weight_s_log = (n-i-j-k) * math.log(iso["S"]["S32"][1]) + i * math.log(iso["S"]["S33"][1]) + j * math.log(iso["S"]["S34"][1]) + k * math.log(iso["S"]["S36"][1]) + math.log(fact(n, (n-i-j-k))) - math.log(math.factorial(i)) - math.log(math.factorial(j)) - math.log(math.factorial(k))
						sulfur_com_sub[mono_iso_s] = weight_s_log
		sulfur_com[n] = sulfur_com_sub
	return sulfur_com  
						
def phosphorus():
	phosphorus_com = {}
	for n in range(1, 11):
		phosphorus_com_sub = {}
		mono_iso_p = n * iso["P"]["P31"][0]
		weight_p_log = 0
		phosphorus_com_sub[mono_iso_p] = weight_p_log
		phosphorus_com[n] = phosphorus_com_sub
	return phosphorus_com

def boron():
	boron_com = {}
	for n in range(1,11):
		boron_com_sub = {}
		for i in range(n+1):
			mono_iso_b = (n - i) * iso["B"]["B11"][0] + i * iso["B"]["B10"][0]
			weight_b_log = (n - i) * math.log(iso["B"]["B11"][1]) + i * math.log(iso["B"]["B10"][1]) + math.log(fact(n, n-i)) - math.log(math.factorial(i))
			boron_com_sub[mono_iso_b] = weight_b_log
		boron_com[n]=boron_com_sub
	return boron_com

def fluorine():
	fluorine_com = {}
	for n in range(1, 11):
		fluorine_com_sub = {}
		mono_iso_f = n * iso["F"]["F19"][0]
		weight_f_log = 0
		fluorine_com_sub[mono_iso_f] = weight_f_log
		fluorine_com[n] = fluorine_com_sub
	return fluorine_com									
			
def chlorine():
	chlorine_com = {}
	for n in range(1,11):
		chlorine_com_sub = {}
		for i in range(n+1):
			mono_iso_cl = (n - i) * iso["Cl"]["Cl35"][0] + i * iso["Cl"]["Cl37"][0]
			weight_cl_log = (n - i) * math.log(iso["Cl"]["Cl35"][1]) + i * math.log(iso["Cl"]["Cl37"][1]) + math.log(fact(n, n-i)) - math.log(math.factorial(i))
			chlorine_com_sub[mono_iso_cl] = weight_cl_log
		chlorine_com[n]=chlorine_com_sub
	return chlorine_com

def arsenic():
	arsenic_com = {}
	for n in range(1, 6):
		arsenic_com_sub = {}
		mono_iso_as = n * iso["As"]["As75"][0]
		weight_as_log = 0
		arsenic_com_sub[mono_iso_as] = weight_as_log
		arsenic_com[n] = arsenic_com_sub
	return arsenic_com	
	
def bromine():
	bromine_com = {}
	for n in range(1,11):
		bromine_com_sub = {}
		for i in range(n+1):
			mono_iso_br = (n - i) * iso["Br"]["Br79"][0] + i * iso["Br"]["Br81"][0]
			weight_br_log = (n - i) * math.log(iso["Br"]["Br79"][1]) + i * math.log(iso["Br"]["Br81"][1]) + math.log(fact(n, n-i)) - math.log(math.factorial(i))
			bromine_com_sub[mono_iso_br] = weight_br_log
		bromine_com[n]=bromine_com_sub
	return bromine_com

def iodine():
	iodine_com = {}
	for n in range(1, 6):
		iodine_com_sub = {}
		mono_iso_i = n * iso["I"]["I127"][0]
		weight_i_log = 0
		iodine_com_sub[mono_iso_i] = weight_i_log
		iodine_com[n] = iodine_com_sub
	return iodine_com	

f1 = open("/Users/wliu/Desktop/text.txt")
#f2 = open("/Users/wliu/Desktop/test_result.txt", "w")



for line in f1:
	mw = {}
	line_sp = line.split()
	form = re.split("(?<=\\D)(?=\\d)|(?<=\\d)(?=\\D)", line_sp[0])
	form_new =[]
	for i in form:
		if sum(1 for c in i if c.isupper()) > 1:
			i_split = re.findall('[A-Z][^A-Z]*', i)
			for j in i_split:
				if j == i_split[-1]:
					form_new.append(j)
				else:
					form_new.append(j)
					form_new.append("1")
		else:
			form_new.append(i)
			
	for i in range(len(form_new)):
		if i%2 == 0:
			element = form_new[i]
		else:
			number = form_new[i]
		if i%2 == 1:
			mw[element] = int(number)
			
			
			
iso_weight = []

for i in mw:
	if i == "C":
		iso_weight.append(carbon(mw[i]))
	elif i == "H":
		iso_weight.append(hydrogen(mw[i]))
		
data = {}

check = 0

while check < len(iso_weight):
	mono_iso_com = 0
	weight_com = 0
	for i in iso_weight:
		for j in i:
		
		
	for j in iso_weight[i]:
		if i == 0:
			mono_iso_com = j
			weight_com = iso_weight[i][j]
		else:
			mono_iso_com += j
			weight_com += iso_weight[i][j]
		if i == len(iso_weight)-1:
			data[mono_iso_com] = math.exp(weight_com)
			
			
			
			
f1.close()
for i in data:
	print(str(i) + "\t" + str(data[i]) + "\n")

