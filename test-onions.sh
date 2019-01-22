#!/bin/bash
START=`date +%s`
SRCURL='http://onionlistzboedqe.onion/?format=text'
URLFILE='testonions.txt'
OLDFILE='oldonions.txt'
TMPFILE='tmponions.txt'
OUTFILE='testout.txt'

if [ -f $URLFILE ]; then
	mv $URLFILE $OLDFILE
fi

if [ -f $OLDFILE ]; then
	torify curl "$SRCURL" | sort -u > $TMPFILE
	sort -u $OLDFILE $TMPFILE > $URLFILE
	rm $OLDFILE $TMPFILE
else
	torify curl "$SRCURL" | sort -u > $URLFILE
fi

wc -l $URLFILE
printf "\n"
printf "\n"
split -l 1000 --numeric-suffixes=1 --additional-suffix=.list testonions.txt urls/onions
for file in urls/*.list; do
	while read url; do
		printf "============================================================\n" >> ${file%.list}$OUTFILE
		printf "\nURL: http://$url/\n\n"                                        >> ${file%.list}$OUTFILE
		torify curl -f -I --connect-timeout 30 -m 30 "http://$url/"             >> ${file%.list}$OUTFILE
		printf "\nRequest Time:\n"                                              >> ${file%.list}$OUTFILE
		TZ='GMT' date -R                                                        >> ${file%.list}$OUTFILE
	  printf "\n"                                                             >> ${file%.list}$OUTFILE
		sleep 5s
	done < $URLFILE
done
END=`date +%s`

RUNTIME=$((END-START))

echo $RUNTIME
