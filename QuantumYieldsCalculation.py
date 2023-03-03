from pathlib import Path
import os
import data_base as db

class Main():

    def __init__(self):
        self.solvent_data = self.get_solvent_data()
        self.ref_data = self.get_ref_data()

    def get_solvent_data(self):
        data = db.DATA_SOLVENT
        return data

    def get_ref_data(self):
        data = db.DATA_REF
        return data

    def ref(self, name):
        data = self.ref_data[name]
        for solvent, phi in data.items():
            return solvent, phi

    def solvent(self, name):
        data = self.solvent_data[name]
        return data

    def calcul(self, fluo_ref, fluo_sample, abs_ref, abs_sample, solvent_sample, ref_name):
        n_sample=self.solvent(name=solvent_sample)
        solvent_ref, phi_ref = self.ref(name=ref_name)
        n_ref= self.solvent(name=solvent_ref)

        abs_ratio=(1-pow(10, -abs_ref))/(1-pow(10, -abs_sample)) # pow(10, -2) == 10^-2 == 0.01
        phi_sample = (phi_ref*(abs_ratio)*(fluo_sample/fluo_ref)*((n_sample*n_sample)/(n_ref*n_ref)))
        return round(phi_sample, 3)



if __name__ == "__main__":
    a = Main()
    print(a.get_ref_data())
    print(a.get_solvent_data())
    print(a.calcul(fluo_ref=0.9, fluo_sample=0.45, abs_ref=0.5, abs_sample=2, n_ref=1.36, n_sample=1.4, phi_ref=0.9))
    s, b = a.ref("Fluorescein")
    print(a.solvent(s))
