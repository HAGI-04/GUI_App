import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import JSONcreater as jc


def treeview(data, title, nest, caller=None):
    tmp = []
    # summary部分
    tmp.append(html.Summary(title))
    # 要素部分
    for block in data:
        # 辞書部分
        if type(block) == dict:
            tmp2 = []
            for k, v in block.items():
                tmp2.append(html.P(f"{k} : {v}", style={"margin": "0"}))
            tmp.append(html.Div(tmp2, style={"backgroundColor": "lightgray", "borderRadius": "5px", "padding": "10px", "margin" : "5px 0 5px 10px"}))
        # 配列部分
        else:
            num = len(block)
            tmp.append(treeview(block, num, nest+1))
    return html.Details(tmp, style={"padding": "5px 0 5px 5px", "margin" : "5px 0 5px 10px"})


# テスト用JSONデータ作成
datas = [jc.generate_recursive_array() for i in range(10)]

# Dashアプリケーションを作成する
app = Dash(__name__)
app.layout = html.Div([
    html.Div(id='left-column', children=[
        # ここに左側のコンテンツを配置します。
    ], style={
        'width': '75%',
        'height': '97vh',
        'display': 'inline-block',
        'background-color': 'lightgray',
        'vertical-align': 'top'
    }),
    
    html.Div(id='right-column', children=[
        treeview(datas[0], "testtt", 1)
    ], style={
        'width': '25%',
        'height': '97vh',
        'display': 'inline-block',
        'background-color': 'gainsboro',
        'vertical-align': 'top',
        'overflow': 'auto'
    })
])


if __name__ == "__main__":
    app.run_server(debug=True)
