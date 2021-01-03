安装 python 3.8.x
更新 python -m pip install --upgrade pip

进入 go-cqhttp 文件夹
    修改  文件夹内 config.hjson 改成机器人的qq号与密码
        uin: 0
        password: ""
    执行 chmod +x go-cqhttp

进入 yobot 文件夹 
    修改 yobot/src/client/yobot_data 文件夹内 yobot_config.json, 1.2.3.4 修改为你的公网ip，super-admin为管理员qq
        "public_address": "http://1.2.3.4:9222/",
        "super-admin": [1234556,2345623],
    进入 yobot/src/client/ 文件夹内
        执行 pip install -r requirements.txt

进入 HoshinoBot 文件夹
    修改 HoshinoBot/hoshino/config 文件夹内 __bot__.python
        SUPERUSERS = [1234556,2345623]    # 管理员的qq号，可以多个
        NICKNAME = ('ue', '优衣')           # 机器人的昵称。呼叫昵称等同于@bot，可用元组配置多个昵称
    执行 pip install -r requirements.txt


启动与重启：bash restart.sh
关闭：bash stop.sh
