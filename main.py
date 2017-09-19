from MY_STATS import MY_STATS
from MY_PLOT import MY_PLOT
import pandas as pd

st = MY_STATS()
pt = MY_PLOT()


######volcano plot example
f1 = open("example_data/volcano_plot_data.tsv","r") #file read
f1_data = f1.read().strip().split("\n") #file read
f1_data = [x.split("\t") for x in f1_data] #file read

head = f1_data[0] #file head
head = head[1:] #excluding index head in full head
f1_data = f1_data[1:]
index = [x[0] for x in f1_data] #file index
data = [x[1:] for x in f1_data] #file data

df = pd.DataFrame(data=data, index=index, columns=head) # make matrix
pt.volcano_plot(df, x_ax='Fold Change', y_ax='FDR', output_name='volcano') # plotting

f1.close()
######volcano plot example



######rank-sorting-plot example
f1 = open("example_data/rank_plot_data.tsv","r") #file read
f1_data = f1.read().strip().split("\n") #file read
f1_data = [x.split("\t") for x in f1_data] #file read

head = f1_data[0] #file head
head = head[1:] #excluding index head in full head
f1_data = f1_data[1:]
index = [x[0] for x in f1_data] #file index
data = [x[1:] for x in f1_data] #file data
df = pd.DataFrame(data=data, index=index, columns=head) # make matrix

df_c = df.columns.tolist()
selected_data = ['6061.0', '2191.0', '1479.0', '9072.0', '1479.0', '8993.0'] # selected rows

#pt.rankplot(df,df_c) # No marker
pt.rankplot(df,df_c, selected_on=True, selected_data=selected_data) # With marker

f1.close()
######rank-sorting-plot example



######3 Venn diagram example
def file_read(file_name):
	f1 = open(file_name,"r") #file read
	f1_data = f1.read().strip().split("\n") #file read
	f1_data = [x.split("\t") for x in f1_data] #file read

	head = f1_data[0] #file head
	head = head[1:] #excluding index head in full head
	f1_data = f1_data[1:]
	index = [x[0] for x in f1_data] #file index
	data = [x[1:] for x in f1_data] #file data

	df = pd.DataFrame(data=data, columns=head, index=index)
	f1.close()

	return df

df1 = file_read("example_data/venn_diagram_data_set1.tsv") # read set1
df2 = file_read("example_data/venn_diagram_data_set2.tsv") # read set2
df3 = file_read("example_data/venn_diagram_data_set3.tsv") # read set3

n_df = pd.concat([df1,df2,df3], axis=1) # Merge set1, set2, set3
n_df.columns = ['set1', 'set2', 'set3'] # Rename labels

#pt.venn_dia(n_df, scaling='bypass') # No scaling
pt.venn_dia(n_df, scaling='log2') # Log2 scaling
######3 Venn diagram example

