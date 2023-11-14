import pandas as pd
from subprocess import Popen as pp

f = open("C:/*****/****/****/****/********")
content = f.read()

df=pd.DataFrame([content])
df.to_clipboard(index=False,header=False,sep="")

