import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def causal_moving_average(series: pd.Series, window: int) -> pd.Series:
    """
    Computes causal moving average for a pandas Series.
    For index t, average of values from t-(window-1) to t.
    """
    return series.rolling(window=window, min_periods=1).mean()


def plot_time_series(df, categories, title="Category Trends Over Time", moving_avg=1):
    """
    Plots line chart of selected categories over time, plus their sum, with optional causal moving average.
    """
    if not categories:
        st.info("Select categories to view their trends.")
        return

    # Data prep
    chart_data = df.loc[categories].T
    chart_data.index.name = "Month"
    chart_data = chart_data.sort_index()
    months = chart_data.index.tolist()

    fig = go.Figure()

    # Individual smoothed category lines
    for cat in categories:
        y = chart_data[cat]
        if moving_avg > 1:
            y = causal_moving_average(y, moving_avg)
        fig.add_trace(go.Scatter(
            x=months,
            y=y,
            mode="lines",
            name=cat,
            line=dict(width=2)
        ))

    # Smoothed sum line
    sum_series = chart_data.sum(axis=1)
    if moving_avg > 1:
        sum_series = causal_moving_average(sum_series, moving_avg)
    fig.add_trace(go.Scatter(
        x=months,
        y=sum_series,
        mode="lines",
        name="Sum of Categories",
        line=dict(width=5, color="#d62728")
    ))
    
    # Dynamic title with moving average info
    if moving_avg == 1:
        ma_info = "(no moving average)"
    else:
        ma_info = f"(moving average M={moving_avg})"

    fig.update_layout(
        title=f"{title} {ma_info}",
        xaxis_title="Month",
        yaxis_title="Value",
        legend_title="Category",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.caption("Each line is a category; 'Sum of Categories' is the bold curve.")
    
