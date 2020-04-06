from versions import versions, langEncDict, dbcsEncs
import re
from pathlib import Path
from getfilepaths import getFilePaths
from dbcs_special import encodeDbcsSpecialFile, decodeDbcsSpecial
import shutil
import configparser


def copyDirectory(src, dest):
	try:
		shutil.copytree(src, dest)
	except shutil.Error as e:
		print('Directory not copied. Error: %s' % e)
	except OSError as e:
		print('Directory not copied. Error: %s' % e)

if Path('5_postprod').exists():
	shutil.rmtree('5_postprod')

for p in getFilePaths(Path('4_prod'), '', True):
	if p.name == 'nonprod' and p.exists():
		shutil.rmtree(p)

for p in getFilePaths(Path('4_prod'), '', False):
	if p.name in dbcsEncs:
		encodeDbcsSpecialFile(p, Path('5_postprod').joinpath(p.name), langEncDict[p.name])
	else:
		copyDirectory(p, Path('5_postprod').joinpath(p.name))

for p in getFilePaths(Path('5_postprod'), '', False):
	pTemp = p.joinpath('mmmerge/Data/01LocLANG.EnglishT')
	if pTemp.exists():
		pTemp.rename(pTemp.parent.joinpath('10 Loc' + p.name.upper().replace('_', '') + '.EnglishT'))

	for pTemp in getFilePaths(p, '', True):
		if pTemp.name[:19] == 'LocalizeTables.LANG':
			pTemp.rename(pTemp.parent.joinpath('LocalizeTables.' + p.name.upper().replace('_', '') + pTemp.name[19:]))

	for versionNum in ['6', '7', '8', 'merge']:
		pTemp = p.joinpath('mm' + versionNum + '/Data/LocalizeConf.ini')
		config = configparser.ConfigParser()
		config.read(pTemp, encoding = langEncDict[p.name])
		if p.name in dbcsEncs:
			config['Settings']['program_name'] = decodeDbcsSpecial(config['Settings']['program_name'])

		config['Settings']['game_version']     = versionNum                          # 6/7/8/merge

		if versionNum == 'merge':
			config['Settings']['grayface_version'] = versions['grayface']['8']           # GrayFace Patch's version
			config['Settings']['merge_version']    = versions['merge']                   # 0 (not mmmerge)/YYYY-MM-DD
		else:
			config['Settings']['grayface_version'] = versions['grayface'][versionNum]
			config['Settings']['merge_version']    = '0'

		config['Settings']['lang']             = p.name
		config['Settings']['i18n_version']     = versions['i18n'][p.name]
		config['Settings']['encoding']         = langEncDict[p.name]

		with open(pTemp, mode = 'w', encoding = langEncDict[p.name]) as configfile:
			config.write(configfile, False)

	if p.name in dbcsEncs:
		for versionNum in ['6', '7', '8', 'merge']:
			versionNum2 = versionNum
			if versionNum2 == 'merge':
				versionNum2 = '8'
			pTemp = p.joinpath('mm' + versionNum + '/mm' + versionNum2 + 'lang.ini')
			config = configparser.RawConfigParser()
			config.optionxform = str
			config.read(pTemp, encoding = langEncDict[p.name])

			for opt in ['RecoveryTimeInfo', 'PlayerNotActive', 'DoubleSpeed', 'NormalSpeed', 'GameSavedText', 'ArmorHalved']:
				if config.has_option('Settings', opt):
					config['Settings'][opt] = '.' + config['Settings'][opt]

			with open(pTemp, mode = 'w', encoding = langEncDict[p.name]) as configfile:
				config.write(configfile, False)



# non_text/scripts_datatables
# diff copy to [all lang]/mmmerge/

# non_text/font/zh_CN/*.fnt
# copy to zh_CN/[mmmerge|mm8|mm7|mm6]/Data/10 LocZHCN.EnglishT
# see other langs

# non_text/MM8Setup/zh_CN/prod/[mmmerge|mm8]

# non_text/sound/zh_CN -> Data/10 LocZHCN.EnglishD

# non_text/video/zh_CN -> Anims/10 LocZHCN.Magicdod.vid

# non_text/img/zh_CN/prod -> Data/10 LocZHCN.EnglishD  Data/z10 LocZHCN.icons
