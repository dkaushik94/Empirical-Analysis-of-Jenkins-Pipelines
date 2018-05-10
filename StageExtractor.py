from shlex import shlex
from pprint import pprint

class EntityState:
    waiting, start_entity_name, entity_name ,end_entity_name, start_entity_block, entity_block, end_entity_block = range(7)

class EntityExtractor(object):

    state = EntityState.waiting
    current_entity_name = None
    entity_dict = {}
    
    def get_elements(self,filepath):
        elem_list = list(shlex(open(filepath)))
        return elem_list
    

    def get_all_entities(self,elements,pat_elem,name,return_dict):
        done_count = 0
        self.entity_dict = {}
        
        if name != None:
            self.current_entity_name = name
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
            
            elif self.state == EntityState.start_entity_name:
                if elem == '(':
                    self.state = EntityState.entity_name

            elif self.state == EntityState.entity_name:
                self.entity_dict[elem] = []
                self.current_entity_name = elem
                self.state = EntityState.end_entity_name

            elif self.state == EntityState.end_entity_name:
                if elem == '{':
                    self.state = EntityState.start_entity_block
                    done_count = done_count + 1
            
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


            elif self.state == EntityState.end_entity_block:
                self.state = EntityState.waiting

        if not return_dict:
            content = self.entity_dict[self.current_entity_name]
            del self.entity_dict[self.current_entity_name]
        else:
            content = self.entity_dict
        return content
                



s = EntityExtractor()
elems = s.get_elements('./sample.groovy')
# content = s.get_all_entities(elems,'post','post',False)

# pprint(content)
meta_dict = s.get_all_entities(elems,'stage',None,True)
pprint(meta_dict)
# aa_dict = s.get_all_entities(elems,'always','always',True)
# res = {'steps':meta_dict}
# print(aa_dict)

# succ_dict = s.get_all_entities(elems,'success',None,True)
# print(succ_dict)
# pprint(res)

