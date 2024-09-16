from dataset import ecom_sales_total
import plotly.express as px

bar_fig = px.bar(
    data_frame= ecom_sales_total, 
    x='Total Sales (R$)',
    y='Country',
    orientation='h',
    title='Total Sales by Country'
)

bar_fig.update_layout({'bargap':0.5})
