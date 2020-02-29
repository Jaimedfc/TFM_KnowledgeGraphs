import pandas as pd
datasetS2 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S2/S2.pkl")
emgS2 = datasetS2["signal"]["chest"]["EMG"]
emgDatasetS2=pd.DataFrame(emgS2,columns=["EMG"])
ecgS2 = datasetS2["signal"]["chest"]["ECG"]
ecgDatasetS2=pd.DataFrame(ecgS2,columns=["ECG"])
tempS2 = datasetS2["signal"]["chest"]["Temp"]
tempDatasetS2=pd.DataFrame(tempS2,columns=["TEMP"])
edaS2 = datasetS2["signal"]["chest"]["EDA"]
edaDatasetS2=pd.DataFrame(edaS2,columns=["EDA"])
respS2 = datasetS2["signal"]["chest"]["Resp"]
respDatasetS2=pd.DataFrame(respS2,columns=["RESP"])
labelS2 = datasetS2["label"]
labelDatasetS2=pd.DataFrame(labelS2,columns=["label"])
dataChestS2=pd.concat([ecgDatasetS2, emgDatasetS2, edaDatasetS2, tempDatasetS2, respDatasetS2, labelDatasetS2], axis=1)
dataChestCleanS2 = dataChestS2.loc[dataChestS2["label"]>0]
dataChestCleanS2 = dataChestCleanS2.loc[dataChestCleanS2["label"]<5]
dataChestCleanS2["Sujeto"] = "S2"
dataChestCleanS2 = dataChestCleanS2.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS3 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S3/S3.pkl")
emgS3 = datasetS3["signal"]["chest"]["EMG"]
emgDatasetS3=pd.DataFrame(emgS3,columns=["EMG"])
ecgS3 = datasetS3["signal"]["chest"]["ECG"]
ecgDatasetS3=pd.DataFrame(ecgS3,columns=["ECG"])
tempS3 = datasetS3["signal"]["chest"]["Temp"]
tempDatasetS3=pd.DataFrame(tempS3,columns=["TEMP"])
edaS3 = datasetS3["signal"]["chest"]["EDA"]
edaDatasetS3=pd.DataFrame(edaS3,columns=["EDA"])
respS3 = datasetS3["signal"]["chest"]["Resp"]
respDatasetS3=pd.DataFrame(respS3,columns=["RESP"])
labelS3 = datasetS3["label"]
labelDatasetS3=pd.DataFrame(labelS3,columns=["label"])
dataChestS3=pd.concat([ecgDatasetS3, emgDatasetS3, edaDatasetS3, tempDatasetS3, respDatasetS3, labelDatasetS3], axis=1)
dataChestCleanS3 = dataChestS3.loc[dataChestS3["label"]>0]
dataChestCleanS3 = dataChestCleanS3.loc[dataChestCleanS3["label"]<5]
dataChestCleanS3["Sujeto"] = "S3"
dataChestCleanS3 = dataChestCleanS3.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS4 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S4/S4.pkl")
emgS4 = datasetS4["signal"]["chest"]["EMG"]
emgDatasetS4=pd.DataFrame(emgS4,columns=["EMG"])
ecgS4 = datasetS4["signal"]["chest"]["ECG"]
ecgDatasetS4=pd.DataFrame(ecgS4,columns=["ECG"])
tempS4 = datasetS4["signal"]["chest"]["Temp"]
tempDatasetS4=pd.DataFrame(tempS4,columns=["TEMP"])
edaS4 = datasetS4["signal"]["chest"]["EDA"]
edaDatasetS4=pd.DataFrame(edaS4,columns=["EDA"])
respS4 = datasetS4["signal"]["chest"]["Resp"]
respDatasetS4=pd.DataFrame(respS4,columns=["RESP"])
labelS4 = datasetS4["label"]
labelDatasetS4=pd.DataFrame(labelS4,columns=["label"])
dataChestS4=pd.concat([ecgDatasetS4, emgDatasetS4, edaDatasetS4, tempDatasetS4, respDatasetS4, labelDatasetS4], axis=1)
dataChestCleanS4 = dataChestS4.loc[dataChestS4["label"]>0]
dataChestCleanS4 = dataChestCleanS4.loc[dataChestCleanS4["label"]<5]
dataChestCleanS4["Sujeto"] = "S4"
dataChestCleanS4 = dataChestCleanS4.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS5 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S5/S5.pkl")
emgS5 = datasetS5["signal"]["chest"]["EMG"]
emgDatasetS5=pd.DataFrame(emgS5,columns=["EMG"])
ecgS5 = datasetS5["signal"]["chest"]["ECG"]
ecgDatasetS5=pd.DataFrame(ecgS5,columns=["ECG"])
tempS5 = datasetS5["signal"]["chest"]["Temp"]
tempDatasetS5=pd.DataFrame(tempS5,columns=["TEMP"])
edaS5 = datasetS5["signal"]["chest"]["EDA"]
edaDatasetS5=pd.DataFrame(edaS5,columns=["EDA"])
respS5 = datasetS5["signal"]["chest"]["Resp"]
respDatasetS5=pd.DataFrame(respS5,columns=["RESP"])
labelS5 = datasetS5["label"]
labelDatasetS5=pd.DataFrame(labelS5,columns=["label"])
dataChestS5=pd.concat([ecgDatasetS5, emgDatasetS5, edaDatasetS5, tempDatasetS5, respDatasetS5, labelDatasetS5], axis=1)
dataChestCleanS5 = dataChestS5.loc[dataChestS5["label"]>0]
dataChestCleanS5 = dataChestCleanS5.loc[dataChestCleanS5["label"]<5]
dataChestCleanS5["Sujeto"] = "S5"
dataChestCleanS5 = dataChestCleanS5.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS6 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S6/S6.pkl")
emgS6 = datasetS6["signal"]["chest"]["EMG"]
emgDatasetS6=pd.DataFrame(emgS6,columns=["EMG"])
ecgS6 = datasetS6["signal"]["chest"]["ECG"]
ecgDatasetS6=pd.DataFrame(ecgS6,columns=["ECG"])
tempS6 = datasetS6["signal"]["chest"]["Temp"]
tempDatasetS6=pd.DataFrame(tempS6,columns=["TEMP"])
edaS6 = datasetS6["signal"]["chest"]["EDA"]
edaDatasetS6=pd.DataFrame(edaS6,columns=["EDA"])
respS6 = datasetS6["signal"]["chest"]["Resp"]
respDatasetS6=pd.DataFrame(respS6,columns=["RESP"])
labelS6 = datasetS6["label"]
labelDatasetS6=pd.DataFrame(labelS6,columns=["label"])
dataChestS6=pd.concat([ecgDatasetS6, emgDatasetS6, edaDatasetS6, tempDatasetS6, respDatasetS6, labelDatasetS6], axis=1)
dataChestCleanS6 = dataChestS6.loc[dataChestS6["label"]>0]
dataChestCleanS6 = dataChestCleanS6.loc[dataChestCleanS6["label"]<5]
dataChestCleanS6["Sujeto"] = "S6"
dataChestCleanS6 = dataChestCleanS6.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS7 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S7/S7.pkl")
emgS7 = datasetS7["signal"]["chest"]["EMG"]
emgDatasetS7=pd.DataFrame(emgS7,columns=["EMG"])
ecgS7 = datasetS7["signal"]["chest"]["ECG"]
ecgDatasetS7=pd.DataFrame(ecgS7,columns=["ECG"])
tempS7 = datasetS7["signal"]["chest"]["Temp"]
tempDatasetS7=pd.DataFrame(tempS7,columns=["TEMP"])
edaS7 = datasetS7["signal"]["chest"]["EDA"]
edaDatasetS7=pd.DataFrame(edaS7,columns=["EDA"])
respS7 = datasetS7["signal"]["chest"]["Resp"]
respDatasetS7=pd.DataFrame(respS7,columns=["RESP"])
labelS7 = datasetS7["label"]
labelDatasetS7=pd.DataFrame(labelS7,columns=["label"])
dataChestS7=pd.concat([ecgDatasetS7, emgDatasetS7, edaDatasetS7, tempDatasetS7, respDatasetS7, labelDatasetS7], axis=1)
dataChestCleanS7 = dataChestS7.loc[dataChestS7["label"]>0]
dataChestCleanS7 = dataChestCleanS7.loc[dataChestCleanS7["label"]<5]
dataChestCleanS7["Sujeto"] = "S7"
dataChestCleanS7 = dataChestCleanS7.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS8 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S8/S8.pkl")
emgS8 = datasetS8["signal"]["chest"]["EMG"]
emgDatasetS8=pd.DataFrame(emgS8,columns=["EMG"])
ecgS8 = datasetS8["signal"]["chest"]["ECG"]
ecgDatasetS8=pd.DataFrame(ecgS8,columns=["ECG"])
tempS8 = datasetS8["signal"]["chest"]["Temp"]
tempDatasetS8=pd.DataFrame(tempS8,columns=["TEMP"])
edaS8 = datasetS8["signal"]["chest"]["EDA"]
edaDatasetS8=pd.DataFrame(edaS8,columns=["EDA"])
respS8 = datasetS8["signal"]["chest"]["Resp"]
respDatasetS8=pd.DataFrame(respS8,columns=["RESP"])
labelS8 = datasetS8["label"]
labelDatasetS8=pd.DataFrame(labelS8,columns=["label"])
dataChestS8=pd.concat([ecgDatasetS8, emgDatasetS8, edaDatasetS8, tempDatasetS8, respDatasetS8, labelDatasetS8], axis=1)
dataChestCleanS8 = dataChestS8.loc[dataChestS8["label"]>0]
dataChestCleanS8 = dataChestCleanS8.loc[dataChestCleanS8["label"]<5]
dataChestCleanS8["Sujeto"] = "S8"
dataChestCleanS8 = dataChestCleanS8.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS9 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S9/S9.pkl")
emgS9 = datasetS9["signal"]["chest"]["EMG"]
emgDatasetS9=pd.DataFrame(emgS9,columns=["EMG"])
ecgS9 = datasetS9["signal"]["chest"]["ECG"]
ecgDatasetS9=pd.DataFrame(ecgS9,columns=["ECG"])
tempS9 = datasetS9["signal"]["chest"]["Temp"]
tempDatasetS9=pd.DataFrame(tempS9,columns=["TEMP"])
edaS9 = datasetS9["signal"]["chest"]["EDA"]
edaDatasetS9=pd.DataFrame(edaS9,columns=["EDA"])
respS9 = datasetS9["signal"]["chest"]["Resp"]
respDatasetS9=pd.DataFrame(respS9,columns=["RESP"])
labelS9 = datasetS9["label"]
labelDatasetS9=pd.DataFrame(labelS9,columns=["label"])
dataChestS9=pd.concat([ecgDatasetS9, emgDatasetS9, edaDatasetS9, tempDatasetS9, respDatasetS9, labelDatasetS9], axis=1)
dataChestCleanS9 = dataChestS9.loc[dataChestS9["label"]>0]
dataChestCleanS9 = dataChestCleanS9.loc[dataChestCleanS9["label"]<5]
dataChestCleanS9["Sujeto"] = "S9"
dataChestCleanS9 = dataChestCleanS9.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS10 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S10/S10.pkl")
emgS10 = datasetS10["signal"]["chest"]["EMG"]
emgDatasetS10=pd.DataFrame(emgS10,columns=["EMG"])
ecgS10 = datasetS10["signal"]["chest"]["ECG"]
ecgDatasetS10=pd.DataFrame(ecgS10,columns=["ECG"])
tempS10 = datasetS10["signal"]["chest"]["Temp"]
tempDatasetS10=pd.DataFrame(tempS10,columns=["TEMP"])
edaS10 = datasetS10["signal"]["chest"]["EDA"]
edaDatasetS10=pd.DataFrame(edaS10,columns=["EDA"])
respS10 = datasetS10["signal"]["chest"]["Resp"]
respDatasetS10=pd.DataFrame(respS10,columns=["RESP"])
labelS10 = datasetS10["label"]
labelDatasetS10=pd.DataFrame(labelS10,columns=["label"])
dataChestS10=pd.concat([ecgDatasetS10, emgDatasetS10, edaDatasetS10, tempDatasetS10, respDatasetS10, labelDatasetS10], axis=1)
dataChestCleanS10 = dataChestS10.loc[dataChestS10["label"]>0]
dataChestCleanS10 = dataChestCleanS10.loc[dataChestCleanS10["label"]<5]
dataChestCleanS10["Sujeto"] = "S10"
dataChestCleanS10 = dataChestCleanS10.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS11 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S11/S11.pkl")
emgS11 = datasetS11["signal"]["chest"]["EMG"]
emgDatasetS11=pd.DataFrame(emgS11,columns=["EMG"])
ecgS11 = datasetS11["signal"]["chest"]["ECG"]
ecgDatasetS11=pd.DataFrame(ecgS11,columns=["ECG"])
tempS11 = datasetS11["signal"]["chest"]["Temp"]
tempDatasetS11=pd.DataFrame(tempS11,columns=["TEMP"])
edaS11 = datasetS11["signal"]["chest"]["EDA"]
edaDatasetS11=pd.DataFrame(edaS11,columns=["EDA"])
respS11 = datasetS11["signal"]["chest"]["Resp"]
respDatasetS11=pd.DataFrame(respS11,columns=["RESP"])
labelS11 = datasetS11["label"]
labelDatasetS11=pd.DataFrame(labelS11,columns=["label"])
dataChestS11=pd.concat([ecgDatasetS11, emgDatasetS11, edaDatasetS11, tempDatasetS11, respDatasetS11, labelDatasetS11], axis=1)
dataChestCleanS11 = dataChestS11.loc[dataChestS11["label"]>0]
dataChestCleanS11 = dataChestCleanS11.loc[dataChestCleanS11["label"]<5]
dataChestCleanS11["Sujeto"] = "S11"
dataChestCleanS11 = dataChestCleanS11.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS13 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S13/S13.pkl")
emgS13 = datasetS13["signal"]["chest"]["EMG"]
emgDatasetS13=pd.DataFrame(emgS13,columns=["EMG"])
ecgS13 = datasetS13["signal"]["chest"]["ECG"]
ecgDatasetS13=pd.DataFrame(ecgS13,columns=["ECG"])
tempS13 = datasetS13["signal"]["chest"]["Temp"]
tempDatasetS13=pd.DataFrame(tempS13,columns=["TEMP"])
edaS13 = datasetS13["signal"]["chest"]["EDA"]
edaDatasetS13=pd.DataFrame(edaS13,columns=["EDA"])
respS13 = datasetS13["signal"]["chest"]["Resp"]
respDatasetS13=pd.DataFrame(respS13,columns=["RESP"])
labelS13 = datasetS13["label"]
labelDatasetS13=pd.DataFrame(labelS13,columns=["label"])
dataChestS13=pd.concat([ecgDatasetS13, emgDatasetS13, edaDatasetS13, tempDatasetS13, respDatasetS13, labelDatasetS13], axis=1)
dataChestCleanS13 = dataChestS13.loc[dataChestS13["label"]>0]
dataChestCleanS13 = dataChestCleanS13.loc[dataChestCleanS13["label"]<5]
dataChestCleanS13["Sujeto"] = "S13"
dataChestCleanS13 = dataChestCleanS13.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS14 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S14/S14.pkl")
emgS14 = datasetS14["signal"]["chest"]["EMG"]
emgDatasetS14=pd.DataFrame(emgS14,columns=["EMG"])
ecgS14 = datasetS14["signal"]["chest"]["ECG"]
ecgDatasetS14=pd.DataFrame(ecgS14,columns=["ECG"])
tempS14 = datasetS14["signal"]["chest"]["Temp"]
tempDatasetS14=pd.DataFrame(tempS14,columns=["TEMP"])
edaS14 = datasetS14["signal"]["chest"]["EDA"]
edaDatasetS14=pd.DataFrame(edaS14,columns=["EDA"])
respS14 = datasetS14["signal"]["chest"]["Resp"]
respDatasetS14=pd.DataFrame(respS14,columns=["RESP"])
labelS14 = datasetS14["label"]
labelDatasetS14=pd.DataFrame(labelS14,columns=["label"])
dataChestS14=pd.concat([ecgDatasetS14, emgDatasetS14, edaDatasetS14, tempDatasetS14, respDatasetS14, labelDatasetS14], axis=1)
dataChestCleanS14 = dataChestS14.loc[dataChestS14["label"]>0]
dataChestCleanS14 = dataChestCleanS14.loc[dataChestCleanS14["label"]<5]
dataChestCleanS14["Sujeto"] = "S14"
dataChestCleanS14 = dataChestCleanS14.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS15 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S15/S15.pkl")
emgS15 = datasetS15["signal"]["chest"]["EMG"]
emgDatasetS15=pd.DataFrame(emgS15,columns=["EMG"])
ecgS15 = datasetS15["signal"]["chest"]["ECG"]
ecgDatasetS15=pd.DataFrame(ecgS15,columns=["ECG"])
tempS15 = datasetS15["signal"]["chest"]["Temp"]
tempDatasetS15=pd.DataFrame(tempS15,columns=["TEMP"])
edaS15 = datasetS15["signal"]["chest"]["EDA"]
edaDatasetS15=pd.DataFrame(edaS15,columns=["EDA"])
respS15 = datasetS15["signal"]["chest"]["Resp"]
respDatasetS15=pd.DataFrame(respS15,columns=["RESP"])
labelS15 = datasetS15["label"]
labelDatasetS15=pd.DataFrame(labelS15,columns=["label"])
dataChestS15=pd.concat([ecgDatasetS15, emgDatasetS15, edaDatasetS15, tempDatasetS15, respDatasetS15, labelDatasetS15], axis=1)
dataChestCleanS15 = dataChestS15.loc[dataChestS15["label"]>0]
dataChestCleanS15 = dataChestCleanS15.loc[dataChestCleanS15["label"]<5]
dataChestCleanS15["Sujeto"] = "S15"
dataChestCleanS15 = dataChestCleanS15.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS16 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S16/S16.pkl")
emgS16 = datasetS16["signal"]["chest"]["EMG"]
emgDatasetS16=pd.DataFrame(emgS16,columns=["EMG"])
ecgS16 = datasetS16["signal"]["chest"]["ECG"]
ecgDatasetS16=pd.DataFrame(ecgS16,columns=["ECG"])
tempS16 = datasetS16["signal"]["chest"]["Temp"]
tempDatasetS16=pd.DataFrame(tempS16,columns=["TEMP"])
edaS16 = datasetS16["signal"]["chest"]["EDA"]
edaDatasetS16=pd.DataFrame(edaS16,columns=["EDA"])
respS16 = datasetS16["signal"]["chest"]["Resp"]
respDatasetS16=pd.DataFrame(respS16,columns=["RESP"])
labelS16 = datasetS16["label"]
labelDatasetS16=pd.DataFrame(labelS16,columns=["label"])
dataChestS16=pd.concat([ecgDatasetS16, emgDatasetS16, edaDatasetS16, tempDatasetS16, respDatasetS16, labelDatasetS16], axis=1)
dataChestCleanS16 = dataChestS16.loc[dataChestS16["label"]>0]
dataChestCleanS16 = dataChestCleanS16.loc[dataChestCleanS16["label"]<5]
dataChestCleanS16["Sujeto"] = "S16"
dataChestCleanS16 = dataChestCleanS16.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
datasetS17 = pd.read_pickle("/media/jaime/tocho/Universidad/Master/TFM/WESAD/S17/S17.pkl")
emgS17 = datasetS17["signal"]["chest"]["EMG"]
emgDatasetS17=pd.DataFrame(emgS17,columns=["EMG"])
ecgS17 = datasetS17["signal"]["chest"]["ECG"]
ecgDatasetS17=pd.DataFrame(ecgS17,columns=["ECG"])
tempS17 = datasetS17["signal"]["chest"]["Temp"]
tempDatasetS17=pd.DataFrame(tempS17,columns=["TEMP"])
edaS17 = datasetS17["signal"]["chest"]["EDA"]
edaDatasetS17=pd.DataFrame(edaS17,columns=["EDA"])
respS17 = datasetS17["signal"]["chest"]["Resp"]
respDatasetS17=pd.DataFrame(respS17,columns=["RESP"])
labelS17 = datasetS17["label"]
labelDatasetS17=pd.DataFrame(labelS17,columns=["label"])
dataChestS17=pd.concat([ecgDatasetS17, emgDatasetS17, edaDatasetS17, tempDatasetS17, respDatasetS17, labelDatasetS17], axis=1)
dataChestCleanS17 = dataChestS17.loc[dataChestS17["label"]>0]
dataChestCleanS17 = dataChestCleanS17.loc[dataChestCleanS17["label"]<5]
dataChestCleanS17["Sujeto"] = "S17"
dataChestCleanS17 = dataChestCleanS17.reindex(columns=['ECG','EMG','EDA','TEMP','RESP','Sujeto', 'label'])
dataChest=pd.concat([dataChestCleanS17, dataChestCleanS16, dataChestCleanS15, dataChestCleanS14, dataChestCleanS13, dataChestCleanS11, dataChestCleanS10, dataChestCleanS9, dataChestCleanS8, dataChestCleanS7, dataChestCleanS6, dataChestCleanS5, dataChestCleanS4, dataChestCleanS3, dataChestCleanS2], axis=0)
dataChest = dataChest.sample(frac=1).reset_index(drop=True)
dataChest.to_pickle("../Data/cleanDataset.pkl")