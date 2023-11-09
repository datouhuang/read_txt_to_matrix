import numpy as np

row=32
data_in=1  #1：bpc output file;  0:bpc input file
mirror_flip=0 #{flip, mirror}

if (data_in==1):
    if (row==32):
        if (mirror_flip==0):
            file_name='test_matrix_3264_32_out.txt'
            write_file='test_3264_32_out_0.txt'
        elif (mirror_flip==1):
            file_name='test_matrix_mirror_3264_32_out.txt'
            write_file='test_mirror_3264_32_out_0.txt'
        elif (mirror_flip==2):
            file_name='test_matrix_flip_3264_32_out.txt'
            write_file='test_flip_3264_32_out_0.txt'
        else:
            file_name='test_matrix_mirror_flip_3264_32_out.txt'
            write_file='test_mirror_flip_3264_32_out_0.txt'
else:
    if (row==32):
        file_name='test_matrix_3263_32_in.txt'
        write_file='test_3264_32_in.txt'


# 32 out
# file_name='data_file_32/matrix_bpc_mirror_3264_32_out.txt'
# write_file='data_file_32/bpc_mirror_3264_32_out.txt'
# 32 in
# file_name='data_file/eroded_NRBPC_3264_32_2.txt'
# write_file='data_file/data_3264_32_in.txt'
# 2448 out
# file_name='data_file_2448/matrix_bpc_3264_2448_out.txt'
# write_file='data_file_2448/bpc_3264_2448_out.txt'
# 2448 in
# file_name='data_file_2448/eroded_NRBPC_3264_2448_2.txt'
# write_file='data_file_2448/bpc_3264_2448_in.txt'

#打开文件
# file=open(file_name, 'r')

#读取文件
# content=file.read()
def file2array(path, delimiter=' '):     # delimiter是数据分隔符
    fp = open(path, 'r', encoding='utf-8')
    string = fp.read()              # string是一行字符串，该字符串包含文件所有内容
    fp.close()
    row_list = string.splitlines()  # splitlines默认参数是‘\n’
    data_list = [[float(i) for i in row.strip().split(delimiter)] for row in row_list]
    return np.array(data_list)
 
data = file2array(file_name)
print(data)
print("data's shape", data.shape)

[row, col] = data.shape

data_out=data.reshape(row*col,1)

#关闭文件
# file.close()

np.savetxt(write_file, data_out, fmt='%i')

print('矩阵成功写入')

