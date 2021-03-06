# main.py

from data_processing import *

#---------------------------------------------------------------#
#---------------------------------------------------------------#
#--------------------------- 获取数据 ---------------------------#

# get_titles()	# 已保存在 "hash_data.py" 文件中，故不必重复获取
get_datas()

#------------------------- 获取数据 end -------------------------#
#---------------------------------------------------------------#
#---------------------------------------------------------------#



#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------- 问题2: 处理内容 -------------------------#

# 另外两个问题用到内容信息，故提前到第一个执行
get_content()		# 统计邮件中 出现的词语 及 词频
filter_content()	# 过滤邮件中的关键词
output_content()	# 按json格式输出关键词
classify_content()	# 按分类统计关键词

#----------------------- 问题2: 处理内容 end -----------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#



#----------------------------------------------------------------#
#----------------------------------------------------------------#
#------------------------- 问题1: 处理人 -------------------------#

# 1. 以人员信息为线索，处理邮件信息
# classify_by_display()		# 按 "display" 聚合email，观察结果
# classify_by_address()		# 按 "address" 聚合email，观察结果

# 2. 发现按 "address" 聚合 email 效果更好，故对该方法得到的数据进行处理
# get_info_by_address()		# 按 "address" 聚合email，记录信息
# find_staff()				# 认为使用 “hackingteam” 域名 的人为员工，筛选结果
# merge_staff()				# 合并同一个人的多个名字

# 3. 对员工分类
##	- 按收发重要邮件数量排序
# get_people_important()
##	- 按工作时间（发送邮件时间）分类
# get_people_work_time()
##	- 按邮件内容分类
# get_people_content()		# 需要先处理出问题二中的content表

#----------------------- 问题1: 处理人 end -----------------------#
#----------------------------------------------------------------#
#----------------------------------------------------------------#



#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------- 问题3: 处理时间 -------------------------#

classify_by_period() 			# 按时间将各个邮件分组
extract_period_content('year')	# 提取相关内容信息

#----------------------- 问题3: 处理时间 end -----------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#

