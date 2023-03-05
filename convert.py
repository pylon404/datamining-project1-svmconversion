import pandas


def main(): 
    df_training = pandas.read_excel('Testing dataset.xlsx')
    df_training = df_training.drop(columns=['Unnamed: 0'])
    
    output_file = open("testing_data.txt", "w")
    output = ""
    prechange = ""
    input_file = df_training.to_csv(None,' ','',None,header=False)
    modifiable_list = input_file.split('\n')
    #A counter since I didn't feel like enumerating modifiable_list
    i = 0
    for index in modifiable_list:
        remade_line = ""
        
        if len(index) != 0:
            chars = index.split()
            chars[0] = ''
            if chars[1] == '0':
                chars[1] = '-1'
            for c in enumerate(chars):
                if c[0] > 0:
                    prechange = c[1]
                    changed = ""
                if c[0] > 1:
                    changed = " " + str(c[0]-1) + ":" + prechange
                    # chars[int(c[1])] = changed
                else:
                    changed = "" + str(c[1])
                    if c[0] != 0:
                        changed += " "
                
                #Remake the line (index in modifiable_list) 
                remade_line += changed
        
        #if chars[1] == '1':
        #    index += " #1"
        #if chars[1] == '0':
        #    index += " #2"
        #After converting all characters in the line, replace index in modifiable_list
        index = remade_line
        modifiable_list[i] = index
        output += index + "\n"
        i = i+1
    
    sep = ""
    tail = ""
    output, sep, tail = output.rpartition('\n\n')
        
    output_file.write(output)


if __name__ == "__main__": 
    main()