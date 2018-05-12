from shlex import shlex
from pprint import pprint


# Used as an enum to hold all the states for parsing through the output of the lexer of Jenkinsfile
class EntityState:
    waiting, start_entity_name, entity_name ,end_entity_name, start_entity_block, entity_block, end_entity_block = range(7)

class EntityExtractor:

    """
        This class is used to extract content of code for a set of predefined patterns. For example, in Jenkinsfile, we 
        want to extract various patterns like : 

        steps {          
            ...          
            ...          
        }             

        stage ('...') {
            ...
        }

        parallel {
            stage ('...') {
                ...
            }

            stage ('...') {
                ...
            }
        }

        We specify the pattern in the input and the method in the class `get_all_entities` returns content present inside those code
        blocks specified in the input as patterns. This way, by exploiting the commonly occurring patterns in the Jenkinsfile,
        We can extract all sorts of statistics from ech Jenkinsfile to get insights.
    """
    
    state = EntityState.waiting
    current_entity_name = None
    entity_dict = {}
    
    def get_elements(self,filepath):
        '''
            Takes the Jenkinsfile path and returns the output
            of the lexer
        '''
        try:
            elem_list = list(shlex(open(filepath)))
            
        except:
            
            elem_list = []
        
        return elem_list
    

    def get_all_entities(self,elements,pat_elem,name,return_dict):
        '''
            This method returns content for a given pattern. It can return multiple occurances of the
            pattern too.
        '''
        
        # Done count is used to keep track of barckets and check 
        # if we need to consider the content being parsed or not
        done_count = 0
        self.entity_dict = {}
        
        # name is specified if pattern contains something like stage ('name'). In that case,
        # we need to record that name while parsing. If pattern is like steps { }, then
        # the name need not be specified and the method will take the starting point as the name
        if name != None:
            self.current_entity_name = name

        # We now loop through the output of the lexer. Based on the element and the state 
        # in which the parser is, we'll accept/reject the elements
        for elem in elements:    
            if   self.state == EntityState.waiting:
                if elem == pat_elem:
                    if name != None:
                        self.state = EntityState.end_entity_name
                        self.entity_dict[name] = []
                    else:
                        self.state = EntityState.start_entity_name

                else:
                    continue
            
            # Recognize the "("  in  --> " stage ( "
            elif self.state == EntityState.start_entity_name:
                if elem == '(':
                    self.state = EntityState.entity_name

            elif self.state == EntityState.entity_name:
                self.entity_dict[elem] = []
                self.current_entity_name = elem
                self.state = EntityState.end_entity_name

            # Recognize the "{"  in  --> " stage ( '##' ) {"
            elif self.state == EntityState.end_entity_name:
                if elem == '{':
                    self.state = EntityState.start_entity_block
                    done_count = done_count + 1
            
            # Recognize the "}"  in  --> " stage ( '##' ) { ### }"
            elif self.state == EntityState.start_entity_block:
                if elem == '}':
                    done_count = done_count - 1
                elif elem == '{':
                    done_count = done_count + 1
                if done_count == 0:
                    self.state = EntityState.waiting
                    continue
                
                if self.current_entity_name != None:
                    content_list = self.entity_dict[self.current_entity_name]
                    content_list.append(elem)
                    self.entity_dict[self.current_entity_name] = content_list

            # Go back to waiting state after recognizing the pattern
            elif self.state == EntityState.end_entity_block:
                self.state = EntityState.waiting

        # Returns either a dictionary or a list based on the return_dict param
        if not return_dict and self.entity_dict != {}:
            content = self.entity_dict[self.current_entity_name]
            del self.entity_dict[self.current_entity_name]
        else:
            content = self.entity_dict
        return content
                



