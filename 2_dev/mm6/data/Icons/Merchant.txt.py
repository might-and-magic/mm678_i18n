def t(_, _x): return ('\tBuy\tSell\tRepair\tIdentify\r\n'
'Not enough gold\t' + _x("merchant", "I'm sorry, %06, but you don't have enough money.") + '\t' + _x("merchant", "n/a") + '\t' + _x("merchant", "I'm sorry, %06, but you don't have enough money.") + '\t' + _x("merchant", "I'm sorry, %06, but you don't have enough money.") + '\r\n'
'no merchant skill\t' + _x("merchant", "An excellent choice!  This %24 is of the finest quality.  I am willing to virtually give it away for %27 gold.") + '\t' + _x("merchant", "Hmph.  Looks like junk to me. <yawn> I suppose I could give you oh, say, %27 gold pieces for it.") + '\t' + _x("merchant", "This %24 is nearly beyond repair.  It will take a superhuman effort to fix it!  I'll have to charge %27 gold.") + '\t' + _x("merchant", "I'll tell you what it is for %29 gold pieces.") + '\r\n'
'regular merchant skill\t' + _x("merchant", "Ordinarily I sell things like this %24 for %25 gold.  But you drive a hard bargain-- I'll sell it to you for %27.") + '\t' + _x("merchant", "Usually I try to buy something like this %24 for %25 gold.  I'll give you %27 for it.") + '\t' + _x("merchant", "This %24 is in bad shape, but it can be fixed.  I usually want %25 gold, but for you I will charge a mere %27.") + '\t' + _x("merchant", "I'll tell you what it is for %29 gold pieces.") + '\r\n'
'good merchant skill\t' + _x("merchant", "I try to sell things like this %24 for %25 gold.  But we both know it's really worth %27.  So that's my price.") + '\t' + _x("merchant", "Normally, I do my best to buy a %24 for %25 gold.  But I can see you know it's worth %27.  Agreed?") + '\t' + _x("merchant", "Hmmm.  Nothing a little glue and polish won't fix, I warrant.  My policy is to ask for %25 gold, but I can go as low as %27.") + '\t' + _x("merchant", "I'll tell you what it is for %29 gold pieces.") + '\r\n'
'wrong type of merchant\t' + _x("merchant", "n/a") + '\t' + _x("merchant", "Sorry, I am a %28.  I'm not interested in such things.") + '\t' + _x("merchant", "Sorry, I have no idea how to fix a %24.  ") + '\t' + _x("merchant", "Sorry, I can't identify a %24 because I'm a %28.  I don't know anything about those.") + '\r\n'
'Unnecessary\t' + _x("merchant", "n/a") + '\t' + _x("merchant", "I'm a simple %28 and that %24 is beyond my meager knowledge.") + '\t' + _x("merchant", "That %24 isn't broken!  You don't fix what isn't broken, I always say.") + '\t' + _x("merchant", "You already know what that is.  You don't need me to identify it.") + '\r\n'
)