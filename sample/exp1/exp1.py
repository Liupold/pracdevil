#!/usr/bin/python
from pracdevil import Experiment, pracdevilTable

exp = Experiment(name="exp1",date="DD-MM-YY")
exp.mans("man1.pdf", "man2.pdf")
exp.imgs({"Img1":"img1.png"}, {"Img2":"img2.png"})

# data
table1 = exp.table("table1", ["R1", "R2", "No.Obs", "V1", "V2", "V3", "Vin","Theory","Exp"])
table2 = exp.table("table2", ["R1", "R2", "No.Obs", "V1", "V2", "V3", "Vin","Theory","Exp"])

table1.load_data("data.csv")
table2.load_data("table2.csv")

# calculation
table1["Vin"] = table1["V1"] + table1["V2"] + table1["V3"]
table1["Theory"] = -table1["R2"] / table1["R1"]  * table1["Vin"]

table1.print(2)
exp.plot(table1, "Vin", "Exp")
# exp.sync()
# exp.output("exp1.output.pdf")
