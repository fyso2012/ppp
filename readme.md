安装 python 3.8.x

更新 python -m pip install --upgrade pip

git clone git@github.com:fyso2012/ppp.git pcrbot

cd pcrbot/go-cqhttp
    
    编辑 config.hjson 以下两项，改成机器人的qq号与密码
        uin: 0
        password: ""
    执行 chmod +x go-cqhttp

cd ../yobot

    编辑 src/client/yobot_data/yobot_config.json, 1.2.3.4修改为你的公网ip，super-admin为管理员qq
        "public_address": "http://1.2.3.4:9222/",
        "super-admin": [1234556,2345623],
    cd src/client/
        执行 pip install -r requirements.txt

cd ../../../HoshinoBot/

    编辑 hoshino/config/__bot__.py 以下两项, 
        SUPERUSERS = [1234556,2345623]  # 管理员的qq号，可以多个
        NICKNAME = ('ue', '优衣')       # 机器人的昵称。呼叫昵称等同于@bot，可用元组配置多个昵称
    执行 pip install -r requirements.txt

cd ../

    启动与重启：bash restart.sh
    关闭：bash stop.sh
