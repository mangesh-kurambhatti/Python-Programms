def fromkeys(input_dict,output_dict_values):
    result_dict={}
    
    if type(output_dict_values)==list or type(output_dict_values)==tuple:
        key_list=list(input_dict.keys())
        values_length=len(output_dict_values)
        
        for i in range(len(key_list)):
            if i<values_length:
                result_dict[key_list[i]]=output_dict_values[i]
            else:
                 result_dict[keys_list[i]]=None
    else:
        result_dict=dict.fromkeys(input_dict,output_dict_values)


    print(result_dict)

def main():

    input_dict={1:1,2:2,3:3}
    output_dict_values=[100,101,102]

    fromkeys(input_dict,output_dict_values)

if __name__=='__main__':
    main()

'''
    {1:1,2:2,3:3}
    [100,200,300]

    output should 

    {1:100,2:200,3:300}
'''
