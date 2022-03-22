#!/bin/bash
#SBATCH -p debug
#SBATCH -n 1


	unset DISPLAY
	/users/sumit/softwares/ovito/ovito-pro-3.7.2-x86_64/bin/ovitos ov_render11000.py
