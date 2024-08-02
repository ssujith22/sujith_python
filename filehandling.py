'''
#we need to create file as sample with data
f_sample = open("sample.txt")
read_content = f_sample.read();
print(read_content)
f_sample.close()


#new file will create as demo
f_demo = open("demo.txt",'w') #new write
#f_demo = open("demo.txt",'a') #append
f_demo.write("programming in python by parag joshi\n")
f_demo.write("topics covered \n")
f_demo.write("datatypes,modules,control flow \n");
f_demo.write("*"*70)
f_demo.close();
'''

import csv
with open('portfolio.csv',mode='w',newline='') as pfile:
    pfile_writer = csv.writer(pfile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    #pfile_writer.writerow("Portfolio List,Parag Joshi") 
    pfile_writer.writerow(['Stock NAme','Quantity','Stock Price'])
    pfile_writer.writerow(['Infosys',10,2700])
    pfile_writer.writerow(['TCS',2,3000])

with open('portfolio.csv',mode='r') as pfile:
    csv_reader = csv.reader(pfile,delimiter= ",")
    line_count = 0;
    for row in csv_reader:
        if line_count ==0:
            print(f'{",".join(row)}')
            line_count +=1;
        else:
            print(f'{row[0]}\t{row[1]}\t{row[2]}')
            line_count +=1;
    print(f'Read {line_count-1} shares from the portfolio')

'''
import csv #this line we need to give so that it will run below block
data = [
        ['Name','Age','City'],
        ['Parag Joshi','40','Pune,Maharashtra'],
        ['Jane Smith','25','Mumbai']
    ]
with open('output.csv','w',newline='') as f:
        writer = csv.writer(f,quotechar="'",quoting=csv.QUOTE_ALL);
        writer.writerows(data)
'''
