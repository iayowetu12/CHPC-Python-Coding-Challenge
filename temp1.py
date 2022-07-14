import pandas as pd

df= pd.read_csv('covid_data_01012021.csv')

# 1. Solution
print()
print("1. Solution")
print(df.head(10))

# # # 2. Solution
print()
print("2. Solution")
collist=df.columns[df.isnull().any()].tolist()
print(collist)

# # 3. Solution
print()
print("3. Solution")
filteredColumns = df.dtypes[df.dtypes == "float64"]
print("Number of float64 Dtypes: " + str(len(filteredColumns)))

# # 4. Solution
print()
print("4. Solution")
mean_FIPS=df['FIPS'].mean()
print("FIPS mean: " + str(mean_FIPS))

# # 5. Solutions
print()
print("5. Solution")
df_aust = df.loc[df['Country_Region'] == 'Australia']
aust=pd.DataFrame(df_aust, columns=['Last_Update','Confirmed','Deaths','Recovered','Active'])
print(aust)
print()

# Lastest total number of Confirmed cases
confirmed=aust['Confirmed'].sum()
print('Total confirmed cases: ' + str(confirmed))

# Lastest total number of Deaths cases
deaths=aust['Deaths'].sum()
print('Total Deaths cases: ' + str(deaths))

# Lastest total number of Recorvered cases
recovered=aust['Recovered'].sum()
print('Total confirmed cases: ' + str(recovered))

# Lastest total number of Active cases
active=aust['Active'].sum()
print('Total Deaths cases: ' + str(active))

# # 6 Solution
print()
print("6. Solution")
df_china = df.loc[df['Country_Region']=='China']
china=pd.DataFrame(df_china, columns=['Province_State','Confirmed','Deaths','Recovered'])
# sort Confrimed in an Descending order
china_sorted=china.sort_values(by=['Confirmed'], inplace=False)
print(china_sorted)

# # 6.1  Solution
print()
print("6.1 Solution")
max_confirmed=china_sorted['Confirmed'].max()
df_china = china_sorted.loc[china_sorted['Confirmed'] == max_confirmed]
print(df_china)
print("Chinese province with the highest number of confirmed cases: Hubei")


# # 7. Solution 
print()
print("7. Solution")
uniqueCountry = df['Country_Region'].unique()
ctry_list=[]
confirmedSum_list=[]
for i in uniqueCountry:
    ctry= df.loc[df['Country_Region']==i]
    ctry_confirmed=pd.DataFrame(ctry, columns=[i,'Confirmed'])
    sum_confirmed=ctry_confirmed['Confirmed'].sum()
    ctry_list.append(i)
    confirmedSum_list.append(sum_confirmed)
data={'Country':ctry_list, 'Confirmed_Sum':confirmedSum_list}
country_confirmed = pd.DataFrame(data)
ctry_max=country_confirmed['Confirmed_Sum'].max()
df_ctry = country_confirmed.loc[country_confirmed['Confirmed_Sum'] == ctry_max]
print(df_ctry)
print("The country with the largest confirmed cases: US")


# # 8. Solution
print()
print("8. Solution")
df['Last_Update'] = pd.to_datetime(df['Last_Update'])
start_date = '2020-01-01 00:00:01'
end_date = '2020-12-31 11:59:59'
mask = (df['Last_Update'] > start_date) & (df['Last_Update'] <= end_date)
df = df.loc[mask]
#print(df) This line display all the cases for 2020
print('Number of cases in 2020: ' + str(len(df))) #This line give the number of cases