#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright FunASR (https://github.com/alibaba-damo-academy/FunASR). All Rights Reserved.
#  MIT License  (https://opensource.org/licenses/MIT)


# method1, inference from model hub

from funasr import AutoModel
wav_file = "https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/vad_example.wav"

model = AutoModel(model="damo/speech_fsmn_vad_zh-cn-16k-common-pytorch", model_revision="v2.0.4")

res = model.export(input=wav_file, type="onnx", quantize=False)
print(res)

# method2, inference from local path

from funasr import AutoModel

wav_file = "https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/vad_example.wav"

model = AutoModel(model="/Users/zhifu/.cache/modelscope/hub/damo/speech_fsmn_vad_zh-cn-16k-common-pytorch")

res = model.export(input=wav_file, type="onnx", quantize=False)
print(res)
