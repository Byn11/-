from os import path,mkdir,walk,listdir
import datetime
import logic,batch_print,keyword_search
def showfile(searchpath):
    isexist={}
    item_list=['GDPS','MCDS','CGFAIL','DSPL','SMSSGCHK','STORAGE','RMFSUM']
    for item in item_list:
        if item=='STORAGE':
            temp_path1=searchpath+'/'+item+'/'+item+'1.txt'
            temp_path2=searchpath+'/'+item+'/'+item+'2.txt'
            isexist[item]=path.exists(temp_path1) and path.isfile(temp_path1) and path.exists(temp_path2) and path.isfile(temp_path2)
        else:
            temp_path=searchpath+'/'+item+'/'+item+'.txt'
            isexist[item]=path.exists(temp_path) and path.isfile(temp_path)
    return isexist

def generator(generate_boolean_dict,input_file_root,output_file_root,rmfsum_last_week):
    now_time=datetime.datetime.today()
    #generate_boolean_dict={'GDPS':True,'MCDS':True,'CGFAIL':True,'DSPL':True,'SMSSGCHK':True,'STORAGE':True,'RMFSUM':True}
    #print('please input the output folder root')
    #output_file_root=input()
    #output_file_root='C:/vscode_workspace\项目组相关\CAPA/txt_input'
    output_folder_path=output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング'
    if not path.exists(output_folder_path) or not path.isdir(output_folder_path):
        mkdir(output_folder_path)
    msg=[]
    if generate_boolean_dict['GDPS']:
        flag=True
        
        for _,_,filelist in walk(output_folder_path):
            for filename in filelist:
                if 'GDPS' in filename:
                    msg.append('GDPSファイルが既に存在するので、生成が失敗した！！！')
                    flag=False
        if flag:
            try:
                logic.GDPS(input_file_root+'/GDPS/GDPS.txt','excel_input/mmdd1_mmdd2_GDPS.xlsx',output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング/')
                msg.append('GDPS 生成が成功した！！！')
            except Exception as e:
                msg.append('GDPS 生成が失敗した！！！')
            
    if generate_boolean_dict['MCDS']:
        flag=True
        for _,_,filelist in walk(output_folder_path):
            for filename in filelist:
                if 'MCDS' in filename:
                    msg.append('MCDSファイルが既に存在するので、生成が失敗した！！！')
                    flag=False
        if flag:
            try:
                logic.MCDS(input_file_root+'/MCDS/MCDS.txt','excel_input/mmdd_MCDS.xlsx',output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング/')
                msg.append('MCDS 生成が成功した！！！')
            except Exception as e:
                msg.append('MCDS 生成が失敗した！！！')

    if generate_boolean_dict['CGFAIL']:
        flag=True
        for _,_,filelist in walk(output_folder_path):
            for filename in filelist:
                if 'CGFAIL' in filename:
                    msg.append('CGFAILファイルが既に存在するので、生成が失敗した！！！')
                    flag=False
        if flag:
            try:
                logic.CGFAIL(input_file_root+'/CGFAIL/CGFAIL.txt','excel_input/mmdd1_mmdd2_CGFAIL.xlsx',output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング/')            
                msg.append('CGFAIL 生成が成功した！！！')
            except Exception as e:
                msg.append('CGFAIL 生成が失敗した！！！')
    if generate_boolean_dict['DSPL']:
        flag=True
        for _,_,filelist in walk(output_folder_path):
            for filename in filelist:
                if 'DSPL' in filename:
                    msg.append('DSPLファイルが既に存在するので、生成が失敗した！！！')
                    flag=False
        if flag:
            try:
                logic.DSPL(input_file_root+'/DSPL/DSPL.txt','excel_input/mmdd1_mmdd2_DSPL.xlsx',output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング/')
                msg.append('DSPL 生成が成功した！！！')
            except Exception as e:
                msg.append('DSPL 生成が失敗した！！！')

    if generate_boolean_dict['SMSSGCHK']:
        flag=True
        for _,_,filelist in walk(output_folder_path):
            for filename in filelist:
                if 'SMSSGCHK' in filename:
                    msg.append('SMSSGCHKファイルが既に存在するので、生成が失敗した！！！')
                    flag=False
        if flag:
            try:
                logic.SMSSGCHK(input_file_root+'/SMSSGCHK/SMSSGCHK.txt','excel_input/mmdd1_mmdd2_SMSSGCHK.xlsx',output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング/')
                msg.append('SMSSGCHK 生成が成功した！！！')
            except Exception as e:
                msg.append('SMSSGCHK 生成が失敗した！！！')

    if generate_boolean_dict['STORAGE']:
        flag=True
        for _,_,filelist in walk(output_folder_path):
            for filename in filelist:
                if 'STORAGE' in filename:
                    msg.append('STORAGEファイルが既に存在するので、生成が失敗した！！！')
                    flag=False
        if flag:
            try:
                logic.STORAGE(input_file_root+'/STORAGE','excel_input/mmdd1_mmdd2_STORAGE.xlsx',output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング/')
                msg.append('STORAGE 生成が成功した！！！')
            except Exception as e:
                msg.append('STORAGE 生成が失敗した！！！')

    if generate_boolean_dict['RMFSUM']:
        flag=True
        for _,_,filelist in walk(output_folder_path):
            for filename in filelist:
                if 'RMFSUM' in filename:
                    msg.append('RMFSUMファイルが既に存在するので、生成が失敗した！！！')
                    flag=False
        #rmfsum_last_week=input('please input RMFSUM file last week')
        if flag:
            try:
                logic.RMFSUM(input_file_root+'/RMFSUM/RMFSUM.txt','excel_input/mmdd1_mmdd2_RMFSUM.xlsx',rmfsum_last_week,output_file_root+'/'+str(now_time)[2:10].replace('-','')+'モニタリング/')
                msg.append('RMFSUM 生成が成功した！！！')
            except Exception as e:
                msg.append('RMFSUM 生成が失敗した！！！')
    now_time1=datetime.datetime.today()
    delta=now_time1-now_time
    msg.append('****************************************************')
    msg.append('今回の生成は'+str((delta.seconds//60) % 60)+'分'+str(delta.seconds%60)+'秒がかかりました')
    return msg

def printconnect(input_folder_path):
    msg=batch_print.printfolder(input_folder_path)
    return msg

def browser(input_path):
    try:
        excel_files = [f for f in listdir(input_path) if f.endswith(".xlsx")]
        return '\n'.join(excel_files)
    except Exception as e:
        return ''
def gen_keywordfile(text_path,output_path):
    
    keyword_search.fileloop(text_path,output_path)
