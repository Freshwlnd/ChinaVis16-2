# LDA.py

from data_processing import *
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora

def get_doc():
	get_datas()
	print(len(datas))
	doc_complete = []
	for every_data in datas:
		content = every_data[titles["Subject"]]+every_data[titles["Attachment Names"]]
		doc_complete.append(content)
	return doc_complete

def pretreatment(doc_complete):
	# 变为小写，引入停用词，移除标点符号，词形还原
	stop = set(stopwords.words('english')+['re','r','fwd','i','fw'])	# 停用词
	exclude = set(string.punctuation)		# 标点符号
	lemma = WordNetLemmatizer()

	def clean(doc):
		stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
		punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
		normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
		return normalized

	doc_clean = [clean(doc).split() for doc in doc_complete]

	return doc_clean

def train(doc_clean, n_p):
	# 创建语料的词语词典，每个单独的词语都会被赋予一个索引
	dictionary = corpora.Dictionary(doc_clean)
	# 使用上面的词典，将转换文档列表（语料）变成 DT 矩阵
	doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
	# 使用 gensim 来创建 LDA 模型对象
	Lda = gensim.models.ldamodel.LdaModel
	# 在 DT 矩阵上运行和训练 LDA 模型
	ldamodel = Lda(doc_term_matrix, num_topics=n_p, id2word = dictionary, passes=2)
	return ldamodel


# doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
# doc2 = "My father spends a lot of time driving my sister around to dance practice."
# doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
# doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
# doc5 = "Health experts say that Sugar is not good for your lifestyle."
# 整合文档数据
# doc_complete = [doc1, doc2, doc3, doc4, doc5]
doc_complete = get_doc()
doc_clean = pretreatment(doc_complete)
for n_p in [2,5,10,20,30]:
	ldamodel = train(doc_clean, n_p)
	# 输出结果
	res = ldamodel.print_topics(num_topics=n_p,num_words=20)
	for itm in res:
		print(itm)