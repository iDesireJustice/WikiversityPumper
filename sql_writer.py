#functions which will write the queries
import re

def text_writer(file_name ,txt):
	file_obj = open(file_name, 'w')
	file_obj.write(txt)
	file_obj.close()
# End of text_writer

def sql_parsing(file_name):
    file_obj = open(file_name)
    array = []
    for line in file_obj:
        array.append(line)
    file_obj.close()
    array = array[1:len(array)] #get a sublist from the list, because we don't need the first line of tables
    string_return = ""
    for i in range(len(array)):
            begin_str = '('
            end_str = '),'
            final_str = ');'
            temp_string = array[i]
            tmp_list = re.split('\t',temp_string)
            #print tmp_list
            tmp_list = tmp_list[1:len(tmp_list)-1]
            for j in range(len(tmp_list)):
            	begin_str = begin_str + tmp_list[j]
            	if(j+2 != len(tmp_list)):
            		begin_str = begin_str + ','
            #end of first line, adding the ending if necessary
            if(i+1 != len(array)): #not last value
            	begin_str = begin_str + '),\n'
            else:
            	begin_str = begin_str + ');\n'
            #print begin_str
            string_return = string_return + begin_str
    return string_return
#end of sql parsing

def inject_challenges(table_name):
	print "Starting " + str(table_name) + " challenge query"
  
	table_creation = "ALTER TABLE " + str(table_name) + "AUTO_INCREMENT = 1;\n"
	table_insertion = "insert into " + str(table_name)
	table_parameters = "(challengeName,points,mentor,description,multi_uni,deadline)" + " VALUES\n" 
	insert_query = table_creation + table_insertion + table_parameters
	print "Creating File"
	text = insert_query+sql_parsing(table_name)
	table_name += '.sql'
	text_writer(table_name,text)
  
#end of inject challenges


#main 
list_tables = ['Android_Challenges.table','Assembly_Challenges.table','Blender_3D_Challenges.table','C_Challenges.table',
		'CPP_Challenges.table','Encryption_Challenges.table','HTML_Challenges.table','Linux_Challenges.table',
		'Math_Challenges.table','PHP_Challenges.table','Python_Challenges.table','Resources_Challenges.table',
		'Reversing_Challenges.table','Security_Challenges.table','Thinking_Challenges.table']
		
inject_challenges("Python_Challenges.table")	
