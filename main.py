import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)

class ServiceRunner(dl.BaseServiceRunner):

    def move_item(self, item):
        # Get dataset
        dataset = item.dataset

        dataset.items.make_dir(directory="/Faas")
        dst_folder = '/Faas'
        item.move(new_path=dst_folder)

        print('Successfully move all items to new dir')


