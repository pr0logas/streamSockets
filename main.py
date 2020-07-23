#!/usr/bin/env python3
##:: Author: Anonymous
##:: 2020-07-14
##:: Description: Playing with pirdaTV

from streamer import streamRequest
from writer import Writer
from defaults import sourceURL
from udpsocket import startSocket

streamedData = streamRequest(sourceURL)
w = Writer('LTVHD.tv', streamedData)
w.channelWriter()
#startSocket()