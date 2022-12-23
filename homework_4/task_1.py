class Solution:
    def twoCitySchedCost(self, costs):
        a = sorted(costs, key=lambda x: x[0]-x[1]) # список сначала дешёвые потом дороже
        Sa = 0
        Sb = 0
        for i in range(len(a)//2): # половина
            Sa += a[i][0]

        for i in range(len(a)//2, len(a)): #от середины до конца
            Sb += a[i][1]

        return Sa + Sb