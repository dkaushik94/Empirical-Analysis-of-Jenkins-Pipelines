import unittest
from Statistics import Statistics
import os

class Statistics_Test(unittest.TestCase):
    stat = Statistics()

    def test_get_post_block_data(self):
        os.chdir('./Test_files/')
        self.assertNotEqual(self.stat.get_post_block_data('post_block_file'),{})
        os.chdir('../')

    def test_get_post_block_statistics(self):
        os.chdir('./Test_files/')
        self.assertNotEqual(self.stat.get_post_block_statistics('post_block_file'),{})
        os.chdir('../')

    def test_get_stage_data(self):
        os.chdir('./Test_files/')
        self.assertNotEqual(self.stat.get_stage_data('post_block_file'),{})
        os.chdir('../')

    def test_get_triggers_and_stages(self):
        os.chdir('./Test_files/')
        self.assertNotEqual(self.stat.get_triggers_and_stages('trigger_file'),(0,0))
        os.chdir('../')

    def test_get_trigger_statistics(self):
        self.stat.get_trigger_statistics()
        self.assertNotEqual(self.stat.statistics_dict['Correlation_of_num_triggers_to_avg_num_of_stages'],{})

    def test_get_post_block_correlation_statistics(self):
        self.stat.get_post_block_correlation_statistics()
        self.assertNotEqual(self.stat.statistics_dict['Do_different_post_blocks_indicate_more_stages?'],{})
    
    def test_consolidate_post_block_statistics(self):
        self.stat.consolidate_post_block_statistics()
        self.assertNotEqual(self.stat.statistics_dict['What_are_the_most(least)_frequent_post_condition_blocks?'],{})

    def test_get_parallel_block_statistics(self):
        self.stat.get_parallel_block_statistics()
        self.assertNotEqual(self.stat.statistics_dict['Do_files_with_parallel_blocks_have_more_stages?'],{})

    def test_get_timeout_stats(self):
        self.stat.get_timeout_stats('./Jenkinsfiles/')
        self.assertNotEqual(self.stat.statistics_dict['Various_statistics_of_timeouts'],{})

    def test_build_tool_stats(self):
        self.stat.build_tool_stats('./Jenkinsfiles/')
        self.assertNotEqual(self.stat.statistics_dict['What_are_the_most_used_build_tools?'],{})

if __name__ == '__main__':
    unittest.main()