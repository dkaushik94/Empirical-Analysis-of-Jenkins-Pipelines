from shlex import shlex
from pprint import pprint

class StageState:
    waiting, start_stage_name, stage_name ,end_stage_name, start_stage_block, stage_block, end_stage_block = range(7)

class StageExtractor(object):

    state = StageState.waiting
    current_stage_name = None
    stage_dict = {}
    
    def get_elements(self,filepath):
        elem_list = list(shlex(open(filepath)))
        return elem_list
    

    def get_all_stages(self,elements,pat_elem,name,return_dict):
        done_count = 0
        
        if name != None:
            self.current_stage_name = name
        for elem in elements:
            
            
            if   self.state == StageState.waiting:
                if elem == pat_elem:
                    if name != None:
                        self.state = StageState.end_stage_name
                        self.stage_dict[name] = []
                    else:
                        self.state = StageState.start_stage_name

                else:
                    continue
            
            elif self.state == StageState.start_stage_name:
                if elem == '(':
                    self.state = StageState.stage_name

            elif self.state == StageState.stage_name:
                self.stage_dict[elem] = []
                self.current_stage_name = elem
                self.state = StageState.end_stage_name

            elif self.state == StageState.end_stage_name:
                if elem == '{':
                    self.state = StageState.start_stage_block
                    done_count = done_count + 1
            
            elif self.state == StageState.start_stage_block:
                if elem == '}':
                    done_count = done_count - 1
                elif elem == '{':
                    done_count = done_count + 1
                if done_count == 0:
                    self.state = StageState.waiting
                    continue
                
                if self.current_stage_name != None:
                    content_list = self.stage_dict[self.current_stage_name]
                    content_list.append(elem)
                    self.stage_dict[self.current_stage_name] = content_list


            elif self.state == StageState.end_stage_block:
                self.state = StageState.waiting

        if not return_dict:
            content = self.stage_dict[self.current_stage_name]
            del self.stage_dict[self.current_stage_name]
        else:
            content = self.stage_dict
        return content
                



s = StageExtractor()
elems = s.get_elements('./jenkins_parallel.groovy')
content = s.get_all_stages(elems,'parallel','parallel',False)

# pprint(content)
meta_dict = s.get_all_stages(content,'stage',None,True)
pprint(meta_dict)
# aa_dict = s.get_all_stages(elems,'always','always',True)
# res = {'steps':meta_dict}
# print(aa_dict)
# pprint(res)

