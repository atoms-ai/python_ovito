#!/bin/bash
#SBATCH -p debug
#SBATCH -n 1


	unset DISPLAY
	/home/sas15102/OVITO/ovito-3.0.0-dev456-x86_64/bin/ovitos ov_render11000.py
