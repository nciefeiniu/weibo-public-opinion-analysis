# coding='utf-8'
import re
import jieba
import jieba.analyse
from multiprocessing.dummy import Pool as ThreadPool


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords  # 停用词


def synwordslist(filepath):
    syn = dict()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            synword = line.strip().split("\t")
            num = len(synword)
            for i in range(1, num):
                syn[synword[i]] = synword[0]
    return syn  # 近义词典


# 对句子进行分词
def seg_sentence(sentence):
    sentence = re.sub(u'[0-9\.]+', u'', sentence)
    jieba.load_userdict('自建词表.txt')  # 加载自建词表
    # suggest_freq((), tune=True) #修改词频，使其能分出来
    # jieba.add_word('知识集成')		# 这里是加入用户自定义的词来补充jieba词典
    sentence_seged = jieba.cut(sentence.strip(), cut_all=False, use_paddle=10)  # 默认精确模式
    # sentence_seged =jieba.cut_for_search(sentence.strip(),HMM=True)#搜索引擎模式
    # keywords =jieba.analyse.extract_tags(sentence, topK=30, withWeight=True, allowPOS=('n', 'v','nr', 'ns'))#关键词模式
    # sentence_seged=[item[0] for item in keywords]
    stopwords = stopwordslist('停用词表.txt')  # 这里加载停用词的路径
    synwords = synwordslist('近义词表.txt')  # 这里加载近义词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords and word.__len__() > 1:
            if word != '\t':  # 判断出不是停用词
                if word in synwords.keys():  # 如果是同义词
                    word = synwords[word]
                    outstr += word
                    outstr += " "
                else:
                    outstr += word
                    outstr += " "
    return outstr


if __name__ == "__main__":
    a_na = ['中国.xlsx.txt']
    for name in a_na:
        inputs = open(f'./excel转txt结果/{name}', 'r', encoding='utf-8')
        outputs = open(f'./分词结果/{name}', 'w', encoding='utf-8')

        pool = ThreadPool()
        alls = pool.map(seg_sentence, inputs)  # 多线程和普通的列表嵌套不一样，是直接将列表里面的元素取出来了。而且输出是二次嵌套列表
        pool.close()
        pool.join()

        alls_1 = []
        n = []
        for i in alls:
            if i != n:
                outputs.write(i + '\n')

        outputs.close()
        inputs.close()
