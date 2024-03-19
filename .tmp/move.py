import os
import shutil
import sys

ns2source = ["/Users/dkguo/Downloads/WenetSpeech4TTS_result/ns2_3.6",
             '/Users/dkguo/Downloads/WenetSpeech4TTS_result/ns2_3.8',
             "/Users/dkguo/Downloads/WenetSpeech4TTS_result/ns2_4.0"]
vallesource = ["/Users/dkguo/Downloads/WenetSpeech4TTS_result/valle_3.6",
               "/Users/dkguo/Downloads/WenetSpeech4TTS_result/valle_3.8",
               "/Users/dkguo/Downloads/WenetSpeech4TTS_result/valle_4.0"]

ns2target = ["/Users/dkguo/Downloads/wenetspeech4tts/demos/NS2",
             "/Users/dkguo/Downloads/wenetspeech4tts/demos/NS2_S",
             "/Users/dkguo/Downloads/wenetspeech4tts/demos/NS2_P"]
valletarget = ["/Users/dkguo/Downloads/wenetspeech4tts/demos/Valle",
               "/Users/dkguo/Downloads/wenetspeech4tts/demos/Valle_S",
               "/Users/dkguo/Downloads/wenetspeech4tts/demos/Valle_P"]

spk = sys.argv[1]
utt = sys.argv[2]

with open("/Users/dkguo/Downloads/wenetspeech4tts/spk.lst","a+") as f:
    spks = [line.strip() for line in f.readlines()]
    if spk not in spks:
        f.write(spk+'\n')
    
with open("/Users/dkguo/Downloads/wenetspeech4tts/utt.lst","a+") as f:
    utts = [line.strip() for line in f.readlines()]
    if utt not in utts:
        f.write(utt+'\n')

# for ns2
sname = f"{utt}.lab_{spk}.npy.wav"
tname = f"{spk}_{utt}.wav"

for i in range(3):
    if os.path.exists(ns2source[i]+f'/inset/{sname}'):
        shutil.copy(ns2source[i]+f'/inset/{sname}',ns2target[i]+f'/{tname}')
    elif os.path.exists(ns2source[i]+f'/inset2/{sname}'):
        shutil.copy(ns2source[i]+f'/inset2/{sname}',ns2target[i]+f'/{tname}')
    elif os.path.exists(ns2source[i]+f'/outset/{sname}'):
        shutil.copy(ns2source[i]+f'/outset/{sname}',ns2target[i]+f'/{tname}')
    else:
        print("ns2 not such audio")
        print(sname)
        exit(0)
# for valle
sname = f"{spk}_{utt}.wav"
tname = f"{spk}_{utt}.wav"
for i in range(3):
    if os.path.exists(vallesource[i]+f'/inset/{sname}'):
        shutil.copy(vallesource[i]+f'/inset/{sname}',valletarget[i]+f'/{tname}')
    if os.path.exists(vallesource[i]+f'/outset/{sname}'):
        shutil.copy(vallesource[i]+f'/outset/{sname}',valletarget[i]+f'/{tname}')
    if os.path.exists(vallesource[i]+f'/outset_ckpt1/{sname}'):
        shutil.copy(vallesource[i]+f'/outset_ckpt1/{sname}',valletarget[i]+f'/{tname}')

