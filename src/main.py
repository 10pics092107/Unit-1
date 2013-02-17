from folder import unit1main
from folder import globaltable
import sys

if __name__=='__main__':
        a=True
        while a:
                no_entries=raw_input('specify the number of entries (range 1-100) in the database\n')
                if no_entries=='' or no_entries.isalpha() :
                        print 'Invalid entry \nExiting ...'
                        sys.exit()
                no_entries = int(no_entries)
                if no_entries < 0 or no_entries > 100:
                        print 'invalid no_entries',no_entries
                        print 'enter again \n'
                        a=True
                else:
                        a=False
        globaltable.list_of_enteries = unit1main.gen_table(int(no_entries))


        continu = 'y'

        while continu == 'y' : 
                input = raw_input('Enter the query : \n\n')
                if input  =='':
                        print'no query asked \nexiting...\n'
                        sys.exit()
                        
                result = unit1main.query(input) 
                
                print 'result for the query is : \n\n', result
                continu = raw_input('do you want to continue (y/n) :\n')

        
