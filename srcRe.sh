#!/usr/bin/env bash

sourcePlaylist=''
parsingParam='storade_tv'
dir="$PWD/playlists/"
sreamingDir="$PWD/channels/"
path="${dir}playlist"

latestVideoFile=''

function getData {
	timestamp=$(date +"%Y-%m-%d_%H-%M-%S-%s")
	result=$(/usr/bin/curl -s $sourcePlaylist | grep $parsingParam)

	if [[ $? -ne "0" ]]; then
		echo "FATAL! Cannot get data from ${playlist}!" 
	else
		echo "$result" > ${path}-${timestamp}.m3u8
		cd ${dir} && ls -1tr | head -n -10 | xargs -d '\n' rm -f --
		ln -nsf ${path}-${timestamp}.m3u8 ${dir}playlist.m3u8 || true
	fi
}

function saveVideoFile {
	timestamp=$(date +"%Y-%m-%d_%H-%M-%S-%s")
	cd $sreamingDir
	/usr/bin/curl -s $1 -o mov-${timestamp}.ts
	cd ${sreamingDir} && ls -1tr | head -n -10 | xargs -d '\n' rm -f --
	ln -nsf ${sreamingDir}mov-${timestamp}.ts ${sreamingDir}currentFile.ts || true
}


function getFileList {
	fresult=$(cat ${dir}playlist.m3u8 | head -1)
	cresult=$(/usr/bin/curl -s $fresult | grep $parsingParam)
	set -- $cresult
		latestVideoFile=$1
}

function startProcess {
	for (( ; ; ))
	do
		getData
		getFileList
		saveVideoFile $latestVideoFile
		sleep 5
	done
}

startProcess
