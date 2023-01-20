from chemspace_vis.preprocess import preprocess_chembl, make_tsne_from_fingerprints
from chemspace_vis.visualizer import make_visualizer_script


def preprocess_part1():

	# From downloaded ChEMBL .csv, generate a text file with Smiles and ChEMBL IDs and a dataframe
	# with the desired activity
	chembl_csv = "mor_chembl_emax.csv"

	activity_name = "Emax" # The text name of the activity (in this case, Emax)

	# Optional arguments specify heavy atom count (hac) and molecular weight (mw) filters, and
	# the folder where images of each molecule will be written (default is "mol_images")
	preprocess_chembl(chembl_csv, activity_name, max_hac=35, max_mw=600, img_folder="mol_images")

	# preprocess_chembl will generate two files, with the same name as the chembl_csv file but
	# a .smi extension for the Smiles file and _activity.df extension for the activity dataframe.
	# These can be overridden with the smi_fn and df_fn optional arguments


def preprocess_part2():
	fingerprints_file = "mor_chembl_emax.fp"

	# This computes tSNE from the fingerprints, which is saved in "tsne_data.df" by default
	# (can be changed with out_filename argument)
	make_tsne_from_fingerprints(fingerprints_file)

	# This will write the script for the interactive plot with molecule images. When the optional
	# activity_filename is iven, the points will be colored according to the measured activity. 
	# The script will be called visualizer_script.py and will be located in the current directory.
	make_visualizer_script("tsne_data.df", "mol_images",
						   activity_filename="mor_chembl_emax_activity.df", use_log10=False)



if __name__ == "__main__":
	preprocess_part1()

	# Before running part2, you need to compute the ECFP fingerprints from the generated .smi file.
	# See wiki page here for instructions:
	# https://wiki.docking.org/index.php?title=Interactive_ligands_visualizer

	# UCOMMENT following line when you have the fingerprints file:

	# preprocess_part2() # <------ UNCOMMENT

	# When done running preprocessing, just execute the generated visualizer_script.py to launch the
	# visualization.

