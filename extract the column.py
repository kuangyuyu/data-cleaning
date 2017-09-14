#coding=utf-8
import numpy 
import csv
def test(src, dst, index):  
    with open(dst, 'wb') as df:  
        with open(src, 'rb') as csvfile:  
  
            # 使用reader函数，接收一个可迭代的对象  
            reader = csv.reader(csvfile)
             
            #读取第二列的内容
           # column=[row[3] for row in reader]
            # 列表解析  
            for row in reader:
            #print row[3],row[21]
            
            	column = [row[3],row[21]]
                #fileHeader=["Title","PrimaryCategoryName"]
                # 执行写操作 
               # writer.writerow(fileHeader)
                writer = csv.writer(df) 
                writer.writerow(column)  

  
  #the first csv is the original read file,and the second csv is the last written saved file.
if __name__ == "__main__":  
      test('s_finditemsbystores.csv', 'test.csv', 0)  
