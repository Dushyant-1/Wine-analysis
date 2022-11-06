
import tkinter as ttk
import pandas as pd

model=pd.read_pickle(r'wine/Wineanalysis.pickle')

app=ttk.Tk()
app.geometry('480x480')
app.title('Wine Quality')

cols=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']

#fixed acidity
ttk.Label(app,text='fixed acidity',padx=20,pady=0).grid(row=1,column=0)
fixedacidityVar=ttk.DoubleVar(app)
fixedacidityVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=fixedacidityVar,width=10).grid(row=1,column=1)

#volatile acidity
ttk.Label(app,text='volatile acidity',padx=20,pady=0).grid(row=2,column=0)
volatileacidityVar=ttk.DoubleVar(app)
volatileacidityVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=volatileacidityVar,width=10).grid(row=2,column=1)

#citric acid
ttk.Label(app,text='citric acid',padx=20,pady=0).grid(row=3,column=0)
citricacidVar=ttk.DoubleVar(app)
citricacidVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=citricacidVar,width=10).grid(row=3,column=1)

#residual sugar
ttk.Label(app,text='residual sugar',padx=20,pady=0).grid(row=4,column=0)
residualsugarVar=ttk.DoubleVar(app)
residualsugarVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=residualsugarVar,width=10).grid(row=4,column=1)

#chlorides
ttk.Label(app,text='chlorides',padx=20,pady=0).grid(row=5,column=0)
chloridesVar=ttk.DoubleVar(app)
chloridesVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=chloridesVar,width=10).grid(row=5,column=1)

#free sulfur dioxide
ttk.Label(app,text='free sulfur dioxide',padx=20,pady=0).grid(row=6,column=0)
freesulfurdioxideVar=ttk.DoubleVar(app)
freesulfurdioxideVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=freesulfurdioxideVar,width=10).grid(row=6,column=1)

#total sulfur dioxide
ttk.Label(app,text='total sulfur dioxide',padx=20,pady=0).grid(row=7,column=0)
totalsulfurdioxideVar=ttk.DoubleVar(app)
totalsulfurdioxideVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=totalsulfurdioxideVar,width=10).grid(row=7,column=1)

#density
ttk.Label(app,text='density',padx=20,pady=0).grid(row=8,column=0)
densityVar=ttk.DoubleVar(app)
densityVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=densityVar,width=10).grid(row=9,column=1)

#pH
ttk.Label(app,text='pH',padx=20,pady=0).grid(row=9,column=0)
pHVar=ttk.DoubleVar(app)
pHVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=pHVar,width=10).grid(row=9,column=1)

#sulphates
ttk.Label(app,text='sulphates',padx=20,pady=0).grid(row=10,column=0)
sulphatesVar=ttk.DoubleVar(app)
sulphatesVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=sulphatesVar,width=10).grid(row=10,column=1)

#alcohol
ttk.Label(app,text='alcohol',padx=20,pady=0).grid(row=11,column=0)
alcoholVar=ttk.DoubleVar(app)
alcoholVar.set(0.0)
ttk.Spinbox(app,from_=0, to=10000,textvariable=alcoholVar,width=10).grid(row=11,column=1)


#Prediction Bottom
def wine_analysis():
    global model
    query_df=pd.DataFrame({'fixed acidity':[fixedacidityVar.get()],
                           'volatile acidity':[volatileacidityVar.get()],
                           'citric acid':[citricacidVar.get()],
                           'residual sugar':[residualsugarVar.get()],
                           'chlorides':[chloridesVar.get()],
                           'free sulfur dioxide':[freesulfurdioxideVar.get()],
                           'total sulfur dioxide':[totalsulfurdioxideVar.get()],
                           'density':[densityVar.get()],
                           'pH':[pHVar.get()],
                           'sulphates':[sulphatesVar.get()],
                           'alcohol':[alcoholVar.get()]})

    pred=model.predict(query_df)
    if pred[0]==1:
        resultVar.set('Good Wine')
    else:
        resultVar.set('Bad Wine')
    return 

ttk.Button(app,text='Check',command=wine_analysis,padx=20,pady=2).grid(row=13,column=0,columnspan=2)

#Result
resultVar=ttk.Variable(app)
ttk.Label(app,textvariable=resultVar,font=('Times New Roman',20)).grid(row=14,column=0,columnspan=2)

app.mainloop()