<h3>Simple Plots for Python (3 Venn diagram, Volcano plot, Rank sorted line-plot</h3>
<p>This library includes 3 simple plots function and easy-to-use, and data should be formed by Pandas. For the detail, please see the main.py code.</p>
<p>If you find any bugs or troubles, let me know(Contact : swiri021@gmail.com)</p>
<p>Required library : Pandas, Numpy, matplotlib, seaborn, matplotlib_venn</p>
<p>Please install these required libraries by using pip install</p>
<br/>
<br/>
<h4>Installation: </h4>
<p>No installation required for this library, just download and use it.</p>
<br/>
<br/>
<h4>Usage example: </h4>
<br/>
<h5>Volcano plot</h5>
<p>pt.volcano_plot(df, x_ax='Fold Change', y_ax='FDR', output_name='volcano') # Volcano plot</p>
<br/>
<h5>Rank sorted line-plot</h5>
<p>pt.rankplot(df,df_c) # No marker</p>
<p>pt.rankplot(df,df_c, selected_on=True, selected_data=selected_data) # With marker</p>
<br/>
<h5>3 Venn diagram</h5>
<p>pt.venn_dia(n_df, scaling='bypass') # No scaling</p>
<p>pt.venn_dia(n_df, scaling='log2') # Log2 scaling</p>
<br/>
<br/>
<h4>Output example: </h4>
<p>Volcano plot</p>
<img src="volcano.png"/>
<p>Rank sorted line-plot</p>
<img src="rankplot.png"/>
<p>3Venn diagram</p>
<img src="venn_diagram.png"/>