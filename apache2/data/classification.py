#!/home/woongsup/anaconda3/bin/python
import konlpy 
from konlpy.tag import Mecab
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder


def stop_word(text):
    pos_tagger = Mecab()
    result = []
    a = pos_tagger.morphs(text)
    stop_word = [
                "으로","개월","습니다","하지만","이나","또는",
                "다만","습니다","심지어","합니다","관련","이러",
                "으며","경우","라는","이를","입니다","다행히",
                "시켜","에서","경우","인해","라는","됩니다",
                "지만","그렇","다고","해서","그러므로","통해",
                "특히","거의","없이","거나","시킬","대한",
                "처럼","따른","시키","비해","아닙니다","다면",
                "라고","으므로","해야","그러나","이런","대해서",
                "으므로","함","으로써","이루어지","아닙니다","에게",
                "통한","그리고","다는","는데","으나","인한",
                "집니다","때문","이후","크","나타나","만큼",
                "의한","의해서","대개","또한","도록","관해",
                "해준다","이르","므로","따라","때로","위해",
                "주후","대로","따라서","다가","아야","이때",
                "아니","물론","계시","대단히","오직","계시",
                "어쩔","이룰","무척","똑같이","실제로","그래서",
                "왜냐하면","바랍니다","비로소","에선","가령","빈번히",
                "이른바","라면","아니","못한","대단히","철저히",
                "물론","네이버","그것","중요","요즘","그때",
                "무엇","이제","해당","한동안","예전","주지",
                "뭔가","듯이","약간","도중","계속","의학",
                "정보","듭니다","간혹","에서부터","의해","한다",
                "에게서","혹은","아주","일부","결국","빠질",
                "생긴다","대체","그러","제대로","너무","된다",
                "로부터","는지","까지","주로","면서","이내",
                "더라도","보인다면","보다","아직","위한","우리",
                "는다","인데","어야","어서","정도","한다고",
                "nan","어요","생겨","생긴","기타","졌어요",
                "어떤","못하","보이","해짐","여러","나타남",
                "갑자기","대하","어도","동안","떠올라","때때로",
                "서로","내게","양쪽","한쪽"
                ]
    non_stop_word = ["낮","밤",
                    "뇌","팔","눈","코","입","귀","혀","손","배","등","뼈","골","목","속","턱"
                    "물","불","간","똥","멍","위","털","않","변","맥",
                    "말","욕","암","성","형","병","증","콩","해","토","술","칼","화","열","몸","안","좋"]
    for i in a:
        if i not in stop_word:
            if len(i) != 1:
                result.append(i)
            elif i in non_stop_word:
                result.append(i)
    return result


def classification_(ex):
    inputlen = 1042
    ex2 = stop_word(ex)
    # tokenizer loading
    with open('./models/tokenizer.pickle', 'rb') as handle:
        new_tokenizer = pickle.load(handle)
    # model loading
    new_model = load_model("./models/classification_model.h5")
    # label loading
    new_encoder = LabelEncoder()
    new_encoder.classes_ = np.load('./models/classes.npy',allow_pickle=True)
    class_ = new_encoder.inverse_transform(new_model.predict(pad_sequences([sum(new_tokenizer.texts_to_sequences(ex2),[])],maxlen=inputlen))[0].argsort()[::-1][:5])
    return list(class_)
