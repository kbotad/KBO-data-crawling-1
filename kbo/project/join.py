import pandas as pd
import glob
import os

def concat(year):
    input_file = r'/Users/seungsoo/Documents/GitHub/kbo/project/data' # csv파일들이 있는 디렉토리 위치
    output_file = f'/Users/seungsoo/Documents/GitHub/kbo/project/annual_data/{year}_annual.csv' # 병합하고 저장하려는 파일명
    allFile_list = glob.glob(os.path.join(input_file, f'{year}*')) 
    allData = [] # 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다
    for file in allFile_list:
        df = pd.read_csv(file) # for구문으로 csv파일들을 읽어 들인다
        allData.append(df) # 빈 리스트에 읽어 들인 내용을 추가한다

    if len(allData[0].columns) > len(allData[1].columns):  
        pass   
    else:
        allData.reverse()


    dataCombine = pd.concat(allData, axis=1) 
    dataCombine.to_csv(output_file, index = False)


for year in range(2002,2022):
    concat(year);




def final():
    input_file = r'/Users/seungsoo/Documents/GitHub/kbo/project/annual_data' # csv파일들이 있는 디렉토리 위치
    output_file = f'/Users/seungsoo/Documents/GitHub/kbo/project/final_data/final.csv' # 병합하고 저장하려는 파일명
    allFile_list = glob.glob(os.path.join(input_file,'*')) 

    allData = [] # 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다
    for file in allFile_list:
        df = pd.read_csv(file) # for구문으로 csv파일들을 읽어 들인다
        allData.append(df) # 빈 리스트에 읽어 들인 내용을 추가한다
    
    dataCombine = pd.concat(allData, axis=0) 
    dataCombine.to_csv(output_file, index = False)

final();
