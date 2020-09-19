import csv

def major_handle():
        
    input = open(r'major.csv', 'r')
    p = open(r'province.csv', 'r')
    output = open(r'major_output.csv', 'a', newline='')
    
    data = csv.reader(input)
    p_data = csv.reader(p)
    writer = csv.writer(output)
    
    subject = ['文科', '理科', '全科']
    province = []
    
    for i in p_data:
        province.append(i[1])
    p.close()
    
    print(province)
    
    j = 0
    for i in data:
    
        arr = i[:]
        
        #major + m
        arr[0] = arr[0].replace('Unnamed: ','')
        if int(arr[0]) == 0:
            writer.writerow(arr)
            continue
        arr[0] = 'm' + str(arr[0])
        
        #college + c
        arr[1] = 'c' + str(arr[1])
        
        #province convert
        if arr[3].isdigit() == False:
            for pro in province:
                if pro in arr[3]:
                    arr[3] = 'p' + str(province.index(pro))
        else:
            arr[3] = 'p' + str(arr[3])
        
        #subject convert
        arr[4] = 's' + str(subject.index(arr[4]) + 1)
        
        
        #disambiguated dealing
        if arr[-2].find(';')>=0:
            major = arr[-2]
            ID = arr[-1]
            
            arr_major = major.split(';')
            arr_ID = ID.split(';')
            
            for flag in range(len(arr_major)):
                arr[-2] = arr_major[flag]
                arr[-1] = arr_ID[flag]
    
        else:
            arr[-1] = arr[-1][:-1]
            
        writer.writerow(arr)    
        #print(arr)  
            
        j += 1
        if j%5000 == 0:
            print(j)
    
    input.close()
    output.close()       
            
def college_handle():
     input = open('college.csv', 'r')
     output = open('college_improved.csv', 'a', newline='')
     
     data = csv.reader(input)
     writer = csv.writer(output)
     
     for i in data:
         arr = i[:]
         if arr[0].isdigit() == False:
             writer.writerow(arr)
             continue
         
         arr[0] = 'p' + str(arr[0])
         arr[-1] = 'c' + str(arr[-1])
         
         writer.writerow(arr)
         
    input.close()
    output.close()
    

if __name__ == '__main__':
    major_handle()
    college_handle()