import pandas as pd
import math
import matplotlib as mlab
mlab.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_style("whitegrid")
from scipy import stats
import numpy as np
from matplotlib_venn import venn3


class MY_PLOT:
	def volcano_plot(self, df, x_ax='', y_ax='', colors=['red','blue'], output_name='volcano_plot'):
		floating = lambda x : [float(y) for y in x]
		df_arr_dat = [floating(x) for x in df.values.tolist()]
		df_arr_index = df.index.tolist()
		df_arr_dat = [[x[0],-math.log10(x[1])] for x in df_arr_dat]

		df1 = pd.DataFrame(data=df_arr_dat, columns=[x_ax, y_ax], index=df_arr_index)
		df1_values = df1[df1[y_ax]>-math.log10(0.05)]

		###### fold > 0
		df2_values = df1_values[df1_values[x_ax]>np.log2(1.5)]
		df2_ex = pd.DataFrame(df2_values)

		###### fold < 0
		df2_values = df1_values[df1_values[x_ax]<-np.log2(1.5)]
		df3_ex = pd.DataFrame(df2_values)

		ax = df1.plot(kind='scatter', x=x_ax, y=y_ax, color='grey')
		df2_ex.plot(kind='scatter', x=x_ax, y=y_ax, color=colors[0], ax=ax)
		df3_ex.plot(kind='scatter', x=x_ax, y=y_ax, color=colors[1], ax=ax)

		ax.set_xlabel("Fold Change(log2)")
		ax.set_ylabel("-log(P)")

		fig = ax.get_figure()
		fig.savefig(output_name+".png")

	def venn_dia(self,df, scaling='bypass', output_name='venn_diagram'):

		def only_agroup(a,b,c):
			a1 = [x for x in a if x not in b] #A
			a_result = [x for x in a1 if x not in c] #B
			return a_result

		ind_list = [df[x].dropna().index.tolist() for x in df.columns.tolist()]

		ghead_c = df.columns.tolist()
		ind_list_c = ind_list

		cs110_1 = list(set(ind_list_c[0]).intersection(ind_list_c[1])) ###AB
		cs011_1 = list(set(ind_list_c[1]).intersection(ind_list_c[2])) ####BC
		cs101_1 = list(set(ind_list_c[0]).intersection(ind_list_c[2])) ###AC
		cs111 = list(set(cs110_1).intersection(ind_list_c[2]))####ABC
		cs110 = len([x for x in cs110_1 if x not in cs111])###AB-ABC
		cs011 = len([x for x in cs011_1 if x not in cs111]) ####BC-ABC
		cs101 = len([x for x in cs101_1 if x not in cs111]) ###AC-ABC
		cs100 = len(only_agroup(ind_list_c[0],ind_list_c[1],ind_list_c[2])) ### A
		cs010 = len(only_agroup(ind_list_c[1],ind_list_c[2],ind_list_c[0])) ### B
		cs001 = len(only_agroup(ind_list_c[2],ind_list_c[0],ind_list_c[1])) ### C
		cs111 = len(list(set(cs110_1).intersection(ind_list_c[2])))####ABC

		figure, axes = plt.subplots(1, 1)### plot array 1,1, (2,2) means 2by2

		if scaling=="bypass":
			v = venn3(subsets=(cs100, cs010, cs110, cs001, cs101, cs011, cs111), set_labels = ghead_c, ax=axes)
		elif scaling=="log2":
			v = venn3(subsets=(np.log2(cs100), np.log2(cs010), np.log2(cs110), np.log2(cs001), np.log2(cs101), np.log2(cs011), np.log2(cs111)), set_labels = ghead_c, ax=axes)

			v.get_label_by_id('100').set_text(str(cs100))
			v.get_label_by_id('010').set_text(str(cs010))
			v.get_label_by_id('001').set_text(str(cs001))
			v.get_label_by_id('110').set_text(str(cs110))
			v.get_label_by_id('011').set_text(str(cs011))
			v.get_label_by_id('101').set_text(str(cs101))
			v.get_label_by_id('111').set_text(str(cs111))

		figure.savefig(output_name+".png")


	def rankplot(self, df, picked='', selected_on = False, selected_data=[], legend=False, output_name='rankplot'):
		if selected_on==False:

			df=df.astype(float)

			or_head = df.columns.tolist()
			df_sorted = df.sort_values(df.columns.tolist(), ascending=[True])
			df_sorted['index_value'] = pd.Series(df_sorted.index.tolist(), index=df_sorted.index)
			df_sorted = df_sorted.dropna()
			ax = df_sorted.plot(x='index_value', y=or_head[0], color='Blue')


			#ax.set_xlabel("Fold Change(log2)")
			#ax.set_ylabel("-log(P)")

			fig = ax.get_figure()
			fig.savefig(output_name+".png")

		else:
			df=df.astype(float)
			df_sorted = df.sort_values(df.columns.tolist(), ascending=[True])
			df_sorted['index_value'] = pd.Series(df_sorted.index.tolist(), index=df_sorted.index)
			df_sorted = df_sorted.dropna()
			list_df_sorted_index = df_sorted.index.tolist()

			#selected_data_entrez = [x[entrez_col_indata] for x in selected_data]
			#print selected_data_entrez
			####index select######

			dat = [i for i,item in enumerate(list_df_sorted_index) if item in selected_data]
			print dat

			ax = df_sorted.plot(x='index_value', y=picked, color='Blue', legend=legend)
			for x in dat:
				ax.axvspan(x, x+1, ymax=0.05, color='red', alpha=0.5)

			fn = ax.get_figure()
			fn.savefig(output_name+'.png')


	def __init__(self):
		print "PLOT ON!"
