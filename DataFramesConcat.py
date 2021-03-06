import pandas as pd

# filenames
excel_names = ["DiscoverWordCountFinal.xlsx", "DiscoverTFIDFCount.xlsx", "DiscoverTextRank.xlsx", "SuntrustWordCountFinal.xlsx", "SuntrustTFIDFCount.xlsx", "SuntrustTextRank.xlsx"]

# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them..
combined = pd.concat(frames)

# write it out
combined.to_excel("FinTechDataFrame.xlsx", header=False, index=False)

'''

def combine(indir = '/Users/Nidhi/PycharmProjects/dataScience', outdir = '/Users/Nidhi/PycharmProjects/dataScience/FinalDataFrame'):
    


dataframe = pd.DataFrame()
for f in ['DiscoverResult.xlsx','SuntrustResult.xlsx' ]:
    data = pd.read_excel(f, 'DraftDataframe')
    dataframe = dataframe.append(data)
dataframe = pd.concat(dataframe)


'''
