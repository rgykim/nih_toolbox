"""
Robert Kim
Python 3
"""

import glob
import numpy as np
import os
import os.path as op
import pandas as pd


def main():
	templateHeader = list(pd.read_csv(template))

	reference = [	# variable, csv_file, row, column
		['subject_id', 'Registration Data', 0, 1],
		['nih_age', 'Registration Data', 3, 1],
		['nih_education', 'Registration Data', 4, 1],
		['nih_momeducation', 'Registration Data', 5, 1],
		['nih_gender', 'Registration Data', 9, 1],
		['nih_handedness', 'Registration Data', 10, 1],
		['nih_race', 'Registration Data', 11, 1],
		['nih_ethnicity', 'Registration Data', 12, 1],
		['nih_picvocab_theta', 'Assessment Scores', 5, 1],
		['nih_picvocab_se', 'Assessment Scores', 7, 1],
		['nih_picvocab_itemcount', 'Assessment Scores', 8, 1],
		['nih_picvocab_uncorr', 'Assessment Scores', 17, 1],
		['nih_picvocab_agecorr_stand', 'Assessment Scores', 18, 1],
		['nih_picvocab_fullycorr_tscore', 'Assessment Scores', 19, 1],
		['nih_readrecog_theta', 'Assessment Scores', 5, 2],
		['nih_readrecog_se', 'Assessment Scores', 7, 2],
		['nih_readrecog_itemcount', 'Assessment Scores', 8, 2],
		['nih_readrecog_uncorr', 'Assessment Scores', 17, 2],
		['nih_readrecog_agecorr_stand', 'Assessment Scores', 18, 2],
		['nih_readrecog_fullycorr_tscore', 'Assessment Scores', 19, 2],
		['nih_sortingmem_raw', 'Assessment Scores', 4, 3],
		['nih_sortingmem_itemcount', 'Assessment Scores', 8, 3],
		['nih_sortingmem_uncorr', 'Assessment Scores', 17, 3],
		['nih_sortingmem_agecorr', 'Assessment Scores', 18, 3],
		['nih_sortingmem_fullycorr_tscore', 'Assessment Scores', 19, 3],
		['nih_patterncom_speed_raw', 'Assessment Scores', 4, 4],
		['nih_patterncom_speed_itemcount', 'Assessment Scores', 8, 4],
		['nih_patterncom_speed_computed_score', 'Assessment Scores', 16, 4],
		['nih_patterncom_speed_uncorr', 'Assessment Scores', 17, 4],
		['nih_patterncom_speed_agecorr', 'Assessment Scores', 18, 4],
		['nih_patterncom_speed_fullycorr_tscore', 'Assessment Scores', 19, 4],
		['nih_picseqmem_raw', 'Assessment Scores', 4, 5],
		['nih_picseqmem_theta', 'Assessment Scores', 5, 5],
		['nih_picseqmem_se', 'Assessment Scores', 7, 5],
		['nih_picseqmem_itemcount', 'Assessment Scores', 8, 5],
		['nih_picseqmem_computed', 'Assessment Scores', 16, 5],
		['nih_picseqmem_uncorr', 'Assessment Scores', 17, 5],
		['nih_picseqmem_agecorr', 'Assessment Scores', 18, 5],
		['nih_picseqmem_fullycorr_tscore', 'Assessment Scores', 19, 5],
		['nih_flanker_raw', 'Assessment Scores', 4, 6],
		['nih_flanker_itemcount', 'Assessment Scores', 8, 6],
		['nih_flanker_computed', 'Assessment Scores', 16, 6],
		['nih_flanker_uncorr', 'Assessment Scores', 17, 6],
		['nih_flanker_agecorr', 'Assessment Scores', 18, 6],
		['nih_flanker_fullycorr_tscore', 'Assessment Scores', 19, 6],
		['nih_cardsort_raw', 'Assessment Scores', 4, 7],
		['nih_cardsort_itemcount', 'Assessment Scores', 8, 7],
		['nih_cardsort_computed', 'Assessment Scores', 16, 7],
		['nih_cardsort_uncorr', 'Assessment Scores', 17, 7],
		['nih_cardsort_agecorr', 'Assessment Scores', 18, 7],
		['nih_cardsort_fullycorr_tscore', 'Assessment Scores', 19, 7],
		['nih_audverbal_raw', 'Assessment Scores', 4, 12],
		['nih_audverbal_itemcount', 'Assessment Scores', 8, 12],
		# RAVLTT1, RAVLTT2, and RALTT3 have variable cell coordinates based on subject performance
		# these values will be appended later at the end during output generation
		# ['nih_audverbal_ravltt1', 'Assessment Data', 10, 2XX],
		# ['nih_audverbal_ravltt2', 'Assessment Data', 10, 2XX],
		# ['nih_audverbal_raltt3', 'Assessment Data', 10, 2XX],
		['nih_oralsym_raw', 'Assessment Scores', 4, 13],
		['nih_oralsym_itemcount', 'Assessment Scores', 8, 13],
		['nih_cogfluid_uncorr', 'Assessment Scores', 17, 8],
		['nih_cogfluid_agecorr', 'Assessment Scores', 18, 8],
		['nih_cogfluid_tscore', 'Assessment Scores', 19, 8],
		['nih_cogcryst_uncorr', 'Assessment Scores', 17, 9],
		['nih_cogcryst_agecorr', 'Assessment Scores', 18, 9],
		['nih_cogcryst_fullycorr_tscore', 'Assessment Scores', 19, 9],
		['nih_cog_totalcomp_uncorr', 'Assessment Scores', 17, 10],
		['nih_cog_totalcomp_agecorr', 'Assessment Scores', 18, 10],
		['nih_cog_totalcomp_fullycorr_tscore', 'Assessment Scores', 19, 10]
		]

	fileDir = 'NIH Toolbox'
	fileDict_keys = ['Assessment Data', 'Assessment Scores', 'Registration Data']	# string values based on reference list above

	globList = list(glob.iglob('*/{}/*'.format(fileDir)))
	subjList = []
	for f in globList:
		s = f.split(os.sep)[0]
		if s.lower() not in [a[0].lower() for a in subjList]:
			subjList.append([s, None, None, None])
		idx = [a[0].lower() for a in subjList].index(s.lower())
		
		for i, j in enumerate(fileDict_keys):
			if j.lower() in f.lower():
				subjList[idx][i+1] = f

	for subj in subjList:	# check for and exclude any subjects that do not have all three NIH Toolbox files
		if any(x is None for x in subj):
			subjList.delete(subj)
			continue

		fileDict_values = [df_data, df_scores, df_reg] = [pd.read_csv(x, header=None) for x in subj[1: ]]	# header=None used to offset row indices
		fileDict = dict(zip(fileDict_keys, fileDict_values))

		y = df_data.loc[df_data[8] == 'RAVLT_TITLE'].index[0]	# RAVLTT1, RAVLTT2, and RALTT3 search
		reference_ravltt = [
			['nih_audverbal_ravltt1', 'Assessment Data', 10, y + 1],
			['nih_audverbal_ravltt2', 'Assessment Data', 10, y + 2],
			['nih_audverbal_raltt3', 'Assessment Data', 10, y + 3]
			]

		df_output = pd.DataFrame(np.nan, index=[0], columns=templateHeader)
		for row in reference + reference_ravltt:
			df_output.ix[0, row[0]] = fileDict[row[1]].iat[row[3], row[2]]
			# df_output.set_value(0, row[0], fileDict[row[1]].iat[row[3], row[2]])		# set_value() deprecated in #17739 (https://github.com/pandas-dev/pandas/pull/17739)

		df_output.to_csv(op.join(outDir, '{}.csv'.format(subj[0])), index=False)


if __name__ == '__main__':
	scriptDir = op.dirname(op.abspath(__file__))
	template = op.join(scriptDir, 'AirBrainAndBehavior_ImportTemplate_2017-10-26_NIHTemplate.csv')

	mainDir = '/Volumes/projects_herting/ABB_Project/Subjects/'
	# mainDir = 'Z:/ABB_Project/Subjects/'
	os.chdir(mainDir)

	outDir = 'NIH Redcap'
	if not op.exists(outDir):
		os.makedirs(outDir)

	main()
