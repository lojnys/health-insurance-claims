import pandas as pd
from IPython.display import display_html

def display_side_by_side(*dfs, titles=None):
    html_str = ""
    
    for i, df in enumerate(dfs):
        title = titles[i] if titles and i < len(titles) else ""
        
        html_str += f"""
        <div style="display:inline-block; vertical-align:top; margin-right:20px;">
            <h4>{title}</h4>
            {df.to_html()}
        </div>
        """
        
    display_html(html_str, raw=True)
