
from StageExtractor import EntityExtractor
import pprint

class Statistics(object):

    def get_post_block_data(self,filepath):
        extractor = EntityExtractor()
        elements = extractor.get_elements(filepath)

        post_content = extractor.get_all_entities(elements,'post','post',False)
        post_block_names = ['always','success','failure']

        post_elem_dict = []
        for name in post_block_names:
            post_dict = extractor.get_all_entities(post_content,name,name,True)
            
            post_elem_dict.append(post_dict)
        final_dict = {}
        for d in post_elem_dict:
            for key in d.keys():
                final_dict[key] = d[key]
        return final_dict



s = Statistics()
data = s.get_post_block_data('./sample.groovy')
print(data.keys())