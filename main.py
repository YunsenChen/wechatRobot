#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
from argparse import ArgumentParser

from base.func_jinrirebang_quanzhan import *
from base.func_report_reminder import ReportReminder
from configuration import Config
from constants import ChatType
from robot import Robot, __version__
from wcferry import Wcf


def weather_report(robot: Robot) -> None:
    """模拟发送天气预报
    """

    # 获取接收人
    receivers = ["filehelper"]

    # 获取天气，需要自己实现，可以参考 https://gitee.com/lch0821/WeatherScrapy 获取天气。
    report = "这就是获取到的天气情况了"

    for r in receivers:
        robot.sendTextMsg(report, r)
        # robot.sendTextMsg(report, r, "notify@all")   # 发送消息并@所有人


def main(chat_type: int):
    config = Config()
    wcf = Wcf(debug=True)

    def handler(sig, frame):
        wcf.cleanup()  # 退出前清理环境
        exit(0)

    signal.signal(signal.SIGINT, handler)

    robot = Robot(config, wcf, chat_type)
    robot.LOG.info(f"WeChatRobot【{__version__}】成功启动···")

    # 机器人启动发送测试消息
    robot.sendTextMsg("马家淇启动成功！", "44349604950@chatroom")
    # 机器人启动发送测试消息
    # robot.sendTextMsg("Nash重启成功！", "25266529681@chatroom")
    # 接收消息
    #robot.enableRecvMsg()     # 可能会丢消息？

    robot.enableReceivingMsg()  # 加队列

    # 每天 7 点发送天气预报
    # robot.onEveryTime("20:33", weather_report, robot=robot)


    #8.29 send jirirebang
    #robot.onEveryTime("23:30", robot.jiriRedian)
    #times="22:51"


    newstime="07:00"
    robot.onEveryTime(newstime, robot.newsReport)
    robot.onEveryTime("07:30", robot.weahterReport)
    robot.onEveryTime(newstime, lambda: robot.sendNews(get36krUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getZhihuUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getXueqiuUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getHuxiuUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getPengpaiUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getAifanUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getShaoshupaiUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getPojieUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getGuanfengwangUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getDongfangCaifuUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getLandianUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getXiaozhongUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getFandouXianTuUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getJuejinUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getJishuUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getGithubUrl()))
    robot.onEveryTime(newstime, lambda: robot.sendNews(getITUrl()))
    robot.onEveryTime("23:45", lambda: robot.sendNews(getUrl()))



    #print(getUrl())
    #     print(getZhihuUrl())
    #     print(getITUrl())
    #     print(getShaoshupaiUrl())
    #    print(get36krUrl())
    #    print(getXueqiuUrl())
    #    print(getHuxiuUrl())
    #    print(getPengpaiUrl())
    #    print(getAifanUrl())
    #    print(getPojieUrl())
    #    print(getGuanfengwangUrl())
    #    print(getDongfangCaifuUrl())
    # print(getLandianUrl())
    # print(getXiaozhongUrl())
    #    print(getFandouXianTuUrl())
    #   print(getJuejinUrl())
    #    print(getJishuUrl())
    #    print(getGithubUrl())

    # 每天 16:30 提醒发日报周报月报
#    robot.onEveryTime("16:35", ReportReminder.remind, robot=robot)

    #robot.sendTextMsg("机器人启动成功！", "filehelper")

    # 接收消息
    # robot.enableRecvMsg()     # 可能会丢消息？
    robot.enableReceivingMsg()  # 加队列

    # 每天 7 点发送天气预报
    #robot.onEveryTime("07:00", weather_report, robot=robot)



    # 每天 16:30 提醒发日报周报月报
    #robot.onEveryTime("16:30", ReportReminder.remind, robot=robot)

    # 让机器人一直跑
    robot.keepRunningAndBlockProcess()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-c', type=int, default=0, help=f'选择模型参数序号: {ChatType.help_hint()}')
    args = parser.parse_args().c
    main(args)
