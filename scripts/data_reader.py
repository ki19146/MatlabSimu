# THIS IS FOR READING DATA FROM EXCEL AND RETURN IT FOR USING
import chardet
import pandas as pd
import os


# READ CSV FILE IN DATA FRAME
#获取当前目录
current_dir = '/Users/tia/PycharmProjects/MatlabSimu/data'

fileList = []
#遍历当前目录
for filename in sorted(os.listdir(current_dir)):
#判断是否为文件
	if os.path.isfile(os.path.join(current_dir, filename)) and filename.endswith(".csv"):
		print('\"',filename,'\"',sep="")
		fileList.append(filename)

print(fileList)

# DEFINE draw FUNCTION TO GET ENCODING & NUMPY ARRAY
def draw(filepath):
	with open(filepath, 'rb') as f:
		result = chardet.detect(f.read())
		df = pd.read_csv(filepath, skiprows=5, encoding=result['encoding'])
		# print(filepath)
		F = df.dropna(axis=1, how='all').values   # CONVERT DATA FRAME TO NUMPY ARRAY
		return F

# READ DATA
F = draw('/Users/tia/PycharmProjects/MatlabSimu/data/SQP305098_F_11.csv')
print(F)
rows, cols = F.shape
print(rows, cols)
B = draw('/Users/tia/PycharmProjects/MatlabSimu/data/SQP305098_B_11.csv')
T = draw('/Users/tia/PycharmProjects/MatlabSimu/data/SQP305098_T_11.csv')





