class App:
    def __init__(self):
        self.poly_degree = 0
        self._inp = ""
        self.coef_divisors = []
        self.is_last = False
        self.temp = 0
        self.temp_arr = []
        self.new_polynom = []
        self.has_solution = False
        self.result = ""

    def run(self):
        self.process_user_input()
        self.get_last_coef_divs(self._inp[-1])
        self.apply_scheme(self._inp)

    def process_user_input(self):
        self._inp = input("Zadejte koeficienty polynomu (oddělte mezerou)\n> ").split(" ")
        if self._inp[-1] == "0":
            self._inp = self._inp[:-1]
            print("Posledni hodnota polynomu je 0, po vytknuti vznikne polynom ", end="")
            print("x", end="")
        self.print_polynom(self._inp)

    def get_last_coef_divs(self, last_coef):
        print("Nyni je potreba zjistit vsechny delitele posledniho koeficientu.")
        for i in range(1, abs(int(last_coef)) + 1):
            if int(last_coef) % i == 0:
                self.coef_divisors.append(i)
                self.coef_divisors.append(-i)
        print("Seznam delitelu: [", end="")
        for j in range(len(self.coef_divisors)):
            if j == len(self.coef_divisors) - 1:
                self.is_last = True
            if self.is_last:
                print("{item}]\n".format(item=self.coef_divisors[j]))
            else:
                print("{item}, ".format(item=self.coef_divisors[j]), end="")
        self.is_last = False
        print("Nakonec uz jen prozeneme ziskane hodnoty hornerovym algoritmem.\n")

    def print_polynom(self, polynom):
        self.poly_degree = len(polynom)
        print("(", end="")
        for i in range(self.poly_degree):
            if polynom[i] != 0:
                if i == self.poly_degree - 1:
                    self.is_last = True
                if self.is_last:
                    print("{coef})\n".format(coef=polynom[i]))
                elif i == self.poly_degree - 2:
                    print("{coef}x ".format(coef=polynom[i]), end="")
                else:
                    print("{coef}x^{poly_index} ".format(coef=polynom[i], poly_index=self.poly_degree - i - 1), end="")
        self.is_last = False

    def apply_scheme(self, polynom):
        for i in range(len(self.coef_divisors)):
            self.temp = self.coef_divisors[0]
            self.temp_arr = []
            for j in range(len(polynom)):
                if j > 0:
                    self.temp = int(self.coef_divisors[i]) * self.temp + int(polynom[j])
                    self.temp_arr.append(self.temp)
                else:
                    self.temp *= int(polynom[0])
                    self.temp_arr.append(self.temp)
            if self.temp == 0:
                self.has_solution = True
                self.temp_arr.pop(-1)
                self.new_polynom = self.temp_arr
                if self.coef_divisors[i] > 0:
                    self.result += "(x^1-{coef}) ".format(coef=self.coef_divisors[i])
                else:
                    self.result += "(x^1+{coef}) ".format(coef=abs(self.coef_divisors[i]))
                print(self.result, end="")
                self.print_polynom(self.new_polynom)
                if len(self.new_polynom) > 2:
                    self.apply_scheme(self.new_polynom)
                    self.has_solution = False
        if not self.has_solution:
            print("Dale jiz nelze vyraz upravit.")
            self.result += "("
            for i in range(len(self.new_polynom)):
                if polynom[i] != 0:
                    if i == self.poly_degree - 1:
                        self.is_last = True
                    if self.is_last:
                        self.result += str(self.new_polynom[i]) + ")"
                    else:
                        self.result += str(self.new_polynom[i]) + "x^{index} ".format(index=len(self.new_polynom) - i - 1)
            self.is_last = False
            exit(0)


app = App()
app.run()