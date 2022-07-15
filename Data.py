import pandas as pd
import io
LSMS1=pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect11b_harvestw3.csv')
LSMS2=pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect3_plantingw3.csv',low_memory=False)
LSMS1['s3q21a']=pd.Series(LSMS2['s3q21a'])
print(LSMS1)
LSMS1['s3q13a']=pd.Series(LSMS2['s3q13a'])
print(LSMS1)
LSMS3 = pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect4c2_plantiNG.csv')
LSMS1['s4cq6']=pd.Series(LSMS3['s4cq6'])
print(LSMS1)
LSMS1.rename(columns={'s11bq4': 'expenditure',},inplace=True)
LSMS1.rename(columns={'s3q21a': 'Income_dist',},inplace=True)
LSMS1.rename({'s3q21a':'Income_earn'},inplace=True)
LSMS1.rename(columns={"s4cq6": "credit"}, inplace=True)
LSMS1.rename(columns={"s3q13a": 'labour_type'}, inplace=True)
LSMS1.dropna(subset=['Income_dist'],inplace=True)
LSMS1.dropna(subset=['expenditure'],inplace=True)
LSMS1.dropna(subset=['labour_type'],inplace=True)
LSMS1.dropna(subset=['credit'],inplace=True)
from datar.all import case_when, f, mutate, pivot_wider
LSMS_df=mutate(LSMS1,state_name=case_when(f.state==1,'Abia', f.state==2,'Adamawa',f.state==3,'Akwa Ibom',
                                                         f.state==4,'Anambra',f.state==5,'Bauchi',f.state==6,'Bayelsa',
                                                          f.state==7,'Benue',f.state==8,'Borno',f.state==9,'Cross River',
                                                       f.state==10,'Delta', f.state==11,'Ebonyi',f.state==12,'Edo', 
                                                        f.state==13,'Ekiti', f.state==14,'Enugu',f.state==15,'Gombe',
                                                        f.state==16,'Imo',f.state==17,'Jigawa',f.state==18,'Kaduna',
                                                          f.state==19,'Kano',f.state==20,'Katsina',f.state==21,'Kebbi',
                                                         f.state==22,'Kogi',f.state==23,'Kwara',f.state==24,'Lagos',
                                                         f.state==25,'Nasarawa',f.state==26,'Niger',f.state==27,'Ogun',
                                                         f.state==28,'Ondo',f.state==29,'Osun',f.state==30,'Oyo',
                                                         f.state==31,'Plateau',f.state==32,'Rivers',f.state==33,'Sokoto',
                                                        f.state==34,'Taraba',f.state==35,'Yobe',f.state==36,'Zamfara',
                                                         f.state==37,'FCT Abuja')
                                        .drop(columns='state'))
LSMS_df