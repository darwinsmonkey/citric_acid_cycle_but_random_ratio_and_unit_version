import random
import matplotlib.pyplot as plt



def sas(oxaloacetate, citrate, isocitrate, aketoglutarate, succinyl_coa, succinate, fumarate, malate):
    reg1 = oxaloacetate           # stores the inital value of oxaloacetate
    reg2 = random.random() / 100  # stores the inital value of acetlycoa
    reg3 = citrate                # stores the inital value of citrate
    reg4 = isocitrate             # stores the inital value of isocitrate
    reg5 = aketoglutarate   # stores the inital value of alfa ketoglutarate
    reg6 = succinyl_coa     # stores the inital value of succinly_coa
    reg7 = succinate        # stores the inital value of succinate
    reg8 = fumarate         # stores the inital value of fumarate
    reg9 = malate           # stores the inital value of malate

    e1 = 1
    e2 = 1
    e3 = 1
    e4 = 1
    e5 = 1
    e6 = 1
    e7 = 1
    e8 = 1


    oxaloacetate = reg1 + ((reg9 * 1) * e8) - ((reg2 * 1) * e1) - (reg1/100) + reg9/100

    citrate = reg3 + ((reg2 * 1) * e1) - ((reg3 * 1) * e2)

    isocitrate = reg4 +  ((reg3 * 1) * e2) - ((reg4 * 6/5) * e3)

    aketoglutarate = reg5 + ((reg4 * 6/5) * e3) - ((reg5 * 5/4) * e4)

    succinyl_coa = reg6 + ((reg5 * 5/4) * e4) - ((reg6 * 1) * e5)

    succinate = reg7 + ((reg6 * 1) * e5) - ((reg7 * 1) * e6)

    fumarate = reg8 + ((reg7 * 1) * e6) - ((reg8 * 1) * e7)

    malate = reg9 + ((reg8 * 1) * e7) - ((reg9 * 1) * e8)

    return oxaloacetate, citrate, isocitrate, aketoglutarate, succinyl_coa, succinate, fumarate, malate





