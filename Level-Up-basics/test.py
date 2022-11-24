
from bokeh.plotting import figure,output_file,show

x= [1,2,3,4,5,6,7,8,9,10]
y=[2,4,6,8,10,12,14,16,18,20]

output_file('bokehh.html')

# create figure object
fig_obj= figure()

fig_obj.line(x,y)

show(fig_obj)             