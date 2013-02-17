import random,string
import globaltable

features = ('large_screen_size' , 'medium_screen_size', 'small_screen_size', 'camera','flash_support','media_queries' , 'geolocation','app_cache','local_storage')
screen_size=('large_screen_size','medium_screen_size','small_screen_size')

"""
the gen_table fun is used to generate a test database
and stores it in file database.txt 
"""
def gen_table(rec):
        list_of_enteries=[]
        wfile = open("database.txt","w")
        for i in range(rec) :
                d={}            #list of dictionaries representing database
                url = 'www.' + ''.join(random.sample(string.letters,random.randint(10,15)))+random.choice(('.com','.org','.edu','.net'))
                d['url']= url
                d['large_screen_size'] = True    #it is assumed that every url supports large_screen_size(ie PC) 
                for j in range(1,9) :
                        d[features[j]] = random.choice((True,False))
                d['media_queries'] = d[features[1]] or d[features[2]]   #media query is true if any other screen size apart from large is also supported 
                list_of_enteries.append(d)
                for each in d.keys() :  #writing the test database to a file
                        wfile.write(str(each)+' : '+str(d[each])+'  ')
                wfile.write('\n')
        return list_of_enteries         


'''
Resolves the query depending on whether constraint is tuple or not
A keyError exception is handled when invalid fields are entered in the query
'''
def resolve_query(find,constraint) :
        try :
                d = {'screen_size':screen_size,'features':features} #dict of aliases
                if (len(constraint) == 1) and (constraint.keys()[0] in d.keys()) : #To handle cases where constraint is a tuple               
                        cond = constraint.keys()[0]
                        cons = d[cond]
                        result={}    #dict containing results of the query
                        row=None	
                        for each in globaltable.list_of_enteries:
                                if each['url']==find[0]:
                                        row = each
                                        break
                        if row is None:
                                return 'no such url'
                        for i in cons:
                                if row[i]==constraint[cond]:
                                        result[i] = row[i]			
                        return result
                
                else:
                        rows=[]
                        cons = constraint.keys() 
                        for elem in globaltable.list_of_enteries:       
                                add = True
                                for con in cons :
                                        if elem[con] != constraint[con]:
                                                add = False
                                                break
                                if add :                                        #adding the field to result if value is what is mensioned in the query
                                        row={}
                                        for select in find :
                                                row[select] = elem[select]
                                        rows.append(row)
                        return rows
        except KeyError as k:
                print 'check your query no such field in table',k


'''
the query function is used to split up the query into requirements and constraints format
and pass the the constraints as key value pairs
'''
def query(stmt):
        
	line = stmt.split(':')          #separating requirements and constraints
	find = line[0].split(',')       
	for i in range(0,len(find)):
                find[i] = find[i].strip()
	constraint ={}
	if len(line) > 1 :
                cons = line[1].split(',')
                for con in cons :
                        key,val = con.split('-')
                        key = key.strip()
                        val = val.strip()
                        if val.lower() == 'true' :      #making true/false case insensitive
                                val = True
                        elif val.lower() == 'false':
                                val = False
                        constraint[key] = val      
	return resolve_query(find,constraint)



        
