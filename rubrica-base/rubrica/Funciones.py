import pandas as pd
import numpy as np
def evaluacion(nombres,n,obs):
    try:
        columnas = ["Item","Peso (%)","Observaciones","Nota"]
        filas = [1,2,3,"Total"]
        items = np.array(["Funcionamiento","Requerimientos","Paradigma Funcional",""])
        p = np.array([40,40,20])
        ps = np.array([np.sum(p,axis=0)])
        pesos = np.concatenate([p,ps])
        ns = np.array([np.average(n,0,p)])
        notas = np.concatenate([n,ns])
        datos = np.array([items,pesos,obs,notas])
        info = np.transpose(datos)
        df = pd.DataFrame(info,columns=columnas,index=filas)
        print(f"Apreciados estudiantes {nombres},a continuación, entrego su evaluación del Reto 2\n\n")
        display(df)
    except:
        pass