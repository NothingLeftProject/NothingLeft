# coding=utf-8
# author: Lan_zhijiang
# desciption: inbox相关内容操作
# date: 2020/10/17

import json
import os


class GtdInboxManager():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting
        self.inbox_path = self.setting["dataPath"] + "inbox/"

        self.inbox = {}
        self.get_inbox()

    def get_inbox(self):

        """
        获取inbox
        :return:
        """
        inbox_list = os.listdir(self.inbox_path)

        if inbox_list is None or inbox_list == []:
            info = {
                "numberOfStuff": 0
            }
            json.dump(info, open(self.inbox_path + "info.json", "w", encoding="utf-8"))

        for event in inbox_list:
            if event == "info.json":
                self.inbox["info"] = json.load(open(self.inbox_path+event, "r", encoding="utf-8"))
            else:
                stuff_info = json.load(open(self.inbox_path + event, "r", encoding="utf-8"))
                event = event.replace(".json", "")
                # self.inbox["stuff"].append(event)  # 小于最大值不就得了？
                self.inbox["stuff"].append(stuff_info)

    def update_inbox_to_local(self, stuff_info, stuff_path):

        """
        更新inbox到本地
        :param stuff_path: stuff路径
        :param stuff_info: stuff信息
        :return:
        """
        if stuff_info is not None and stuff_path is not None:  # may be a bug
            json.dump(stuff_info, open(stuff_path, "w", encoding="utf-8"))
        json.dump(self.inbox["info"], open(self.inbox_path + "info.json", "w", encoding="utf-8"))

    def add_stuff(self, name, tags=None, remarks=None, desc=None):

        """
        添加一个stuff到inbox中
        :param name: stuff的名称
        :param tags: 标签（不推荐填写）
        :param remarks: 备注（对后续处理可以起到提示）
        :param desc: 更加详细的描述（不推荐）
        :return: int(index), bool(remind_clean)
        """
        remind_clean = False
        stuff_info = json.load(open("./backend/data/json/inbox_stuff_template.json", "r", encoding="utf-8"))
        stuff_info["name"] = name
        stuff_info["tags"] = tags
        stuff_info["remarks"] = remarks
        stuff_info["desc"] = desc
        stuff_info["createdTime"] = self.log.get_data + " " + self.log.get_formatted_time()

        self.inbox["info"]["numberOfStuff"] += 1
        if self.inbox["info"]["numberOfStuff"] > self.setting["inboxStuffLimit"]:
            remind_clean = True

        self.log.add_log("InboxManager: Add stuff-" + name, 1)
        self.inbox["stuff"].append(stuff_info)
        self.update_inbox_to_local(stuff_info, self.inbox_path + self.inbox["info"]["numberOfStuff"] + ".json")

        return self.inbox["info"]["numberOfStuff"], remind_clean

    def delete_stuff(self, index):

        """
        删除某个stuff
        :param index: stuff的index
        :return: bool
        """
        index = str(index)
        if int(index) <= self.inbox["info"]["numberOfStuff"]:
            self.log.add_log("InboxManager: Delete stuff-" + index, 1)

            stuff_path = self.inbox_path + index + ".json"
            self.inbox["info"]["numberOfStuff"] -= 1
            self.inbox["stuff"].remove(index)
            os.remove(stuff_path)
            self.update_inbox_to_local(None, None)
            return True
        else:
            self.log.add_log("InboxManager: Can't find stuff-" + index + " in the inbox", 3)
            return False

    def get_stuff(self, index):

        """
        获取某个stuff的信息
        :param index: stuff的index
        :return: dict
        """
        index = int(index)
        if index <= self.inbox["info"]["numberOfStuff"]:
            self.log.add_log("InboxManager: Try getting stuff-" + str(index), 1)

            return self.inbox["stuff"][index]
        else:
            self.log.add_log("InboxManager: Can't find stuff-" + str(index) + " in the inbox", 3)
            return None

    def update_stuff(self, index, key, value):

        """
        更新stuff信息
        :param index: stuff的index
        :param key: 要更新的键
        :param value: 值
        :return: bool
        """
        index = int(index)
        if index <= self.inbox["info"]["numberOfStuff"]:
            if (type(key) is list or type(key) is tuple) and (type(value) is list or type(value) is tuple):

                self.log.add_log("InboxManager: Update stuff info: \n    "
                                + str(key) + "\n    " + str(value), 1)

                for n_k in range(0, len(key)):
                    try:
                        self.inbox["stuff"][index][key[n_k]] = value[n_k]
                    except KeyError:
                        self.log.add_log("InboxManager: Can't find key: " + key[n_k] + " while updating info!", 3)
                        continue

                return True
            else:
                self.log.add_log("InboxManger: param key and value has to be a list or tuple!", 3)
                return False
        else:
            self.log.add_log("InboxManager: Can't find stuff-" + str(index) + " in the inbox", 3)
            return False

    def search_stuff(self, keyword):

        """
        搜索stuff
        :param keyword: 搜索关键词
        :return:
        """

