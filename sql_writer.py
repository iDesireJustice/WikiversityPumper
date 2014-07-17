#functions which will write the queries

def text_writer(file_name ,txt):
	file_obj = open(file_name, 'w')
	file_obj.write(txt)
	file_obj.close()
# End of text_writer

def sql_parsing(file_name):
	file_obj = open(file_name)
	lines = file_obj.readlines()
	print lines
	file_obj.close()
	return lines	

#end of sql parsing

def inject_challenges(table_name):
	print "Starting " + str(table_name) + " challenge query"
  
	table_creation = "ALTER TABLE " + str(table_name) + "AUTO_INCREMENT = 1;"
	table_insertion = "insert into " + str(table_name)
	table_parameters = "(challengeName,points,mentor,description,multi_uni,deadline)" + " VALUES" 
	insert_query = table_creation + table_insertion + table_parameters
  
  
  
#end of inject challenges


#main 
list_tables = ['Android_Challenges.table','Assembly_Challenges.table','Blender_3D_Challenges.table','C_Challenges.table',
		'CPP_Challenges.table','Encryption_Challenges.table','HTML_Challenges.table','Linux_Challenges.table',
		'Math_Challenges.table','PHP_Challenges.table','Python_Challenges.table','Resources_Challenges.table',
		'Reversing_Challenges.table','Security_Challenges.table','Thinking_Challenges.table']
		
		
