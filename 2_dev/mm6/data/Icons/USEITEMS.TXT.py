def t(_, _x): return ('USE ITEM\t\t\t\t\t\t\t\t\t\t\t"Selected Char gets, remove both Items and Explode:"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
'Pickup Item ( in hand ) and Right Click.\t\t\t\t\t\t\t\t\t\tE1\tRnd 10-20 pts Fire dmg\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
'\t\t\t\t\t\t\t\t\t\tE2\tRnd 30-100 pts Fire dmg + do Break Item\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
'Scrolls\tCast spell #  and delete Item. Close windows and get target as nessasary. ESC cancels.\t\t\t\t\t\t\t\t\tE3\tRnd 50-250 pts Fire dmg + do break Item x5\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
'\t\t\t\t\t\t\t\t\t\tE4\tSet Erradicated + do break Item all\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
'Books\tMust Right Click on Char face to work and Char Must Have Magic Skill Group of spell to learn. No effect if already has it.\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
'\r\n'
'Potions and Herbs\t\t\t\tDrink / Eat\t\t\t\t\t\tRed\tBlu\tYel\tOra\tGre\tPur\tW1\tW2\tW3\tW4\tW5\tW6\tW7\tW8\tB1\tB2\tB3\tB4\tB5\tB6\tB7\tB8\tB9\tB10\tB11\r\n'
'\t\t\t\tRight Click on Face\tChange Item\t160\t161\t162\t163\t164\t165\t166\t167\t168\t169\t170\t171\t172\t173\t174\t175\t176\t177\t178\t179\t180\t181\t182\t183\t184\t185\t186\t187\t188\r\n'
'160\therb1\t' + _x("items", "Poppysnaps") + '\t' + _x("items", "Herb") + '\tSet Poison1 condition\tremove Item\tno\tno\tno\t166\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'161\therb2\t' + _x("items", "Phirna Root") + '\t' + _x("items", "Herb") + '\tCure 2 Spell points\tremove Item\tno\tno\tno\t165\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'162\therb3\t' + _x("items", "Widoweeps Berries") + '\t' + _x("items", "Herb") + '\tCure 2 Hit points\tremove Item\tno\tno\tno\t164\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'163\tbottle30\t' + _x("items", "Potion Bottle") + '\t' + _x("items", "Potion Bottle") + '\tno effect\t-\t166\t165\t164\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'164\tbottle26\t' + _x("items", "Cure Wounds") + '\t' + _x("items", "Red Potion") + '\tCure 10 Hit points\tChange Item to 163\tno\tno\tno\tno\tno\t169\t167\t174\tE1\tE1\tE2\tE2\tE2\tE2\t181\t186\tE2\tE2\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\r\n'
'165\tbottle23\t' + _x("items", "Magic Potion") + '\t' + _x("items", "Blue Potion") + '\tCure 10 Spell points\tChange Item to 163\tno\tno\tno\tno\t169\tno\t168\t176\t173\t177\tE2\t183\tE2\tE2\tE2\tE2\t182\tE2\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\r\n'
'166\tbottle28\t' + _x("items", "Energy") + '\t' + _x("items", "Yellow Potion") + '\tSet Temp 7 Stats to 10\tChange Item to 163\tno\tno\tno\tno\t167\t168\tno\t172\t175\tE1\t184\tE2\tE2\tE2\tE2\tE2\tE2\t185\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\r\n'
'167\tbottle25\t' + _x("items", "Protection") + '\t' + _x("items", "Orange Potion") + '\tSet Temp AC to 10\tChange Item to 163\tno\tno\tno\tno\t174\t176\t172\tno\t170\tE1\tE2\t179\tE2\tE2\tE2\tE2\tE2\tE2\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\r\n'
'168\tbottle24\t' + _x("items", "Resistance") + '\t' + _x("items", "Green Potion") + '\tSet Temp Resistances to 10\tChange Item to 163\tno\tno\tno\tno\tE1\t173\t175\t170\tno\t171\tE2\tE2\t188\t180\tE2\tE2\tE2\tE2\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\r\n'
'169\tbottle29\t' + _x("items", "Cure Poison") + '\t' + _x("items", "Purple Potion") + '\t"Cure poison1,2,3"\tChange Item to 163\tno\tno\tno\tno\tE1\t177\tE1\tE1\t171\tno\tE2\tE2\t178\t187\tE2\tE2\tE2\tE2\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\tE3\r\n'
'170\tbottle27\t' + _x("items", "Supreme Protection") + '\t' + _x("items", "White Potion") + '\tSet Temp AC to 20\tChange Item to 163\tno\tno\tno\tno\tE2\tE2\t184\tE2\tE2\tE2\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'171\tbottle27\t' + _x("items", "Restoration") + '\t' + _x("items", "White Potion") + '\t"Cure all Conditions ( no dead,stone Erad)"\tChange Item to 163\tno\tno\tno\tno\tE2\t183\tE2\t179\tE2\tE2\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'172\tbottle27\t' + _x("items", "Extreme Energy") + '\t' + _x("items", "White Potion") + '\tSet Temp 7 Stats to 20\tChange Item to 163\tno\tno\tno\tno\tE2\tE2\tE2\tE2\t188\t178\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'173\tbottle27\t' + _x("items", "Super Resistance") + '\t' + _x("items", "White Potion") + '\tSet Temp 4 Resistances to 20\tChange Item to 163\tno\tno\tno\tno\tE2\tE2\tE2\tE2\t180\t187\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'174\tbottle27\t' + _x("items", "Heroism") + '\t' + _x("items", "White Potion") + '\tSet Heroism to 6 Hrs\tChange Item to 163\tno\tno\tno\tno\t181\tE2\tE2\tE2\tE2\tE2\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'175\tbottle27\t' + _x("items", "Haste") + '\t' + _x("items", "White Potion") + '\tSet Haste to 6 Hrs\tChange Item to 163\tno\tno\tno\tno\t186\tE2\tE2\tE2\tE2\tE2\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'176\tbottle27\t' + _x("items", "Stone Skin") + '\t' + _x("items", "White Potion") + '\tSet Stone Skin to 6 Hrs\tChange Item to 163\tno\tno\tno\tno\tE2\t182\tE2\tE2\tE2\tE2\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'177\tbottle27\t' + _x("items", "Bless") + '\t' + _x("items", "White Potion") + '\tSet Bless to 6 Hrs\tChange Item to 163\tno\tno\tno\tno\tE2\tE2\t185\tE2\tE2\tE2\tno\tno\tno\tno\tno\tno\tno\tno\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\r\n'
'178\tbottle22\t' + _x("items", "Divine Power") + '\t' + _x("items", "Black Potion") + '\tSet Temp Level to 20 and +1 Age temp\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'179\tbottle22\t' + _x("items", "Divine Cure") + '\t' + _x("items", "Black Potion") + '\tHp +100 (over max ok 1time) +1 Age temp\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'180\tbottle22\t' + _x("items", "Divine Magic") + '\t' + _x("items", "Black Potion") + '\tSp +100 (over max ok 1time) +1 Age temp\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'181\tbottle22\t' + _x("items", "Pure Might") + '\t' + _x("items", "Black Potion") + '\t"Might +15 Perm, Int -5 perm 1 time only"\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'182\tbottle22\t' + _x("items", "Pure Intelect") + '\t' + _x("items", "Black Potion") + '\t"Int +15 Perm, Might -5 perm 1 time only"\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'183\tbottle22\t' + _x("items", "Pure Personality") + '\t' + _x("items", "Black Potion") + '\t"Per +15 Perm, Spd -5 perm 1 time only"\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'184\tbottle22\t' + _x("items", "Pure Endurance") + '\t' + _x("items", "Black Potion") + '\t"End +15 Perm, -1 all 6 other perm 1 time only"\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'185\tbottle22\t' + _x("items", "Pure Accuracy") + '\t' + _x("items", "Black Potion") + '\t"Acc +15 Perm, Luck -5 perm 1 time only"\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'186\tbottle22\t' + _x("items", "Pure Speed") + '\t' + _x("items", "Black Potion") + '\t"Spd +15 Perm, Per -5 perm 1 time only"\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'187\tbottle22\t' + _x("items", "Pure Luck") + '\t' + _x("items", "Black Potion") + '\t"Luck +15 Perm, Acc -5 perm 1 time only"\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'188\tbottle22\t' + _x("items", "Rejuvination") + '\t' + _x("items", "Black Potion") + '\t"Set temp Age to 0, -1 all 7 stats perm "\tChange Item to 163\tno\tno\tno\tno\tE3\tE3\tE3\tE3\tE3\tE3\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tE4\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\tno\r\n'
'\t\t\t\t(all Subtractions if < 6 then NO Sub)\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n'
)