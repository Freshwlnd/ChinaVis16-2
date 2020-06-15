# -*- coding: utf-8 -*-

# lib
import csv
import os
from prettytable import PrettyTable
from datetime import datetime
import json

# local file
from hash_data import *
# from solved_datas import *	# 文件太大导致读取速度过慢，放弃该方法



#-------------------------------------------------------------#
#-------------------------------------------------------------#
#------------------------- 全局变量区 -------------------------#

# constant list
all_prefixs = ['From', 'To', 'Cc', 'Bcc']
get_prefixs = ['To', 'Cc', 'Bcc']

## datas
# titles = {}
datas = []

## people
staff_info = {}		# 按人员聚合后的结果	
# staff_info
# 	info as senter	-	staff_info['xxx'][0]
# 	info as geter	-	staff_info['xxx'][1]
# 	nums_of_email	-	staff_info['xxx'][x][0]
#	address_prefix	-	staff_info['xxx'][x][1][0]
# 	address_prefix	-	staff_info['xxx'][x][1][1]
# 	display			-	staff_info['xxx'][x][2]
#	emials			-	staff_info['xxx'][x][3]

## email_content
content_words = {}
classified_content = {}

## company_history
period_info = {}

#----------------------- 全局变量区 end -----------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#





#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
#---------------------------- 获取信息 ----------------------------#

## 获取title
def get_titles():

	global titles

	all_file_path = os.listdir("../data")

	# get_title
	fin_path = "../data/"+all_file_path[0]
	with open(fin_path, "r", encoding="ISO-8859-1") as file_in:
		reader = csv.reader(file_in)
		data_list = list(reader)
		# print(data_list)
		x = 0
		for name in data_list[0]:
			titles[name] = x
			x += 1

## 获取数据
def get_datas():

	global datas

	all_file_path = os.listdir("../data")

	# get_all_data
	for fin_path in all_file_path:
		fin_path = "../data/"+fin_path
		try:
			with open(fin_path, "r", encoding="ISO-8859-1") as file_in:
				reader = csv.reader(file_in)
				data_list = list(reader)
				datas += data_list[1:]
			# break
		except BaseException as e:
			print(fin_path, e)

	#output_to_one_file #一次性读取文件时会卡住【也许是内存问题】
	# with open('solved_datas.py', 'w') as output_file:
	# 	output_file.write("datas = "+str(datas))

#-------------------------- 获取信息 end --------------------------#
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#





#----------------------------------------------------------------#
#----------------------------------------------------------------#
#------------------------- 问题1: 处理人 -------------------------#


## 按不同 "识别人员规则" 将邮件分类，并输出到文件，方便观察结果
def classify_by_display():
	staff_dict = {}
	# classify datas by display
	for data in datas:
		try:
			for pre in all_prefixs:
				disp_title = pre+" (display)"
				disp_datas = data[titles[disp_title]].lower().split(';')
				for disp_data in disp_datas:
					staff_dict.setdefault(disp_data, []).append(data)
		except BaseException as e:
			pass
	# output to file
	staff_list = sorted(staff_dict.items(), key=lambda x:x[0])
	with open('../output/classify_by_display.txt', 'w') as output_file:
		output_file.write(str(['name','nums_of_email'])+'\n')
		for disp,emails in staff_list:
			output_file.write(str([disp,len(emails)]) + '\n')

def classify_by_address():
	staff_dict = {}
	# classify datas by address
	for data in datas:
		try:
			for pre in all_prefixs:
				addr_title = pre+" (address)"
				addr_datas = data[titles[addr_title]].lower().split(';')
				for addr_data in addr_datas:
					addr = addr_data.split('@')
					if len(addr)>1:	# 普通形式
						addr = addr[0]
					else:				# 解析失败形式
						addr = addr[0].split('/')[-1].split('=')[-1]
					staff_dict.setdefault(addr, []).append(data)
		except BaseException as e:
			pass
	# output to file
	staff_list = sorted(staff_dict.items(), key=lambda x:x[0])
	with open('../output/classify_by_address.txt', 'w') as output_file:
		output_file.write(str(['name','nums_of_email'])+'\n')
		for addr,emails in staff_list:
			output_file.write(str([addr,len(emails)]) + '\n')


## 按需求将邮件分类，并记录信息，方便后续使用
def get_info_by_address():
	global staff_info
	for data in datas:
		try:
			for pre in all_prefixs:
				# 解析 display 及 address
				disp_title = pre+" (display)"
				disp_datas = data[titles[disp_title]].lower().split(';')
				addr_title = pre+" (address)"
				addr_datas = data[titles[addr_title]].lower().split(';')
				num_of_data = len(addr_datas)
				for i in range(num_of_data):
					disp_data = disp_datas[i]
					addr_data = addr_datas[i]
					addr = addr_data.split('@')
					if len(addr)>1:		# 普通形式
						addr_pre = addr[0].split('<')[-1]
						addr_suf = addr[1].split('.')[0]
					else:				# 解析失败形式
						addr = addr[0].split('/')
						addr_pre = addr[-1].split('=')[-1]
						addr_suf = addr[0].split('=')[-1]
					addr_pre = addr_pre.strip('"').strip("'") 	# 去除字符串内前后的引号
					if len(addr_pre)>25:	# 排除太长的乱码名字
						continue
					people_name = addr_pre 	# 以address的前缀为人名
					# 信息计入
					staff_info.setdefault(people_name, [[[set(),set()],set(),[]],[[set(),set()],set(),[]]])
					info_id = 0
					if pre!='From':
						info_id = 1	
					staff_info[people_name][info_id][0][0].add(addr_pre)
					staff_info[people_name][info_id][0][1].add(addr_suf)
					staff_info[people_name][info_id][1].add(disp_data)
					staff_info[people_name][info_id][2].append(data)
		except BaseException as e:
			pass


## 筛选员工： 按照规则【认为使用 “hackingteam”域名 且邮件数量大于5的人(后续merge时判断) 为员工】
def find_staff():
	global staff_info
	for people, info in list(staff_info.items()):	# 若直接遍历字典，则删除时会报错 "RuntimeError: dictionary changed size during iteration"
		flag_is_staff = 0
		if "hackingteam" in info[0][0][1] or "hackingteam" in info[1][0][1]:
			flag_is_staff = 1
		if flag_is_staff == 0:
			del staff_info[people]
	# output to file
	staff_list = sorted(staff_info.items(), key=lambda x:x[0])
	# 使用prettytable输出好看的表格
	table = PrettyTable(['name','nums_of_email'])
	for staff_pair in staff_list:
		table.add_row([staff_pair[0],len(staff_pair[1][0][2])+len(staff_pair[1][1][2])])
	with open('../output/staff_list.txt', 'w') as output_file:
		output_file.write(str(table))

		
# staff_info
# 	info as senter	-	staff_info['xxx'][0]
# 	info as geter	-	staff_info['xxx'][1]
#	address_prefix	-	staff_info['xxx'][x][0][0]
# 	address_prefix	-	staff_info['xxx'][x][0][1]
# 	display			-	staff_info['xxx'][x][1]
#	emials			-	staff_info['xxx'][x][2]
## 合并员工
def merge_staff():
	global staff_info
	for people, info in list(staff_info.items()):
		# 同时删除了邮件过少人员
		if people in people_real_name.keys():
			real_name = people_real_name[people]
			staff_info.setdefault(real_name, [[[set(),set()],set(),[]],[[set(),set()],set(),[]]])
			for info_id in range(2):
				staff_info[real_name][info_id][0][0].union(info[info_id][0][0])
				staff_info[real_name][info_id][0][1].union(info[info_id][0][1])
				staff_info[real_name][info_id][1].union(info[info_id][1])
				staff_info[real_name][info_id][2]+=info[info_id][2]
			del staff_info[people]
		elif people not in people_real_name.values():
			del staff_info[people]

	with open('../output/staff_merged_list.txt', 'w') as output_file:
		for people, info in sorted(staff_info.items(), key=lambda x:len(x[1][0][2])+len(x[1][1][2]), reverse=True):
			output_file.write(people+','+str(len(info[0][2])+len(info[1][2]))+'\n')

## 人员的邮件中重要程度信息
def get_people_important():

	staff_important_info = {}
	
	# data processing
	for people, info in staff_info.items():
		staff_important_info[people] = [0,0,0,0,0]
		for info_id in range(2):
			for email in info[info_id][2]:
				try:
					staff_important_info[people][int(email[titles['Importance']])]+=1
					staff_important_info[people][3]+=1
				except BaseException as e:
					print(e)
		staff_important_info[people][4] = staff_important_info[people][2]/staff_important_info[people][3]
	staff_important_list = sorted(staff_important_info.items(), key=lambda x:(x[1][2],x[1][4]), reverse=True)

	# 使用prettytable输出好看的表格
	table = PrettyTable(['name','0','1','2','Num_of_email','rate'])
	for staff_important_pair in staff_important_list:
		table.add_row([staff_important_pair[0]]+staff_important_pair[1])

	# output to file
	with open('../output/staff_importance.txt', 'w') as output_file:
		output_file.write(str(table))


## 人员工作时间
def get_people_work_time():

	staff_worktime_info = {}
	staff_list = sorted(staff_info.items(), key=lambda x:len(x[1][0][2])+len(x[1][1][2]), reverse=True)[0:20]

	# data processing
	for people, info in staff_list:
		staff_worktime_info.setdefault(people, [0 for i in range(24)])
		for email_data in info[0][2]:		# 只考虑发送的邮件
			email_worktime_str = email_data[titles["Date Sent"]].split(' ')[1].split(':')
			try:
				email_worktime = (int(email_worktime_str[0])-8+24)%24	# 按小时统计
				staff_worktime_info[people][email_worktime] += 1
			except BaseException as e:
				print(email_data[titles["Date Sent"]])
				print(e)
	
	# output to file
	
	staff_worktime_list = sorted(staff_worktime_info.items(), key=lambda x:x[0])
	## 使用prettytable输出好看的表格
	table = PrettyTable(['people']+[i for i in range(24)])
	for staff_worktime_pair in staff_worktime_list:
		table.add_row([staff_worktime_pair[0]]+staff_worktime_pair[1])
	
	with open('../output/staff_worktime.txt', 'w') as output_file:
		output_file.write(str(table))

	# json
	output_dict = {
		'value': '2400',
		'num': 0,
		'children': []
	}
	staff_id = 0
	for worktime in range(24):
		child = {}
		for staff_name, email_num in staff_worktime_list:
			if child == {}:
				child = {'id': staff_id, 'staff_name': staff_name, 'worktime': worktime, 'value':'100', 'num':str(email_num[worktime])}
			else:
				child = {'id': staff_id, 'staff_name': staff_name, 'worktime': worktime, 'value':'100', 'num':str(email_num[worktime]), 'children':[child]}
			staff_id = (staff_id+1)%10
		output_dict['children'].append(child)

	with open('../output/people_work_time.json', 'w') as output_file:
		output_file.write(json.dumps(output_dict))

	staff_seq = []
	for staff_name, email_num in staff_worktime_list:
		staff_seq.append(staff_name)
	with open('../output/staff_list.json', 'w') as output_file:
		output_file.write(json.dumps(staff_seq))



## 人员与邮件关键词关系
def get_people_content():

	staff_content_info = {}
	content_staff_info = {}

	# 需要先处理出关键词表 content_words

	# 处理每封邮件
	for people, info in staff_info.items():
		for info_id in range(2):
			for email in info[info_id][2]:
				content = email[titles["Subject"]].split(' ')+email[titles["Attachment Names"]].split(' ')
				for word in content:
					if word in content_words.keys():
						content_staff_info.setdefault(word,[]).append(people)
						staff_content_info.setdefault(people,[]).append(word)

	# 处理成需要的格式输出（表格太大，输出至文件不便查看）




#----------------------- 问题1: 处理人 end -----------------------#
#----------------------------------------------------------------#
#----------------------------------------------------------------#





#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------- 问题2: 处理内容 -------------------------#

def get_content():
	global content_words
	for every_data in datas:
		content = every_data[titles["Subject"]].split(' ')+every_data[titles["Attachment Names"]].split(' ')
		for every_word in content:
			content_words[every_word] = content_words.get(every_word, 0)+1
	word_list = sorted(content_words.items(), key=lambda x:x[1], reverse=True)

	long_word_seq = []

	# 使用prettytable输出好看的表格
	table = PrettyTable(['word','num'])
	for word_pair in word_list:
		if len(word_pair[0])>20:
			# print(word_pair)
			long_word_seq.append(word_pair)
			continue
		table.add_row(word_pair)
	
	with open('../output/sorted_content_data.txt', 'w') as output_file:
		output_file.write(str(table))
		output_file.write('\n')
		output_file.write(str(long_word_seq))


def filter_content():
	global content_words
	for word in list(content_words.keys()):
		if word not in key_words:
			if word.lower() in key_words:
				content_words[word.lower()] = content_words.get(word.lower(),0)+content_words[word]
			del content_words[word]

def output_content():
	content_list = []
	for word, num in content_words.items():
		content_list.append({"name":word, "size":num})
	with open('../output/content.json', 'w') as output_file:
		output_file.write(json.dumps(content_list))

def classify_content():
	global classified_content
	for class_name, content_dict in content_class.items():
		classified_content.setdefault(class_name, [0,{}])
		for content_word,trans_word in content_dict.items():
			try:
				word_times = content_words[content_word]
				classified_content[class_name][1][trans_word] = classified_content[class_name][1].get(trans_word,0)+word_times
				classified_content[class_name][0] += word_times
			except BaseException as e:
				print(e)

	# output
	out_seq1 = []
	out_seq2 = []
	for class_name, content_info in classified_content.items():
		print(class_name)
		out_seq1.append({'name':class_name, 'size':content_info[0], 'children':len(content_info[1])})
		content_info = content_info[1]
		for content_word, content_num in content_info.items():
			print(content_word)
			out_seq2.append({'name':content_word, 'size':content_num})
	with open('../output/content_sunburst1.json', 'w') as output_file:
		output_file.write(json.dumps(out_seq1))
	with open('../output/content_sunburst2.json', 'w') as output_file:
		output_file.write(json.dumps(out_seq2))



#----------------------- 问题2: 处理内容 end -----------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#





#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------- 问题3: 处理时间 -------------------------#
def classify_by_period():
	global period_info
	period_info = {'month':{}, 'year':{}}
	period_email_nums = {'month':{}, 'year':{}}
	for data in datas:
		# 以邮件的发送时间作为分类依据
		email_period_str = data[titles["Date Sent"]].split(' ')[0].split('/')
		try:
			email_period = email_period_str[0] + '/' + email_period_str[1]	# 按月统计
			period_info['month'].setdefault(email_period,[]).append(data)
			period_email_nums['month'][email_period] = period_email_nums['month'].get(email_period,0)+1

			email_period = email_period_str[0]	# 按年统计
			period_info['year'].setdefault(email_period,[]).append(data)
			period_email_nums['year'][email_period] = period_email_nums['year'].get(email_period,0)+1
		except BaseException as e:
			print(e)
	
	# output to file
	period_list = sorted(period_email_nums['month'].items(), key=lambda x:datetime.strptime(x[0],"%Y/%m"))
	## 使用prettytable输出好看的表格
	table = PrettyTable(['period','email_num'])
	for period_pair in period_list:
		table.add_row(period_pair)
	with open('../output/classify_by_period_month.txt', 'w') as output_file:
		output_file.write(str(table))

	period_list = sorted(period_email_nums['year'].items(), key=lambda x:datetime.strptime(x[0],"%Y"))
	## 使用prettytable输出好看的表格
	table = PrettyTable(['period','email_num'])
	for period_pair in period_list:
		table.add_row(period_pair)
	with open('../output/classify_by_period_year.txt', 'w') as output_file:
		output_file.write(str(table))

	out_dict = {'name': 'hackingteam', 'value':[]}
	for period_pair in period_list:
		out_dict['value'].append({'key':period_pair[0], 'value':period_pair[1]})
	with open('../output/period_email_num.json', 'w') as output_file:
		output_file.write(json.dumps(out_dict))


# 对筛选出的关键词语进行统计
def extract_period_content(period_type):
	# period_type - "year" or "month"
	
	period_content = {}

	# 对词频最高的10个词
	# key_topic = set(sorted(content_words, key=lambda x:x[1], reverse=True)[0:10])

	# 对选出的关键词
	key_topic = []
	for topic in work_content_class.values():
		key_topic += topic

	# 统计各个时间段内关键词词频
	for period, info in period_info[period_type].items():
		period_content[period] = {}
		for topic in key_topic:
			period_content[period].setdefault(topic, 0)
		for email in info:
			content = set(email[titles["Subject"]].split(' ')+email[titles["Attachment Names"]].split(' '))
			for word in content:
				if word in key_topic:
					period_content[period][word] += 1

	# output to file
	period_list = []
	if(period_type=='year'):
		period_list = sorted(period_content.items(), key=lambda x:datetime.strptime(x[0],"%Y"), reverse=True)
	elif(period_type=='month'):
		period_list = sorted(period_content.items(), key=lambda x:datetime.strptime(x[0],"%Y/%m"), reverse=True)
	table = PrettyTable(['period']+list(key_topic))
	for period_pair in period_list:
		table.add_row([period_pair[0]]+list(period_pair[1].values()))
	with open('../output/period_content_'+period_type+'.txt', 'w') as output_file:
		output_file.write(str(table))

	# 统计每个数字出现个数
	num_set = {}	# 统计每种数字出现次数，方便设置比例尺
	for topic in key_topic:
		for period, dct in period_list:
			num = dct[topic]
			num_set[num] = num_set.get(num,0)+1


	# 比例尺 [0,1,5,10,25,60,120,180,600,1000,6000,10000]
	scale = []
	# 计算比例尺（使每种颜色的格子个数尽可能平均）
	color_num = 11
	num_set = sorted(num_set.items(),key=lambda x:x[0])
	num_times_count = 0
	for pair in num_set:
		num_times_count += pair[1]
	every_color_num = num_times_count//color_num
	print(str(every_color_num) + ' = ' + str(num_times_count) + ' // ' + str(color_num))
	now_num = 0
	for pair in num_set:
		now_num += pair[1]
		num_times_count -= pair[1]
		if now_num>=every_color_num:
			scale.append(pair[0])
			color_num -= 1
			if color_num <= 0:
				break
			every_color_num = num_times_count//color_num
			print(str(every_color_num) + ' = ' + str(num_times_count) + ' // ' + str(color_num))
			now_num = 0

	with open('../output/period_content_count.json', 'w') as output_file:
		output_file.write(json.dumps(scale)+'\n')
		output_file.write(json.dumps(num_set))


	# 封装成前端所需格式
	output_dict = {
		'num': '0',
		'value': str(len(key_topic)*100),
		'children': []
	}
	for topic in key_topic:
		class_name = ''
		for class_pair in work_content_class.items():
			if topic in class_pair[1]:
				class_name = class_pair[0]
				break
		child = {}
		for period, dct in period_list:
			num = dct[topic]
			flag = 0
			for i in range(len(scale)):
				if num<scale[i]:
					num = i
					flag = 1
					break
			if flag==0:
				num = len(scale)
			if child == {}:
				child = {'period': period, 'topic': topic, 'num':str(num), 'value':'100'}
			else:
				child = {'period': period, 'topic': topic, 'num':str(num), 'value':'100', 'children':[child]}
		output_dict['children'].append(child)

	with open('../output/period_content.json', 'w') as output_file:
		output_file.write(json.dumps(output_dict))


	# output
	out_seq3 = []
	out_seq4 = []
	for class_name, content_info in work_content_class.items():
		class_num = 0
		for topic in content_info:
			num = 0
			for period, dct in period_list:
				num += dct[topic]
			class_num += num
			out_seq4.append({'name':topic, 'size':num})
		out_seq3.append({'name':class_name, 'size':class_num, 'children':len(content_info)})

	with open('../output/content_sunburst3.json', 'w') as output_file:
		output_file.write(json.dumps(out_seq3))
	with open('../output/content_sunburst4.json', 'w') as output_file:
		output_file.write(json.dumps(out_seq4))



#----------------------- 问题3: 处理时间 end -----------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#





#--------------------------------------------------------------------#
#--------------------------------------------------------------------#
#------------------------ 没有思路时的测试代码 ------------------------#
def list_people():
	global content_words
	# global sent_people2add
	# global sent_people2disp
	# global sent_times
	# global get_people2add
	# global get_people2disp
	# global get_times

	#处理数据
	for every_data in datas:
		# 处理发送
		# disp = every_data[titles["From (display)"]].lower()
		addrs = every_data[titles["From (address)"]].lower().split(';')
		for addr in addrs:
			try:
				addr = addr.split('@')
				if(len(addr)<2):
					addr = addr[0]
					addr = addr.split('/')
					people_pre = addr[-1].split('=')[1]
					addr = addr[1].split('=')[1]
				else:
					people_pre = addr[0].split('<')[-1]
					addr = addr[1].split('.')[0]
				if people_real_name.get(people_pre,-1) != -1:
						people_pre = people_real_name[people_pre]
				if "hackingteam" in addr:
					sent_people2add.setdefault(people_pre,[]).append(addr)
					# sent_people2disp.setdefault(people_pre,[]).append(disp)
					sent_times[people_pre] = sent_times.get(people_pre,0)+1
			except BaseException as e:
				pass
			# print(addr, e)
		# 处理接收
		for pref in get_prefixs:
			# disp = every_data[titles[pref+" (display)"]].lower()
			addrs = every_data[titles[pref+" (address)"]].lower().split(';')
			for addr in addrs:
				try:
					addr = addr.split('@')
					if(len(addr)<2):
						addr = addr[0]
						addr = addr.split('/')
						people_pre = addr[-1].split('=')[1]
						addr = addr[1].split('=')[1]
					else:
						people_pre = addr[0].split('<')[-1]
						addr = addr[1].split('.')[0]
					if people_real_name.get(people_pre,-1) != -1:
						people_pre = people_real_name[people_pre]
					if "hackingteam" in addr:
						get_people2add.setdefault(people_pre,[]).append(addr)
						# get_people2disp.setdefault(people_pre,[]).append(disp)
						get_times[people_pre] = sent_times.get(people_pre,0)+1
				except BaseException as e:
					# print(addr, e)
					pass
	sent_list = sorted(sent_times.items(), key=lambda x:x[0], reverse=True)
	get_list = sorted(get_times.items(), key=lambda x:x[0], reverse=True)
	
	# 写入
	with open('../output/sorted_people_sent_data.txt', 'w') as output_file:
		output_file.write(str(['name','times','address','disp'])+'\n')
		for people_pair in sent_list:
			people_pair = list(people_pair)
			people_pair.append(list(set(sent_people2add[people_pair[0]])))
			# people_pair.append(list(set(sent_people2disp[people_pair[0]])))
			# if "hackingteam" in people_pair[2]:
			output_file.write(str(people_pair)+'\n')
	with open('../output/sorted_people_get_data.txt', 'w') as output_file:
		output_file.write(str(['name','times','address','disp'])+'\n')
		for people_pair in get_list:
			people_pair = list(people_pair)
			people_pair.append(list(set(get_people2add[people_pair[0]])))
			# people_pair.append(list(set(get_people2disp[people_pair[0]])))
			#if "hackingteam" in people_pair[2]:
			output_file.write(str(people_pair)+'\n')

#------------------------- 测试部分代码 end -------------------------#
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#