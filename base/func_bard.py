#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import google.generativeai as genai


class BardAssistant:
    def __init__(self, conf: dict) -> None:
        self._api_key = conf["api_key"]
        self._model_name = conf["model_name"]
        self._prompt = conf['prompt']
        self._proxy = conf['proxy']
        genai.configure(api_key=self._api_key, transport="rest")
        # 模型参数
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
        self._bard= genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config,
                                      safety_settings=safety_settings)
       #self._bard = genai.GenerativeModel(self._model_name)

    def __repr__(self):
        return 'BardAssistant'

    @staticmethod
    def value_check(conf: dict) -> bool:
        if conf:
            if conf.get("api_key") and conf.get("model_name") and conf.get("prompt"):
                return True
        return False

    def get_answer(self, msg: str, sender: str = None) -> str:
        response = self._bard.generate_content([{'role': 'user', 'parts': [msg]}])
        return response.text


if __name__ == "__main__":
    from configuration import Config
    config = Config().BardAssistant
    if not config:
        exit(0)

    bard_assistant = BardAssistant(config)
    if bard_assistant._proxy:
        os.environ['HTTP_PROXY'] = bard_assistant._proxy
        os.environ['HTTPS_PROXY'] = bard_assistant._proxy
    rsp = bard_assistant.get_answer(bard_assistant._prompt)
    print(rsp)
