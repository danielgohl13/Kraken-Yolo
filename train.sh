#!/bin/sh
#./darknet detector train release/data/obj.data release/yolov2-voc-daniel.cfg darknet53.conv.74
#./darknet detector train release/data/obj.data release/yolov3-voc-daniel.cfg darknet53.conv.74
#./darknet detector train release/data/obj.data release/yolov3-tiny-daniel.cfg darknet53.conv.74
#./darknet detector train release/data/obj.data release/yolov3-tiny-daniel.cfg darknet19_448.conv.23
../darknet/darknet detector train release/data/obj.data release/yolov2-tiny.cfg darknet19_448.conv.23
