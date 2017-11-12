import os
from ..utils import BasicSegment

def add_docker_machine_segment(powerline):
	if os.getenv('DOCKER_MACHINE_NAME'):
		powerline.append(' %s ' % os.getenv('DOCKER_MACHINE_NAME'), powerline.theme.DOCKER_MACHINE_FG, powerline.theme.DOCKER_MACHINE_BG)

class Segment(BasicSegment):
		def add_to_powerline(self):
			add_docker_machine_segment(self.powerline)