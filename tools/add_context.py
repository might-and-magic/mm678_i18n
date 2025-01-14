# Batch Add Context
# Tool of csv2po.py
# By Tom CHEN <tomchen.org@gmail.com> (tomchen.org)

import re
from pathlib import Path
from getfilepaths import getFilePaths


def addContext(inputPath, outputPath, encoding, context):
	f = inputPath.open(mode = 'r', encoding = encoding, newline = '', errors = "strict")
	content = f.read()
	f.close()
	content = content.replace("_(TRANS)_", "_(TRANS_CONTEXT:'" + context + "')_")
	outputPath.parent.mkdir(parents = True, exist_ok = True)
	fout = outputPath.open(mode = 'w', encoding = encoding, newline = '', errors = "strict")
	content = fout.write(content)
	fout.close()


def batchAddContext(inputPath, extension, encoding, outputPath, filePathToContextFunc):
	for p in getFilePaths(inputPath, extension = extension):
		addContext(inputPath = p, outputPath = outputPath.joinpath(p.relative_to(inputPath)), encoding = encoding, context = filePathToContextFunc(p))


def fn2c(filePath):
	fileName = filePath.name.lower()
	ext = filePath.suffix.lower()
	stem = filePath.stem.lower()

	if fileName == 'intro.str' or fileName == 'lose.str' or fileName == 'win.str':
		return fileName
	elif ext == '.str' or fileName == 'mapstats.txt' or fileName == 'localizetables.lang_2devents.txt' or fileName == 'lang_2devents.txt' or fileName == '2devents.txt':
		return 'location'
	elif fileName == 'localizetables.lang_itemstxt.txt' or fileName == 'lang_itemstxt.txt' or fileName == 'useitems.txt':
		return 'items'
	elif fileName == 'localizetables.lang_monsters.txt' or fileName == 'lang_monsters.txt':
		return 'monsters'
	elif fileName == 'npcbtb.txt' or fileName == 'npctext.txt' or fileName == 'npcgreet.txt' or fileName == 'npcnews.txt' or fileName == 'proftext.txt':
		return 'npc conversation'
	elif fileName == 'npcprof.txt':
		return 'npcprof'
	elif fileName == 'autonote.txt' or fileName == 'awards.txt':
		return 'autonote or awards'
	elif fileName == 'npcnames.txt' or fileName == 'pcnames.txt' or fileName == 'localizetables.lang_npcnames.txt' or fileName == 'lang_npcnames.txt':
		return 'npcnames'
	elif fileName == 'mm7history.txt' or fileName == 'history.txt':
		return 'history'
	elif ext == '.txt':
		if stem[0:5] == 'lang_':
			return stem[5:]
		else:
			return stem
	elif fileName == 'mm8lang.ini' or fileName == 'mm7lang.ini' or fileName == 'mm6lang.ini':
		return 'mm_lang.ini'
	elif fileName == 'localizeconf.ini':
		return 'localizeconf.ini'

batchAddContext(
	inputPath = Path('0.5_template_without_context'),
	extension = ['txt', 'str', 'ini'],
	encoding = 'UTF-8',
	outputPath = Path('1_template'),
	filePathToContextFunc = fn2c
)
