#!/bin/bash

urls_path=$1
download_dir=$2
echo 'opening' $urls_path 'and saving to' $download_dir 
cat $urls_path | while read line
do	
	url=$(echo "$line" | tr -d '"')
	file_name=$(basename $line)
	file_name=$(echo "$file_name" | tr -d '"')
	wget -q $url -O $download_dir'/'$file_name --tries=1 --waitretry=0 --read-timeout=3
	size=$(wc -c $download_dir'/'$file_name | awk '{print $1}')
	if  (($size <= 0)); then
	    	rm $download_dir'/'$file_name
	else
		echo 'downloaded '$file_name	
	fi;
done

cd $current_dir
