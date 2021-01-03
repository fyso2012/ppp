DIR=$(cd "$(dirname "$0")";pwd)

cd $DIR/go-cqhttp
ps -ef|grep -w 'go-cqhttp'|grep -v grep|cut -c 9-17|xargs kill -9
nohup ./go-cqhttp >/dev/null 2>&1 &

cd $DIR/yobot/src/client
ps -ef|grep -w 'yobotg.sh'|grep -v grep|cut -c 9-17|xargs kill -9
ps -ef|grep -w 'main.py'|grep -v grep|cut -c 9-17|xargs kill -9
nohup bash yobotg.sh >/dev/null 2>&1 &

cd $DIR/HoshinoBot
ps -ef|grep -w 'hoshino_run.py'|grep -v grep|cut -c 9-17|xargs kill -9
nohup python3 hoshino_run.py >/dev/null 2>&1 & 




