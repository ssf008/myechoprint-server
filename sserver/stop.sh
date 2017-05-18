#!/bin/sh
pidlist=`ps -ef|grep rest |grep -v "grep"|awk '{print $2}'`

if [ "$pidlist" = "" ]
   then
       echo "no echoprint pid alive!"
else
  echo "echoprint pid list :  $pidlist"
  echo "killing pidlist :  $pidlist"
  kill -9 $pidlist
  echo "echoprint stopped successfully!" 
  sleep 1 
fi
