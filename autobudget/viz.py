import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def plot_time_series(df, categories, title="Category Trends Over Time"):
    """
    Plots a line chart of selected categories over time, plus their sum.
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

    # Individual category lines
    for cat in categories:
        fig.add_trace(go.Scatter(
            x=months,
            y=chart_data[cat],
            mode="lines",
            name=cat,
            line=dict(width=2)
        ))

    # Add the sum line
    sum_series = chart_data.sum(axis=1)
    fig.add_trace(go.Scatter(
        x=months,
        y=sum_series,
        mode="lines",
        name="Sum of Categories",
        line=dict(width=5, color="#d62728")  # Thick, standout color
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Month",
        yaxis_title="Value",
        legend_title="Category",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.caption("Each line is a category; 'Sum of Categories' is the bold curve.")
